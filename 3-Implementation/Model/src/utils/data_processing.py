"""
Data processing utilities for the NutriGenius project.

This module contains functions for data loading, preprocessing, 
augmentation, and other data-related operations.
"""

import os
import numpy as np
import pandas as pd
import cv2
import tensorflow as tf
from typing import Dict, List, Tuple, Union, Optional, Any, Callable
from sklearn.model_selection import train_test_split

# Import common utilities
from .common import create_directory

def load_image_data(
    data_dir: str,
    target_size: Tuple[int, int] = (224, 224),
    batch_size: int = 32,
    validation_split: float = 0.2,
    seed: int = 42
) -> Tuple[tf.data.Dataset, tf.data.Dataset]:
    """
    Load and prepare image data for training using TensorFlow's image_dataset_from_directory.
    
    Args:
        data_dir: Directory containing the image data
        target_size: Size to resize images to
        batch_size: Batch size for training
        validation_split: Fraction of data to use for validation
        seed: Random seed for reproducibility
        
    Returns:
        Tuple of (train_dataset, validation_dataset)
    """
    # Create training dataset
    train_dataset = tf.keras.utils.image_dataset_from_directory(
        data_dir,
        validation_split=validation_split,
        subset="training",
        seed=seed,
        image_size=target_size,
        batch_size=batch_size
    )
    
    # Create validation dataset
    validation_dataset = tf.keras.utils.image_dataset_from_directory(
        data_dir,
        validation_split=validation_split,
        subset="validation",
        seed=seed,
        image_size=target_size,
        batch_size=batch_size
    )
    
    return train_dataset, validation_dataset

def prepare_image_data_pipeline(
    dataset: tf.data.Dataset,
    cache: bool = True,
    shuffle_buffer_size: int = 1000,
    augment: bool = False,
    prefetch: bool = True
) -> tf.data.Dataset:
    """
    Prepare a TensorFlow dataset pipeline with performance optimizations.
    
    Args:
        dataset: Input TensorFlow dataset
        cache: Whether to cache the dataset
        shuffle_buffer_size: Buffer size for shuffling
        augment: Whether to apply data augmentation
        prefetch: Whether to prefetch data
        
    Returns:
        Optimized dataset
    """
    # Cache the dataset in memory if requested
    if cache:
        dataset = dataset.cache()
    
    # Shuffle the data
    dataset = dataset.shuffle(buffer_size=shuffle_buffer_size)
    
    # Apply data augmentation if requested
    if augment:
        dataset = dataset.map(
            data_augmentation,
            num_parallel_calls=tf.data.AUTOTUNE
        )
    
    # Use prefetch to overlap data preprocessing and model execution
    if prefetch:
        dataset = dataset.prefetch(buffer_size=tf.data.AUTOTUNE)
    
    return dataset

def data_augmentation(image, label):
    """
    Apply data augmentation to an image.
    
    Args:
        image: Input image tensor
        label: Input label
        
    Returns:
        Tuple of (augmented_image, label)
    """
    # Create a sequential model with augmentation layers
    augmentation_layers = tf.keras.Sequential([
        tf.keras.layers.RandomFlip("horizontal"),
        tf.keras.layers.RandomRotation(0.1),
        tf.keras.layers.RandomZoom(0.1),
        tf.keras.layers.RandomBrightness(0.1),
        tf.keras.layers.RandomContrast(0.1)
    ])
    
    # Apply the augmentation
    image = augmentation_layers(image)
    
    return image, label

def load_csv_data(
    file_path: str,
    test_size: float = 0.2,
    random_state: int = 42
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Load data from a CSV file and split into train and test sets.
    
    Args:
        file_path: Path to the CSV file
        test_size: Proportion of data to use for testing
        random_state: Random seed for reproducibility
        
    Returns:
        Tuple of (train_df, test_df)
    """
    # Load the data
    df = pd.read_csv(file_path)
    
    # Split into train and test sets
    train_df, test_df = train_test_split(
        df, test_size=test_size, random_state=random_state
    )
    
    return train_df, test_df

def extract_utk_face_metadata(
    image_path: str
) -> Dict[str, Union[int, str]]:
    """
    Extract metadata from UTKFace dataset filename.
    
    Args:
        image_path: Path to the image file
        
    Returns:
        Dictionary with age, gender, and race information
    """
    try:
        # UTKFace filename format: [age]_[gender]_[race]_[date&time].jpg
        filename = os.path.basename(image_path)
        parts = filename.split('_')
        
        age = int(parts[0])
        gender = "male" if int(parts[1]) == 0 else "female"
        race_id = int(parts[2])
        
        # Map race_id to descriptive name
        race_map = {
            0: "White",
            1: "Black",
            2: "Asian",
            3: "Indian",
            4: "Others"
        }
        race = race_map.get(race_id, "Unknown")
        
        return {
            "age": age,
            "gender": gender,
            "race": race,
            "race_id": race_id,
            "path": image_path
        }
    except (IndexError, ValueError) as e:
        return {
            "age": -1,
            "gender": "unknown",
            "race": "unknown",
            "race_id": -1,
            "path": image_path,
            "error": str(e)
        }

def process_utk_face_dataset(
    dataset_dir: str,
    output_csv_path: str = None
) -> pd.DataFrame:
    """
    Process the UTKFace dataset and create a metadata CSV file.
    
    Args:
        dataset_dir: Directory containing UTKFace images
        output_csv_path: Optional path to save metadata CSV
        
    Returns:
        DataFrame with image metadata
    """
    # Get all image paths
    image_extensions = ['.jpg', '.jpeg', '.png']
    image_paths = []
    
    for root, _, files in os.walk(dataset_dir):
        for file in files:
            if any(file.lower().endswith(ext) for ext in image_extensions):
                image_paths.append(os.path.join(root, file))
    
    # Extract metadata for each image
    metadata = []
    for path in image_paths:
        try:
            info = extract_utk_face_metadata(path)
            if info["age"] >= 0:  # Skip invalid entries
                metadata.append(info)
        except Exception as e:
            print(f"Error processing {path}: {e}")
    
    # Create DataFrame
    df = pd.DataFrame(metadata)
    
    # Save to CSV if path is provided
    if output_csv_path:
        create_directory(os.path.dirname(output_csv_path))
        df.to_csv(output_csv_path, index=False)
        print(f"Saved metadata to {output_csv_path}")
    
    return df

def normalize_image(image: np.ndarray) -> np.ndarray:
    """
    Normalize image pixel values to [0, 1].
    
    Args:
        image: Input image array
        
    Returns:
        Normalized image
    """
    return image.astype(np.float32) / 255.0

def resize_image(
    image: np.ndarray, 
    target_size: Tuple[int, int] = (224, 224)
) -> np.ndarray:
    """
    Resize an image to the target size.
    
    Args:
        image: Input image array
        target_size: Target size (width, height)
        
    Returns:
        Resized image
    """
    return cv2.resize(image, target_size)

def create_tf_dataset_from_dataframe(
    df: pd.DataFrame,
    image_col: str,
    label_col: str,
    preprocess_fn: Callable = None,
    batch_size: int = 32,
    shuffle: bool = True,
    seed: int = 42
) -> tf.data.Dataset:
    """
    Create a TensorFlow dataset from a pandas DataFrame.
    
    Args:
        df: Input DataFrame
        image_col: Column containing image paths
        label_col: Column containing labels
        preprocess_fn: Optional preprocessing function
        batch_size: Batch size
        shuffle: Whether to shuffle the data
        seed: Random seed for shuffling
        
    Returns:
        TensorFlow dataset
    """
    # Create lists of image paths and labels
    image_paths = df[image_col].tolist()
    labels = df[label_col].tolist()
    
    # Create a dataset of image paths and labels
    dataset = tf.data.Dataset.from_tensor_slices((image_paths, labels))
    
    # Define a function to load and preprocess images
    def load_and_preprocess(path, label):
        # Read the image file
        img = tf.io.read_file(path)
        # Decode the image
        img = tf.image.decode_image(img, expand_animations=False)
        # Apply custom preprocessing if provided
        if preprocess_fn:
            img = preprocess_fn(img)
        return img, label
    
    # Apply the load and preprocess function
    dataset = dataset.map(load_and_preprocess, num_parallel_calls=tf.data.AUTOTUNE)
    
    # Shuffle if requested
    if shuffle:
        dataset = dataset.shuffle(buffer_size=len(df), seed=seed)
    
    # Batch the data
    dataset = dataset.batch(batch_size)
    
    # Optimize performance
    dataset = dataset.prefetch(buffer_size=tf.data.AUTOTUNE)
    
    return dataset

# Example preprocessing function for article text data
def preprocess_text_data(
    df: pd.DataFrame,
    text_columns: List[str],
    combined_column: str = 'text_combined'
) -> pd.DataFrame:
    """
    Preprocess text data for NLP tasks.
    
    Args:
        df: Input DataFrame
        text_columns: List of columns containing text
        combined_column: Name for the combined text column
        
    Returns:
        DataFrame with preprocessed text
    """
    # Create a copy to avoid modifying the original
    df_processed = df.copy()
    
    # Combine text columns
    df_processed[combined_column] = df_processed[text_columns].fillna('').agg(' '.join, axis=1)
    
    # Convert to lowercase
    df_processed[combined_column] = df_processed[combined_column].str.lower()
    
    # Remove special characters and extra whitespace
    df_processed[combined_column] = df_processed[combined_column].str.replace(
        r'[^\w\s]', ' ', regex=True
    ).str.replace(r'\s+', ' ', regex=True).str.strip()
    
    return df_processed 