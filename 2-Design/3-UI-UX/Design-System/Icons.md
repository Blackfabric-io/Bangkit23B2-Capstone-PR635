# NutriGenius Icon System

## Icon Style

NutriGenius uses a cohesive icon system to enhance usability and visual appeal of the application.

### Style Guidelines

- **Style**: Outlined with rounded corners
- **Weight**: 2px stroke weight
- **Corner Radius**: 2px
- **Grid**: Based on 24x24px grid
- **Padding**: Minimum 2px padding from edge
- **Colors**: Inherit from parent text color by default

### Icon Sizes

| Size Name | Dimensions | Usage |
|-----------|------------|-------|
| Small | 16 × 16px | Inline text, dense UIs, indicators |
| Standard | 24 × 24px | Navigation, buttons, most UI elements |
| Large | 36 × 36px | Feature highlights, empty states |
| Extra Large | 48 × 48px | Onboarding, splash screens, illustrations |

## Core Icon Set

### Navigation Icons

| Icon Name | Description | Usage |
|-----------|-------------|-------|
| home | House symbol | Home/dashboard navigation |
| growth | Upward arrow with height marks | Growth tracking section |
| food_scanner | Camera with plate outline | Food scanning feature |
| education | Book or graduation cap | Educational content |
| consultation | Chat bubble with heart | Expert consultation |
| profile | Person silhouette | User profile |
| settings | Gear symbol | Application settings |

### Action Icons

| Icon Name | Description | Usage |
|-----------|-------------|-------|
| add | Plus symbol | Add new items |
| remove | Minus symbol | Remove items |
| edit | Pencil | Edit content |
| delete | Trash can | Delete items |
| share | Arrow leaving box | Share content |
| favorite | Heart | Save favorites |
| search | Magnifying glass | Search functionality |
| filter | Funnel | Filter content |
| sort | Stacked lines with arrows | Sort content |
| camera | Camera | Take photo |
| gallery | Image frame | Select from gallery |

### Nutritional Icons

| Icon Name | Description | Usage |
|-----------|-------------|-------|
| protein | Meat/fish symbol | Protein content |
| carbs | Grain/rice symbol | Carbohydrate content |
| fat | Oil drop | Fat content |
| vitamins | Pill/capsule | Vitamin content |
| minerals | Mineral crystal | Mineral content |
| water | Water drop | Hydration |
| calories | Flame | Calorie content |
| meal | Plate with utensils | Meal logging |
| portion | Measuring cup | Portion size |
| allergen | Warning symbol | Allergen indication |

### Status Icons

| Icon Name | Description | Usage |
|-----------|-------------|-------|
| success | Checkmark | Successful action |
| error | Exclamation mark | Error states |
| warning | Triangle with ! | Warning states |
| info | Letter i in circle | Informational states |
| locked | Padlock | Restricted content |
| verified | Shield or badge | Verified content |
| loading | Circular arrows | Loading states |
| complete | Checkmark in circle | Completed items |
| incomplete | Empty circle | Incomplete items |

### Growth Tracking Icons

| Icon Name | Description | Usage |
|-----------|-------------|-------|
| height | Vertical ruler | Height measurement |
| weight | Scale | Weight measurement |
| head | Head with measuring tape | Head circumference |
| bmi | Person silhouette with chart | BMI calculation |
| growth_chart | Line chart with growth curve | Growth charting |
| milestone | Flag on path | Development milestone |
| calendar | Calendar | Date selection, scheduling |

## Icon Implementation

### Technical Specifications

- **Format**: SVG for web/app, PNG fallbacks
- **Optimization**: Optimized SVGs (compressed, clean paths)
- **Naming Convention**: lowercase_with_underscores
- **File Structure**: /assets/icons/{category}/{icon_name}.svg

### Usage Guidelines

1. **Consistency**: Use icons consistently across the application
2. **Clarity**: Icons should clearly communicate their meaning
3. **Accessibility**: Always include text labels with icons except for very common actions
4. **Touch Targets**: Ensure minimum 48 × 48px touch target for interactive icons
5. **Color Usage**: Use primary color for interactive icons, neutral colors for static icons

### Interactive States

| State | Visual Change |
|-------|---------------|
| Default | Regular opacity (100%) |
| Hover | Subtle background tint or glow |
| Active/Pressed | Darker color, slight scale down (95%) |
| Disabled | Reduced opacity (50%) |
| Selected | Filled version or primary color |

## Custom Icon Cases

### Food Category Icons

- **Fruits**: Apple shape
- **Vegetables**: Broccoli shape
- **Grains**: Wheat/rice shape
- **Proteins**: Meat/fish/egg shape
- **Dairy**: Milk bottle/cheese shape
- **Fats**: Oil drop
- **Sweets**: Candy/dessert shape

### Achievement Badges

- **First Measurement**: Ruler with star
- **Complete Profile**: Completed checklist
- **Consistent Tracker**: Calendar with streak
- **Nutrition Expert**: Book with star
- **Healthy Choice**: Apple with checkmark

## Accessibility Considerations

- **Alternative Text**: All icons have associated alt text
- **Color Independence**: Icons convey meaning without relying solely on color
- **Screen Reader Support**: Icons that are not purely decorative have appropriate ARIA labels
- **High Contrast Support**: Icons maintain visibility in high contrast mode

## Icon Customization

### Dynamic Icons

Some icons have dynamic states that change based on:

- **Progress**: Circular fill to show completion percentage
- **Status**: Color changes to reflect different states
- **Time**: Different icons based on time of day (meal tracking)
- **Value**: Different icons based on value ranges (weight status)

### Animated Icons

Icons with simple animations to improve engagement:

- **Loading**: Rotating circular arrows
- **Success**: Checkmark drawing animation
- **Notification**: Subtle pulse or bounce
- **Camera**: Flash effect when capturing
- **Achievement**: Sparkle effect for unlocked badges 