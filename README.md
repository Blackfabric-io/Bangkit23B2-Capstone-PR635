> [!info]
> ## Table of Contents
> - [Table of Contents](#table-of-contents)
> - [Project Overview](#project-overview)
> - [Team Information](#team-information)
> - [Executive Summary](#executive-summary)
> - [Problem Statement \& Research](#problem-statement--research)
> 	- [Problem Statement](#problem-statement)
> 	- [Research Questions](#research-questions)
> - [Project Scope \& Deliverables](#project-scope--deliverables)
> - [Technology \& Implementation](#technology--implementation)
> 	- [Technology Stack](#technology-stack)
> 	- [Implementation Plan](#implementation-plan)
> 	- [Market Strategy](#market-strategy)
> - [Key Features](#key-features)
> - [Project Status \& Feedback](#project-status--feedback)
> - [Project Artifacts](#project-artifacts)
> - [Action Items \& Progress](#action-items--progress)
> - [Potential Risks \& Challenges](#potential-risks--challenges)
> - [Resources \& References](#resources--references)
> - [Project Development Journey](#project-development-journey)
> 	- [Initial Concept Development (November 3, 2023)](#initial-concept-development-november-3-2023)
> 	- [Project Theme Refinement (November 9, 2023)](#project-theme-refinement-november-9-2023)
> 	- [Advisor Consultation Insights (December 15, 2023)](#advisor-consultation-insights-december-15-2023)

## Project Overview

NutriGenius is an innovative mobile application designed to address the high prevalence of stunting in Indonesian children through a combination of technology and nutrition education. The app provides personalized nutrition recommendations, educational resources, and tools to help parents monitor their children's growth and development.

## Team Information

**Team ID**: CH2-PR635
**Selected Theme**: Human Healthcare and Living Wellbeings
**Mentor Name**: Ari Kusyanti, 15/12/2023
**Team Members**:
- (ML) M302BSY0936 Fiqri Rasyidiq - Universitas Pertamina [Active]
- (ML) M214BSY1912 Muhammad Ahnaf Zalfa - Universitas Islam Indonesia [Active]
- (CC) C156BSX3410 Rizki Santriani - Sekolah Tinggi Teknologi Terpadu Nurul Fikri [Active]
- (CC) C676BSY3624 As'ad Reza Amaanullah - Universitas Global Jakarta [Active]
- (CC) C006BSY3921 Pieter Rafael Johansz - Universitas Brawijaya [Active]
- (MD) A314BSY2063 Teuku Nurmansyah Puteh - Universitas Singaperbangsa Karawang [Active]
- (MD) A698BSY2090 Bintang Ramadhan - Universitas Persatuan Islam [Inactive]

## Executive Summary

NutriGenius is an innovative project aiming to address the issue of stunting in Indonesian children through a blend of technology and nutritional education. Given the prevalent concern of high stunting rates in public health, NutriGenius emerges as a comprehensive and personalized solution, utilizing a technology-driven approach. 

Stunting is a prevalent issue in Indonesia, mainly due to insufficient awareness about nutrition, limited access to healthcare resources, and imbalanced dietary habits. NutriGenius is dedicated to addressing these challenges and enhancing public awareness regarding the significance of nutrition during the crucial first 1,000 days of a child's life (Reference: BPS, 2021).

Our comprehensive project plan focuses on three key Learning Paths, each playing a vital role in addressing childhood stunting:

1. **Machine Learning**: 
   To track toddler growth, the NutriGenius Capstone Group uses TensorFlow to implement machine learning. We create models that modify lesson plans according to the age of the child and suggest foods depending on their dietary requirements. Using deep learning algorithms, the system incorporates telemedicine to facilitate quick access to nearby health services and allows for daily nutritional intake tracking. The program now has real-time functionality and precise predictions because of the utilization of TensorFlow's capabilities.
2. **Mobile Development**: 
   The NutriGenius app is planned to be launched for Android devices by our team. The user-friendly graphical interface simplifies data entry for children's weight and height, facilitating the assessment of their nutritional health. Integration with wearables is seamlessly achieved through Android Wear APIs, with ViewModel and LiveData optimizing data management efficiency. The app features a quick scanning function using the Android Camera API, offering instant access to nutritional information. Real-time connectivity is established through Firebase Realtime Database and Firestore, while Room Database and Firebase's offline capabilities ensure uninterrupted functionality, even in the absence of an internet connection. This streamlined tech approach empowers NutriGenius to effectively assess children's nutritional health, providing a cutting-edge, user-friendly experience.
3. **Cloud Computing**: 
   In our cloud computing setup, we implement a solid backend API model. Private APIs manage secure login processing and monitoring, while external endpoint APIs supply national data on toddlers and children. The core of our cloud architecture relies on Cloud Storage, Cloud SQL, and Compute Engine with a dedicated external IP address. To facilitate efficient data transfer between the backend and mobile apps, we've employed the MQTT communication mechanism. For user convenience, a straightforward dashboard is implemented to monitor service availability, logging, and housekeeping.

By putting these plans into action, we're combining different paths to come up with a creative solution. It's all about using technology in a compassionate way to look out for the well-being of Indonesian children. This is a big step forward in tackling childhood stunting.

## Problem Statement & Research

### Problem Statement

Stunting is a significant nutritional problem in Indonesia, with approximately 27.7% of toddlers affected as of 2019. This places Indonesia fourth globally in stunting cases. Stunting has long-term negative impacts on:
- Human rights and welfare
- Economic development due to inadequate human resources
- Indonesia's international reputation

Based on research data from the Ministry of Health, before the emergence of the COVID-19 pandemic, around 6.3 million toddlers out of Indonesia's total toddler population of 23 million experienced stunting. The prevalence of stunted toddlers in Indonesia in 2019 reached 27.7%. This puts Indonesia in fourth place globally as the country with the highest cases of stunting.

Reasons for addressing this issue:
- If left unchecked for a long time, Indonesia will indirectly ignore human rights in terms of the welfare of its people.
- Stunting will have an impact on the country's economic progress due to inadequate human resources.
- Indonesia has the potential to get a bad reputation in the international world, which is correlated with stunting cases which are still high.

### Research Questions

1. How can we enhance the effective monitoring of children's growth?
2. How does machine learning technology contribute to personalized nutrition education?
3. What's the most effective approach to incorporate nutritional advice into children's eating habits?

## Project Scope & Deliverables

**Project Scope**:

1. **Research and Data Collection** 
	- Gather comprehensive data on childhood stunting in Indonesia, conduct literature reviews, collaborate with health organizations, and survey stakeholders.
2. **Technology Infrastructure** 
	- Set up cloud computing resources, develop a secure mobile application, and implement ML algorithms.
3. **Machine Learning Model Development** 
	- Create models for growth monitoring and nutrition analysis.
4. **Nutritional Education Content** 
	- Develop culturally relevant educational materials.
5. **User Interface Design** 
	- Create intuitive interfaces and ensure accessibility.
6. **Pilot Testing and Iteration** 
	- Test with select user groups and gather feedback.
7. **Healthcare System Integration** 
	- Develop APIs for integration with health databases.
8. **Public Awareness Campaign** 
	- Develop marketing strategies and promotional materials.

**Project Deliverables**:

1. **Comprehensive Research Report** 
	- Literature reviews, statistical data, and insights from surveys.
2. **Technology Infrastructure** 
	- Cloud computing setup and mobile application with authentication.
3. **Machine Learning Models** 
	- Growth monitoring, food recognition, and nutrition analysis algorithms.
4. **Educational Content** 
	- Customized nutritional materials and documentation.
5. **UI/UX Design** 
	- Application design documentation and user testing reports.
6. **Pilot Test Results** 
	- Feedback analysis and iteration documentation.
7. **Integration Documentation** 
	- API documentation and information sharing protocols.
8. **Awareness Campaign Materials** 
	- Marketing strategy and promotional content.

## Technology & Implementation

### Technology Stack

**Machine Learning**:
- TensorFlow Library (image classification, nutrition analysis)
- NumPy Library (numerical computing)
- Scikit-learn Library (machine learning algorithms)
- Pandas Library (data manipulation and analysis)
- Google Colab (collaborative development)
- Kaggle Datasets (training data)
- GitHub (version control)

**Machine Learning Progress**:
- [ ] Algorithm Selection
- [ ] Data Preprocessing
- [ ] Feature Engineering
- [ ] Hyperparameter Tuning
- [ ] Validation

**Mobile Development**:
- Android Studio (primary IDE)
- Networking (Retrofit/FAN)
- Android JetPack Compose (modern UI toolkit)
- Figma (design work)
- Material.io (Material Design implementation)
- Android Libraries (enhanced functionality)
- Flaticon (icon resources)

**Cloud Computing**:
- GKE / App Engine / Docker (containerization and deployment)
- Firestore (real-time data storage)
- Firebase (app development platform)
- Firebase SDK (integration)
- MySQL (relational database management)
- MySQL Connector (database connectivity)
- Cloud Storage (file storage)
- Postman (API testing)
- BigQuery (data analytics)

### Implementation Plan

To address the stunting issue in children in Indonesia, we will:
1. Build a deep learning model to process data including age, weight, height, allergy history, and food images
2. Detect potential stunting and provide immediate results
3. Retrieve detailed information from the cloud, including articles and tips customized for each user
4. Collect data from multiple sources to regularly update application features
5. Develop a user-friendly mobile application for effective access and use

**Dataset Information**:
We had to use dummy data because finding a suitable dataset proved challenging, and even if available, we were uncertain about obtaining the necessary permission to access such a dataset.

### Market Strategy

- **Target Audience**: Parents/caregivers, health instructors, and medical workers
- **Local Deployment**: Engagement with local health authorities and community organizations
- **User Onboarding**: Simple, intuitive process for new users
- **Community Engagement**: Initiatives to create awareness and accessibility

## Key Features

1. **Nutrition Monitoring**: Provides regular monitoring of children's nutritional status. Parents or caregivers can enter data such as the child's age, weight, height, and nutritional condition. This application will provide visual reports that are easy to understand, such as a graph of a child's growth over time.
2. **Recommendations Feature**: Provides recommendations for balanced menus and nutritious food recipes according to the nutritional status data entered. Users can also obtain information regarding the urgency of certain nutritional intake for children's optimal growth.
3. **Nutrition Education**: Provides health articles and educational information about nutrition to help inspire parents to understand their children's nutritional needs.
4. **Food Scanning**: Provides food photo-taking services using cellphone cameras. The application will automatically identify types of food and provide an overview of their nutritional composition, making it easier for users to make wise decisions regarding their child's growth and development.
5. **Expert Consultation**: Connect with nutrition experts for personalized advice.

Our group feels that these features are still rarely found in other product prototypes. The hope is that the features described above will maximize the real reduction in stunting in Indonesia.

## Project Status & Feedback

**Current Status**: 65% Completed

The delay is primarily due to challenges in implementing the design of the Android application, stemming from limited competence and manpower in the mobile development team. However, noteworthy progress has been made with the mock UI, feature determination for the application along with the conceptual implementation plan for these features and Cloud/API configuration. Similarly, the machine learning component, especially in the scanning feature, has yet to be implemented, further influencing the current status of the project.

**Implementation Changes**:
The capstone project has followed the original plan exactly, without deviation. However, the current reality is that only 65% of progress has been made, underscoring the challenges posed by limited competence and manpower in both mobile development and machine learning. This completion status highlights the crucial features that remain pending and the need for additional resources to fulfill the project's goals. Despite these hurdles, the commitment to the initial vision remains steadfast.

**Mentoring Remarks**:
Strategize to boost user numbers, focusing on a compelling branding strategy to elevate the project's appeal. Implement targeted marketing campaigns to effectively communicate its value. Highlighting the benefits of integrating machine learning will be key to capturing the interest of potential users. This approach aims to not only attract a broader audience but also solidify the project's impact and success.

## Action Items & Progress

- [x] Research applications with similar functionality
- [ ] Develop machine learning features for stunting prevention
- [ ] Demonstrate machine learning benefits in the project
- [ ] Create a user-friendly application with valuable features
- [ ] Increase user adoption
- [ ] Secure partnerships and funding
- [ ] Plan phased development starting with core features
- [ ] Create compelling branding
- [ ] Implement marketing strategy

## Potential Risks & Challenges

1. Standard Operating Procedure problems
2. Identification techniques for children with food allergies
3. Limited accuracy of maps-based monitoring with insufficient data
4. Competition from similar applications
5. User adoption challenges
6. Data privacy and security concerns

## Resources & References

- [Bangkit Academy Dashboard](https://dashboard.bangkit.academy/student-portal)
- [Bangkit 2023 H2 Timeline](https://docs.google.com/spreadsheets/d/e/2PACX-1vSa-RPimYCx0mZXLm8VWhnx8fQY3Qqr_BRhSSF1ggG4Tjpjf8Kk3cjy98uKPz_QOLBRVO1bvUYlDKpQ/pubhtml)
- [Capstone Project GitHub Repository](https://github.com/Capstone-CH2-PR635/NutriGenius)
- BPS (Statistics Indonesia), 2021
- Ministry of Health, Indonesia (2019)

## Project Development Journey

This section highlights key takeaways from team meetings and advisor consultations that shaped the NutriGenius project.

### Initial Concept Development (November 3, 2023)
In our first team meeting, we:
- Established the initial focus on food accessibility and monitoring
- Conceptualized a system to monitor quality and pricing of essential food items
- Set up a collaborative research framework to explore product-based project topics
- Emphasized the importance of mutual support and open communication
- Planned to use Notion for project monitoring and task management

### Project Theme Refinement (November 9, 2023)
During our second team meeting, we:
- Explored various project themes including waste management and textile fabrics
- Considered developing an application for product information (pricing, origin, suppliers)
- Pivoted toward nutrition monitoring for children and infants with a specific focus on toddlers
- Identified key ML parameters needed:
  - Nutritional Adequacy Rate (AKG) data for toddlers
  - Nutritional content in food commodities
  - Android-based application platform
  - Allergen information for sensitive toddlers

### Advisor Consultation Insights (December 15, 2023)
Our advisor consultation provided critical guidance:

1. **Differentiation Strategy**:
   - Need for clear differentiation from similar applications in the market
   - Importance of articulating NutriGenius advantages over competitors
   - Recommendation to focus specifically on stunting in babies as our primary differentiator

2. **Machine Learning Implementation**:
   - Make ML implementation more unique and specialized
   - Avoid too general an approach that would result in many competitors
   - Demonstrate how ML provides value that competitors don't offer
   - Show specifications for stunting babies and ML utility

3. **Branding and Marketing**:
   - Develop strong, clear branding before marketing
   - Claim uniqueness for branding purposes
   - Create attractive branding to elevate the project's appeal

4. **Development Approach**:
   - Don't wait for approval when defining project scope
   - Use Bangkit as an opportunity to showcase abilities
   - Implement continuous updates with versioned features (v1, v2, v3)
   - Focus on user acquisition and team management for impact
   - Participate in funding competitions and seek supporting partners

These meetings were instrumental in shaping our project from an initial concept focused on food accessibility to our final direction of addressing childhood stunting through technology and nutrition education.

---

*This document combines information from multiple project files including the Project Plan, CAPSTONE notes, Responsibility document, Final Project notes, Project Brief, README, and Meeting Notes.* 