# Growth Tracking Mockups

This document presents the mockups for the NutriGenius growth tracking feature, which allows parents to monitor their child's physical development and compare it to standard growth charts.

## Growth Overview Screen

The main screen for the growth tracking feature, providing a summary of the child's growth status.

### Design Specifications

- **Screen**: Growth Overview
- **Navigation**: Accessed from bottom navigation or dashboard
- **Primary Actions**: View charts, add measurement, view history
- **Content Priority**: Current growth status, trends, actionable insights

### Mockup

```
┌─────────────────────────────────────────────┐
│ ≡             Growth Tracking          👤   │
├─────────────────────────────────────────────┤
│ ┌─────────────────────────────────────────┐ │
│ │ Amir, 2 years 3 months                  │ │
│ │ Last measured: Today                    │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ Current Measurements                    │ │
│ │ ┌───────────┐ ┌───────────┐ ┌──────────┐│ │
│ │ │ Height    │ │ Weight    │ │ Head     ││ │
│ │ │ 85 cm     │ │ 12 kg     │ │ 48 cm    ││ │
│ │ │ (45%)     │ │ (50%)     │ │ (52%)    ││ │
│ │ └───────────┘ └───────────┘ └──────────┘│ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ Growth Status                           │ │
│ │                                         │ │
│ │ Height-for-age: Normal                  │ │
│ │ Weight-for-age: Normal                  │ │
│ │ Weight-for-height: Normal               │ │
│ │                                         │ │
│ │ Overall: On track 👍                    │ │
│ │                                         │ │
│ │ [View Detailed Assessment]              │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ Growth Charts                           │ │
│ │                                         │ │
│ │ [Height Chart Preview]                  │ │
│ │                                         │ │
│ │ ◉ Height  ○ Weight  ○ BMI  ○ Head      │ │
│ │                                         │ │
│ │ [View Full Charts]                      │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ [+ Add New Measurement]                 │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ 🏠    📏    📷    📚    👨‍⚕️  │
└─────────────────────────────────────────────┘
```

### Key Components

1. **Child Information Header**
   - Child name and age using H5 typography
   - Last measurement date using Caption typography
   - Child selector (if multiple children) using Dropdown component
   - Standard Card component

2. **Current Measurements Card**
   - Standard Card component with H5 typography header
   - Uses **Measurement Value Card** components for each metric
   - Key metrics with current values
   - Percentile indicators
   - Visual indicators for normal/concerning values

3. **Growth Status Card**
   - Standard Card component with H5 typography header
   - Uses **Growth Status Indicator** components for each parameter
   - Overall growth assessment
   - Status for each key growth parameter
   - Visual indicator of overall status
   - Secondary Button for detailed assessment

4. **Growth Charts Preview**
   - Standard Card component
   - Compact visualization of primary growth chart
   - **Chart Type Selector** component for switching between metrics
   - Secondary Button for full chart view

5. **Add Measurement Button**
   - Primary Button component
   - Prominent call-to-action
   - Quick access to measurement entry

## Growth Charts Screen

Detailed view of growth charts with WHO standard comparisons.

### Design Specifications

- **Screen**: Growth Charts
- **Navigation**: Accessed from Growth Overview
- **Primary Actions**: Switch between chart types, view data points
- **Content Priority**: Visual growth trends, comparison to standards

### Mockup

```
┌─────────────────────────────────────────────┐
│ ←               Growth Charts               │
├─────────────────────────────────────────────┤
│ ┌─────────────────────────────────────────┐ │
│ │ Amir, 2 years 3 months                  │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ Height-for-Age                          │ │
│ │                                         │ │
│ │ ┌─────────────────────────────────────┐ │ │
│ │ │                                     │ │ │
│ │ │                                     │ │ │
│ │ │                                     │ │ │
│ │ │                                     │ │ │
│ │ │                                     │ │ │
│ │ │                                     │ │ │
│ │ │                                     │ │ │
│ │ │                                     │ │ │
│ │ │                                     │ │ │
│ │ │ [Detailed Growth Chart]             │ │ │
│ │ │                                     │ │ │
│ │ └─────────────────────────────────────┘ │ │
│ │                                         │ │
│ │ ── Child's growth                       │ │
│ │ ── 97th percentile                      │ │
│ │ ── 50th percentile                      │ │
│ │ ── 3rd percentile                       │ │
│ │                                         │ │
│ │ Time range: ◉ All  ○ 1y  ○ 6m  ○ 3m    │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ ◉ Height  ○ Weight  ○ BMI  ○ Head      │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ Last 3 Measurements                     │ │
│ │                                         │ │
│ │ Today: 85 cm (45%)                      │ │
│ │ 3 months ago: 83 cm (47%)               │ │
│ │ 6 months ago: 80 cm (48%)               │ │
│ │                                         │ │
│ │ [View All Measurements]                 │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ [+ Add New Measurement]                 │ │
│ └─────────────────────────────────────────┘ │
└─────────────────────────────────────────────┘
```

### Key Components

1. **Chart Selection Tabs**
   - **Chart Type Selector** component (Pills variation)
   - Toggle between different growth parameters
   - Visual indication of current selection

2. **Growth Chart Visualization**
   - Growth Chart component from Data Visualization section
   - Line chart with child's growth trajectory
   - WHO standard percentile curves
   - Clear color coding and legend
   - Interactive data points

3. **Time Range Selector**
   - Radio Button components
   - Options to view different time periods
   - Default to show all available data

4. **Recent Measurements Summary**
   - Standard Card component
   - Quick view of recent measurements
   - Percentile values for context
   - Text Button for full measurement history

5. **Chart Legend**
   - Caption typography
   - Clear explanation of lines and curves
   - Color coding consistent with chart

## Add Measurement Screen

Interface for adding new growth measurements.

### Design Specifications

- **Screen**: Add Measurement
- **Navigation**: Accessed from Growth Overview or Charts
- **Primary Actions**: Enter measurement values, save data
- **Content Priority**: Accurate data entry, guidance

### Mockup

```
┌─────────────────────────────────────────────┐
│ ←            Add Measurement                │
├─────────────────────────────────────────────┤
│ ┌─────────────────────────────────────────┐ │
│ │ Amir, 2 years 3 months                  │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ Measurement Type                            │
│ ┌─────────────────────────────────────────┐ │
│ │ ◉ Height  ○ Weight  ○ Head  ○ Multiple │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ Date                                        │
│ ┌─────────────────────────────────────────┐ │
│ │ Today (May 15, 2023)              📅    │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ Height                                      │
│ ┌─────────────────────────────────────────┐ │
│ │ 85                                 cm ▼ │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ ℹ️ Measuring tips:                       │ │
│ │ • Measure without shoes                  │ │
│ │ • Stand straight against a wall          │ │
│ │ • Keep heels, buttocks, shoulders        │ │
│ │   against the wall                       │ │
│ │ [View detailed instructions]             │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ Additional Information                      │
│ ┌─────────────────────────────────────────┐ │
│ │ Measured by                              │ │
│ │ ○ Parent  ○ Doctor  ○ Other            │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ Notes (optional)                         │ │
│ │ ┌─────────────────────────────────────┐ │ │
│ │ │                                     │ │ │
│ │ └─────────────────────────────────────┘ │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ [Preview & Save]                        │ │
│ └─────────────────────────────────────────┘ │
└─────────────────────────────────────────────┘
```

### Key Components

1. **Measurement Type Selector**
   - Radio Button components for measurement types
   - Option for multiple measurements at once
   - Body 1 typography for labels

2. **Date Selector**
   - Text Input component with calendar icon
   - Default to current date
   - Calendar picker for historical entries

3. **Measurement Input**
   - **Measurement Input** specialized component
   - Numeric input field
   - Unit selector (cm/in, kg/lb) using Dropdown component
   - Clear labeling using Body 1 typography

4. **Measurement Guidance**
   - Standard Card component
   - Tips for accurate measurement using Body 2 typography
   - Expandable detailed instructions using Text Button
   - Visual guidance (optional)

5. **Additional Context Fields**
   - Radio Button components for measurement source
   - Text Area component for optional notes
   - Clear section headers using Body 1 typography

6. **Action Button**
   - Primary Button component
   - Clear call-to-action
   - Two-step process (preview then save)

## Measurement Preview Screen

Review screen before saving a new measurement.

### Design Specifications

- **Screen**: Measurement Preview
- **Navigation**: After entering measurement data
- **Primary Actions**: Confirm and save, edit if needed
- **Content Priority**: Data verification, immediate insights

### Mockup

```
┌─────────────────────────────────────────────┐
│ ←           Measurement Preview             │
├─────────────────────────────────────────────┤
│ ┌─────────────────────────────────────────┐ │
│ │ Amir, 2 years 3 months                  │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ Height: 85 cm                      ✏️   │ │
│ │ Date: May 15, 2023                 ✏️   │ │
│ │ Measured by: Parent                ✏️   │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ Percentile: 45%                         │ │
│ │                                         │ │
│ │ This measurement places Amir in the     │ │
│ │ normal range for height-for-age.        │ │
│ │                                         │ │
│ │ [View on chart]                         │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ Growth Trend                            │ │
│ │                                         │ │
│ │ Previous: 83 cm (3 months ago)          │ │
│ │ Change: +2 cm                           │ │
│ │ Growth rate: Normal                     │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ Next Measurement                        │ │
│ │                                         │ │
│ │ Recommended: In 3 months                │ │
│ │ (August 15, 2023)                       │ │
│ │                                         │ │
│ │ [Set Reminder]                          │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ [Save Measurement]                      │ │
│ └─────────────────────────────────────────┘ │
└─────────────────────────────────────────────┘
```

### Key Components

1. **Measurement Summary**
   - Standard Card component
   - Clear display of entered values using Body 1 typography
   - Edit options (Icon Buttons) for each field
   - Visual confirmation of data

2. **Percentile Information**
   - Standard Card component
   - Calculated percentile based on WHO standards
   - Uses **Growth Status Indicator** component styling
   - Interpretation of the percentile using Body 2 typography
   - Text Button to view on chart

3. **Growth Trend Analysis**
   - Standard Card component
   - Comparison to previous measurement
   - Growth rate calculation
   - Assessment of growth velocity
   - Uses appropriate status colors from color system

4. **Next Steps**
   - Standard Card component
   - Recommendation for next measurement
   - Secondary Button to set reminder
   - Scheduling assistance

5. **Save Button**
   - Primary Button component
   - Clear call-to-action
   - Prominent placement

## Measurement History Screen

List view of all recorded measurements.

### Design Specifications

- **Screen**: Measurement History
- **Navigation**: Accessed from Growth Overview or Charts
- **Primary Actions**: View measurement details, filter history
- **Content Priority**: Chronological data, trends

### Mockup

```
┌─────────────────────────────────────────────┐
│ ←           Measurement History             │
├─────────────────────────────────────────────┤
│ ┌─────────────────────────────────────────┐ │
│ │ Amir, 2 years 3 months                  │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ Filter: ◉ All  ○ Height  ○ Weight  ○ Head │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ May 15, 2023                            │ │
│ │ Height: 85 cm (45%)                     │ │
│ │ Measured by: Parent                     │ │
│ │                                         │ │
│ │ [View Details]                          │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ May 15, 2023                            │ │
│ │ Weight: 12 kg (50%)                     │ │
│ │ Measured by: Parent                     │ │
│ │                                         │ │
│ │ [View Details]                          │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ February 12, 2023                       │ │
│ │ Height: 83 cm (47%)                     │ │
│ │ Measured by: Doctor                     │ │
│ │                                         │ │
│ │ [View Details]                          │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ February 12, 2023                       │ │
│ │ Weight: 11.5 kg (52%)                   │ │
│ │ Measured by: Doctor                     │ │
│ │                                         │ │
│ │ [View Details]                          │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ [+ Add New Measurement]                 │ │
│ └─────────────────────────────────────────┘ │
└─────────────────────────────────────────────┘
```

### Key Components

1. **Filter Controls**
   - Radio Button components
   - Options to filter by measurement type
   - Default to show all measurements

2. **Measurement Entry Cards**
   - List Card components
   - Date and measurement type using Body 1 typography
   - Value and percentile using Body 2 typography
   - Measured by information using Caption typography
   - Text Button for detailed view

3. **Chronological Organization**
   - Most recent measurements at top
   - Clear date headers using Subtitle 1 typography
   - Visual grouping of same-day measurements

4. **Add Measurement Button**
   - Primary Button component
   - Consistent placement with other screens
   - Always accessible

## Growth Assessment Screen

Detailed analysis of the child's growth status.

### Design Specifications

- **Screen**: Growth Assessment
- **Navigation**: Accessed from Growth Overview
- **Primary Actions**: View detailed analysis, access recommendations
- **Content Priority**: Growth status, actionable insights

### Mockup

```
┌─────────────────────────────────────────────┐
│ ←           Growth Assessment               │
├─────────────────────────────────────────────┤
│ ┌─────────────────────────────────────────┐ │
│ │ Amir, 2 years 3 months                  │ │
│ │ Assessment based on latest measurements │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ Overall Growth Status                   │ │
│ │                                         │ │
│ │ Amir is growing normally according to   │ │
│ │ WHO child growth standards.             │ │
│ │                                         │ │
│ │ No signs of stunting, wasting, or       │ │
│ │ overweight detected.                    │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ Height-for-Age                          │ │
│ │                                         │ │
│ │ Current: 85 cm (45th percentile)        │ │
│ │ Status: Normal                          │ │
│ │                                         │ │
│ │ Amir's height is in the normal range    │ │
│ │ for his age, showing consistent growth. │ │
│ │                                         │ │
│ │ [View Chart]                            │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ Weight-for-Age                          │ │
│ │                                         │ │
│ │ Current: 12 kg (50th percentile)        │ │
│ │ Status: Normal                          │ │
│ │                                         │ │
│ │ Amir's weight is appropriate for his    │ │
│ │ age, following the expected pattern.    │ │
│ │                                         │ │
│ │ [View Chart]                            │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ [View Recommendations]                  │ │
│ └─────────────────────────────────────────┘ │
└─────────────────────────────────────────────┘
```

### Key Components

1. **Overall Status Summary**
   - Standard Card component
   - Clear statement of overall growth status using Body 1 typography
   - Reference to standards used
   - Highlight of any concerns or positives

2. **Parameter-Specific Assessments**
   - Standard Card components for each parameter
   - Uses **Growth Status Indicator** components
   - Current value and percentile using **Measurement Value Card** styling
   - Status classification
   - Plain language explanation using Body 2 typography
   - Text Button to relevant chart

3. **Visual Status Indicators**
   - Color coding for normal/concerning values from color system
   - Icons to reinforce status
   - Consistent visual language with **Growth Status Indicator** component

4. **Recommendations Link**
   - Primary Button component
   - Access to personalized recommendations
   - Based on assessment results

## Design Notes

1. **Growth Chart Visualization**
   - Use of standard WHO growth chart patterns
   - Clear color differentiation between child's line and standards
   - Interactive elements for exploring data points
   - Appropriate scaling for different screen sizes

2. **Measurement Entry**
   - Numeric keyboard for measurement values
   - Input validation to prevent impossible values
   - Unit conversion support
   - Clear guidance for accurate measurements

3. **Status Communication**
   - Careful language choices to inform without alarming
   - Clear explanations of medical terms
   - Positive reinforcement for normal growth
   - Actionable guidance for any concerns

4. **Accessibility Considerations**
   - Color is not the only indicator of status (icons and text also used)
   - Charts include alternative text descriptions
   - Numeric data available alongside visual representations
   - Adequate contrast for text and important elements

5. **Educational Integration**
   - Contextual links to educational content
   - Age-appropriate growth information
   - Explanation of growth standards and percentiles
   - Tips for supporting healthy growth 