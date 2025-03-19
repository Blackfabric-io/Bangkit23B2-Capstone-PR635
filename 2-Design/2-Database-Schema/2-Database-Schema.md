# NutriGenius Database Schema

## Overview

This document outlines the database schema for the NutriGenius application. The data storage strategy employs a hybrid approach using relational databases (Cloud SQL/MySQL) for structured data with well-defined relationships, and NoSQL databases (Firestore) for flexible, rapidly changing data and real-time features.

## Database Architecture

NutriGenius uses the following data storage components:

1. **Cloud SQL (MySQL)**: For structured data with complex relationships
2. **Firestore**: For semi-structured data requiring flexibility and real-time capabilities
3. **Cloud Storage**: For binary assets (images, documents)
4. **BigQuery**: For analytics and reporting data

## Relational Database Schema (Cloud SQL/MySQL)

### Entity-Relationship Diagram

![[NG-V1.jpg]]
### Table Definitions

#### Users and Authentication

##### 1. USERS
- **Purpose**: Stores user account information
- **Primary Key**: `user_id` (UUID)
- **Attributes**:
  - `email` (VARCHAR(255), UNIQUE): User's email address
  - `password_hash` (VARCHAR(255)): Hashed password
  - `full_name` (VARCHAR(255)): User's full name
  - `phone_number` (VARCHAR(20)): User's phone number
  - `created_at` (DATETIME): Account creation timestamp
  - `last_login` (DATETIME): Last login timestamp
  - `is_active` (BOOLEAN): Account status

##### 2. USER_PREFERENCES
- **Purpose**: Stores user preferences and settings
- **Primary Key**: `preference_id` (UUID)
- **Foreign Key**: `user_id` references USERS(user_id)
- **Attributes**:
  - `preference_key` (VARCHAR(50)): Setting name/key
  - `preference_value` (VARCHAR(255)): Setting value
  - `updated_at` (DATETIME): Last updated timestamp

#### Child Data and Growth Monitoring

##### 3. CHILDREN
- **Purpose**: Stores information about children
- **Primary Key**: `child_id` (UUID)
- **Foreign Key**: `user_id` references USERS(user_id)
- **Attributes**:
  - `name` (VARCHAR(255)): Child's name
  - `birth_date` (DATE): Child's birth date
  - `gender` (CHAR(1)): 'M' for male, 'F' for female
  - `birth_weight` (FLOAT): Birth weight in kg
  - `birth_height` (FLOAT): Birth height in cm
  - `medical_notes` (TEXT): Any medical conditions or notes
  - `created_at` (DATETIME): Record creation timestamp
  - `updated_at` (DATETIME): Record update timestamp

##### 4. GROWTH_MEASUREMENTS
- **Purpose**: Tracks a child's growth measurements over time
- **Primary Key**: `measurement_id` (UUID)
- **Foreign Key**: `child_id` references CHILDREN(child_id)
- **Attributes**:
  - `measure_date` (DATE): Date of measurement
  - `weight_kg` (FLOAT): Weight in kilograms
  - `height_cm` (FLOAT): Height in centimeters
  - `head_circumference_cm` (FLOAT): Head circumference in centimeters
  - `bmi` (FLOAT): Calculated BMI
  - `measurement_method` (VARCHAR(50)): How measurement was taken
  - `measured_by` (VARCHAR(100)): Person who took measurement
  - `created_at` (DATETIME): Record creation timestamp

##### 5. GROWTH_STANDARDS
- **Purpose**: Stores reference data for normal growth
- **Primary Key**: `standard_id` (UUID)
- **Attributes**:
  - `standard_type` (VARCHAR(50)): Type of standard (WHO, CDC, etc.)
  - `gender` (CHAR(1)): 'M' for male, 'F' for female
  - `age_months` (INT): Age in months
  - `weight_p3` (FLOAT): 3rd percentile weight
  - `weight_p15` (FLOAT): 15th percentile weight
  - `weight_p50` (FLOAT): 50th percentile weight (median)
  - `weight_p85` (FLOAT): 85th percentile weight
  - `weight_p97` (FLOAT): 97th percentile weight
  - `height_p3` (FLOAT): 3rd percentile height
  - `height_p15` (FLOAT): 15th percentile height
  - `height_p50` (FLOAT): 50th percentile height (median)
  - `height_p85` (FLOAT): 85th percentile height
  - `height_p97` (FLOAT): 97th percentile height
  - `source` (VARCHAR(100)): Source of the standard data

##### 6. DIETARY_RESTRICTIONS
- **Purpose**: Records dietary restrictions or allergies
- **Primary Key**: `restriction_id` (UUID)
- **Foreign Key**: `child_id` references CHILDREN(child_id)
- **Attributes**:
  - `restriction_type` (VARCHAR(50)): Type of restriction (allergy, intolerance, etc.)
  - `food_item` (VARCHAR(100)): Restricted food
  - `description` (TEXT): Detailed description
  - `severity` (VARCHAR(50)): Severity level
  - `created_at` (DATETIME): Record creation timestamp

#### Nutrition and Food Data

##### 7. FOOD_ITEMS
- **Purpose**: Catalog of food items
- **Primary Key**: `food_id` (UUID)
- **Foreign Key**: `food_category_id` references FOOD_CATEGORIES(category_id)
- **Attributes**:
  - `food_name` (VARCHAR(255)): Name of the food
  - `description` (VARCHAR(500)): Description of the food
  - `typical_portion_size` (FLOAT): Standard portion size
  - `portion_unit` (VARCHAR(20)): Unit of measurement for portion
  - `image_url` (VARCHAR(255)): URL to food image
  - `verified` (BOOLEAN): Whether nutrition data is verified
  - `created_at` (DATETIME): Record creation timestamp
  - `updated_at` (DATETIME): Record update timestamp

##### 8. FOOD_NUTRIENTS
- **Purpose**: Nutritional content of food items
- **Primary Key**: `nutrient_id` (UUID)
- **Foreign Key**: `food_id` references FOOD_ITEMS(food_id)
- **Attributes**:
  - `nutrient_name` (VARCHAR(100)): Name of nutrient
  - `amount` (FLOAT): Amount of nutrient
  - `unit` (VARCHAR(20)): Unit of measurement
  - `daily_value_percentage` (FLOAT): Percentage of daily value
  - `source` (VARCHAR(100)): Source of nutrition data

##### 9. FOOD_CATEGORIES
- **Purpose**: Categorizes food items
- **Primary Key**: `category_id` (UUID)
- **Attributes**:
  - `category_name` (VARCHAR(100)): Category name
  - `description` (VARCHAR(255)): Category description
  - `parent_category_id` (VARCHAR(36)): Self-reference for hierarchy

##### 10. MEAL_LOGS
- **Purpose**: Records meals consumed by children
- **Primary Key**: `meal_log_id` (UUID)
- **Foreign Key**: `child_id` references CHILDREN(child_id)
- **Attributes**:
  - `meal_time` (DATETIME): When the meal was consumed
  - `meal_type` (VARCHAR(50)): Type of meal (breakfast, lunch, etc.)
  - `notes` (TEXT): Additional notes
  - `image_url` (VARCHAR(255)): URL to meal image
  - `created_at` (DATETIME): Record creation timestamp

##### 11. MEAL_INGREDIENTS
- **Purpose**: Details of food items in a meal
- **Primary Key**: `ingredient_id` (UUID)
- **Foreign Keys**:
  - `meal_log_id` references MEAL_LOGS(meal_log_id)
  - `food_id` references FOOD_ITEMS(food_id)
- **Attributes**:
  - `quantity` (FLOAT): Amount of food
  - `unit` (VARCHAR(20)): Unit of measurement
  - `preparation_notes` (TEXT): How food was prepared

#### Expert Consultation

##### 12. NUTRITIONISTS
- **Purpose**: Information about nutrition experts
- **Primary Key**: `nutritionist_id` (UUID)
- **Attributes**:
  - `full_name` (VARCHAR(255)): Nutritionist's name
  - `credentials` (VARCHAR(255)): Educational credentials
  - `specialization` (VARCHAR(100)): Area of expertise
  - `bio` (TEXT): Professional biography
  - `image_url` (VARCHAR(255)): Profile image URL
  - `contact_email` (VARCHAR(255)): Contact email
  - `contact_phone` (VARCHAR(20)): Contact phone number
  - `is_verified` (BOOLEAN): Verification status
  - `is_active` (BOOLEAN): Active status

##### 13. CONSULTATIONS
- **Purpose**: Records scheduled consultations
- **Primary Key**: `consultation_id` (UUID)
- **Foreign Keys**:
  - `user_id` references USERS(user_id)
  - `nutritionist_id` references NUTRITIONISTS(nutritionist_id)
  - `child_id` references CHILDREN(child_id)
- **Attributes**:
  - `scheduled_time` (DATETIME): Consultation time
  - `duration_minutes` (INT): Length of consultation
  - `status` (VARCHAR(50)): Status (scheduled, completed, etc.)
  - `consultation_notes` (TEXT): Notes from consultation
  - `consultation_type` (VARCHAR(50)): Type of consultation
  - `created_at` (DATETIME): Record creation timestamp
  - `updated_at` (DATETIME): Record update timestamp

#### Educational Content

##### 14. ARTICLES
- **Purpose**: Educational articles about nutrition with focus on stunting prevention
- **Primary Key**: `article_id` (UUID)
- **Attributes**:
  - `title` (VARCHAR(255)): Article title
  - `content` (TEXT): Article content
  - `author` (VARCHAR(100)): Author name
  - `published_date` (DATETIME): Publication date
  - `image_url` (VARCHAR(255)): Featured image URL
  - `read_time_minutes` (INT): Estimated reading time
  - `view_count` (INT): Number of views
  - `is_featured` (BOOLEAN): Whether article is featured
  - `age_range_min_months` (INT): Minimum age target in months
  - `age_range_max_months` (INT): Maximum age target in months
  - `stunting_relevance` (ENUM('prevention', 'treatment', 'general')): Relevance to stunting
  - `nutrition_topics` (JSON): Array of nutrition topics covered
  - `difficulty_level` (ENUM('beginner', 'intermediate', 'advanced')): Content complexity level
  - `created_at` (DATETIME): Record creation timestamp
  - `updated_at` (DATETIME): Record update timestamp

##### 15. ARTICLE_CATEGORIES
- **Purpose**: Categories for articles with hierarchical structure
- **Primary Key**: `category_mapping_id` (UUID)
- **Foreign Key**: `article_id` references ARTICLES(article_id)
- **Attributes**:
  - `category_name` (VARCHAR(100)): Category name
  - `category_type` (VARCHAR(50)): Type of category (nutrition, child development, etc.)
  - `hierarchy_level` (INT): Level in category hierarchy

##### 16. USER_ARTICLE_HISTORY
- **Purpose**: Tracks user interaction with educational content
- **Primary Key**: `history_id` (UUID)
- **Foreign Keys**:
  - `user_id` references USERS(user_id)
  - `article_id` references ARTICLES(article_id)
- **Attributes**:
  - `read_date` (DATETIME): When the article was read
  - `completion_percentage` (INT): How much of the article was completed
  - `rating` (INT): User rating of article (1-5)
  - `feedback` (TEXT): Optional user feedback

##### 17. ARTICLE_RECOMMENDATIONS
- **Purpose**: Personalized article recommendations for children
- **Primary Key**: `recommendation_id` (UUID)
- **Foreign Keys**:
  - `child_id` references CHILDREN(child_id)
  - `article_id` references ARTICLES(article_id)
- **Attributes**:
  - `recommendation_reason` (VARCHAR(255)): Why this article is recommended
  - `priority` (INT): Recommendation priority (higher = more important)
  - `created_at` (DATETIME): When recommendation was generated

##### 18. ARTICLE_PROGRESSION
- **Purpose**: Defines sequential learning paths through articles
- **Primary Key**: `progression_id` (UUID)
- **Foreign Keys**:
  - `article_id` references ARTICLES(article_id)
  - `prerequisite_article_id` references ARTICLES(article_id)
- **Attributes**:
  - `sequence_order` (INT): Order in the progression sequence
  - `progression_path` (VARCHAR(100)): Named learning path/topic

### Indexes

| Table | Index Name | Columns | Type | Purpose |
|-------|------------|---------|------|---------|
| USERS | idx_users_email | email | UNIQUE | Fast lookup by email |
| CHILDREN | idx_children_user_id | user_id | NORMAL | Find children by user |
| CHILDREN | idx_children_birth_date | birth_date | NORMAL | Age-based queries |
| GROWTH_MEASUREMENTS | idx_measurements_child_id | child_id | NORMAL | Find measurements by child |
| GROWTH_MEASUREMENTS | idx_measurements_date | measure_date | NORMAL | Chronological queries |
| GROWTH_STANDARDS | idx_standards_lookup | standard_type, gender, age_months | NORMAL | Standard lookup |
| FOOD_ITEMS | idx_food_category | food_category_id | NORMAL | Category filtering |
| FOOD_ITEMS | idx_food_name | food_name | NORMAL | Search by name |
| MEAL_LOGS | idx_meals_child | child_id | NORMAL | Find meals by child |
| MEAL_LOGS | idx_meals_date | meal_time | NORMAL | Chronological queries |
| CONSULTATIONS | idx_consultations_user | user_id | NORMAL | Find consultations by user |
| CONSULTATIONS | idx_consultations_date | scheduled_time | NORMAL | Date-based queries |
| ARTICLES | idx_articles_age_range | age_range_min_months, age_range_max_months | NORMAL | Age-appropriate content |
| ARTICLES | idx_articles_stunting | stunting_relevance | NORMAL | Stunting-specific content |
| ARTICLES | idx_articles_difficulty | difficulty_level | NORMAL | Content difficulty filtering |
| USER_ARTICLE_HISTORY | idx_history_user | user_id | NORMAL | User reading history |
| USER_ARTICLE_HISTORY | idx_history_article | article_id | NORMAL | Article popularity |
| ARTICLE_RECOMMENDATIONS | idx_recommendations_child | child_id | NORMAL | Child-specific recommendations |
| ARTICLE_RECOMMENDATIONS | idx_recommendations_priority | priority | NORMAL | Priority-based ordering |
| ARTICLE_PROGRESSION | idx_progression_article | article_id | NORMAL | Find progressions by article |
| ARTICLE_PROGRESSION | idx_progression_prereq | prerequisite_article_id | NORMAL | Find prerequisites |
| ARTICLE_PROGRESSION | idx_progression_path | progression_path | NORMAL | Find progressions by path |

## NoSQL Database Schema (Firestore)

For data requiring flexibility, real-time updates, or documents with varying structures, we use Firestore collections.

### Collections and Documents

#### 1. users
- **Purpose**: User profiles and settings
- **Document ID**: `{user_id}` (same as relational database)
- **Fields**:
  - `email`: string
  - `displayName`: string
  - `profileImageUrl`: string
  - `createdAt`: timestamp
  - `lastActive`: timestamp
  - `notificationSettings`: map
    - `pushEnabled`: boolean
    - `emailEnabled`: boolean
    - `reminderTimes`: array of maps
  - `appSettings`: map
    - `theme`: string
    - `language`: string
  - `deviceTokens`: array of strings

#### 2. children_realtime
- **Purpose**: Real-time child data for dashboard
- **Document ID**: `{child_id}` (same as relational database)
- **Fields**:
  - `name`: string
  - `parentId`: string (references users)
  - `birthDate`: timestamp
  - `gender`: string
  - `latestMeasurements`: map
    - `weight`: number
    - `height`: number
    - `bmi`: number
    - `measureDate`: timestamp
  - `growthStatus`: string
  - `nutritionStatus`: string
  - `recentMeals`: array of maps
  - `upcomingCheckups`: array of maps
  - `dietaryRestrictions`: array of strings

#### 3. notifications
- **Purpose**: User notifications
- **Document ID**: auto-generated
- **Fields**:
  - `userId`: string (references users)
  - `title`: string
  - `message`: string
  - `type`: string
  - `referenceId`: string (optional, for deep linking)
  - `timestamp`: timestamp
  - `read`: boolean
  - `actionRequired`: boolean
  - `actionText`: string (optional)

#### 4. food_recommendations
- **Purpose**: Personalized food recommendations
- **Document ID**: auto-generated
- **Fields**:
  - `childId`: string (references children)
  - `generatedDate`: timestamp
  - `nutrients`: map
    - `deficient`: array of strings
    - `adequate`: array of strings
    - `excess`: array of strings
  - `recommendedFoods`: array of maps
    - `foodId`: string
    - `name`: string
    - `reasonForRecommendation`: string
    - `imageUrl`: string
    - `nutrientContribution`: map
  - `recommendedMeals`: array of maps
    - `name`: string
    - `description`: string
    - `imageUrl`: string
    - `ingredients`: array of maps
    - `preparationSteps`: array of strings
    - `nutritionalValue`: map

#### 5. activity_logs
- **Purpose**: Track app usage
- **Document ID**: auto-generated
- **Fields**:
  - `userId`: string
  - `timestamp`: timestamp
  - `action`: string
  - `screen`: string
  - `deviceInfo`: map
    - `deviceModel`: string
    - `osVersion`: string
    - `appVersion`: string
  - `additionalData`: map (flexible)

#### 6. chat_sessions
- **Purpose**: Chat conversations with nutritionists
- **Document ID**: auto-generated
- **Fields**:
  - `userId`: string
  - `nutritionistId`: string
  - `childId`: string (optional)
  - `startTime`: timestamp
  - `endTime`: timestamp (optional)
  - `status`: string
  - `messages`: subcollection
    - `sender`: string
    - `content`: string
    - `timestamp`: timestamp
    - `read`: boolean
    - `attachments`: array of maps (optional)

#### 7. article_engagement
- **Purpose**: Real-time tracking of article engagement metrics
- **Document ID**: `{article_id}`
- **Fields**:
  - `articleId`: string (references ARTICLES)
  - `totalViews`: number
  - `totalCompletions`: number
  - `averageRating`: number
  - `viewsByAge`: map of age groups to count
  - `recentReads`: array of maps
    - `userId`: string
    - `timestamp`: timestamp
    - `completionPercentage`: number
  - `popularTopics`: array of strings
  - `effectivenessScore`: number (calculated metric)

#### 8. learning_paths
- **Purpose**: Structured educational journeys for parents
- **Document ID**: auto-generated
- **Fields**:
  - `pathName`: string
  - `description`: string
  - `targetAgeMonthsMin`: number
  - `targetAgeMonthsMax`: number
  - `stuntingFocus`: boolean
  - `articles`: array of maps
    - `articleId`: string
    - `order`: number
    - `isRequired`: boolean
    - `estimatedTimeMinutes`: number
  - `completionCriteria`: map
    - `requiredArticleCount`: number
    - `minimumTimeMinutes`: number
  - `badgeImageUrl`: string
  - `createdAt`: timestamp
  - `updatedAt`: timestamp

## Storage Structure (Cloud Storage)

### Buckets and Objects

#### 1. nutrigenius-user-content
- **Purpose**: User-generated content
- **Object Path Format**: `users/{user_id}/{content_type}/{file_name}`
- **Content Types**:
  - `profile_images/`
  - `food_images/`
  - `meal_photos/`
  - `growth_charts/`

#### 2. nutrigenius-app-content
- **Purpose**: Application content
- **Object Path Format**: `{content_type}/{category}/{file_name}`
- **Content Types**:
  - `articles/`
  - `food_database/`
  - `educational_resources/`
  - `reference_charts/`

## Data Migration and Backup Strategy

### Migration Strategy
1. **Phased Migration**: Implement changes in batches to minimize disruption
2. **Data Validation**: Verify data integrity before and after migration
3. **Rollback Plan**: Maintain ability to revert to previous schema if needed

### Backup Strategy
1. **Regular Backups**: Daily full backups of all databases
2. **Point-in-Time Recovery**: Transaction log backups for Cloud SQL
3. **Geo-Redundancy**: Backups stored in multiple geographic regions
4. **Retention Policy**: Daily backups retained for 7 days, weekly for 1 month, monthly for 1 year

## Data Access Patterns

### Common Queries
1. **Dashboard View**: Aggregate child data for growth status, recent meals, and recommendations
2. **Growth Tracking**: Retrieve and plot growth measurements against standards
3. **Food Logging**: Record and analyze daily food intake
4. **Article Search**: Search articles by keywords, categories, and relevance
5. **Recommendation Generation**: Analyze child data and generate personalized recommendations
6. **Personalized Learning**:
   - Find articles appropriate for a child's age and development stage
   - Retrieve next articles in a learning progression
   - Track user progress through educational pathways
   - Recommend new content based on previous engagement

### Performance Optimization
1. **Caching**: Frequently accessed data cached in memory
2. **Denormalization**: Key information duplicated for faster access
3. **Composite Indexes**: Custom indexes for common query patterns
4. **Read Replicas**: For read-heavy operations
5. **Sharding**: Plan for horizontal partitioning as data grows

## Data Security and Compliance

1. **Encryption**: All data encrypted at rest and in transit
2. **Access Control**: Row-level security in Cloud SQL, document-level security in Firestore
3. **Audit Logging**: Comprehensive logging of all data access and modifications
4. **Anonymization**: Capability to anonymize data for analytics
5. **Compliance**: Designed to meet healthcare data protection regulations
6. **Data Retention**: Policies for data retention and deletion

## References

1. [Google Cloud SQL Documentation](https://cloud.google.com/sql/docs)
2. [Firebase Firestore Documentation](https://firebase.google.com/docs/firestore)
3. [MySQL Reference Manual](https://dev.mysql.com/doc/refman/8.0/en/)
4. [WHO Child Growth Standards](https://www.who.int/tools/child-growth-standards)
5. [Cloud Storage Documentation](https://cloud.google.com/storage/docs)
