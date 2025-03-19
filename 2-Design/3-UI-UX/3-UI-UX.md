# NutriGenius UI/UX Overview

This document provides overview of the User Interface (UI) and User Experience (UX) design for the NutriGenius application. NutriGenius is designed to address childhood stunting in Indonesia through technology and nutrition education, offering parents a suite of tools to monitor growth, analyze food, access educational content, and consult with nutrition experts.

## Design Philosophy

The NutriGenius UI/UX design follows these core principles:

1. **User-Centered Design**: Focused on the needs of parents and caregivers in Indonesia
2. **Accessibility**: Designed to be usable by individuals with varying levels of technical literacy
3. **Cultural Relevance**: Incorporating Indonesian cultural context and nutritional practices
4. **Evidenced-Based Approach**: Aligning with WHO growth standards and nutrition science
5. **Progressive Disclosure**: Presenting complex information in digestible formats
6. **Consistency**: Maintaining unified design patterns throughout the application

## Design System

The design system provides the fundamental building blocks for creating consistent, accessible interfaces across the application:

- **Colors**: Defined color palette with primary, neutral, and feedback colors
- **Typography**: Dual-font approach with specific type scales and responsive sizing
- **Icons**: Consistent icon set with standardized sizes and styles
- **Components**: Reusable UI components with defined behaviors and states

The design system ensures visual consistency and helps maintain accessibility standards throughout the application.

## User Flows

NutriGenius has five primary user flows, each corresponding to a core feature of the application:

![[Design-System/ML-Integration.svg]]
### 1. User Onboarding Flow
- First-time user experience including registration, authentication, child profile creation
- Progressive introduction to application features
- Personalization setup to tailor content to the child's needs

![[User-Flow/1. User Onboarding Flow Wireframe.svg]]

### 2. Growth Monitoring Flow
- Recording and tracking child measurements (height, weight, head circumference)
- Visualization of growth data against WHO standards
- Growth status assessment and recommendations

![[User-Flow/2. Nutrition Education Flow Wireframe.svg]]

### 3. Food Scanning Flow
- Food identification using camera
- Nutritional analysis of identified foods
- Meal logging and nutritional tracking

![[User-Flow/3. Growth Monitoring Flow Wireframe.svg]]

### 4. Nutrition Education Flow
- Accessing educational content through various discovery paths
- Personalized content recommendations
- Learning paths for structured education

![[User-Flow/4. Food Scanning Flow Wireframe.svg]]

### 5. Expert Consultation Flow
- Finding nutrition experts
- Booking and preparing for consultations
- Conducting and following up on consultation sessions

## Mockups

The mockups provide detailed screen designs for each major section of the application:

- **Dashboard Mockups**: Home screen and main navigation
- **Growth Tracking Mockups**: Growth monitoring interface and visualizations
- **Food Scanning Mockups**: Camera interface and nutritional analysis
- **Education Mockups**: Content discovery and article reading experience
- **Consultation Mockups**: Expert directory and consultation interfaces

Each mockup demonstrates the application of the design system within the context of specific user tasks and flows.

## ML Integration

Machine Learning is seamlessly integrated into the user experience through:

1. **Food Recognition**: Converting food images to identified items with nutritional data
2. **Portion Estimation**: Analyzing images to estimate portion sizes and nutritional content
3. **Personalized Recommendations**: Tailoring content and advice based on child data
4. **Growth Analysis**: Assessing growth data for potential stunting or nutritional issues

The ML integration is designed to be transparent to users while providing powerful functionality that enhances the core features.

## Design Process Artifacts

The UI/UX directory contains several types of design artifacts:

1. **Wireframes (.svg files)**: Visual representations of the flow and layout for each feature
2. **User Flow Diagrams**: Detailed flow charts showing user journeys and decision points
3. **Design System Documentation**: Specifications for design elements and components
4. **Mockups**: High-fidelity representations of final UI screens

## Alignment with Other Design Components

The UI/UX design aligns with:

1. **Architecture Design**: Supporting the technical components and data flows
2. **Database Schema**: Reflecting the data structures and relationships
3. **ML Components**: Integrating machine learning capabilities into the user experience

## Design Evolution

The UI/UX design was developed through an iterative process:

1. Initial research on user needs and context in Indonesia
2. Definition of user personas and journey maps
3. Creation of wireframes and flow diagrams
4. Development of the design system
5. Production of detailed mockups
6. Refinement based on feedback and alignment with technical architecture

The _archive directory contains previous versions showing this evolution.

## Future Enhancements

Areas identified for future UI/UX enhancements include:

1. Additional language support for Indonesian regional languages
2. Offline mode improvements for low-connectivity areas
3. Enhanced visualization options for growth data
4. Integration with wearable devices for automated measurement
5. Expanded educational content formats (video, interactive)

## Using This Documentation

When working with the NutriGenius UI/UX design:

1. Start with this overview to understand the overall approach
2. Reference the design system for component-level decisions
3. Consult user flows to understand feature interactions
4. Refer to mockups for detailed implementation guidance

New features should maintain consistency with the established design patterns while evolving the system to meet emerging user needs.

## Tools Used

The UI/UX design was created using:

- **Figma**: For mockups and design system
- **Draw.io**: For user flow diagrams
- **SVG**: For wireframes and flow visualizations
- **Adobe Creative Suite**: For graphical elements and icons 