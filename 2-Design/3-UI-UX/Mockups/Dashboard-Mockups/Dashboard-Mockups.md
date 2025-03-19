# Dashboard Mockups

This document presents the mockups for the NutriGenius dashboard screens, which serve as the main hub for users to access all app features and monitor their child's nutrition and growth status.

## Main Dashboard

The main dashboard provides an overview of the child's current status and quick access to key features.

### Design Specifications

- **Screen**: Main Dashboard
- **Navigation**: Bottom navigation, top app bar
- **Primary Actions**: Quick access to key features
- **Content Priority**: Growth status, nutritional insights, recent activity

### Mockup

```
┌─────────────────────────────────────────────┐
│ ≡                 NutriGenius          👤   │
├─────────────────────────────────────────────┤
│ ┌─────────────────────────────────────────┐ │
│ │ Good morning, Sarah!                    │ │
│ │ Amir is doing well today.               │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ ┌─────────────────────┐ ┌─────────────────┐ │
│ │ Growth Status       │ │ Today's Meals   │ │
│ │ ┌───────────────┐   │ │ ┌─────────────┐ │ │
│ │ │ [Growth Chart]│   │ │ │ Breakfast   │ │ │
│ │ └───────────────┘   │ │ │ 7:30 AM     │ │ │
│ │ Height: 85cm (45%)  │ │ └─────────────┘ │ │
│ │ Weight: 12kg (50%)  │ │ ┌─────────────┐ │ │
│ │ Last update: Today  │ │ │ + Add Meal  │ │ │
│ └─────────────────────┘ └─────────────────┘ │
│                                             │
│ ┌─────────────────────┐ ┌─────────────────┐ │
│ │ Nutrition Insights  │ │ Upcoming        │ │
│ │ ┌───────────────┐   │ │ ┌─────────────┐ │ │
│ │ │ [Pie Chart]   │   │ │ │ Measurement │ │ │
│ │ └───────────────┘   │ │ │ Due in 2d   │ │ │
│ │ Protein: 80% of goal│ │ └─────────────┘ │ │
│ │ Iron: 65% of goal   │ │ ┌─────────────┐ │ │
│ │ View all →          │ │ │ View more   │ │ │
│ └─────────────────────┘ └─────────────────┘ │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ Recommended for You                      │ │
│ │ ┌─────────────┐ ┌─────────────┐ ┌──────┐ │ │
│ │ │ [Article 1] │ │ [Article 2] │ │ More │ │ │
│ │ └─────────────┘ └─────────────┘ └──────┘ │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ 🏠    📏    📷    📚    👨‍⚕️  │
└─────────────────────────────────────────────┘
```

### Key Components

1. **Top App Bar**
   - Menu icon for drawer navigation
   - App title
   - Profile icon for quick access to user settings

2. **Welcome Section**
   - Personalized greeting with parent's name
   - Child status summary
   - Child selector (if multiple children registered)

3. **Growth Status Card**
   - Implementation of Stat Summary Card component
   - Header: "Growth Status" in H6 typography
   - Metric values: Height, weight percentiles in H4 typography, Primary Green
   - Visual indicator: Mini growth chart visualization (40px × 40px)
   - Last measurement date in Caption typography
   - Quick action to add new measurement

4. **Meal Tracking Card**
   - Implementation of Activity Card component
   - Today's logged meals with timestamps in Caption typography
   - Meal names in Body 2 typography
   - Quick action to add new meal
   - Visual indicator of meal completeness

5. **Nutrition Insights Card**
   - Implementation of Stat Summary Card component
   - Nutritional balance visualization as visual indicator
   - Key nutrient progress metrics in H4 typography
   - Positive/negative variations based on progress
   - Quick link to detailed nutrition view

6. **Upcoming Activities Card**
   - Implementation of Activity Card component
   - Next scheduled measurement
   - Upcoming consultation
   - Due actions or reminders
   - Timestamps in Caption typography, Dark Gray

7. **Recommended Content**
   - Personalized article recommendations
   - Horizontal scrollable list
   - Based on child's age and growth status

8. **Bottom Navigation**
   - Home (Dashboard)
   - Growth (Monitoring)
   - Scan (Food Scanner)
   - Learn (Education)
   - Consult (Expert Consultation)

## Child Selector Dashboard

For users with multiple children, the child selector allows quick switching between children's dashboards.

### Design Specifications

- **Screen**: Child Selector Overlay
- **Trigger**: Tap on child name in welcome section
- **Primary Actions**: Select child to view
- **Content Priority**: Child identification, quick status overview

### Mockup

```
┌─────────────────────────────────────────────┐
│ ≡                 NutriGenius          👤   │
├─────────────────────────────────────────────┤
│ ┌─────────────────────────────────────────┐ │
│ │ Select a child                          │ │
│ │                                         │ │
│ │ ┌─────────────────────────────────────┐ │ │
│ │ │ 👦 Amir, 2y 3m                    ✓ │ │ │
│ │ │ Last update: Today                   │ │ │
│ │ │ Status: On track                     │ │ │
│ │ └─────────────────────────────────────┘ │ │
│ │                                         │ │
│ │ ┌─────────────────────────────────────┐ │ │
│ │ │ 👧 Layla, 4y 1m                     │ │ │
│ │ │ Last update: Yesterday               │ │ │
│ │ │ Status: On track                     │ │ │
│ │ └─────────────────────────────────────┘ │ │
│ │                                         │ │
│ │ ┌─────────────────────────────────────┐ │ │
│ │ │ ➕ Add a child                       │ │ │
│ │ └─────────────────────────────────────┘ │ │
│ │                                         │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ [Dashboard content dimmed in background]    │
│                                             │
└─────────────────────────────────────────────┘
```

### Key Components

1. **Overlay Header**
   - Clear title "Select a child"
   - Optional close button

2. **Child Cards**
   - Child photo/avatar
   - Name and age
   - Last update timestamp
   - Growth status indicator
   - Visual selection indicator for current child

3. **Add Child Option**
   - Prominent "Add a child" button
   - Leads to child profile creation flow

## Quick Actions Menu

The quick actions menu provides fast access to common tasks from the dashboard.

### Design Specifications

- **Screen**: Quick Actions Overlay
- **Trigger**: Floating action button or swipe up gesture
- **Primary Actions**: Common tasks across features
- **Content Priority**: Task clarity, frequent actions

### Mockup

```
┌─────────────────────────────────────────────┐
│                                             │
│                                             │
│                                             │
│                                             │
│                                             │
│                                             │
│                                             │
│                                             │
│                                             │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ Quick Actions                           │ │
│ │                                         │ │
│ │ ┌─────────┐ ┌─────────┐ ┌─────────┐     │ │
│ │ │ 📏      │ │ 📷      │ │ 🍽️      │     │ │
│ │ │ Add     │ │ Scan    │ │ Log     │     │ │
│ │ │ Measure │ │ Food    │ │ Meal    │     │ │
│ │ └─────────┘ └─────────┘ └─────────┘     │ │
│ │                                         │ │
│ │ ┌─────────┐ ┌─────────┐ ┌─────────┐     │ │
│ │ │ 👨‍⚕️      │ │ 📊      │ │ 📝      │     │ │
│ │ │ Book    │ │ View    │ │ Add     │     │ │
│ │ │ Consult │ │ Reports │ │ Notes   │     │ │
│ │ └─────────┘ └─────────┘ └─────────┘     │ │
│ │                                         │ │
│ └─────────────────────────────────────────┘ │
└─────────────────────────────────────────────┘
```

### Key Components

1. **Action Grid**
   - Grid of common actions
   - Clear icons and labels
   - Grouped by feature area

2. **Primary Actions**
   - Add Measurement
   - Scan Food
   - Log Meal
   - Book Consultation
   - View Reports
   - Add Notes

## Dashboard Settings

The dashboard settings allow users to customize their dashboard experience.

### Design Specifications

- **Screen**: Dashboard Settings
- **Navigation**: Accessed from dashboard menu
- **Primary Actions**: Customize dashboard layout and content
- **Content Priority**: Customization options, user preferences

### Mockup

```
┌─────────────────────────────────────────────┐
│ ←           Dashboard Settings              │
├─────────────────────────────────────────────┤
│                                             │
│ Card Visibility                             │
│ ┌─────────────────────────────────────────┐ │
│ │ Growth Status                      ✓    │ │
│ └─────────────────────────────────────────┘ │
│ ┌─────────────────────────────────────────┐ │
│ │ Today's Meals                      ✓    │ │
│ └─────────────────────────────────────────┘ │
│ ┌─────────────────────────────────────────┐ │
│ │ Nutrition Insights                 ✓    │ │
│ └─────────────────────────────────────────┘ │
│ ┌─────────────────────────────────────────┐ │
│ │ Upcoming Activities                ✓    │ │
│ └─────────────────────────────────────────┘ │
│ ┌─────────────────────────────────────────┐ │
│ │ Recommended Content                ✓    │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ Card Order                                  │
│ ┌─────────────────────────────────────────┐ │
│ │ Drag to reorder                         │ │
│ │ ┌─────────────────────────────────────┐ │ │
│ │ │ 1. Growth Status               ⋮⋮   │ │ │
│ │ └─────────────────────────────────────┘ │ │
│ │ ┌─────────────────────────────────────┐ │ │
│ │ │ 2. Today's Meals                ⋮⋮   │ │ │
│ │ └─────────────────────────────────────┘ │ │
│ │ ┌─────────────────────────────────────┐ │ │
│ │ │ 3. Nutrition Insights           ⋮⋮   │ │ │
│ │ └─────────────────────────────────────┘ │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │           Reset to Default              │ │
│ └─────────────────────────────────────────┘ │
└─────────────────────────────────────────────┘
```

### Key Components

1. **Card Visibility Toggles**
   - Checkboxes to show/hide dashboard cards
   - All cards visible by default

2. **Card Order Controls**
   - Drag handles to reorder dashboard cards
   - Visual indication of current order

3. **Reset Option**
   - Button to restore default dashboard configuration

## Design Notes

1. **Personalization**
   - Dashboard adapts to show most relevant information based on child's age and needs
   - Content prioritization changes based on user behavior and critical needs

2. **Information Hierarchy**
   - Most important/actionable information appears at the top
   - Cards organized by frequency of use and importance
   - Visual emphasis on areas requiring attention

3. **Accessibility Considerations**
   - High contrast between text and backgrounds
   - Adequate touch targets for all interactive elements
   - Clear labels and icons with text alternatives

4. **Responsive Behavior**
   - Cards reflow on different screen sizes
   - Critical information remains visible on initial viewport
   - Scrolling required only for supplementary information

5. **States and Variations**
   - First-time user dashboard emphasizes onboarding and setup
   - Regular user dashboard emphasizes tracking and insights
   - Alert states for concerning measurements or missed tracking 