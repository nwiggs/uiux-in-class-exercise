
# In-Class Exercise: Agent-Assisted CSS for UI/UX Best Practices (Flask)

## Course Context
Master of Science in Health Informatics (MSHI)

This in-class exercise demonstrates how to use **GitHub Copilot Agent Mode** to iteratively design and refine **CSS** that adheres to core **UI/UX best practices** within a simple Flask web application.

Students will progressively prompt the agent to apply four UI/UX principles:
1. User-centered design
2. Consistency
3. Visual hierarchy
4. Communication of interactivity

---

## Learning Objectives
By the end of this exercise, students will be able to:
- Write effective prompts that guide an agent to produce high-quality CSS
- Evaluate UI/UX decisions against explicit design principles
- Critically review and refine agent-generated output

---

## Deliverables
By the end of class, students should have:
- A working Flask app with 3–4 routes and templates
- A shared base layout with consistent navigation, header, and footer
- A single CSS file (`static/styles.css`) implementing all four UI/UX principles

---

## Step 1: Test the Application (Student)

### Student Setup
1. Run the application
```bash
python app.py
```
2. Open the application in a browser
3. Navigate through the pages
4. Test the forms
5. Make mental notes of UI/UX challenges in the existing application


---

## Step 2: User-Centered Design (Readability, Contrast, Accessibility)

### UI/UX Principle
Design for readability, accessibility, and comfort for diverse users.

### Prompt to Copilot Agent
```
Update `static/styles.css` (and minimal HTML if needed) to improve user-centered design:

- Readability: system font stack, base font size, line height, readable max width
- High contrast: text and background colors with strong contrast
- Accessibility:
  - Visible `:focus-visible` styles for keyboard navigation
  - Clear spacing and labels for form fields
  - Add a skip-to-content link (include required HTML and CSS)
  - Do not rely on color alone to convey meaning

Provide the updated CSS and any required template changes.
```

### Student Verification
- Text is easy to read and not cramped
- Strong contrast between text and background
- Tabbing shows visible focus indicators
- Skip-to-content link appears when focused

---

## Step 3: Consistency (Shared Navigation, Header, Footer)

### UI/UX Principle
Users should not have to relearn the interface on each page.

### Prompt to Copilot Agent
```
Implement consistency across all pages:

- Ensure every page uses the same base layout with identical header, nav, and footer
- Style the navigation bar as a reusable component
- Highlight the active page in the navigation
- Ensure buttons, spacing, and typography are consistent across views

Provide necessary Jinja and CSS updates.
```

### Student Verification
- Header, navigation, and footer are identical on all pages
- Active page is clearly highlighted in the nav
- Buttons and typography look consistent everywhere

---

## Step 4: Visual Hierarchy (Emphasize What Matters)

### UI/UX Principle
Guide user attention to the most important content and actions.

### Prompt to Copilot Agent
```
Improve visual hierarchy using CSS (and minimal HTML changes if needed):

- Create a clear page header with title and subtitle
- Make the primary action (e.g., submit button) visually prominent
- Use spacing, grouping, and subtle backgrounds or borders to separate sections
- Style secondary information so it is present but visually quieter

Apply these changes to the home page and survey page.
```

### Student Verification
- Primary action is immediately obvious
- Form fields are grouped logically
- Page content is easy to scan

---

## Step 5: Communication (Hover States and Interactivity)

### UI/UX Principle
The interface should clearly communicate what is interactive and what will happen.

### Prompt to Copilot Agent
```
Enhance communication of interactivity:

- Add hover, focus-visible, and active styles for links and buttons
- Use `cursor: pointer` for clickable elements
- Style disabled buttons clearly and appropriately
- Add subtle transitions (respect `prefers-reduced-motion`)
- Improve required/invalid field styling without relying on color alone

Provide updated CSS and any minimal HTML changes.
```

### Student Verification
- Hovering links and buttons produces clear visual feedback
- Cursor changes appropriately for interactive elements
- Disabled states are obvious
- Reduced-motion preferences are respected

---

## Optional Extensions (If Time Allows)
- Add dark mode using `prefers-color-scheme`
- Improve responsive layout with a breakpoint
- Create a reusable button class system
- Add inline validation or error summaries

---

## Key Takeaway
GitHub Copilot Agent is most effective when guided by **explicit design principles**. High-quality UI/UX outcomes depend not just on generated code, but on the human ability to evaluate, refine, and align outputs with user needs.
