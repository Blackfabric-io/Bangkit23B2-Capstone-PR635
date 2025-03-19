# NutriGenius System Architecture

## Overview

This document outlines the system architecture for NutriGenius, a mobile application designed to address childhood stunting in Indonesia through technology and nutrition education. The architecture follows a cloud-based, microservices approach to ensure scalability, maintainability, and optimal performance.

## High-Level Architecture

NutriGenius follows a three-tier architecture consisting of:

1. **Client Tier**: Android mobile application with UI/UX components
2. **Application Tier**: Cloud-based services handling business logic and data processing
3. **Data Tier**: Data storage and management systems

```
┌───────────────┐     ┌────────────────────────────────┐     ┌─────────────────┐
│               │     │                                │     │                 │
│  Client Tier  │◄───►│        Application Tier        │◄───►│    Data Tier    │
│  (Mobile App) │     │  (Cloud Services & ML Models)  │     │  (Databases &   │
│               │     │                                │     │   Storage)      │
└───────────────┘     └────────────────────────────────┘     └─────────────────┘
```

## Detailed Architecture

![[Untitled diagram-2025-03-16-013336.png]]

### 1. Client Tier (Mobile Application)

The Android application serves as the primary interface for users and includes:

- **Presentation Layer**:
  - UI Components built with Android JetPack Compose
  - Material Design implementation
  - Activity/Fragment management
  - ViewModels for state management

- **User Interface Modules**:
  - User authentication and profile management
  - Child growth monitoring dashboard
  - Food scanning interface
  - Nutrition recommendations
  - Educational content viewer
  - Expert consultation interface

- **Client-Side Processing**:
  - Offline data caching using Room Database
  - Local validation and processing
  - Camera interface for food scanning
  - Secure credential management

- **Communication Layer**:
  - API clients (Retrofit)
  - Firebase integration
  - Real-time data synchronization

### 2. Application Tier (Cloud Services)

The application tier handles business logic, data processing, and integrations:

- **API Gateway**:
  - Request routing and load balancing
  - Authentication and authorization
  - Rate limiting and throttling
  - API versioning

- **Microservices**:
  - User Service: Account management and authentication
  - Profile Service: User profile and settings management
  - Nutrition Service: Nutritional analysis and recommendations
  - Education Service: Content management for articles and educational materials
  - Notification Service: Push notifications and reminders
  - Analytics Service: Usage tracking and reporting

- **Machine Learning Pipeline**:
  - Food Recognition Service: Image classification of food items
  - Nutrition Analysis Service: Nutritional content calculation
  - Growth Monitoring Service: Stunting risk assessment
  - Recommendation Engine: Personalized nutrition advice

- **Integration Services**:
  - External API connectors for health databases
  - Telemedicine integration
  - Health authority data services

### 3. Data Tier

The data tier manages persistent storage and data management:

- **Structured Data**:
  - Cloud SQL (MySQL): Relational data storage for user profiles, structured nutritional data
  - Firestore: NoSQL storage for flexible schema needs and real-time data

- **Unstructured Data**:
  - Cloud Storage: Image storage for food scanning and educational content
  - BigQuery: Analytics data for reporting and insights

- **Caching Layer**:
  - In-memory caching for frequently accessed data
  - Session data caching

- **Data Processing**:
  - ETL pipelines for data ingestion
  - Data aggregation for analytics

## Communication Flows

### Primary User Flows

1. **User Registration/Authentication**:
   ```
   Mobile App → API Gateway → User Service → Database
   ```

2. **Food Scanning and Analysis**:
   ```
   Mobile App (Camera) → API Gateway → Food Recognition Service → 
   Nutrition Analysis Service → Database → Mobile App (Results)
   ```

3. **Growth Monitoring**:
   ```
   Mobile App (Input Data) → API Gateway → Growth Monitoring Service → 
   Database → Mobile App (Visualization)
   ```

4. **Content Delivery**:
   ```
   Mobile App (Request) → API Gateway → Education Service → 
   Database/Storage → Mobile App (Display)
   ```

5. **Expert Consultation**:
   ```
   Mobile App (Request) → API Gateway → Profile Service → 
   Integration Services → External Providers → Mobile App
   ```

## Security Architecture

- **Authentication**: JWT-based authentication with OAuth 2.0
- **Data Encryption**: TLS for data in transit, encryption at rest for sensitive data
- **Authorization**: Role-based access control (RBAC)
- **API Security**: API keys, rate limiting, input validation
- **Compliance**: Adherence to healthcare data regulations

## Deployment Architecture

NutriGenius uses Google Cloud Platform (GCP) for its cloud infrastructure:

- **Compute**: Google Kubernetes Engine (GKE) for containerized services
- **Serverless**: Cloud Functions for event-driven processing
- **Storage**: Cloud Storage, Cloud SQL, Firestore
- **Networking**: Cloud DNS, Cloud CDN, Load Balancing
- **DevOps**: Cloud Build, Container Registry

## Scalability Considerations

The architecture is designed to scale horizontally to handle increasing user load:

- Containerized microservices allow independent scaling
- Auto-scaling based on usage metrics
- Load balancing across service instances
- Database read replicas for query-heavy operations
- Caching strategies to reduce database load

## Resilience and Availability

- **Redundancy**: Services deployed across multiple availability zones
- **Fault Tolerance**: Graceful degradation of services
- **Disaster Recovery**: Regular backups and recovery procedures
- **Monitoring**: Comprehensive logging and alerting

## Future Extensibility

The architecture allows for future expansion:

- Additional ML models for enhanced recommendations
- Integration with wearable devices
- Expansion to iOS platform
- Integration with government health systems
- Telehealth consultation features

## References

- [GCP Architecture Center](https://cloud.google.com/architecture)
- [Android Architecture Components](https://developer.android.com/topic/architecture)
- [Microservices Architecture Patterns](https://microservices.io/patterns/index.html)
