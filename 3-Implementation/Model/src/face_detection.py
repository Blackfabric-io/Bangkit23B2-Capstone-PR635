"""
Face detection and age/gender classification module for NutriGenius.

This module implements face detection and age/gender estimation 
using deep learning models trained on the UTKFace dataset.
"""

import os
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
from typing import Dict, List, Tuple, Union, Optional

# Import common utilities
from utils.common import (
    load_config, 
    create_directory, 
    save_model, 
    load_model, 
    plot_training_history,
    convert_to_tflite
)

class FaceDetector:
    """Face detector and age/gender classifier for nutritional recommendations."""
    
    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize the face detector and age/gender classifier.
        
        Args:
            config_path: Optional path to configuration file
        """
        self.config = {}
        if config_path and os.path.exists(config_path):
            self.config = load_config(config_path)
        
        # Set default configurations if not provided
        self.face_detection_model = self.config.get('face_detection_model', 'haarcascade')
        self.age_model_path = self.config.get('age_model_path', None)
        self.gender_model_path = self.config.get('gender_model_path', None)
        
        # Initialize face detector
        self._init_face_detector()
        
        # Initialize age and gender models if paths are provided
        self.age_model = None
        self.gender_model = None
        
        if self.age_model_path and os.path.exists(self.age_model_path):
            self.age_model = load_model(self.age_model_path)
        
        if self.gender_model_path and os.path.exists(self.gender_model_path):
            self.gender_model = load_model(self.gender_model_path)
    
    def _init_face_detector(self) -> None:
        """Initialize the face detection model based on configuration."""
        if self.face_detection_model == 'haarcascade':
            # Use OpenCV's Haar Cascade Classifier
            model_path = self.config.get(
                'haarcascade_path', 
                cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
            )
            self.detector = cv2.CascadeClassifier(model_path)
        else:
            # Default to Haar Cascade if model type is not recognized
            model_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
            self.detector = cv2.CascadeClassifier(model_path)
    
    def detect_faces(self, image: np.ndarray) -> List[np.ndarray]:
        """
        Detect faces in an image.
        
        Args:
            image: Input image (BGR format)
            
        Returns:
            List of detected face regions as numpy arrays
        """
        # Convert to grayscale for face detection
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Detect faces
        faces = self.detector.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )
        
        # Extract face regions
        face_images = []
        for (x, y, w, h) in faces:
            face_img = image[y:y+h, x:x+w]
            face_images.append(face_img)
        
        return face_images
    
    def preprocess_face(self, face: np.ndarray, target_size: Tuple[int, int] = (200, 200)) -> np.ndarray:
        """
        Preprocess a face image for age/gender prediction.
        
        Args:
            face: Face image
            target_size: Target size for resizing
            
        Returns:
            Preprocessed face image
        """
        # Resize to target size
        face_resized = cv2.resize(face, target_size)
        
        # Convert to RGB (if model was trained on RGB)
        face_rgb = cv2.cvtColor(face_resized, cv2.COLOR_BGR2RGB)
        
        # Normalize pixel values to [0, 1]
        face_normalized = face_rgb / 255.0
        
        # Add batch dimension
        face_batch = np.expand_dims(face_normalized, axis=0)
        
        return face_batch
    
    def predict_age(self, face: np.ndarray) -> int:
        """
        Predict age from a face image.
        
        Args:
            face: Face image
            
        Returns:
            Predicted age
        """
        if self.age_model is None:
            raise ValueError("Age model not loaded. Please provide a valid model path.")
        
        # Preprocess face
        face_processed = self.preprocess_face(face)
        
        # Predict age
        age_pred = self.age_model.predict(face_processed)[0][0]
        
        # Round to nearest integer
        age = int(round(age_pred))
        
        return age
    
    def predict_gender(self, face: np.ndarray) -> str:
        """
        Predict gender from a face image.
        
        Args:
            face: Face image
            
        Returns:
            Predicted gender ("male" or "female")
        """
        if self.gender_model is None:
            raise ValueError("Gender model not loaded. Please provide a valid model path.")
        
        # Preprocess face
        face_processed = self.preprocess_face(face)
        
        # Predict gender
        gender_pred = self.gender_model.predict(face_processed)[0][0]
        
        # Convert to label
        gender = "male" if gender_pred > 0.5 else "female"
        
        return gender
    
    def analyze_face(self, face: np.ndarray) -> Dict[str, Union[int, str]]:
        """
        Analyze a face image to determine age and gender.
        
        Args:
            face: Face image
            
        Returns:
            Dictionary with age and gender predictions
        """
        result = {}
        
        # Predict age if model is available
        if self.age_model is not None:
            result['age'] = self.predict_age(face)
        
        # Predict gender if model is available
        if self.gender_model is not None:
            result['gender'] = self.predict_gender(face)
        
        return result
    
    def process_image(self, image: np.ndarray) -> List[Dict[str, Union[int, str, np.ndarray]]]:
        """
        Process an image to detect faces and analyze age/gender.
        
        Args:
            image: Input image
            
        Returns:
            List of dictionaries with face information
        """
        # Detect faces
        faces = self.detect_faces(image)
        
        # Analyze each face
        results = []
        for face in faces:
            result = self.analyze_face(face)
            result['face_image'] = face
            results.append(result)
        
        return results

def build_age_model(input_shape: Tuple[int, int, int] = (200, 200, 3)) -> tf.keras.Model:
    """
    Build a CNN model for age prediction.
    
    Args:
        input_shape: Input image shape
        
    Returns:
        Age prediction model
    """
    model = models.Sequential([
        layers.Input(shape=input_shape),
        
        # First convolutional block
        layers.Conv2D(32, (3, 3), activation='relu', padding='same'),
        layers.BatchNormalization(),
        layers.MaxPooling2D((2, 2)),
        layers.Dropout(0.25),
        
        # Second convolutional block
        layers.Conv2D(64, (3, 3), activation='relu', padding='same'),
        layers.BatchNormalization(),
        layers.MaxPooling2D((2, 2)),
        layers.Dropout(0.25),
        
        # Third convolutional block
        layers.Conv2D(128, (3, 3), activation='relu', padding='same'),
        layers.BatchNormalization(),
        layers.MaxPooling2D((2, 2)),
        layers.Dropout(0.25),
        
        # Fourth convolutional block
        layers.Conv2D(256, (3, 3), activation='relu', padding='same'),
        layers.BatchNormalization(),
        layers.MaxPooling2D((2, 2)),
        layers.Dropout(0.25),
        
        # Flatten and dense layers
        layers.Flatten(),
        layers.Dense(256, activation='relu'),
        layers.BatchNormalization(),
        layers.Dropout(0.5),
        layers.Dense(128, activation='relu'),
        layers.BatchNormalization(),
        layers.Dropout(0.5),
        layers.Dense(64, activation='relu'),
        layers.BatchNormalization(),
        layers.Dropout(0.5),
        
        # Output layer (regression for age)
        layers.Dense(1)
    ])
    
    # Compile model
    model.compile(
        optimizer='adam',
        loss='mse',
        metrics=['mae']
    )
    
    return model

def build_gender_model(input_shape: Tuple[int, int, int] = (200, 200, 3)) -> tf.keras.Model:
    """
    Build a CNN model for gender prediction.
    
    Args:
        input_shape: Input image shape
        
    Returns:
        Gender prediction model
    """
    model = models.Sequential([
        layers.Input(shape=input_shape),
        
        # First convolutional block
        layers.Conv2D(32, (3, 3), activation='relu', padding='same'),
        layers.BatchNormalization(),
        layers.MaxPooling2D((2, 2)),
        layers.Dropout(0.25),
        
        # Second convolutional block
        layers.Conv2D(64, (3, 3), activation='relu', padding='same'),
        layers.BatchNormalization(),
        layers.MaxPooling2D((2, 2)),
        layers.Dropout(0.25),
        
        # Third convolutional block
        layers.Conv2D(128, (3, 3), activation='relu', padding='same'),
        layers.BatchNormalization(),
        layers.MaxPooling2D((2, 2)),
        layers.Dropout(0.25),
        
        # Flatten and dense layers
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.BatchNormalization(),
        layers.Dropout(0.5),
        layers.Dense(64, activation='relu'),
        layers.BatchNormalization(),
        layers.Dropout(0.5),
        
        # Output layer (binary classification for gender)
        layers.Dense(1, activation='sigmoid')
    ])
    
    # Compile model
    model.compile(
        optimizer='adam',
        loss='binary_crossentropy',
        metrics=['accuracy']
    )
    
    return model

# Sample usage demonstration
if __name__ == "__main__":
    # Example of how to use the face detection module
    print("Face detection module for NutriGenius")
    
    # Example of model building
    print("Building sample age prediction model...")
    age_model = build_age_model()
    print(age_model.summary())
    
    print("\nBuilding sample gender prediction model...")
    gender_model = build_gender_model()
    print(gender_model.summary())
    
    # Note: Training would require the UTKFace dataset
    print("\nTo train these models, you'll need the UTKFace dataset.")
    print("See README.md for instructions on dataset preparation.") 