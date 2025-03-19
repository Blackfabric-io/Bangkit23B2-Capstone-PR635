# Food Scanning Mockups

This document presents the mockups for the NutriGenius food scanning feature, which allows parents to identify foods and analyze their nutritional content using their smartphone camera.

## Food Scanner Home Screen

The entry point for the food scanning feature, providing access to the camera and recent scan history.

### Design Specifications

- **Screen**: Food Scanner Home
- **Navigation**: Accessed from bottom navigation or dashboard
- **Primary Actions**: Scan food, view history, manual search
- **Content Priority**: Quick access to scanning, recent results

### Mockup

```
┌─────────────────────────────────────────────┐
│ ≡               Food Scanner           👤   │
├─────────────────────────────────────────────┤
│ ┌─────────────────────────────────────────┐ │
│ │ Scan food to track nutrition            │ │
│ │                                         │ │
│ │ ┌─────────────────────────────────────┐ │ │
│ │ │                                     │ │ │
│ │ │                                     │ │ │
│ │ │                                     │ │ │
│ │ │          [Camera Preview]           │ │ │
│ │ │                                     │ │ │
│ │ │                                     │ │ │
│ │ │                                     │ │ │
│ │ └─────────────────────────────────────┘ │ │
│ │                                         │ │
│ │ [Tap to Scan Food]                      │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ Can't scan? [Search Food Database]      │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ Recent Scans                            │ │
│ │                                         │ │
│ │ ┌───────────┐ ┌───────────┐ ┌──────────┐│ │
│ │ │ [Apple]   │ │ [Rice]    │ │ [Chicken]││ │
│ │ │ Today     │ │ Yesterday │ │ May 10   ││ │
│ │ └───────────┘ └───────────┘ └──────────┘│ │
│ │                                         │ │
│ │ [View All History]                      │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ Scanning Tips                           │ │
│ │ • Good lighting improves accuracy       │ │
│ │ • Center the food in frame              │ │
│ │ • Scan one food item at a time          │ │
│ │ • Hold camera 6-12 inches from food     │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ 🏠    📏    📷    📚    👨‍⚕️  │
└─────────────────────────────────────────────┘
```

### Key Components

1. **Camera Preview**
   - Live camera feed in compact view
   - Clear call-to-action to begin scanning
   - Tap to expand to full camera interface

2. **Alternative Entry Points**
   - Manual search option for when scanning isn't ideal
   - Clear, accessible placement

3. **Recent Scans**
   - Horizontal scrollable list of recent food scans
   - Visual thumbnails with food names
   - Timestamp for context
   - Link to full history

4. **Scanning Tips**
   - Concise guidance for optimal scanning results
   - Improves user success rate

## Camera Scanning Screen

Full-screen camera interface for capturing food images.

### Design Specifications

- **Screen**: Camera Scanner
- **Navigation**: Accessed from Scanner Home
- **Primary Actions**: Capture image, select from gallery, cancel
- **Content Priority**: Clear viewfinder, intuitive controls

### Mockup

```
┌─────────────────────────────────────────────┐
│                                             │
│                                             │
│                                             │
│                                             │
│                                             │
│                                             │
│  ┌───────────────────────────────────────┐  │
│  │                                       │  │
│  │                                       │  │
│  │                                       │  │
│  │                                       │  │
│  │                                       │  │
│  │                                       │  │
│  │                                       │  │
│  │                                       │  │
│  │                                       │  │
│  └───────────────────────────────────────┘  │
│                                             │
│                                             │
│                                             │
│                                             │
│                                             │
│                                             │
│  Center food in the frame                   │
│                                             │
│  ╔═══╗    ⦿    ╔═══╗                       │
│  ║ 🖼️ ║         ║ ⚙️ ║                       │
│  ╚═══╝         ╚═══╝                       │
└─────────────────────────────────────────────┘
```

### Key Components

1. **Camera Viewfinder**
   - Live camera feed in standard Camera Viewfinder component
   - Framing guide overlay for optimal food positioning
   - Focus indicator using Primary Green circle
   - Full screen variation for optimal capture experience

2. **Capture Controls**
   - Primary capture button (60px white circle with Primary Green border)
   - Flash toggle button (40px yellow circle)
   - Gallery access button (40px Secondary Green circle)
   - Control bar with 80% width, centered at bottom of screen

3. **Guidance Text**
   - Simple instruction for optimal scanning
   - Minimal to avoid cluttering the interface

4. **Cancel Option**
   - Easy way to return to scanner home
   - Positioned for easy access

## Image Processing Screen

Feedback screen while the image is being analyzed.

### Design Specifications

- **Screen**: Processing
- **Navigation**: Automatic after image capture
- **Primary Actions**: Cancel processing
- **Content Priority**: Processing status, engaging feedback

### Mockup

```
┌─────────────────────────────────────────────┐
│                                             │
│                                             │
│                                             │
│                                             │
│  ┌───────────────────────────────────────┐  │
│  │                                       │  │
│  │                                       │  │
│  │                                       │  │
│  │                                       │  │
│  │          [Captured Image]             │  │
│  │                                       │  │
│  │                                       │  │
│  │                                       │  │
│  │                                       │  │
│  └───────────────────────────────────────┘  │
│                                             │
│                                             │
│  Analyzing food...                          │
│                                             │
│  ┌───────────────────────────────────────┐  │
│  │         [Progress Indicator]          │  │
│  └───────────────────────────────────────┘  │
│                                             │
│  Identifying ingredients and calculating    │
│  nutritional information                    │
│                                             │
│  [Cancel]                                   │
└─────────────────────────────────────────────┘
```

### Key Components

1. **Captured Image Display**
   - Shows the image being analyzed
   - Maintains context for user

2. **Progress Indicator**
   - Clear visual feedback on processing status
   - Animated to indicate active processing

3. **Status Messages**
   - Informative text about current processing step
   - Manages expectations about processing time

4. **Cancel Option**
   - Allows user to abort lengthy processing
   - Returns to camera screen

## Food Identification Results

Screen showing the results of food recognition.

### Design Specifications

- **Screen**: Recognition Results
- **Navigation**: Automatic after processing completes
- **Primary Actions**: Confirm food, select alternative, retry
- **Content Priority**: Recognition accuracy, food selection

### Mockup

```
┌─────────────────────────────────────────────┐
│ ←            Recognition Results            │
├─────────────────────────────────────────────┤
│                                             │
│  ┌───────────────────────────────────────┐  │
│  │                                       │  │
│  │                                       │  │
│  │          [Captured Image]             │  │
│  │                                       │  │
│  │                                       │  │
│  └───────────────────────────────────────┘  │
│                                             │
│  We found these possible matches:           │
│                                             │
│  ┌───────────────────────────────────────┐  │
│  │ ◉ Apple, Red Delicious (95%)          │  │
│  │   Medium-sized, raw                   │  │
│  └───────────────────────────────────────┘  │
│                                             │
│  ┌───────────────────────────────────────┐  │
│  │ ○ Apple, Gala (82%)                   │  │
│  │   Medium-sized, raw                   │  │
│  └───────────────────────────────────────┘  │
│                                             │
│  ┌───────────────────────────────────────┐  │
│  │ ○ Apple, Generic (78%)                │  │
│  │   Medium-sized, raw                   │  │
│  └───────────────────────────────────────┘  │
│                                             │
│  Not what you're looking for?               │
│  [Search Manually]    [Retake Photo]        │
│                                             │
│  ┌───────────────────────────────────────┐  │
│  │ [Continue with Selected Food]         │  │
│  └───────────────────────────────────────┘  │
└─────────────────────────────────────────────┘
```

### Key Components

1. **Captured Image**
   - Reference to what was scanned
   - Maintains context

2. **Recognition Results**
   - List of potential matches with confidence percentages
   - Radio button selection for choosing correct option
   - Default selection of highest confidence match
   - Brief description of each option

3. **Alternative Actions**
   - Manual search option if recognition failed
   - Retake photo option for poor quality images

4. **Confirmation Button**
   - Clear call-to-action to proceed with selected food
   - Disabled until a food is selected

## Portion Size Selection

Screen for specifying the portion size of the identified food.

### Design Specifications

- **Screen**: Portion Selection
- **Navigation**: After food identification confirmation
- **Primary Actions**: Select portion size, continue
- **Content Priority**: Accurate portion estimation, visual guidance

### Mockup

```
┌─────────────────────────────────────────────┐
│ ←             Portion Selection              │
├─────────────────────────────────────────────┤
│                                             │
│  Apple, Red Delicious                       │
│                                             │
│  ┌───────────────────────────────────────┐  │
│  │                                       │  │
│  │          [Food Image]                 │  │
│  │                                       │  │
│  │                                       │  │
│  └───────────────────────────────────────┘  │
│                                             │
│  How much was consumed?                     │
│                                             │
│  ┌───────────────────────────────────────┐  │
│  │ Portion Size                      ▼   │  │
│  └───────────────────────────────────────┘  │
│  ● 1 medium apple (182g)                    │
│  ○ 1 small apple (149g)                     │
│  ○ 1 large apple (223g)                     │
│  ○ Half medium apple (91g)                  │
│  ○ Custom amount                            │
│                                             │
│  ┌───────────────────────────────────────┐  │
│  │ Visual Reference                       │  │
│  │ ┌─────────┐ ┌─────────┐ ┌─────────┐   │  │
│  │ │ Small   │ │ Medium  │ │ Large   │   │  │
│  │ └─────────┘ └─────────┘ └─────────┘   │  │
│  └───────────────────────────────────────┘  │
│                                             │
│  ┌───────────────────────────────────────┐  │
│  │ [Continue]                            │  │
│  └───────────────────────────────────────┘  │
└─────────────────────────────────────────────┘
```

### Key Components

1. **Food Identification**
   - Clear display of identified food
   - Image reference

2. **Portion Selection**
   - Common portion options with weights
   - Radio button selection
   - Default to most common portion
   - Custom option for precise amounts

3. **Visual Reference**
   - Visual comparison of different portion sizes
   - Helps user make accurate selection

4. **Custom Amount Option**
   - Expands to show numeric input and unit selection
   - Supports precise portion tracking

## Nutritional Information Display

Screen showing the nutritional breakdown of the scanned food.

### Design Specifications

- **Screen**: Nutrition Information
- **Navigation**: After portion selection
- **Primary Actions**: Add to meal log, view details, dietary analysis
- **Content Priority**: Key nutritional information, actionable insights

### Mockup

```
┌─────────────────────────────────────────────┐
│ ←           Nutrition Information            │
├─────────────────────────────────────────────┤
│                                             │
│  Apple, Red Delicious                       │
│  1 medium apple (182g)                      │
│                                             │
│  ┌───────────────────────────────────────┐  │
│  │                                       │  │
│  │          [Food Image]                 │  │
│  │                                       │  │
│  │                                       │  │
│  └───────────────────────────────────────┘  │
│                                             │
│  ┌───────────────────────────────────────┐  │
│  │ Nutrition Summary                     │  │
│  │                                       │  │
│  │ Calories: 95 kcal                     │  │
│  │ Carbohydrates: 25g (8% daily value)   │  │
│  │ Fiber: 4.4g (18% daily value)         │  │
│  │ Sugar: 19g                            │  │
│  │ Protein: 0.5g (1% daily value)        │  │
│  │ Fat: 0.3g (0% daily value)            │  │
│  │                                       │  │
│  │ [View All Nutrients]                  │  │
│  └───────────────────────────────────────┘  │
│                                             │
│  ┌───────────────────────────────────────┐  │
│  │ Dietary Analysis                      │  │
│  │                                       │  │
│  │ ✓ Good source of fiber               │  │
│  │ ✓ Low in fat                         │  │
│  │ ⚠ High in natural sugars             │  │
│  │                                       │  │
│  │ [View Full Analysis]                  │  │
│  └───────────────────────────────────────┘  │
│                                             │
│  ┌───────────────────────────────────────┐  │
│  │ [Add to Meal Log]                     │  │
│  └───────────────────────────────────────┘  │
└─────────────────────────────────────────────┘
```

### Key Components

1. **Food Identification**
   - Clear display of food name and portion
   - Image reference

2. **Nutrition Summary**
   - Key nutrients with values and daily percentages
   - Focus on most important nutritional information
   - Link to view complete nutritional breakdown

3. **Dietary Analysis**
   - Quick insights about the food's nutritional properties
   - Visual indicators for positive and cautionary aspects
   - Link to more detailed analysis

4. **Add to Meal Log**
   - Prominent button to log the food
   - Primary action for the screen

## Detailed Nutrients View

Expanded view showing complete nutritional information.

### Design Specifications

- **Screen**: Detailed Nutrients
- **Navigation**: From Nutrition Information screen
- **Primary Actions**: Return to summary, add to meal log
- **Content Priority**: Comprehensive nutritional data, organized categories

### Mockup

```
┌─────────────────────────────────────────────┐
│ ←            Detailed Nutrients             │
├─────────────────────────────────────────────┤
│                                             │
│  Apple, Red Delicious                       │
│  1 medium apple (182g)                      │
│                                             │
│  ┌───────────────────────────────────────┐  │
│  │ Macronutrients                        │  │
│  │                                       │  │
│  │ Calories: 95 kcal                     │  │
│  │ Carbohydrates: 25g (8% DV)            │  │
│  │   Fiber: 4.4g (18% DV)                │  │
│  │   Sugars: 19g                         │  │
│  │     Added Sugars: 0g (0% DV)          │  │
│  │ Protein: 0.5g (1% DV)                 │  │
│  │ Fat: 0.3g (0% DV)                     │  │
│  │   Saturated: 0.1g (0% DV)             │  │
│  │   Trans: 0g                           │  │
│  │   Polyunsaturated: 0.1g               │  │
│  │   Monounsaturated: 0.1g               │  │
│  └───────────────────────────────────────┘  │
│                                             │
│  ┌───────────────────────────────────────┐  │
│  │ Vitamins                              │  │
│  │                                       │  │
│  │ Vitamin C: 8.4mg (9% DV)              │  │
│  │ Vitamin A: 98 IU (2% DV)              │  │
│  │ Vitamin K: 4µg (3% DV)                │  │
│  │ Vitamin E: 0.3mg (2% DV)              │  │
│  │ Vitamin B6: 0.1mg (4% DV)             │  │
│  └───────────────────────────────────────┘  │
│                                             │
│  ┌───────────────────────────────────────┐  │
│  │ Minerals                              │  │
│  │                                       │  │
│  │ Potassium: 195mg (4% DV)              │  │
│  │ Manganese: 0.1mg (3% DV)              │  │
│  │ Copper: 0.1mg (3% DV)                 │  │
│  │ [Show More]                           │  │
│  └───────────────────────────────────────┘  │
│                                             │
│  ┌───────────────────────────────────────┐  │
│  │ [Add to Meal Log]                     │  │
│  └───────────────────────────────────────┘  │
└─────────────────────────────────────────────┘
```

### Key Components

1. **Nutrient Categories**
   - Organized sections for macronutrients, vitamins, minerals
   - Hierarchical display with indentation for subcategories
   - Daily value percentages where applicable

2. **Comprehensive Data**
   - Complete nutritional breakdown
   - Expandable sections for less common nutrients
   - Consistent formatting and units

3. **Visual Organization**
   - Clear section headers
   - Adequate spacing for readability
   - Collapsible sections for managing screen space

4. **Add to Meal Log**
   - Consistent placement with other screens
   - Maintains primary action availability

## Meal Logging Screen

Interface for adding the scanned food to the meal log.

### Design Specifications

- **Screen**: Add to Meal Log
- **Navigation**: From Nutrition Information screen
- **Primary Actions**: Select child, meal type, and time; save entry
- **Content Priority**: Quick and accurate meal logging

### Mockup

```
┌─────────────────────────────────────────────┐
│ ←               Add to Meal Log              │
├─────────────────────────────────────────────┤
│                                             │
│  Apple, Red Delicious                       │
│  1 medium apple (182g)                      │
│                                             │
│  For which child?                           │
│  ┌───────────────────────────────────────┐  │
│  │ Amir                              ▼   │  │
│  └───────────────────────────────────────┘  │
│                                             │
│  Meal type                                  │
│  ┌───────────────────────────────────────┐  │
│  │ ○ Breakfast                           │  │
│  │ ○ Morning Snack                       │  │
│  │ ● Lunch                               │  │
│  │ ○ Afternoon Snack                     │  │
│  │ ○ Dinner                              │  │
│  │ ○ Evening Snack                       │  │
│  └───────────────────────────────────────┘  │
│                                             │
│  When consumed?                             │
│  ┌───────────────────────────────────────┐  │
│  │ Today, 12:30 PM                  📅   │  │
│  └───────────────────────────────────────┘  │
│                                             │
│  Notes (optional)                           │
│  ┌───────────────────────────────────────┐  │
│  │                                       │  │
│  │                                       │  │
│  └───────────────────────────────────────┘  │
│                                             │
│  ┌───────────────────────────────────────┐  │
│  │ [Save to Meal Log]                    │  │
│  └───────────────────────────────────────┘  │
└─────────────────────────────────────────────┘
```

### Key Components

1. **Food Summary**
   - Clear display of food being logged
   - Maintains context

2. **Child Selection**
   - Dropdown for households with multiple children
   - Hidden if only one child is registered

3. **Meal Type Selection**
   - Radio buttons for common meal categories
   - Default based on current time

4. **Time Selection**
   - Date and time picker
   - Defaults to current time
   - Option to adjust for past meals

5. **Notes Field**
   - Optional additional context
   - Preparation details, combinations, etc.

6. **Save Button**
   - Clear call-to-action
   - Completes the food scanning workflow

## Confirmation Screen

Feedback after successfully logging a meal.

### Design Specifications

- **Screen**: Logging Confirmation
- **Navigation**: Automatic after saving to meal log
- **Primary Actions**: Scan another food, view meal log, return to dashboard
- **Content Priority**: Success feedback, next steps

### Mockup

```
┌─────────────────────────────────────────────┐
│                                             │
│                                             │
│                                             │
│                                             │
│  ┌───────────────────────────────────────┐  │
│  │                                       │  │
│  │                 ✓                     │  │
│  │                                       │  │
│  │      Added to Amir's Meal Log!        │  │
│  │                                       │  │
│  │  Apple, Red Delicious                 │  │
│  │  Lunch - Today, 12:30 PM              │  │
│  │                                       │  │
│  └───────────────────────────────────────┘  │
│                                             │
│  ┌───────────────────────────────────────┐  │
│  │ Nutrition Progress Today               │  │
│  │                                       │  │
│  │ [Progress Bar Visualization]          │  │
│  │                                       │  │
│  │ Calories: 876/1400 kcal               │  │
│  │ Protein: 22/40g                       │  │
│  │ Fiber: 12/25g                         │  │
│  │                                       │  │
│  │ [View Full Nutrition Report]          │  │
│  └───────────────────────────────────────┘  │
│                                             │
│  What would you like to do next?            │
│                                             │
│  [Scan Another Food]  [View Meal Log]       │
│                                             │
│  [Return to Dashboard]                      │
└─────────────────────────────────────────────┘
```

### Key Components

1. **Success Confirmation**
   - Clear visual indicator of successful logging
   - Summary of what was logged
   - Positive reinforcement

2. **Nutrition Progress**
   - Updated daily nutrition summary
   - Visual progress indicators
   - Context for how this food contributes to daily goals

3. **Next Action Options**
   - Multiple paths forward based on user intent
   - Continue scanning for multi-item meals
   - View complete meal log
   - Return to dashboard

## Scan History Screen

List view of previously scanned foods.

### Design Specifications

- **Screen**: Scan History
- **Navigation**: From Scanner Home
- **Primary Actions**: View food details, filter history
- **Content Priority**: Chronological history, quick access to past scans

### Mockup

```
┌─────────────────────────────────────────────┐
│ ←                Scan History                │
├─────────────────────────────────────────────┤
│                                             │
│  Filter: ◉ All  ○ This Week  ○ This Month │
│                                             │
│  Today                                      │
│  ┌───────────────────────────────────────┐  │
│  │ ┌─────┐ Apple, Red Delicious          │  │
│  │ │ 🍎  │ 1 medium apple                │  │
│  │ │     │ Lunch - 12:30 PM              │  │
│  │ └─────┘ [View Details]                │  │
│  └───────────────────────────────────────┘  │
│                                             │
│  ┌───────────────────────────────────────┐  │
│  │ ┌─────┐ Yogurt, Greek, Plain          │  │
│  │ │ 🥛  │ 1 cup                         │  │
│  │ │     │ Breakfast - 8:15 AM           │  │
│  │ └─────┘ [View Details]                │  │
│  └───────────────────────────────────────┘  │
│                                             │
│  Yesterday                                  │
│  ┌───────────────────────────────────────┐  │
│  │ ┌─────┐ Rice, White, Cooked           │  │
│  │ │ 🍚  │ 1 cup                         │  │
│  │ │     │ Dinner - 7:00 PM              │  │
│  │ └─────┘ [View Details]                │  │
│  └───────────────────────────────────────┘  │
│                                             │
│  ┌───────────────────────────────────────┐  │
│  │ ┌─────┐ Chicken Breast, Grilled       │  │
│  │ │ 🍗  │ 3 oz                          │  │
│  │ │     │ Dinner - 7:00 PM              │  │
│  │ └─────┘ [View Details]                │  │
│  └───────────────────────────────────────┘  │
│                                             │
│  ┌───────────────────────────────────────┐  │
│  │ [Scan New Food]                       │  │
│  └───────────────────────────────────────┘  │
└─────────────────────────────────────────────┘
```

### Key Components

1. **Filter Controls**
   - Options to filter by time period
   - Default to show all scans

2. **Date Grouping**
   - Clear date headers
   - Chronological organization (newest first)

3. **Scan Entry Cards**
   - Food image/icon
   - Food name and portion
   - Meal context (type and time)
   - Link to detailed view

4. **Scan New Food**
   - Quick access to scanner
   - Consistent placement

## Design Notes

1. **Camera Experience**
   - Optimized viewfinder for food photography
   - Real-time feedback on image quality
   - Clear visual guides for optimal positioning
   - Flash control for low-light environments

2. **Recognition Feedback**
   - Transparent confidence levels
   - Multiple alternatives when recognition is uncertain
   - Easy fallback to manual search
   - Learning from user corrections

3. **Nutritional Visualization**
   - Color coding for nutrient levels (high/medium/low)
   - Context-aware highlighting of important nutrients
   - Age-appropriate nutritional focus
   - Clear daily value references

4. **Accessibility Considerations**
   - Alternative text for food images
   - Manual entry options for all scanning features
   - High contrast UI elements
   - Voice guidance for camera positioning

5. **Offline Capabilities**
   - Local database of common foods
   - Queue for processing when connectivity returns
   - Cached nutritional data for previously scanned items
   - Sync when connection is restored 