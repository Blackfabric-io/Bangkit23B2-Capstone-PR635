"""
Common utility functions for the NutriGenius project.
This module provides common utilities for file operations, configuration management,
and other shared functionality across the project.
"""

import os
import yaml
import logging
import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, List, Union, Any, Tuple
from datetime import datetime
import tensorflow as tf

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def get_project_root():
    """
    Get the absolute path to the project root directory.
    This is useful for referencing files from anywhere in the project.
    
    Returns:
        str: Absolute path to the project root directory
    """
    # This function assumes it's always in src/utils/common.py
    # relative to the project root
    current_file_path = os.path.abspath(__file__)
    utils_dir = os.path.dirname(current_file_path)
    src_dir = os.path.dirname(utils_dir)
    return os.path.dirname(src_dir)

def load_config(config_path: str) -> Dict[str, Any]:
    """
    Load configuration from a YAML file.
    
    Args:
        config_path: Path to the YAML configuration file
        
    Returns:
        Dictionary containing configuration parameters
    """
    try:
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
        logger.info(f"Configuration loaded from {config_path}")
        return config
    except Exception as e:
        logger.error(f"Error loading configuration: {e}")
        raise

def create_directory(directory: str) -> None:
    """
    Create directory if it doesn't exist.
    
    Args:
        directory: Directory path to create
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
        logger.info(f"Created directory: {directory}")

def save_model(model: tf.keras.Model, save_path: str) -> None:
    """
    Save a TensorFlow model to the specified path.
    
    Args:
        model: TensorFlow model to save
        save_path: Path to save the model
    """
    try:
        create_directory(os.path.dirname(save_path))
        model.save(save_path)
        logger.info(f"Model saved to {save_path}")
    except Exception as e:
        logger.error(f"Error saving model: {e}")
        raise

def load_model(model_path: str) -> tf.keras.Model:
    """
    Load a TensorFlow model from the specified path.
    
    Args:
        model_path: Path to the saved model
        
    Returns:
        Loaded TensorFlow model
    """
    try:
        model = tf.keras.models.load_model(model_path)
        logger.info(f"Model loaded from {model_path}")
        return model
    except Exception as e:
        logger.error(f"Error loading model: {e}")
        raise

def plot_training_history(history: Dict[str, List[float]], save_path: str = None) -> None:
    """
    Plot training history metrics.
    
    Args:
        history: Dictionary containing training history
        save_path: Optional path to save the plot
    """
    plt.figure(figsize=(12, 5))
    
    # Plot training & validation accuracy values
    plt.subplot(1, 2, 1)
    if 'accuracy' in history:
        plt.plot(history['accuracy'])
    if 'val_accuracy' in history:
        plt.plot(history['val_accuracy'])
    plt.title('Model Accuracy')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Validation'], loc='upper left')
    
    # Plot training & validation loss values
    plt.subplot(1, 2, 2)
    if 'loss' in history:
        plt.plot(history['loss'])
    if 'val_loss' in history:
        plt.plot(history['val_loss'])
    plt.title('Model Loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Validation'], loc='upper left')
    
    plt.tight_layout()
    
    if save_path:
        create_directory(os.path.dirname(save_path))
        plt.savefig(save_path)
        logger.info(f"Training history plot saved to {save_path}")
    
    plt.show()

def get_timestamp() -> str:
    """
    Get current timestamp string for file naming.
    
    Returns:
        Timestamp string in format YYYYMMDD_HHMMSS
    """
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def convert_to_tflite(model: tf.keras.Model, save_path: str) -> None:
    """
    Convert TensorFlow model to TFLite format for mobile deployment.
    
    Args:
        model: TensorFlow model to convert
        save_path: Path to save the TFLite model
    """
    try:
        converter = tf.lite.TFLiteConverter.from_keras_model(model)
        tflite_model = converter.convert()
        
        create_directory(os.path.dirname(save_path))
        with open(save_path, 'wb') as f:
            f.write(tflite_model)
        
        logger.info(f"TFLite model saved to {save_path}")
    except Exception as e:
        logger.error(f"Error converting to TFLite: {e}")
        raise

def preprocess_image(image_path: str, target_size: Tuple[int, int] = (224, 224)) -> np.ndarray:
    """
    Load and preprocess an image for model inference.
    
    Args:
        image_path: Path to the image file
        target_size: Target size for resizing
        
    Returns:
        Preprocessed image as numpy array
    """
    try:
        img = tf.keras.preprocessing.image.load_img(
            image_path, target_size=target_size
        )
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = img_array / 255.0  # Normalize to [0,1]
        
        return img_array
    except Exception as e:
        logger.error(f"Error preprocessing image: {e}")
        raise 