# NutriGenius Typography System

## Font Families

NutriGenius uses a dual-font approach for clear hierarchy and optimal readability across devices.

### Primary Font: Nunito

A rounded, friendly sans-serif that communicates warmth and approachability while maintaining excellent readability.

**Usage**: Headings, buttons, navigation, and emphasis text.

```css
font-family: 'Nunito', sans-serif;
```

### Secondary Font: Open Sans

A neutral, clean sans-serif font that provides excellent readability for body text.

**Usage**: Body text, paragraphs, lists, and form inputs.

```css
font-family: 'Open Sans', sans-serif;
```

## Type Scale

Our typographic scale follows an 8px baseline grid with a 1.25 ratio for harmonious progression.

| Element | Font | Size (px/rem) | Weight | Line Height | Letter Spacing | Use Cases |
|---------|------|---------------|--------|-------------|----------------|-----------|
| Display | Nunito | 48px / 3rem | 700 | 1.1 | -0.5px | Large heroes, landing page headlines |
| H1 | Nunito | 40px / 2.5rem | 700 | 1.1 | -0.5px | Page titles, main sections |
| H2 | Nunito | 32px / 2rem | 700 | 1.2 | -0.25px | Section headings, feature titles |
| H3 | Nunito | 24px / 1.5rem | 600 | 1.3 | 0 | Card titles, sub-sections |
| H4 | Nunito | 20px / 1.25rem | 600 | 1.4 | 0 | List headings, minor sections |
| H5 | Nunito | 18px / 1.125rem | 600 | 1.4 | 0.15px | Form labels, small titles |
| H6 | Nunito | 16px / 1rem | 600 | 1.4 | 0.15px | Small headings, emphasized text |
| Body 1 | Open Sans | 16px / 1rem | 400 | 1.5 | 0.15px | Primary body text |
| Body 2 | Open Sans | 14px / 0.875rem | 400 | 1.5 | 0.25px | Secondary body text, longer form content |
| Subtitle 1 | Nunito | 16px / 1rem | 500 | 1.5 | 0.15px | Supporting headers, emphasized body |
| Subtitle 2 | Nunito | 14px / 0.875rem | 500 | 1.4 | 0.1px | Supporting text, emphasized small text |
| Button | Nunito | 14px / 0.875rem | 600 | 1.75 | 0.4px | Button labels |
| Caption | Open Sans | 12px / 0.75rem | 400 | 1.4 | 0.4px | Helper text, footnotes, legal text |
| Overline | Nunito | 10px / 0.625rem | 600 | 1.4 | 1.5px | Labels, tags, badges (all caps) |

## Font Weights

| Weight Name | Value | Font | Usage |
|-------------|-------|------|-------|
| Regular | 400 | Open Sans | Body text, normal content |
| Medium | 500 | Both | Subtitles, slightly emphasized content |
| Semi-Bold | 600 | Nunito | Buttons, section headings, interactive elements |
| Bold | 700 | Nunito | Headlines, major emphasis, page titles |

## Responsive Typography

Typography scales responsively across different breakpoints:

### Mobile (< 600px)
- Base font size: 16px
- Scale factor: 0.85 (multiply desktop sizes by this factor)

### Tablet (600px - 1024px)
- Base font size: 16px
- Scale factor: 0.9 (multiply desktop sizes by this factor)

### Desktop (> 1024px)
- Base font size: 16px
- Full scale as defined in the type scale table

## Text Colors

| Text Type | Light Mode | Dark Mode |
|-----------|------------|-----------|
| Primary Text | `#212121` | `#FFFFFF` |
| Secondary Text | `#616161` | `#B0BEC5` |
| Disabled Text | `#9E9E9E` | `#757575` |
| Links | `#2E7D32` | `#81C784` |
| Error Text | `#F44336` | `#EF9A9A` |

## Usage Guidelines

1. **Hierarchy**: Maintain clear typographic hierarchy to guide users through the interface
2. **Consistency**: Use type styles consistently across similar elements
3. **Readability**: Ensure sufficient contrast (WCAG AA standard) and adequate line heights
4. **Line Length**: Keep body text line length between 60-75 characters for optimal readability
5. **Alignment**: Left-align text for better readability (RTL languages should be right-aligned)

## Special Cases

### Articles and Educational Content
- Body text size: 18px/1.125rem
- Line height: 1.6
- Line length: 680px max-width container
- Margins: 24px bottom margin between paragraphs

### Data Visualization
- Use the clearer Open Sans for all chart labels and legends
- Minimum size: 12px for all data labels
- Use proper hierarchy for chart titles (H4) and subtitles (Subtitle 2)

### Form Fields
- Labels: Caption style (12px)
- Input text: Body 1 style
- Helper text: Caption style
- Error messages: Caption style in error color 