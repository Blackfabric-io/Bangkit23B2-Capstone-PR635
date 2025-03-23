# NutriGenius Design Documentation

This directory contains all design artifacts for the NutriGenius application, supporting the implementation described in the main project README. These design documents serve as blueprints for the development process.

## Directory Structure

The design documentation is organized into three main categories:

### 1. Architecture (`1-Architecture/`)

This directory contains the technical architecture designs for NutriGenius, including:

- System architecture diagrams
- Component interaction flowcharts
- Cloud infrastructure design
- Machine learning pipeline architecture
- Mobile application architecture

These architecture designs support the three key learning paths described in the main README:
- Machine Learning implementation using TensorFlow
- Mobile Development for Android devices
- Cloud Computing infrastructure with API models

### 2. Database Schema (`2-Database-Schema/`)

This directory contains database designs and schema definitions:

- Entity-Relationship Diagrams (ERD)
- Schema definitions for:
  - User profiles and authentication
  - Child growth data storage
  - Nutritional information database
  - Educational content management
  - Food recognition data

These database designs align with the Cloud Computing infrastructure mentioned in the main README, particularly the MySQL, Firestore, and Cloud Storage components.

### 3. UI/UX (`3-UI-UX/`)

This directory contains user interface and user experience designs:

- Wireframes and mockups
- User flow diagrams
- Design system documentation
- Prototype screens
- Interaction models

These designs implement the Mobile Development path described in the main README, focusing on creating a user-friendly graphical interface that simplifies data entry for children's weight and height.

## Relationship to Implementation Progress

As noted in the main README, the overall project implementation is approximately 65% complete. The design artifacts in this directory reflect:

- [x] UI/UX mockup design (complete)
- [x] Core architecture setup (complete)
- [x] Database schema creation (complete)
- [ ] End-to-end integration design (in progress)

## Design Canvas

The `2-Design.canvas` file provides a visual overview of how all design components interconnect and support the key features described in the main README:

1. Nutrition Monitoring
2. Recommendations Feature
3. Nutrition Education
4. Food Scanning
5. Expert Consultation

## Proof of Concept Limitations

As stated in the main README disclaimer, these designs represent a proof of concept demonstration for Bangkit Academy capstone project. Due to healthcare data limitations, the designs utilize abstraction and generic data types where actual healthcare data would be used in a production environment.

## Next Steps

These design artifacts will guide the remaining 35% of implementation work, particularly focusing on:

1. ML model integration with the mobile app
2. Cloud services connection with the mobile app
3. End-to-end system testing

## Related Documentation

For implementation details, please refer to the `/3-Implementation` directory and the main project README. 