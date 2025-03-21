# Face Detection Models (v1.0.0)

This folder contains trained models for age estimation and gender classification.

## Models

- **Age Estimation**: Predicts age from facial images
- **Gender Classification**: Predicts gender (male/female) from facial images

## Usage

```python
# Load models
age_model = tf.keras.models.load_model('age_model')
gender_model = tf.keras.models.load_model('gender_model')

# Preprocess image
img = preprocess_image(image_path)  # Scale to [0,1] and resize to (200,200)

# Predict
age = age_model.predict(np.expand_dims(img, axis=0))[0][0]
gender_prob = gender_model.predict(np.expand_dims(img, axis=0))[0][0]
gender = 'Female' if gender_prob > 0.5 else 'Male'
```
