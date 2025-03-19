"""
Notebook helper utilities for the NutriGenius project.
This module provides helper functions specifically for use in Jupyter notebooks
to ensure consistent path handling and configuration loading.
"""
import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf

from .common import get_project_root, load_config

def setup_notebook():
    """
    Set up the notebook environment with standard imports, configuration,
    and path settings. This helps ensure consistency across all notebooks.
    
    Returns:
        dict: Configuration dictionary loaded from model_config.yaml
    """
    # Set random seeds for reproducibility
    np.random.seed(42)
    tf.random.set_seed(42)
    
    # Configure plots
    plt.style.use('seaborn-whitegrid')
    sns.set_context('notebook')
    
    # Ensure we can import from the project root
    project_root = get_project_root()
    if project_root not in sys.path:
        sys.path.append(project_root)
    
    # Load configuration
    config_path = os.path.join(project_root, 'config', 'model_config.yaml')
    config = load_config(config_path)
    
    print("Notebook environment setup complete.")
    print(f"Project root: {project_root}")
    print(f"Configuration loaded from: {config_path}")
    
    return config

def get_paths_from_config(config, model_type):
    """
    Extract relevant paths from the configuration for the specified model type.
    
    Args:
        config (dict): Configuration dictionary
        model_type (str): Type of model ('face_detection', 'food_detection', or 'article_recommender')
    
    Returns:
        dict: Dictionary of paths for the specified model
    """
    paths = {}
    
    # Dataset paths
    if model_type == 'face_detection':
        paths['raw_data_dir'] = config['dataset']['face']['train_dir']
        paths['processed_data_dir'] = config['dataset']['face']['processed_dir']
        paths['metadata_file'] = config['dataset']['face']['metadata_file']
        paths['age_model_path'] = config['model_paths']['face_detection']['age_model']
        paths['gender_model_path'] = config['model_paths']['face_detection']['gender_model']
        paths['tflite_age_path'] = config['model_paths']['face_detection']['tflite_age_model']
        paths['tflite_gender_path'] = config['model_paths']['face_detection']['tflite_gender_model']
    
    elif model_type == 'food_detection':
        paths['raw_data_dir'] = config['dataset']['food']['train_dir']
        paths['processed_data_dir'] = config['dataset']['food']['processed_dir']
        paths['labels_file'] = config['dataset']['food']['labels_file']
        paths['model_path'] = config['model_paths']['food_detection']['model']
        paths['tflite_model_path'] = config['model_paths']['food_detection']['tflite_model']
        paths['labels_path'] = config['model_paths']['food_detection']['labels']
    
    elif model_type == 'article_recommender':
        paths['data_file'] = config['dataset']['articles']['data_file']
        paths['processed_file'] = config['dataset']['articles']['processed_file']
        paths['model_path'] = config['model_paths']['article_recommender']['model']
    
    else:
        raise ValueError(f"Unknown model type: {model_type}")
    
    # Create directories for all paths
    for path in paths.values():
        if isinstance(path, str):
            dir_path = os.path.dirname(path)
            if dir_path:
                os.makedirs(dir_path, exist_ok=True)
    
    return paths

def example_usage():
    """
    Example usage of the notebook helper functions.
    This demonstrates how to use these functions in a notebook.
    """
    print("Example usage of notebook_helper:")
    print("--------------------------------")
    print("# Add this at the beginning of your notebook:")
    print("from src.utils.notebook_helper import setup_notebook, get_paths_from_config")
    print("config = setup_notebook()")
    print("paths = get_paths_from_config(config, 'face_detection')")
    print("")
    print("# Now you can use paths in a standardized way:")
    print("print(f\"Raw data directory: {paths['raw_data_dir']}\")")
    print("print(f\"Model output path: {paths['age_model_path']}\")") 