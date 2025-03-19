# NutriGenius Component Diagram

## Overview

This document presents the component diagram for the NutriGenius application, illustrating the key components, their relationships, and interactions. The component diagram follows the C4 model approach, focusing on the component-level view of the system.

## Component Diagram

![[Untitled diagram-2025-03-16-013336.png]]

## Component Descriptions

### Mobile Application Components

1. **UI Components**
   - Description: The presentation layer of the application
   - Responsibilities: Render interface elements, handle user interactions
   - Technologies: Android JetPack Compose, Material Design

2. **Authentication Module**
   - Description: Handles user authentication and security
   - Responsibilities: Login, registration, password management
   - Dependencies: API Client, Local Database

3. **Food Scanner**
   - Description: Interface for capturing and analyzing food images
   - Responsibilities: Camera access, image capture, result display
   - Dependencies: API Client, Food Recognition Service

4. **Profile Manager**
   - Description: Manages user and child profiles
   - Responsibilities: Profile creation, editing, deletion
   - Dependencies: API Client, Profile Service

5. **Growth Monitor**
   - Description: Tracking and visualization of child growth metrics
   - Responsibilities: Data entry, chart generation, status tracking
   - Dependencies: API Client, Growth Analysis Service

6. **Recommendation Engine Client**
   - Description: Client-side interface for nutrition recommendations
   - Responsibilities: Display recommendations, personalized advice
   - Dependencies: API Client, Recommendation Engine

7. **Educational Content**
   - Description: Interface for educational articles and resources
   - Responsibilities: Content browsing, searching, bookmarking
   - Dependencies: API Client, Education Service

8. **Consultation Module**
   - Description: Interface for expert consultation
   - Responsibilities: Scheduling, messaging, video calls
   - Dependencies: API Client, Telemedicine Connector

9. **Local Database**
   - Description: Client-side data persistence
   - Responsibilities: Offline data storage, caching
   - Technologies: Room Database

10. **API Client**
    - Description: Interface to backend services
    - Responsibilities: API communication, error handling
    - Technologies: Retrofit, OkHttp

### Cloud Backend Components

#### API Gateway

- Description: Entry point for all client-server communication
- Responsibilities: Request routing, authentication, load balancing
- Technologies: Cloud Endpoints, App Engine

#### Core Services

1. **User Service**
   - Description: Manages user accounts and authentication
   - Responsibilities: User registration, authentication, authorization
   - Dependencies: Cloud SQL, Cache Layer

2. **Profile Service**
   - Description: Manages user and child profiles
   - Responsibilities: Profile CRUD operations, data validation
   - Dependencies: Cloud SQL, Firestore

3. **Nutrition Service**
   - Description: Core service for nutritional data and analysis
   - Responsibilities: Nutritional data management, meal planning
   - Dependencies: Cloud SQL, Firestore, ML Components

4. **Education Service**
   - Description: Manages educational content
   - Responsibilities: Content storage, retrieval, categorization
   - Dependencies: Firestore, Cloud Storage

5. **Notification Service**
   - Description: Manages user notifications
   - Responsibilities: Push notifications, email alerts, reminders
   - Dependencies: Firestore, Firebase Cloud Messaging

6. **Analytics Service**
   - Description: Collects and processes usage data
   - Responsibilities: Data aggregation, reporting, insights
   - Dependencies: BigQuery

#### ML Components

1. **Food Recognition Service**
   - Description: Image analysis for food identification
   - Responsibilities: Image classification, food item detection
   - Technologies: TensorFlow, Cloud Vision API
   - Dependencies: Cloud Storage

2. **Nutrition Analysis Service**
   - Description: Analyzes nutritional content of identified foods
   - Responsibilities: Nutrient calculation, portion estimation
   - Technologies: TensorFlow, Custom ML models
   - Dependencies: Cloud SQL

3. **Growth Analysis Service**
   - Description: Analyzes child growth data for stunting risk
   - Responsibilities: Growth curve analysis, risk assessment
   - Technologies: Scikit-learn, Custom ML models
   - Dependencies: Cloud SQL

4. **Recommendation Engine**
   - Description: Generates personalized nutrition recommendations
   - Responsibilities: Meal suggestions, dietary advice
   - Technologies: TensorFlow, Custom ML models
   - Dependencies: Cloud SQL, Firestore

#### Integration Components

1. **External API Connector**
   - Description: Integrates with third-party APIs
   - Responsibilities: API communication, data transformation
   - Dependencies: Various external services

2. **Telemedicine Connector**
   - Description: Integrates with telemedicine services
   - Responsibilities: Appointment scheduling, video consultation
   - Dependencies: Telemedicine providers

3. **Health Authority Connector**
   - Description: Integrates with health authority databases
   - Responsibilities: Data exchange, compliance reporting
   - Dependencies: Government health systems

### Data Layer Components

1. **Cloud SQL**
   - Description: Relational database service
   - Responsibilities: Structured data storage (user data, child data, nutritional data)
   - Technologies: MySQL

2. **Firestore**
   - Description: NoSQL document database
   - Responsibilities: Semi-structured data storage (user preferences, content metadata)
   - Technologies: Firestore

3. **Cloud Storage**
   - Description: Object storage service
   - Responsibilities: Binary data storage (images, videos, documents)
   - Technologies: Google Cloud Storage

4. **BigQuery**
   - Description: Data warehouse and analytics service
   - Responsibilities: Large-scale data analysis, reporting
   - Technologies: BigQuery

5. **Cache Layer**
   - Description: In-memory caching service
   - Responsibilities: Temporary data storage, performance optimization
   - Technologies: Redis, Memcached

## Key Interactions

### Food Scanning Flow
1. User captures food image via Scanner component
2. Image is sent to Food Recognition Service through API Gateway
3. Food Recognition Service identifies food items
4. Nutrition Analysis Service calculates nutritional content
5. Results are stored in databases and returned to mobile application
6. UI displays nutritional information to user

### Growth Monitoring Flow
1. User enters child growth data via Monitor component
2. Data is sent to Growth Analysis Service through API Gateway
3. Growth Analysis Service processes data and assesses stunting risk
4. Results are stored in databases and returned to mobile application
5. UI displays growth charts and risk assessment to user

### Recommendation Flow
1. Profile data and food preferences are sent to Recommendation Engine
2. Recommendation Engine generates personalized advice
3. Recommendations are stored in databases and returned to mobile application
4. UI displays recommendations to user

## Design Considerations

### Modularity
Components are designed with high cohesion and low coupling to enable:
- Independent development and testing
- Easier maintenance and updates
- Team specialization (ML, mobile, backend)

### Scalability
The component architecture supports horizontal scaling:
- Stateless services can be replicated
- Database sharding for increased capacity
- Caching layer reduces database load

### Reliability
The system incorporates several reliability features:
- Redundant components to prevent single points of failure
- Graceful degradation when services are unavailable
- Local storage for offline functionality

### Security
Security considerations are implemented at multiple levels:
- Secure communication between components
- Authentication and authorization at service boundaries
- Data encryption for sensitive information

## Future Extensions

The component architecture is designed to accommodate future extensions:
- Additional ML models for enhanced analysis
- Integration with wearable devices for automated data collection
- Expansion to iOS platform
- Additional consultation services
- Enhanced analytics capabilities

## References

- [C4 Model for Software Architecture](https://c4model.com/)
- [Google Cloud Architecture Framework](https://cloud.google.com/architecture/framework)
- [Microservices Design Patterns](https://microservices.io/patterns/index.html)
