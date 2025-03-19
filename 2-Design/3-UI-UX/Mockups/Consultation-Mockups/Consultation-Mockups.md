# Expert Consultation Mockups

This document presents the mockups for the NutriGenius expert consultation feature, which allows parents to connect with nutrition experts for personalized guidance and advice regarding their child's nutrition and growth.

## Consultation Home Screen

The main entry point for the consultation feature, providing access to find experts, view upcoming consultations, and consultation history.

### Design Specifications

- **Screen**: Consultation Home
- **Navigation**: Accessed from bottom navigation or dashboard
- **Primary Actions**: Find expert, view upcoming consultations, view history
- **Content Priority**: Quick access to booking, upcoming appointments

### Key Components

1. **Header Section**
   - Title "Expert Consultation"
   - Subtitle explaining the feature's purpose: "Connect with nutrition experts for personalized guidance"
   - Illustration of a healthcare professional and parent/child

2. **Find Expert Section**
   - Prominent "Find an Expert" button with consultation icon
   - Brief explanation of the consultation process
   - Quick filters for common specializations (stunting, allergies, picky eating)

3. **Upcoming Consultations Card**
   - List of scheduled consultations with:
     - Expert photo and name
     - Date and time
     - Consultation type (video, audio, chat)
     - Countdown timer for imminent consultations
   - "Join Now" button for consultations within 15 minutes of start time
   - "Prepare" button for upcoming consultations
   - Empty state with suggestion to book first consultation

4. **Recent Consultations Section**
   - Preview of most recent consultation
   - Expert name and photo
   - Date of consultation
   - Brief summary of topics discussed
   - "View All History" button

5. **Expert Spotlight**
   - Featured expert with photo
   - Brief credentials and specialization
   - Availability indicator
   - "View Profile" button

6. **Educational Content**
   - "Why Consult an Expert?" expandable section
   - Benefits of professional nutrition guidance
   - Common scenarios when consultation is recommended

## Expert Directory Screen

A searchable, filterable list of available nutrition experts.

### Design Specifications

- **Screen**: Expert Directory
- **Navigation**: Accessed from Consultation Home
- **Primary Actions**: Search experts, apply filters, view profiles
- **Content Priority**: Expert discovery, credentials, availability

### Key Components

1. **Search and Filter Bar**
   - Search field with placeholder "Search by name or specialty"
   - Filter button with active filter indicator
   - Sort options (Recommended, Availability, Rating)

2. **Active Filters Display**
   - Horizontal scrollable list of active filter chips
   - Each chip shows filter type and value
   - "Clear All" option when filters are active

3. **Expert List**
   - Cards for each expert containing:
     - Professional photo
     - Name and credentials (MD, RD, etc.)
     - Primary specialization
     - Years of experience
     - Languages spoken (icons)
     - Star rating (average from reviews)
     - Availability indicator ("Available today" badge)
     - Brief introduction (2-3 lines)
   - Vertical scrolling list
   - "Load More" button or infinite scroll

4. **Filter Panel (Expandable)**
   - Specialization checkboxes:
     - Pediatric Nutrition
     - Stunting Prevention
     - Food Allergies & Intolerances
     - Picky Eating
     - Infant Feeding
     - Malnutrition
     - Special Dietary Needs
   - Availability date picker
   - Language selection
   - Experience level range
   - Rating threshold
   - Consultation type preference
   - Price range slider
   - "Apply Filters" and "Reset" buttons

5. **No Results State**
   - Friendly message when no experts match filters
   - Suggestions to broaden search
   - Option to join waitlist for specific needs

## Expert Profile Screen

Detailed information about a specific expert, their qualifications, and booking options.

### Design Specifications

- **Screen**: Expert Profile
- **Navigation**: Accessed from Expert Directory
- **Primary Actions**: Check availability, read reviews, view credentials
- **Content Priority**: Expert qualifications, booking process initiation

### Key Components

1. **Expert Header**
   - Large professional photo
   - Name and credentials
   - Primary specialization
   - Overall rating with star visualization
   - Number of consultations conducted
   - Verification badge

2. **Quick Action Buttons**
   - Prominent "Check Availability" primary button
   - "Save to Favorites" icon button
   - "Share Profile" icon button

3. **About Section**
   - Professional bio paragraph
   - Areas of expertise (tags)
   - Languages spoken
   - Years of experience
   - Video introduction (optional)

4. **Credentials Section**
   - Education history
   - Certifications
   - Professional associations
   - "View Credentials" expandable section

5. **Consultation Options**
   - Types offered (Video, Audio, Chat, In-person)
   - Duration options
   - Price for each type
   - Insurance information

6. **Availability Preview**
   - Calendar heatmap showing available days
   - "Next Available" highlight
   - "Check Detailed Availability" button

7. **Reviews Section**
   - Average rating breakdown by category:
     - Knowledge & Expertise
     - Communication
     - Helpfulness
     - Overall Satisfaction
   - Preview of most recent reviews (2-3)
   - "View All Reviews" button
   - Total review count

8. **Similar Experts**
   - Horizontal scrollable list of similar experts
   - Quick switch option if this expert doesn't meet needs

## Booking Screen

Interface for selecting consultation time, type, and providing relevant information.

### Design Specifications

- **Screen**: Booking Process
- **Navigation**: Multi-step process from Expert Profile
- **Primary Actions**: Select time, consultation type, provide details
- **Content Priority**: Clear booking steps, context preservation

### Key Components

1. **Booking Progress Indicator**
   - Step visualization (1. Select Time, 2. Consultation Details, 3. Payment, 4. Confirmation)
   - Current step highlighted
   - Expert name and photo persistent across steps

2. **Calendar View (Step 1)**
   - Month view calendar
   - Available dates highlighted
   - Date selection functionality
   - Time slot grid for selected date
   - Available slots clearly marked
   - Time zone information and selector
   - "Next" button to proceed

3. **Consultation Details (Step 2)**
   - Consultation type selection (Video, Audio, Chat)
   - Duration selection
   - Child selection (if multiple children registered)
   - Reason for consultation field
   - Common concerns checklist:
     - Growth concerns
     - Feeding difficulties
     - Nutritional deficiencies
     - Food allergies/intolerances
     - Picky eating
     - Other (with text field)
   - Option to share growth data
   - Option to share meal logs
   - Additional notes field
   - "Next" and "Back" buttons

4. **Payment Information (Step 3)**
   - Consultation summary (expert, date/time, type)
   - Price breakdown
   - Insurance information entry (if applicable)
   - Payment method selection
   - Terms and conditions checkbox
   - Privacy policy regarding medical information
   - "Confirm Booking" and "Back" buttons

5. **Confirmation Screen (Step 4)**
   - Success message with checkmark animation
   - Consultation details summary
   - Add to calendar button
   - Set reminder options
   - "What to prepare" guidance
   - "Return to Home" button

## Upcoming Consultation Screen

Details and preparation for a scheduled consultation.

### Design Specifications

- **Screen**: Upcoming Consultation
- **Navigation**: Accessed from Consultation Home or notifications
- **Primary Actions**: Prepare for consultation, reschedule, cancel
- **Content Priority**: Preparation steps, consultation details

### Key Components

1. **Consultation Header**
   - Expert photo and name
   - Date and time with countdown
   - Consultation type icon
   - Child name
   - Status indicator (Confirmed `#4CAF50`, Pending `#FFC107`, Cancelled `#F44336`, Rescheduled `#FF9800`)

2. **Action Buttons**
   - "Join Consultation" button (active near start time)
   - "Reschedule" button
   - "Cancel" button
   - Add to calendar button (if not already added)

3. **Preparation Checklist**
   - Interactive checklist of preparation steps:
     - Complete pre-consultation questionnaire
     - Share relevant growth data
     - Share recent meal logs
     - Prepare questions
     - Test device (for video/audio)
   - Progress indicator for preparation completion

4. **Pre-consultation Questionnaire**
   - Form with questions about:
     - Current concerns
     - Child's eating habits
     - Recent changes in appetite or diet
     - Goals for the consultation
   - Save progress functionality
   - Completion status

5. **Data Sharing Controls**
   - Growth data sharing toggle with preview
   - Meal log sharing toggle with preview
   - Privacy explanation
   - Selective sharing options (date ranges)

6. **Technical Requirements**
   - Device compatibility check
   - Internet connection test
   - Camera and microphone test (for video consultations)
   - Troubleshooting tips

7. **Consultation Information**
   - Expert bio reminder
   - Consultation duration
   - What to expect section
   - How to make the most of your consultation tips

## Active Consultation Screen

Interface for the actual consultation session.

### Design Specifications

- **Screen**: Active Consultation
- **Navigation**: Entered from Upcoming Consultation or notification
- **Primary Actions**: Video/audio communication, chat, end consultation
- **Content Priority**: Clear communication, relevant information access

### Key Components

1. **Video/Audio Area**
   - Expert video feed (primary)
   - Self video feed (smaller)
   - Mute/unmute button
   - Camera on/off button
   - Speaker/headphone toggle
   - Connection quality indicator

2. **Consultation Information Bar**
   - Expert name
   - Consultation type
   - Timer showing elapsed/remaining time
   - Child name

3. **Communication Tools**
   - Chat panel (expandable)
   - File/image sharing button
   - Screen sharing option
   - Drawing/annotation tools

4. **Quick Access Information**
   - Growth data tab (if shared)
   - Meal log tab (if shared)
   - Notes tab for consultation notes
   - Questionnaire responses

5. **Action Buttons**
   - End consultation button
   - Report technical issue button
   - Settings button

6. **Post-Consultation Preview**
   - Summary section to be filled during/after consultation
   - Recommendations preview
   - Follow-up indicator

## Consultation Summary Screen

Post-consultation review of discussion, recommendations, and next steps.

### Design Specifications

- **Screen**: Consultation Summary
- **Navigation**: Shown after consultation ends, accessible from history
- **Primary Actions**: View recommendations, book follow-up, provide feedback
- **Content Priority**: Expert advice, actionable recommendations

### Key Components

1. **Consultation Overview**
   - Expert name and photo
   - Date and time
   - Duration
   - Consultation type
   - Child name
   - Topics discussed tags

2. **Summary Section**
   - Written summary of discussion
   - Key points highlighted
   - Voice recording playback (if enabled)
   - Expandable sections by topic

3. **Recommendations List**
   - Actionable items with checkboxes
   - Priority indicators
   - Timeframe for each recommendation
   - Links to relevant app features
   - Save or share options

4. **Resources Provided**
   - Articles shared by expert
   - External resources
   - Downloadable materials
   - App feature recommendations

5. **Follow-up Section**
   - Recommendation for follow-up (if applicable)
   - Suggested timeframe
   - "Book Follow-up" button
   - Quick scheduling options

6. **Feedback Request**
   - Star rating system
   - Category-specific ratings
   - Optional comment field
   - "Submit Feedback" button
   - Thank you message after submission

7. **Action Buttons**
   - Share summary button
   - Download summary (PDF) button
   - Add to health record button

## Consultation History Screen

List of past consultations with access to summaries and recommendations.

### Design Specifications

- **Screen**: Consultation History
- **Navigation**: Accessed from Consultation Home
- **Primary Actions**: View past consultations, track recommendation progress
- **Content Priority**: Chronological history, recommendation follow-through

### Key Components

1. **History Filter Bar**
   - Date range selector
   - Expert filter
   - Child filter (if multiple)
   - Consultation type filter
   - Search by topic

2. **Consultation List**
   - Cards for each past consultation:
     - Expert photo and name
     - Date and time
     - Consultation type icon
     - Child name
     - Primary topic/reason
     - Status indicator using standard status colors (Completed `#2E7D32`, Cancelled `#F44336`)
     - Recommendation completion indicator
   - Chronological order (newest first)
   - Load more functionality

3. **Recommendation Tracking**
   - Overall completion percentage
   - Progress visualization
   - Overdue recommendations highlighted
   - Quick action to mark as complete

4. **No History State**
   - Friendly message for new users
   - Benefits of consultation
   - "Find an Expert" button

5. **Export Options**
   - Export complete history
   - Select consultations to export
   - Format options (PDF, CSV)
   - Share with healthcare provider option

## Design Notes

1. **Accessibility Considerations**
   - High contrast between text and backgrounds
   - Screen reader compatibility for all elements
   - Keyboard navigation support
   - Captions for video consultations
   - Text size adjustability

2. **Responsive Behavior**
   - Consultation interface adapts to different screen sizes
   - Video feed resizing based on device orientation
   - Critical controls always accessible
   - Touch-friendly interface elements

3. **Privacy and Security**
   - Clear indicators of data sharing status
   - Encryption notices for sensitive information
   - Consent confirmations for data sharing
   - Secure connection indicators

4. **Offline Considerations**
   - Graceful handling of connection loss during consultation
   - Cached consultation history for offline viewing
   - Reconnection protocol
   - Offline recommendation tracking

5. **Integration with Other Features**
   - Seamless transitions to/from growth tracking
   - Meal logging suggestions from recommendations
   - Educational content tied to consultation topics
   - Calendar integration for scheduling 