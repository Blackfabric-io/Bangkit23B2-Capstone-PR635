# NutriGenius Component System

This document outlines the core UI components used throughout the NutriGenius application.

## Buttons

Buttons provide clear, tappable targets for user actions.

### Primary Button

Used for the main call-to-action on each screen.

- **Background**: Primary Green (#2E7D32)
- **Text**: White (#FFFFFF)
- **Font**: Nunito Semi-Bold, 14px
- **Height**: 48px
- **Padding**: 16px horizontal
- **Border Radius**: 8px
- **States**:
  - Hover: 10% darker
  - Pressed: 15% darker
  - Disabled: 50% opacity, not clickable

### Secondary Button

Used for secondary actions and less prominent choices.

- **Background**: White (#FFFFFF)
- **Border**: 1px solid Primary Green (#2E7D32)
- **Text**: Primary Green (#2E7D32)
- **Font**: Nunito Semi-Bold, 14px
- **Height**: 48px
- **Padding**: 16px horizontal
- **Border Radius**: 8px
- **States**:
  - Hover: Light Green (#C8E6C9) background
  - Pressed: Darker Light Green background
  - Disabled: 50% opacity, not clickable

### Text Button

Used for tertiary actions or in space-constrained areas.

- **Background**: Transparent
- **Text**: Primary Green (#2E7D32)
- **Font**: Nunito Semi-Bold, 14px
- **Height**: 36px
- **Padding**: 8px horizontal
- **States**:
  - Hover: 10% Light Green background
  - Pressed: 15% Light Green background
  - Disabled: 50% opacity, not clickable

### Icon Button

Used for actions that can be represented by a clear icon.

- **Background**: Transparent
- **Icon**: 24px, Primary Green (#2E7D32)
- **Size**: 48px × 48px (touch target)
- **States**:
  - Hover: 10% Light Green background
  - Pressed: 15% Light Green background
  - Disabled: 50% opacity, not clickable

### Floating Action Button (FAB)

Used for the primary action on screens (e.g., add a meal, take a measurement).

- **Background**: Accent Orange (#FF8F00)
- **Icon**: 24px, White (#FFFFFF)
- **Size**: 56px × 56px
- **Shadow**: 2dp elevation
- **Border Radius**: 28px (circular)
- **States**:
  - Hover: 10% darker
  - Pressed: 15% darker
  - Disabled: 50% opacity, not clickable

## Cards

Cards contain content and actions about a single subject.

### Standard Card

Used for displaying discrete information in a structured format.

- **Background**: White (#FFFFFF)
- **Border Radius**: 12px
- **Shadow**: 1dp elevation
- **Padding**: 16px
- **Structure**:
  - Title: H4 typography
  - Subtitle (optional): Subtitle 2 typography
  - Content: Body 2 typography
  - Actions: Text Buttons or Icon Buttons
- **States**:
  - Hover: Subtle shadow increase
  - Pressed: Darker background

### Dashboard Card

Specialized cards for the main dashboard screen.

- **Background**: White (#FFFFFF)
- **Border Radius**: 16px
- **Border**: 1px solid Light Gray (#E0E0E0)
- **Shadow**: 1dp elevation
- **Padding**: 16px
- **Structure**:
  - Icon: 24px, Primary Green
  - Title: H5 typography
  - Value: H3 typography, Primary Green
  - Change indicator: Caption typography with appropriate color
  - Chart (optional): Inline mini chart
- **States**:
  - Hover: Subtle shadow increase
  - Pressed: Darker background

### List Card

Used for displaying items in a vertical list format.

- **Background**: White (#FFFFFF)
- **Border Radius**: 12px
- **Shadow**: 1dp elevation
- **Item Height**: 72px minimum
- **Item Padding**: 16px
- **Structure**:
  - Leading element (icon/avatar): 40px × 40px
  - Primary text: Body 1 typography
  - Secondary text: Body 2 typography, Dark Gray
  - Trailing element (optional): Icon Button or meta text
- **Divider**: 1px Light Gray (#E0E0E0)

## Form Elements

### Text Input

Used for single-line text entry.

- **Height**: 56px
- **Background**: White (#FFFFFF)
- **Border**: 1px solid Light Gray (#E0E0E0)
- **Border Radius**: 8px
- **Structure**:
  - Label: Caption typography, Dark Gray
  - Input Text: Body 1 typography
  - Helper Text: Caption typography
- **States**:
  - Focus: Primary Green border, 2px
  - Error: Error Red border, error message in helper text
  - Disabled: 50% opacity, Light Gray background

### Text Area

Used for multi-line text entry.

- **Min Height**: 112px
- **Background**: White (#FFFFFF)
- **Border**: 1px solid Light Gray (#E0E0E0)
- **Border Radius**: 8px
- **Padding**: 16px
- **Structure**:
  - Label: Caption typography, Dark Gray
  - Input Text: Body 1 typography
  - Helper Text: Caption typography
- **States**:
  - Focus: Primary Green border, 2px
  - Error: Error Red border, error message in helper text
  - Disabled: 50% opacity, Light Gray background

### Dropdown

Used for selecting options from a predefined list.

- **Height**: 56px
- **Background**: White (#FFFFFF)
- **Border**: 1px solid Light Gray (#E0E0E0)
- **Border Radius**: 8px
- **Structure**:
  - Label: Caption typography, Dark Gray
  - Selected Value: Body 1 typography
  - Dropdown Icon: 24px, Dark Gray
  - Options Menu: White background, 1dp elevation
  - Option Item: Body 1 typography, 48px height
- **States**:
  - Focus: Primary Green border, 2px
  - Error: Error Red border, error message in helper text
  - Disabled: 50% opacity, Light Gray background

### Checkbox

Used for multi-select options or toggles.

- **Size**: 24px × 24px
- **Touch Target**: 40px × 40px
- **Colors**:
  - Unchecked: 2px border, Dark Gray
  - Checked: Primary Green fill
  - Check Mark: White
- **Label**: Body 2 typography, aligned to right of checkbox
- **States**:
  - Focus: Light Green halo effect
  - Error: Error Red border
  - Disabled: 50% opacity

### Radio Button

Used for single-select options.

- **Size**: 20px × 20px
- **Touch Target**: 40px × 40px
- **Colors**:
  - Unselected: 2px border, Dark Gray
  - Selected: Primary Green outer ring, Primary Green center dot
- **Label**: Body 2 typography, aligned to right of radio button
- **States**:
  - Focus: Light Green halo effect
  - Error: Error Red border
  - Disabled: 50% opacity

### Switch

Used for binary toggles.

- **Size**: 32px × 20px
- **Touch Target**: 40px × 40px
- **Colors**:
  - Off: Light Gray track, White thumb
  - On: Primary Green track, White thumb
- **Label**: Body 2 typography, aligned to left of switch
- **States**:
  - Focus: Light Green halo effect
  - Disabled: 50% opacity

## Navigation

### Bottom Navigation Bar

Primary navigation for the mobile app.

- **Height**: 56px
- **Background**: White (#FFFFFF)
- **Shadow**: 4dp elevation, top only
- **Item Structure**:
  - Icon: 24px
  - Label: Caption typography
- **Item States**:
  - Active: Primary Green icon and text
  - Inactive: Medium Gray icon and text
  - Pressed: Light Green background

### Top App Bar

Contains page title and key actions.

- **Height**: 56px
- **Background**: Primary Green (#2E7D32)
- **Text**: White (#FFFFFF), H6 typography
- **Icons**: 24px, White (#FFFFFF)
- **Structure**:
  - Left: Navigation icon (menu or back)
  - Center: Page title
  - Right: Action icons (max 2-3)

### Tabs

Used for switching between related content views.

- **Height**: 48px
- **Structure**:
  - Tab: Equal width or content-based
  - Label: Button typography
  - Indicator: 2px, Primary Green
- **States**:
  - Active: Primary Green text, indicator visible
  - Inactive: Dark Gray text, no indicator
  - Hover: Light Green background
  - Pressed: Darker Light Green background

## Feedback & Alerts

### Snackbar

Used for brief, non-disruptive feedback.

- **Height**: 48px minimum
- **Background**: Dark Gray (#616161)
- **Text**: White (#FFFFFF), Body 2 typography
- **Border Radius**: 4px
- **Padding**: 16px
- **Action**: Text Button, Accent Orange (#FF8F00)
- **Position**: Bottom center, 16px margin
- **Duration**: 4 seconds by default

### Dialog

Used for critical information requiring user decision.

- **Width**: 280px minimum, 80% of screen width maximum
- **Background**: White (#FFFFFF)
- **Border Radius**: 12px
- **Shadow**: 24dp elevation
- **Structure**:
  - Title: H5 typography, 24px top padding, 16px side padding
  - Content: Body 1 typography, 16px padding
  - Actions: Button row, 8px padding, right-aligned
- **Scrim**: Black at 30% opacity for background

### Toast

Used for lightweight feedback.

- **Height**: 48px
- **Background**: Dark Gray (#616161) semi-transparent
- **Text**: White (#FFFFFF), Body 2 typography
- **Border Radius**: 24px
- **Padding**: 16px horizontal
- **Position**: Bottom center, 16px margin
- **Duration**: 2 seconds by default

### Progress Indicators

#### Circular Progress

Used for indeterminate loading states.

- **Size**: 24px, 40px, or 56px
- **Color**: Primary Green (#2E7D32)
- **Track**: Light Gray (#E0E0E0) or transparent

#### Linear Progress

Used for determinate progress indication.

- **Height**: 4px
- **Colors**:
  - Track: Light Gray (#E0E0E0)
  - Indicator: Primary Green (#2E7D32)
- **Animation**: Left-to-right fill for determinate, indeterminate animation for unknown progress

## Data Visualization

### Charts

Common properties for all chart types:

- **Container**: Standard Card
- **Title**: H5 typography
- **Subtitle**: Caption typography, Dark Gray
- **Legend**: Caption typography
- **Axes Labels**: Caption typography
- **Data Labels**: Caption typography
- **Colors**: Chart color palette from Color System

#### Growth Chart

Specialized chart for tracking child growth metrics.

- **X-Axis**: Age in months
- **Y-Axis**: Measurement value (height, weight)
- **Reference Lines**: WHO growth percentiles (3rd, 15th, 50th, 85th, 97th)
- **Child Data**: Primary Green line with data points
- **Interaction**: Tap on point shows detailed tooltip

#### Nutrition Pie Chart

Shows nutritional breakdown of food items or meals.

- **Segments**: Major nutrient groups (proteins, carbs, fats)
- **Colors**: Chart color palette
- **Center Text**: Total calories or primary value
- **Legend**: Caption typography with percentage values

## Special Components

### Camera Scanner Overlay

Used during food scanning process.

- **Full Screen Overlay**: Semi-transparent black background
- **Scan Area**: Center rectangle with white border
- **Helper Text**: Body 2 typography, white
- **Cancel Button**: Text Button, white
- **Flash Toggle**: Icon Button, white

### Measurement Input

Specialized input for capturing child measurements.

- **Container**: Standard Card
- **Title**: H5 typography
- **Value**: Large input field, Body 1 typography
- **Unit**: Caption typography next to value
- **Date Picker**: Caption typography with calendar icon
- **Save Button**: Primary Button

### Food Item Card

Specialized card for displaying food items.

- **Container**: Standard Card
- **Food Image**: 80px × 80px, rounded corners
- **Food Name**: H5 typography
- **Nutritional Summary**: Body 2 typography, Dark Gray
- **Serving Size**: Caption typography
- **Actions**: Add button or serving size selector
- **Expanded State**: Shows detailed nutritional breakdown 

### Media Capture Components

#### Camera Viewfinder
- **Purpose**: Provides a preview for camera capture
- **Container**: Full width with 3:4 or 1:1 aspect ratio
- **Overlay**: Semi-transparent guides for optimal food positioning
- **Focus indicator**: Primary green circle
- **States**: Normal, Focusing, Capturing
- **Variations**: Full screen, In-card

#### Capture Controls
- **Purpose**: Controls for image capture
- **Attributes**:
  - Capture button: Large circular button (60px diameter)
  - Secondary controls: 40px diameter circular buttons
  - Control bar: 80% width, centered, 12px padding, light background
- **Buttons**:
  - Primary capture: White with Primary Green border
  - Flash toggle: Yellow (`#F8D64E`)
  - Gallery access: Secondary Green (`#43A047`)

### Dashboard-Specific Cards

#### Stat Summary Card
- **Purpose**: Displays key metrics with visual indicators
- **Attributes**:
  - Container: Standard card with reduced padding (12px)
  - Header: H6 typography, left-aligned
  - Metric value: H4 typography, Primary Green
  - Visual indicator: 40px × 40px area for chart/icon
  - Metric change: Caption typography with directional indicator
- **Variations**: 
  - Positive change (Success Green)
  - Negative change (Error Red)
  - Neutral (Medium Gray)

#### Activity Card
- **Purpose**: Shows recent activities in compact format
- **Attributes**:
  - Container: Standard card
  - Timestamp: Caption typography, Dark Gray
  - Activity text: Body 2 typography
  - Icon: 16px standard icon, left-aligned
- **Variations**:
  - With action button
  - With expandable view

### Education-Specific Components

#### Article Card
- **Purpose**: Displays educational article previews
- **Attributes**:
  - Container: Standard card
  - Image: 16:9 aspect ratio
  - Title: H6 typography
  - Description: Body 2 typography, Dark Gray
  - Reading time: Caption typography, Medium Gray
  - Category tag: Caption typography, Primary Green
- **Variations**:
  - Horizontal layout (image left, text right)
  - Vertical layout (image top, text bottom)
  - Featured layout (larger image, more prominent)
  - Compact layout (minimal information, used in lists)

#### Learning Path Card
- **Purpose**: Displays educational learning paths with progress
- **Attributes**:
  - Container: Standard card with 16px padding
  - Title: H6 typography
  - Icon: 24px standard icon related to topic
  - Progress indicator: 4px height linear progress bar
  - Progress text: Caption typography ("X% complete")
  - Status: Caption typography, Primary Green
- **Variations**:
  - Not started (empty progress bar)
  - In progress (partial fill, Primary Green)
  - Completed (full fill, Success Green)
  - Recommended (accent highlight)

#### Category Card
- **Purpose**: Navigation to content categories
- **Attributes**:
  - Container: Square card, 80px × 80px
  - Icon: 32px category icon, centered
  - Label: Caption typography, centered below icon
  - Background: Light Gray or Light Green
- **Variations**:
  - Standard (Light Gray background)
  - Featured (Light Green background)
  - With count badge (shows number of articles)

### Growth Tracking Components

#### Measurement Value Card
- **Purpose**: Displays individual measurement metrics
- **Attributes**:
  - Container: Compact card with 12px padding
  - Metric name: Caption typography, Dark Gray
  - Value: H5 typography, Primary Green
  - Percentile: Body 2 typography in parentheses
  - Trend indicator: Small arrow icon (up/down/neutral)
- **Variations**:
  - Normal range (Primary Green)
  - Below range (Warning Orange)
  - Above range (Info Blue)
  - Critical (Error Red)

#### Chart Type Selector
- **Purpose**: Toggle between different chart types
- **Attributes**:
  - Container: Horizontal row with equal spacing
  - Options: Text with radio button style indicators
  - Selected state: Filled circle (Primary Green)
  - Unselected state: Empty circle (Medium Gray)
  - Label: Body 2 typography
- **Variations**:
  - Compact (icons only)
  - Standard (text labels)
  - Pills (rounded button style)

#### Growth Status Indicator
- **Purpose**: Shows growth parameter status assessment
- **Attributes**:
  - Container: Row with label and status
  - Parameter: Body 2 typography, Dark Gray
  - Status text: Body 2 typography, varies by status
  - Status icon: 16px icon matching status
- **Variations**:
  - Normal (Success Green, checkmark icon)
  - Stunted/Underweight (Warning Orange, warning icon)
  - Severely stunted/underweight (Error Red, alert icon)
  - Overweight (Info Blue, info icon) 