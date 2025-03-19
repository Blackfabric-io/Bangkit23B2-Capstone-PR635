"""
Food object detection module for NutriGenius.

This module implements food object detection and classification
using pre-trained models fine-tuned for food recognition.
"""

import os
import cv2
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
from typing import Dict, List, Tuple, Union, Optional, Any

# Import common utilities
from utils.common import (
    load_config,
    create_directory,
    save_model,
    load_model,
    plot_training_history,
    convert_to_tflite,
    preprocess_image
)

class FoodDetector:
    """Food detector and classifier for nutritional recommendations."""
    
    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize the food detector model.
        
        Args:
            config_path: Optional path to configuration file
        """
        self.config = {}
        if config_path and os.path.exists(config_path):
            self.config = load_config(config_path)
        
        # Set default configurations
        self.detection_threshold = self.config.get('detection_threshold', 0.5)
        self.model_path = self.config.get('model_path', None)
        self.labels_path = self.config.get('labels_path', None)
        self.input_size = self.config.get('input_size', (224, 224))
        
        # Load model if path is provided
        self.model = None
        if self.model_path and os.path.exists(self.model_path):
            self.model = load_model(self.model_path)
        
        # Load class labels if path is provided
        self.labels = []
        if self.labels_path and os.path.exists(self.labels_path):
            with open(self.labels_path, 'r') as f:
                self.labels = [line.strip() for line in f.readlines()]
    
    def load_pretrained_model(self) -> None:
        """
        Load a pre-trained object detection model from TensorFlow Hub.
        """
        # For demonstration, load a pre-trained EfficientDet model
        model_url = "https://tfhub.dev/tensorflow/efficientdet/d0/1"
        self.model = hub.load(model_url)
        print(f"Loaded pre-trained model from: {model_url}")
    
    def preprocess_image(self, image_path: str) -> np.ndarray:
        """
        Preprocess an image for food detection.
        
        Args:
            image_path: Path to the image file
            
        Returns:
            Preprocessed image as numpy array
        """
        # Load image
        img = tf.io.read_file(image_path)
        img = tf.image.decode_image(img, channels=3)
        
        # Convert to float and resize
        img = tf.image.convert_image_dtype(img, tf.float32)
        img = tf.image.resize(img, self.input_size)
        
        # Add batch dimension
        img = tf.expand_dims(img, axis=0)
        
        return img
    
    def detect_food(self, image: Union[str, np.ndarray, tf.Tensor]) -> Dict[str, Any]:
        """
        Detect food objects in an image.
        
        Args:
            image: Image path or numpy array
            
        Returns:
            Dictionary with detection results
        """
        if self.model is None:
            raise ValueError("Model not loaded. Please provide a valid model path or load a pre-trained model.")
        
        # Preprocess image
        if isinstance(image, str):
            img = self.preprocess_image(image)
        elif isinstance(image, np.ndarray):
            # Convert numpy array to tensor
            img = tf.convert_to_tensor(image, dtype=tf.float32)
            img = tf.image.resize(img, self.input_size)
            img = tf.expand_dims(img, axis=0)
        else:
            img = image
        
        # Run detection
        detections = self.model(img)
        
        # Process results
        result = self._process_detections(detections)
        
        return result
    
    def _process_detections(self, detections: Dict[str, tf.Tensor]) -> Dict[str, Any]:
        """
        Process the raw detection results.
        
        Args:
            detections: Raw detections from model
            
        Returns:
            Processed detection results
        """
        # Extract detection components
        boxes = detections['detection_boxes'][0].numpy()
        scores = detections['detection_scores'][0].numpy()
        classes = detections['detection_classes'][0].numpy().astype(np.int32)
        
        # Filter by threshold
        valid_indices = scores >= self.detection_threshold
        
        valid_boxes = boxes[valid_indices]
        valid_scores = scores[valid_indices]
        valid_classes = classes[valid_indices]
        
        # Convert class indices to class names if labels are available
        class_names = []
        if self.labels:
            for class_id in valid_classes:
                if 0 <= class_id < len(self.labels):
                    class_names.append(self.labels[class_id])
                else:
                    class_names.append(f"Class {class_id}")
        else:
            class_names = [f"Class {class_id}" for class_id in valid_classes]
        
        # Combine results
        result = {
            'boxes': valid_boxes,
            'scores': valid_scores,
            'classes': valid_classes,
            'class_names': class_names
        }
        
        return result
    
    def draw_detections(self, image: np.ndarray, detections: Dict[str, Any]) -> np.ndarray:
        """
        Draw detection results on the image.
        
        Args:
            image: Input image
            detections: Detection results from detect_food method
            
        Returns:
            Image with detection boxes and labels
        """
        # Create a copy of the image
        img_with_detections = image.copy()
        
        # Get image dimensions
        height, width = img_with_detections.shape[:2]
        
        # Draw each detection
        for i, (box, score, class_name) in enumerate(zip(
            detections['boxes'], 
            detections['scores'], 
            detections['class_names'])
        ):
            # Convert normalized coordinates to pixel coordinates
            ymin, xmin, ymax, xmax = box
            xmin = int(xmin * width)
            xmax = int(xmax * width)
            ymin = int(ymin * height)
            ymax = int(ymax * height)
            
            # Draw bounding box
            cv2.rectangle(
                img_with_detections, 
                (xmin, ymin), 
                (xmax, ymax), 
                (0, 255, 0), 
                2
            )
            
            # Draw label
            label = f"{class_name}: {score:.2f}"
            cv2.putText(
                img_with_detections, 
                label, 
                (xmin, ymin - 10), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.5, 
                (0, 255, 0), 
                2
            )
        
        return img_with_detections
    
    def get_nutrition_info(self, food_items: List[str]) -> Dict[str, Dict[str, float]]:
        """
        Get nutrition information for detected food items.
        
        Args:
            food_items: List of detected food item names
            
        Returns:
            Dictionary with nutrition information for each food item
        """
        # In a real implementation, this would query a database or API
        # For demonstration, return dummy data
        
        # Sample nutrition data (per 100g)
        nutrition_data = {
            "apple": {
                "calories": 52,
                "protein": 0.3,
                "carbs": 14.0,
                "fat": 0.2,
                "fiber": 2.4
            },
            "banana": {
                "calories": 89,
                "protein": 1.1,
                "carbs": 22.8,
                "fat": 0.3,
                "fiber": 2.6
            },
            "orange": {
                "calories": 47,
                "protein": 0.9,
                "carbs": 11.8,
                "fat": 0.1,
                "fiber": 2.4
            },
            "pizza": {
                "calories": 266,
                "protein": 11.0,
                "carbs": 33.0,
                "fat": 10.0,
                "fiber": 2.5
            },
            "burger": {
                "calories": 295,
                "protein": 17.0,
                "carbs": 31.0,
                "fat": 14.0,
                "fiber": 1.0
            }
        }
        
        # Get nutrition info for each detected food item
        result = {}
        for food in food_items:
            # Convert to lowercase for matching
            food_lower = food.lower()
            
            # Check if food is in our database
            if food_lower in nutrition_data:
                result[food] = nutrition_data[food_lower]
            else:
                # Default values for unknown foods
                result[food] = {
                    "calories": 0,
                    "protein": 0,
                    "carbs": 0,
                    "fat": 0,
                    "fiber": 0,
                    "note": "Nutrition data not available for this item"
                }
        
        return result

def build_food_classification_model(
    num_classes: int, 
    input_shape: Tuple[int, int, int] = (224, 224, 3)
) -> tf.keras.Model:
    """
    Build a CNN model for food classification using transfer learning.
    
    Args:
        num_classes: Number of food classes to predict
        input_shape: Input image shape
        
    Returns:
        Food classification model
    """
    # Use MobileNetV2 as base model
    base_model = tf.keras.applications.MobileNetV2(
        input_shape=input_shape,
        include_top=False,
        weights='imagenet'
    )
    
    # Freeze the base model
    base_model.trainable = False
    
    # Add classification head
    model = tf.keras.Sequential([
        base_model,
        tf.keras.layers.GlobalAveragePooling2D(),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(num_classes, activation='softmax')
    ])
    
    # Compile model
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    
    return model

# Sample usage demonstration
if __name__ == "__main__":
    # Example of how to use the food detection module
    print("Food detection module for NutriGenius")
    
    # Create food detector
    detector = FoodDetector()
    
    # Example of model building
    print("Building sample food classification model...")
    model = build_food_classification_model(num_classes=10)
    print(model.summary())
    
    # Note: Training would require a food image dataset
    print("\nTo train this model, you'll need a food image dataset.")
    print("See README.md for instructions on dataset preparation.")
    
    # Example of loading a pre-trained model
    print("\nFor quick testing, you can load a pre-trained model:")
    print("detector.load_pretrained_model()") 