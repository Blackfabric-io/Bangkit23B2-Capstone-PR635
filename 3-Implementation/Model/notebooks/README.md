# NutriGenius Proof-of-Concept Notebooks

This directory contains Jupyter notebooks demonstrating prototype implementations of key ML capabilities for the NutriGenius proof-of-concept:

- `face_detection/`: Prototype for age/gender estimation from facial images
- `object_detection/`: Prototype for food item recognition in images
- `article_recommender/`: Prototype for simple content-based recommendation system

## Purpose of These Notebooks

These notebooks serve as **proof-of-concept demonstrations** rather than production implementations. They are designed to:

1. Demonstrate technical feasibility of key ML components
2. Provide working prototypes that can be integrated into a minimal viable product
3. Serve as educational examples of how these ML techniques can be implemented
4. Act as starting points for more sophisticated implementations if the project advances

## Simplified Approach

In line with our abstracted proof-of-concept strategy:

```python
# Example of simplified implementation approach
import os
import sys

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname("__file__"), '../..')))

# Import helper utilities
from src.utils.notebook_helper import setup_notebook, get_paths_from_config

# Load configuration and get standard paths
config = setup_notebook()
paths = get_paths_from_config(config, 'face_detection')  # Change model type as needed

# Use simplified datasets and models for prototype purposes
```

## Notebook Structure

Each component contains two main notebooks:

1. `1_EDA.ipynb`: Basic exploratory analysis using simplified datasets
   - Analyzes sample data sufficient for prototype demonstration
   - Focuses on key patterns rather than comprehensive analysis
   
2. `2_Model.ipynb`: Simplified model implementation
   - Implements basic ML functionality 
   - Uses transfer learning and pre-trained models where possible
   - Focuses on demonstration rather than optimization

## Prototype Limitations

These notebooks intentionally implement simplified versions with known limitations:

- **Smaller datasets**: Using minimal datasets sufficient for demonstration
- **Simplified models**: Favoring simpler architectures and pre-trained models
- **Limited optimization**: Minimal hyperparameter tuning and optimization
- **Focused scope**: Implementing only core functionality needed for the proof-of-concept

## Integration with Prototype Application

For guidance on integrating these ML components with the prototype application, refer to:
- Implementation Approaches documentation
- Pipeline documentation for model conversion and deployment

## Next Steps

If advancing beyond the proof-of-concept stage:

1. Expand datasets with more diverse and comprehensive data
2. Implement more sophisticated models with custom architectures
3. Perform proper hyperparameter optimization and model tuning
4. Add production-ready features like model monitoring and online learning 