# Education Mockups

This document presents the mockups for the NutriGenius education feature, which provides parents with personalized nutritional education content to help prevent stunting and support healthy child development.

## Education Home Screen

The main screen for accessing educational content, featuring personalized recommendations and content categories.

### Design Specifications

- **Screen**: Education Home
- **Navigation**: Accessed from bottom navigation or dashboard
- **Primary Actions**: Browse content, search, access learning paths
- **Content Priority**: Personalized recommendations, easy content discovery

### Mockup

```
┌─────────────────────────────────────────────┐
│ ≡             Nutrition Education       👤   │
├─────────────────────────────────────────────┤
│ ┌─────────────────────────────────────────┐ │
│ │ 🔍 Search articles and topics...        │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ Recommended for You                     │ │
│ │                                         │ │
│ │ ┌─────────────────────────────────────┐ │ │
│ │ │                                     │ │ │
│ │ │ [Article Image]                     │ │ │
│ │ │                                     │ │ │
│ │ │ Nutrient-Rich Foods for Toddlers    │ │ │
│ │ │ 5 min read                          │ │ │
│ │ └─────────────────────────────────────┘ │ │
│ │                                         │ │
│ │ ◀ [1] [2] [3] [4] [5] ▶                │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ Learning Paths                          │ │
│ │                                         │ │
│ │ ┌───────────┐ ┌───────────┐ ┌──────────┐│ │
│ │ │ Stunting  │ │ First     │ │ Picky    ││ │
│ │ │ Prevention│ │ 1000 Days │ │ Eaters   ││ │
│ │ │ 30% done  │ │           │ │          ││ │
│ │ └───────────┘ └───────────┘ └──────────┘│ │
│ │                                         │ │
│ │ [View All Paths]                        │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ Browse by Category                      │ │
│ │                                         │ │
│ │ ┌───────────┐ ┌───────────┐ ┌──────────┐│ │
│ │ │ Age-Based │ │ Nutrients │ │ Recipes  ││ │
│ │ │ Nutrition │ │           │ │          ││ │
│ │ └───────────┘ └───────────┘ └──────────┘│ │
│ │                                         │ │
│ │ ┌───────────┐ ┌───────────┐ ┌──────────┐│ │
│ │ │ Growth &  │ │ Feeding   │ │ More     ││ │
│ │ │ Developmnt│ │ Challenges│ │ Topics   ││ │
│ │ └───────────┘ └───────────┘ └──────────┘│ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ Recently Viewed                         │ │
│ │                                         │ │
│ │ • Protein Sources for Vegetarian Kids   │ │
│ │ • Understanding Growth Charts           │ │
│ │ • Iron-Rich Foods for Toddlers          │ │
│ │                                         │ │
│ │ [View History]                          │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ 🏠    📏    📷    📚    👨‍⚕️  │
└─────────────────────────────────────────────┘
```

### Key Components

1. **Search Bar**
   - Prominent placement for quick content discovery
   - Placeholder text suggesting search topics
   - Uses standard Text Input component with search icon

2. **Recommended Content**
   - Personalized article recommendations
   - Based on child's age, growth status, and user interests
   - Carousel format with pagination
   - Uses **Article Card** component (Vertical layout variation)
   - Preview image and reading time

3. **Learning Paths**
   - Structured educational journeys
   - Progress indicators for started paths
   - Horizontal scrollable format
   - Uses **Learning Path Card** component with progress indicator
   - Focus on key topics like stunting prevention

4. **Category Browsing**
   - Grid of content categories
   - Visual icons for quick recognition
   - Uses **Category Card** component (Standard variation)
   - Comprehensive coverage of nutrition topics

5. **Recently Viewed**
   - Quick access to recently read articles
   - Encourages continuation of learning
   - Link to full history
   - Uses List Card component with Text Button

## Category Listing Screen

Screen showing articles within a selected category.

### Design Specifications

- **Screen**: Category Listing
- **Navigation**: From Education Home categories
- **Primary Actions**: Filter articles, select article to read
- **Content Priority**: Relevant content organization, filtering options

### Mockup

```
┌─────────────────────────────────────────────┐
│ ←           Age-Based Nutrition             │
├─────────────────────────────────────────────┤
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ 🔍 Search in this category...           │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ Filter: ◉ Relevant to Amir (2y)  ○ All Ages│
│                                             │
│ Sort by: ● Recommended  ○ Newest  ○ Popular│
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ ┌─────┐ Nutrition Needs: Ages 2-3       │ │
│ │ │     │                                 │ │
│ │ │ 🍎  │ Key nutrients and portion sizes │ │
│ │ │     │ for toddlers entering the       │ │
│ │ └─────┘ preschool years.                │ │
│ │                                         │ │
│ │ 6 min read  •  Recommended for you      │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ ┌─────┐ Transitioning from Milk to      │ │
│ │ │     │ Solid Foods                     │ │
│ │ │ 🥣  │                                 │ │
│ │ │     │ When and how to introduce new   │ │
│ │ └─────┘ textures and food groups.       │ │
│ │                                         │ │
│ │ 8 min read  •  Popular                  │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ ┌─────┐ Meal Planning for Toddlers      │ │
│ │ │     │                                 │ │
│ │ │ 📋  │ Creating balanced meals that    │ │
│ │ │     │ meet nutritional needs while    │ │
│ │ └─────┘ managing picky eating.          │ │
│ │                                         │ │
│ │ 7 min read                              │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ ┌─────┐ Snack Ideas for Preschoolers    │ │
│ │ │     │                                 │ │
│ │ │ 🥪  │ Healthy, easy-to-prepare snacks │ │
│ │ │     │ that support growth and         │ │
│ │ └─────┘ development.                    │ │
│ │                                         │ │
│ │ 5 min read                              │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ [Load More Articles]                        │
└─────────────────────────────────────────────┘
```

### Key Components

1. **Category Header**
   - Clear category title
   - Back navigation
   - Uses Top App Bar component

2. **Search and Filter**
   - Category-specific search using Text Input component
   - Age-relevance filter using Radio Button component
   - Sorting options using Radio Button component

3. **Article Cards**
   - Uses **Article Card** component (Horizontal layout variation)
   - Topic icon or thumbnail
   - Clear title
   - Brief description
   - Reading time
   - Special tags (recommended, popular, etc.)

4. **Load More**
   - Text Button component for pagination
   - Pagination control for longer category lists
   - Infinite scroll alternative

## Article Detail Screen

Screen for reading an educational article.

### Design Specifications

- **Screen**: Article Detail
- **Navigation**: From category listing or recommendations
- **Primary Actions**: Read content, bookmark, share, take action
- **Content Priority**: Clear, readable content, related actions

### Mockup

```
┌─────────────────────────────────────────────┐
│ ←                                 🔖   ⋮    │
├─────────────────────────────────────────────┤
│                                             │
│ Nutrition Needs: Ages 2-3                   │
│                                             │
│ By Dr. Sarah Johnson • May 10, 2023         │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │                                         │ │
│ │             [Article Image]             │ │
│ │                                         │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ The toddler years (ages 2-3) are a critical │
│ period for nutritional development. During  │
│ this time, children are growing rapidly and │
│ developing eating habits that may last a    │
│ lifetime.                                   │
│                                             │
│ ## Key Nutrients for Toddlers               │
│                                             │
│ **Protein:** Essential for growth and       │
│ muscle development. Aim for 2-3 servings    │
│ daily from sources like:                    │
│                                             │
│ • Lean meats and poultry                    │
│ • Fish                                      │
│ • Eggs                                      │
│ • Dairy products                            │
│ • Legumes and tofu                          │
│                                             │
│ **Calcium:** Critical for bone development. │
│ Toddlers need 700mg daily from:             │
│                                             │
│ • Milk (whole milk until age 2)             │
│ • Yogurt                                    │
│ • Cheese                                    │
│ • Fortified non-dairy alternatives          │
│                                             │
│ [Continue reading...]                       │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ Take Action                             │ │
│ │                                         │ │
│ │ [Create Meal Plan]  [Track Nutrients]   │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ Related Articles                        │ │
│ │                                         │ │
│ │ • Meal Planning for Toddlers            │ │
│ │ • Iron-Rich Foods for Toddlers          │ │
│ │ • Managing Picky Eating                 │ │
│ └─────────────────────────────────────────┘ │
└─────────────────────────────────────────────┘
```

### Key Components

1. **Article Header**
   - Clear title using H4 typography
   - Author and publication date using Caption typography
   - Featured image
   - Bookmark (Icon Button) and share options (Icon Button)

2. **Article Content**
   - Clean, readable typography using Body 1 and Body 2 typography
   - Well-structured with headings using H5 typography
   - Bullet points for easy scanning
   - Appropriate paragraph length

3. **Action Section**
   - Standard Card component
   - Contextual actions using Secondary Button components
   - Direct links to relevant app features

4. **Related Content**
   - Standard Card component
   - List of **Article Card** components (Compact layout variation)
   - Topically related to current article

## Learning Path Screen

Overview screen for a structured learning path.

### Design Specifications

- **Screen**: Learning Path
- **Navigation**: From Education Home learning paths
- **Primary Actions**: Continue learning, view progress, start new modules
- **Content Priority**: Clear learning structure, progress tracking

### Mockup

```
┌─────────────────────────────────────────────┐
│ ←           Stunting Prevention             │
├─────────────────────────────────────────────┤
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │                                         │ │
│ │             [Path Banner]               │ │
│ │                                         │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ Understanding and preventing stunting in    │
│ early childhood through proper nutrition    │
│ and monitoring.                             │
│                                             │
│ Your Progress: 30% Complete                 │
│ ┌─────────────────────────────────────────┐ │
│ │ [███████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░]  │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ Module 1: Understanding Stunting        │ │
│ │ ✓ What is Stunting?                     │ │
│ │ ✓ Causes and Risk Factors               │ │
│ │ ✓ Long-term Impact on Development       │ │
│ │                                         │ │
│ │ [Completed]                             │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ Module 2: Nutrition Fundamentals        │ │
│ │ ✓ Essential Nutrients for Growth        │ │
│ │ ► Key Foods to Prevent Stunting         │ │
│ │ ○ Creating Balanced Meals               │ │
│ │                                         │ │
│ │ [Continue Learning]                     │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ Module 3: Growth Monitoring             │ │
│ │ ○ Understanding Growth Charts           │ │
│ │ ○ Regular Measurement Techniques        │ │
│ │ ○ When to Consult a Healthcare Provider │ │
│ │                                         │ │
│ │ [Locked - Complete Module 2 First]      │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ Module 4: Practical Implementation      │ │
│ │ ○ Meal Planning Strategies              │ │
│ │ ○ Addressing Feeding Challenges         │ │
│ │ ○ Community Resources                   │ │
│ │                                         │ │
│ │ [Locked - Complete Module 3 First]      │ │
│ └─────────────────────────────────────────┘ │
└─────────────────────────────────────────────┘
```

### Key Components

1. **Path Overview**
   - Clear title using Top App Bar component
   - Visual banner representing the topic
   - Description using Body 1 typography
   - Progress indicator using Linear Progress component

2. **Module Structure**
   - Each module uses Standard Card component
   - Sequential modules with clear topics using H5 typography
   - Article list within each module using Body 2 typography
   - Status indicators (completed, in progress, locked)
   - Clear navigation using Primary Button or Secondary Button components

3. **Progress Visualization**
   - Overall progress bar using Linear Progress component
   - Checkmarks for completed articles
   - Current position indicator (arrow symbol)
   - Lock indicators for content that requires prerequisites

4. **Module Actions**
   - Contextual buttons based on module status
   - Uses Primary Button for active modules
   - Uses Secondary Button (disabled state) for locked modules
   - Clear indication of next steps

## Article Search Results

Screen showing search results for educational content.

### Design Specifications

- **Screen**: Search Results
- **Navigation**: From search bar in Education Home
- **Primary Actions**: Refine search, select article
- **Content Priority**: Relevant results, filtering options

### Mockup

```
┌─────────────────────────────────────────────┐
│ ←                                           │
├─────────────────────────────────────────────┤
│ ┌─────────────────────────────────────────┐ │
│ │ 🔍 iron-rich foods          ✕           │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ 12 results found                            │
│                                             │
│ Filter: ◉ All  ○ Articles  ○ Recipes       │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ ┌─────┐ Iron-Rich Foods for Toddlers    │ │
│ │ │     │                                 │ │
│ │ │ 🍗  │ Essential iron sources to       │ │
│ │ │     │ support healthy growth and      │ │
│ │ └─────┘ brain development.              │ │
│ │                                         │ │
│ │ 7 min read  •  Relevant to Amir (2y)    │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ ┌─────┐ Preventing Iron Deficiency      │ │
│ │ │     │                                 │ │
│ │ │ 📊  │ Signs, symptoms, and strategies │ │
│ │ │     │ to ensure adequate iron intake  │ │
│ │ └─────┘ in young children.              │ │
│ │                                         │ │
│ │ 9 min read  •  Relevant to Amir (2y)    │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ ┌─────┐ 5 Iron-Boosting Recipes for     │ │
│ │ │     │ Picky Eaters                    │ │
│ │ │ 🍲  │                                 │ │
│ │ │     │ Kid-friendly meal ideas that    │ │
│ │ └─────┘ pack an iron punch.             │ │
│ │                                         │ │
│ │ Recipe  •  15 min preparation           │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ ┌─────┐ Understanding Iron Absorption   │ │
│ │ │     │                                 │ │
│ │ │ 🔬  │ How vitamin C helps iron        │ │
│ │ │     │ absorption and other factors    │ │
│ │ └─────┘ that affect nutrient uptake.    │ │
│ │                                         │ │
│ │ 6 min read                              │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ [Load More Results]                         │
└─────────────────────────────────────────────┘
```

### Key Components

1. **Search Query Display**
   - Text Input component with search icon
   - Clear display of current search term
   - Option to clear search (✕ icon)
   - Result count using Caption typography

2. **Filter Options**
   - Radio Button component for content type filters
   - Applied filters clearly indicated
   - Uses Body 2 typography for labels

3. **Result Cards**
   - Uses **Article Card** component (Horizontal layout variation)
   - Highlighted search terms
   - Relevance indicators
   - Content type indicators
   - Reading time or preparation time

4. **Load More**
   - Text Button component
   - Pagination control for longer result lists
   - Infinite scroll alternative

## Bookmarks Screen

Collection of saved educational content.

### Design Specifications

- **Screen**: Bookmarks
- **Navigation**: From Education Home or menu
- **Primary Actions**: Access saved content, organize bookmarks
- **Content Priority**: Easy access to saved articles, organization

### Mockup

```
┌─────────────────────────────────────────────┐
│ ←               My Bookmarks                │
├─────────────────────────────────────────────┤
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ 🔍 Search bookmarks...                  │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ Collections                                 │
│ ┌─────────────────────────────────────────┐ │
│ │ ◉ All Bookmarks (12)                    │ │
│ │ ○ Favorites (5)                         │ │
│ │ ○ To Read Later (4)                     │ │
│ │ ○ Meal Planning (3)                     │ │
│ │                                         │ │
│ │ [+ Create New Collection]               │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ Sort by: ● Recently Saved  ○ Title  ○ Date │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ ┌─────┐ Protein Sources for Vegetarian  │ │
│ │ │     │ Kids                            │ │
│ │ │ 🥗  │                                 │ │
│ │ │     │ Saved 2 days ago                │ │
│ │ └─────┘ In: Favorites, Meal Planning    │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ ┌─────┐ Understanding Growth Charts     │ │
│ │ │     │                                 │ │
│ │ │ 📈  │ Saved 1 week ago                │ │
│ │ │     │ In: To Read Later               │ │
│ │ └─────┘                                 │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ ┌─────┐ Iron-Rich Foods for Toddlers    │ │
│ │ │     │                                 │ │
│ │ │ 🍗  │ Saved 2 weeks ago               │ │
│ │ │     │ In: Favorites, Meal Planning    │ │
│ │ └─────┘                                 │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ ┌─────┐ Meal Planning for Toddlers      │ │
│ │ │     │                                 │ │
│ │ │ 📋  │ Saved 3 weeks ago               │ │
│ │ │     │ In: Meal Planning               │ │
│ │ └─────┘                                 │ │
│ └─────────────────────────────────────────┘ │
└─────────────────────────────────────────────┘
```

### Key Components

1. **Bookmark Search**
   - Text Input component with search icon
   - Search within saved content
   - Quick filtering of personal library

2. **Collections**
   - Standard Card component
   - Radio Button components for collection selection
   - User-created collections
   - Article count per collection
   - Text Button component for creating new collections

3. **Sorting Options**
   - Radio Button components for sort options
   - Multiple ways to organize bookmarks
   - Default to recently saved

4. **Bookmark Cards**
   - Uses **Article Card** component (Horizontal layout variation)
   - Save date for context using Caption typography
   - Collection tags using Caption typography
   - Quick access to saved content

## Design Notes

1. **Content Personalization**
   - Age-appropriate content filtering based on child's age
   - Growth-status-aware recommendations
   - Learning history influences suggestions
   - Dietary preferences/restrictions considered

2. **Educational Progression**
   - Structured learning paths with prerequisites
   - Gradual introduction of complex topics
   - Clear progress tracking using **Learning Path Card** components
   - Achievement recognition

3. **Content Accessibility**
   - Readable typography with adequate contrast
   - Clear content hierarchy with headings
   - Bullet points and lists for scannable content
   - Offline reading capabilities

4. **Visual Learning Support**
   - Consistent use of icons for topic recognition
   - Informative images and diagrams
   - Visual progress indicators using Linear Progress components
   - Color coding for content categories

5. **Integration with App Features**
   - Contextual links to relevant app features
   - Direct application of knowledge (meal planning, growth tracking)
   - Educational content referenced in other app sections
   - Bookmarking and history synced across app 