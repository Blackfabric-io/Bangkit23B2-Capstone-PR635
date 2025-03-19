# NutriGenius Model

This directory contains all ML model development resources for the NutriGenius application, following a structured data science project approach.

## Directory Structure

```
NutriGenius/Model/
├── notebooks/                     # Jupyter notebooks for data exploration and model development
│   ├── face_detection/            # Age classification from child's face
│   │   ├── 1_EDA.ipynb            # Exploratory Data Analysis 
│   │   └── 2_Model.ipynb          # Model development and evaluation
│   ├── object_detection/          # Food object detection
│   │   ├── 1_EDA.ipynb
│   │   └── 2_Model.ipynb
│   └── article_recommender/       # Nutrition article recommendation system
│       ├── 1_EDA.ipynb
│       └── 2_Model.ipynb
├── data/                          # All data-related resources
│   ├── raw/                       # Original, immutable data
│   │   ├── UTKFace/               # Face dataset for age classification
│   │   ├── test_images/           # Test images for food detection
│   │   └── articles/              # Nutrition articles dataset
│   └── processed/                 # Cleaned, transformed, ready-to-use data
├── models/                        # Trained and serialized models
│   ├── face_detection/            # Face/age detection models 
│   ├── object_detection/          # Food detection models
│   └── article_recommender/       # Article recommender models
├── src/                           # Source code for use in this project
│   ├── face_detection.py          # Scripts for face detection pipeline
│   ├── object_detection.py        # Scripts for object detection pipeline
│   ├── article_recommender.py     # Scripts for article recommendation
│   └── utils/                     # Utility functions used across the project
│       ├── data_processing.py     # Data loading and processing functions
│       └── visualization.py       # Visualization helpers
├── assets/                        # Deployment-ready files for the Android app
│   ├── ml/                        # ML models in TFLite format
│   │   ├── face_age_classifier.tflite
│   │   ├── age_labels.txt
│   │   ├── object_detector.tflite
│   │   └── object_labels.txt
│   └── data/                      # Data files needed by the app
│       └── articles_data.json     # Curated nutrition articles
└── requirements.txt               # Package dependencies
```

## Setup Instructions

1. Navigate to the Model directory:
   ```
   cd 3-Implementation/Model
   ```

2. Run the setup script to create the directory structure:
   ```
   powershell -ExecutionPolicy Bypass -File setup_structure.ps1
   ```

3. Create a Python virtual environment:
   ```
   python -m venv env
   env\Scripts\activate  # Windows
   source env/bin/activate  # Linux/Mac
   ```

4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Development Workflow

1. **Data Collection**: Place datasets in appropriate folders under `data/raw/`
2. **Exploration**: Use notebooks in `notebooks/` for EDA and prototyping
3. **Implementation**: Move production code to `src/` folder
4. **Model Training**: Train models in notebooks, save trained models to `models/`
5. **Model Conversion**: Convert models to TFLite format and save to `assets/ml/`
6. **Integration**: Android developers can use files in `assets/` folder

## Models Overview

1. **Face Detection & Age Classification**
   - Purpose: Detect child's face and classify age group
   - Implementation: MobileNetV2 + transfer learning
   - Input: Photo of child's face
   - Output: Age classification (0-2, 3-5, 6-9, 10-14 years)

2. **Food Object Detection** 
   - Purpose: Identify food items in photos
   - Implementation: EfficientDet Lite or SSD MobileNet
   - Input: Food image
   - Output: Bounding boxes around food items with class labels

3. **Article Recommender**
   - Purpose: Recommend nutrition articles based on text input
   - Implementation: TF-IDF vectorization + Naive Bayes classification
   - Input: Search query or relevant text
   - Output: Recommended nutrition articles by category

## Dataset Sources

- UTKFace dataset: https://susanqq.github.io/UTKFace/
- Food images: Can use Open Images or custom Indonesian food dataset
- Articles: Custom dataset of nutrition articles in Indonesian language 