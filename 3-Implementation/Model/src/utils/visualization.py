"""
Visualization utilities for the NutriGenius project.

This module contains functions for data visualization, model performance
visualization, and results visualization.
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import cv2
from typing import Dict, List, Tuple, Union, Optional, Any
import tensorflow as tf
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.metrics import precision_recall_curve, roc_curve, auc

# Import common utilities
from .common import create_directory

def set_plotting_style(style: str = 'whitegrid', context: str = 'notebook'):
    """
    Set the global plotting style.
    
    Args:
        style: Seaborn style
        context: Seaborn context
    """
    sns.set_style(style)
    sns.set_context(context)
    plt.rcParams['figure.figsize'] = (12, 8)
    plt.rcParams['axes.titlesize'] = 16
    plt.rcParams['axes.labelsize'] = 14
    plt.rcParams['xtick.labelsize'] = 12
    plt.rcParams['ytick.labelsize'] = 12

def plot_image_grid(
    images: List[np.ndarray],
    labels: Optional[List[str]] = None,
    n_cols: int = 4,
    figsize: Tuple[int, int] = None,
    title: str = "Image Grid",
    save_path: Optional[str] = None
) -> None:
    """
    Plot a grid of images.
    
    Args:
        images: List of images to display
        labels: Optional list of labels for images
        n_cols: Number of columns in the grid
        figsize: Figure size as (width, height)
        title: Figure title
        save_path: Optional path to save the figure
    """
    n_images = len(images)
    n_rows = (n_images + n_cols - 1) // n_cols
    
    if figsize is None:
        figsize = (4 * n_cols, 4 * n_rows)
    
    fig, axes = plt.subplots(n_rows, n_cols, figsize=figsize)
    fig.suptitle(title, fontsize=16)
    
    # Flatten axes array for easier indexing
    if n_rows == 1 and n_cols == 1:
        axes = np.array([axes])
    elif n_rows == 1 or n_cols == 1:
        axes = axes.flatten()
    
    # Plot each image
    for i, ax in enumerate(axes.flatten()):
        if i < n_images:
            # Check if image is grayscale and convert to RGB if needed
            if len(images[i].shape) == 2:
                img = cv2.cvtColor(images[i], cv2.COLOR_GRAY2RGB)
            elif len(images[i].shape) == 3 and images[i].shape[2] == 1:
                img = cv2.cvtColor(images[i], cv2.COLOR_GRAY2RGB)
            else:
                img = images[i]
                
            # Display image
            ax.imshow(img)
            
            # Add label if provided
            if labels is not None and i < len(labels):
                ax.set_title(labels[i])
                
            # Remove axis ticks
            ax.set_xticks([])
            ax.set_yticks([])
        else:
            # Hide empty subplots
            ax.axis('off')
    
    # Adjust spacing
    plt.tight_layout()
    fig.subplots_adjust(top=0.9)
    
    # Save figure if path provided
    if save_path:
        create_directory(os.path.dirname(save_path))
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.show()

def plot_training_history(
    history: Union[tf.keras.callbacks.History, Dict[str, List[float]]],
    metrics: Optional[List[str]] = None,
    figsize: Tuple[int, int] = (12, 5),
    save_path: Optional[str] = None
) -> None:
    """
    Plot training history for a model.
    
    Args:
        history: Training history object or dictionary
        metrics: List of metrics to plot (defaults to all available)
        figsize: Figure size as (width, height)
        save_path: Optional path to save the figure
    """
    # Convert to dictionary if it's a History object
    if isinstance(history, tf.keras.callbacks.History):
        history = history.history
    
    # Get all metrics if not specified
    if metrics is None:
        metrics = [m for m in history.keys() if not m.startswith('val_')]
    
    # Create figure
    plt.figure(figsize=figsize)
    
    # Plot each metric
    for i, metric in enumerate(metrics):
        plt.subplot(1, len(metrics), i+1)
        
        # Plot training metric
        plt.plot(history[metric], label=f'Training {metric}')
        
        # Plot validation metric if available
        val_metric = f'val_{metric}'
        if val_metric in history:
            plt.plot(history[val_metric], label=f'Validation {metric}')
        
        # Add labels and legend
        plt.title(f'{metric.capitalize()} Over Epochs')
        plt.xlabel('Epoch')
        plt.ylabel(metric.capitalize())
        plt.legend()
        plt.grid(True)
    
    # Adjust layout
    plt.tight_layout()
    
    # Save figure if path provided
    if save_path:
        create_directory(os.path.dirname(save_path))
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.show()

def plot_confusion_matrix(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    class_names: Optional[List[str]] = None,
    figsize: Tuple[int, int] = (10, 8),
    title: str = "Confusion Matrix",
    normalize: bool = False,
    save_path: Optional[str] = None
) -> None:
    """
    Plot a confusion matrix.
    
    Args:
        y_true: True class labels
        y_pred: Predicted class labels
        class_names: Names of classes
        figsize: Figure size as (width, height)
        title: Figure title
        normalize: Whether to normalize the confusion matrix
        save_path: Optional path to save the figure
    """
    # Compute confusion matrix
    cm = confusion_matrix(y_true, y_pred)
    
    # Normalize if requested
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        fmt = '.2f'
    else:
        fmt = 'd'
    
    # Create figure
    plt.figure(figsize=figsize)
    
    # Plot confusion matrix
    sns.heatmap(
        cm, 
        annot=True, 
        fmt=fmt, 
        cmap='Blues',
        xticklabels=class_names,
        yticklabels=class_names
    )
    
    # Add labels and title
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.title(title)
    
    # Adjust layout
    plt.tight_layout()
    
    # Save figure if path provided
    if save_path:
        create_directory(os.path.dirname(save_path))
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.show()
    
    # Print classification report
    if class_names:
        print("\nClassification Report:")
        print(classification_report(y_true, y_pred, target_names=class_names))
    else:
        print("\nClassification Report:")
        print(classification_report(y_true, y_pred))

def plot_distribution(
    data: Union[np.ndarray, pd.Series],
    title: str = "Distribution",
    xlabel: str = "Value",
    ylabel: str = "Frequency",
    bins: int = 30,
    kde: bool = True,
    figsize: Tuple[int, int] = (12, 6),
    save_path: Optional[str] = None
) -> None:
    """
    Plot a distribution of values.
    
    Args:
        data: Data to plot
        title: Plot title
        xlabel: X-axis label
        ylabel: Y-axis label
        bins: Number of histogram bins
        kde: Whether to include KDE curve
        figsize: Figure size as (width, height)
        save_path: Optional path to save the figure
    """
    plt.figure(figsize=figsize)
    
    # Plot distribution
    sns.histplot(data, bins=bins, kde=kde)
    
    # Add labels and title
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    
    # Save figure if path provided
    if save_path:
        create_directory(os.path.dirname(save_path))
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.show()
    
    # Print summary statistics
    if isinstance(data, pd.Series):
        print("\nSummary Statistics:")
        print(data.describe())
    else:
        print("\nSummary Statistics:")
        print({
            "count": len(data),
            "mean": np.mean(data),
            "std": np.std(data),
            "min": np.min(data),
            "25%": np.percentile(data, 25),
            "50%": np.median(data),
            "75%": np.percentile(data, 75),
            "max": np.max(data)
        })

def plot_roc_curve(
    y_true: np.ndarray,
    y_prob: np.ndarray,
    class_names: Optional[List[str]] = None,
    figsize: Tuple[int, int] = (10, 8),
    title: str = "ROC Curve",
    save_path: Optional[str] = None
) -> None:
    """
    Plot ROC curve for binary or multi-class classification.
    
    Args:
        y_true: True class labels (one-hot encoded for multi-class)
        y_prob: Predicted class probabilities
        class_names: Names of classes
        figsize: Figure size as (width, height)
        title: Figure title
        save_path: Optional path to save the figure
    """
    plt.figure(figsize=figsize)
    
    # Check if binary or multi-class
    if len(y_prob.shape) == 1 or y_prob.shape[1] == 1:
        # Binary classification
        fpr, tpr, _ = roc_curve(y_true, y_prob)
        roc_auc = auc(fpr, tpr)
        
        plt.plot(fpr, tpr, lw=2, label=f'ROC curve (AUC = {roc_auc:.2f})')
        
    else:
        # Multi-class classification
        n_classes = y_prob.shape[1]
        
        # If class_names not provided, create generic names
        if class_names is None:
            class_names = [f'Class {i}' for i in range(n_classes)]
        
        # Compute ROC curve and ROC area for each class
        fpr = dict()
        tpr = dict()
        roc_auc = dict()
        
        for i in range(n_classes):
            fpr[i], tpr[i], _ = roc_curve(
                y_true[:, i] if len(y_true.shape) > 1 else (y_true == i).astype(int),
                y_prob[:, i]
            )
            roc_auc[i] = auc(fpr[i], tpr[i])
        
        # Plot all ROC curves
        for i in range(n_classes):
            plt.plot(
                fpr[i], 
                tpr[i], 
                lw=2,
                label=f'{class_names[i]} (AUC = {roc_auc[i]:.2f})'
            )
    
    # Add diagonal line
    plt.plot([0, 1], [0, 1], 'k--', lw=2)
    
    # Add labels and title
    plt.title(title)
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.legend(loc="lower right")
    plt.grid(True)
    
    # Save figure if path provided
    if save_path:
        create_directory(os.path.dirname(save_path))
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.show()

def plot_feature_importance(
    feature_importance: np.ndarray,
    feature_names: List[str],
    top_n: int = 20,
    figsize: Tuple[int, int] = (12, 8),
    title: str = "Feature Importance",
    save_path: Optional[str] = None
) -> None:
    """
    Plot feature importance.
    
    Args:
        feature_importance: Array of feature importance values
        feature_names: Names of features
        top_n: Number of top features to display
        figsize: Figure size as (width, height)
        title: Figure title
        save_path: Optional path to save the figure
    """
    # Create DataFrame with feature names and importance
    features_df = pd.DataFrame({
        'Feature': feature_names,
        'Importance': feature_importance
    })
    
    # Sort by importance and select top N
    features_df = features_df.sort_values('Importance', ascending=False).head(top_n)
    
    # Create figure
    plt.figure(figsize=figsize)
    
    # Plot feature importance
    sns.barplot(x='Importance', y='Feature', data=features_df)
    
    # Add labels and title
    plt.title(title)
    plt.xlabel('Importance')
    plt.ylabel('Feature')
    plt.grid(True, axis='x')
    
    # Save figure if path provided
    if save_path:
        create_directory(os.path.dirname(save_path))
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.show()

def plot_model_predictions(
    model: tf.keras.Model,
    images: List[np.ndarray],
    true_labels: Optional[List[Any]] = None,
    class_names: Optional[List[str]] = None,
    figsize: Tuple[int, int] = None,
    n_cols: int = 4,
    preprocess_fn: Optional[callable] = None,
    save_path: Optional[str] = None
) -> None:
    """
    Plot model predictions on a set of images.
    
    Args:
        model: Trained model
        images: List of images to predict on
        true_labels: Optional list of true labels
        class_names: Optional list of class names
        figsize: Figure size as (width, height)
        n_cols: Number of columns in the grid
        preprocess_fn: Optional preprocessing function for images
        save_path: Optional path to save the figure
    """
    n_images = len(images)
    n_rows = (n_images + n_cols - 1) // n_cols
    
    if figsize is None:
        figsize = (4 * n_cols, 4 * n_rows)
    
    # Make predictions
    processed_images = []
    for img in images:
        # Apply preprocessing if provided
        if preprocess_fn:
            proc_img = preprocess_fn(img)
        else:
            # Default preprocessing (add batch dimension if needed)
            proc_img = img.copy()
            if len(proc_img.shape) == 3:
                proc_img = np.expand_dims(proc_img, axis=0)
        
        processed_images.append(proc_img)
    
    # Stack all images for batch prediction
    batch_images = np.vstack(processed_images)
    predictions = model.predict(batch_images)
    
    # Create figure
    fig, axes = plt.subplots(n_rows, n_cols, figsize=figsize)
    
    # Flatten axes array for easier indexing
    if n_rows == 1 and n_cols == 1:
        axes = np.array([axes])
    elif n_rows == 1 or n_cols == 1:
        axes = axes.flatten()
    
    # Plot each image and prediction
    for i, ax in enumerate(axes.flatten()):
        if i < n_images:
            # Display image
            ax.imshow(images[i])
            
            # Format prediction
            if len(predictions.shape) > 1 and predictions.shape[1] > 1:
                # Multi-class prediction
                pred_class = np.argmax(predictions[i])
                pred_prob = predictions[i][pred_class]
                
                if class_names:
                    pred_label = f"{class_names[pred_class]}: {pred_prob:.2f}"
                else:
                    pred_label = f"Class {pred_class}: {pred_prob:.2f}"
            else:
                # Binary or regression prediction
                pred_value = predictions[i][0]
                pred_label = f"Prediction: {pred_value:.2f}"
            
            # Add true label if provided
            if true_labels is not None and i < len(true_labels):
                if class_names and isinstance(true_labels[i], int):
                    true_label = class_names[true_labels[i]]
                else:
                    true_label = str(true_labels[i])
                
                title = f"True: {true_label}\n{pred_label}"
            else:
                title = pred_label
            
            ax.set_title(title)
            
            # Remove axis ticks
            ax.set_xticks([])
            ax.set_yticks([])
        else:
            # Hide empty subplots
            ax.axis('off')
    
    # Adjust spacing
    plt.tight_layout()
    
    # Save figure if path provided
    if save_path:
        create_directory(os.path.dirname(save_path))
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.show()

def plot_food_detections(
    image: np.ndarray,
    boxes: np.ndarray,
    class_names: List[str],
    scores: np.ndarray,
    figsize: Tuple[int, int] = (12, 10),
    title: str = "Food Detection Results",
    threshold: float = 0.5,
    save_path: Optional[str] = None
) -> None:
    """
    Plot food detection results on an image.
    
    Args:
        image: Input image
        boxes: Bounding box coordinates (normalized [y1, x1, y2, x2])
        class_names: Class names for each detection
        scores: Confidence scores for each detection
        figsize: Figure size as (width, height)
        title: Figure title
        threshold: Confidence threshold for displaying detections
        save_path: Optional path to save the figure
    """
    # Create figure
    plt.figure(figsize=figsize)
    
    # Create a copy of the image for drawing
    img_copy = image.copy()
    
    # Get image dimensions
    height, width = img_copy.shape[:2]
    
    # Filter detections by threshold
    valid_indices = scores >= threshold
    
    valid_boxes = boxes[valid_indices]
    valid_class_names = [class_names[i] for i in np.where(valid_indices)[0]]
    valid_scores = scores[valid_indices]
    
    # Draw each detection
    for box, class_name, score in zip(valid_boxes, valid_class_names, valid_scores):
        # Convert normalized coordinates to pixel coordinates
        ymin, xmin, ymax, xmax = box
        xmin = int(xmin * width)
        xmax = int(xmax * width)
        ymin = int(ymin * height)
        ymax = int(ymax * height)
        
        # Draw bounding box
        color = (0, 255, 0)  # Green
        cv2.rectangle(img_copy, (xmin, ymin), (xmax, ymax), color, 2)
        
        # Draw label
        label = f"{class_name}: {score:.2f}"
        cv2.putText(
            img_copy,
            label,
            (xmin, ymin - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            color,
            2
        )
    
    # Convert from BGR to RGB for display
    if len(img_copy.shape) == 3 and img_copy.shape[2] == 3:
        img_copy = cv2.cvtColor(img_copy, cv2.COLOR_BGR2RGB)
    
    # Display the image
    plt.imshow(img_copy)
    plt.title(f"{title}\n{len(valid_boxes)} detections with confidence >= {threshold}")
    plt.axis('off')
    
    # Save figure if path provided
    if save_path:
        create_directory(os.path.dirname(save_path))
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.show() 