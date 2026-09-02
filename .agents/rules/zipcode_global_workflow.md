
# ZipCode Global - Project Rules & Workflow Learnings

## 1. 🚨 STRICT CONSTRAINT: Never Remove Old Data
- **Rule:** When updating HTML, JSON, or Python scripts, **NEVER** remove existing content, data, or styling unless explicitly ordered by the user. Append or modify instead.

## 2. 🌍 Multi-File Architecture & Patching
- **Structure:** The project contains 130+ static country HTML pages in the `pages/` directory.
- **Workflow:** Never manually edit single country pages (like `pages/india.html`) for global UI features. Always write a Python patching script (e.g., `patch_ui.py`) to parse, regex-replace, and update all `*.html` files simultaneously.
- **Gotcha:** When patching HTML files in Python, include a `utf-16` fallback in the `try-except UnicodeDecodeError` block, as some older HTML files in this project are UTF-16 encoded.

## 3. 🚀 Lighthouse & SEO Optimization (Agentic Browsing 2/2)
- **Web Fonts (CLS Fix):** Do NOT use `display=swap` or `media="print"` tricks for Google Fonts, as they cause massive Cumulative Layout Shifts (CLS > 0.1) on the main `<h1>` due to the Space Grotesk font. Always use `display=optional` to score 100/100 and guarantee Agentic Browsing 2/2 on Desktop.
- **Animations:** Never animate `border-color`, `margin`, or `box-shadow` (causes non-composited animation warnings). Always use `opacity` or `transform` for animations (like `.pulse-btn` and `.hero-badge`).
- **FlagCDN:** FlagCDN does not support `w100`. Use `w80` for valid flags.

## 4. 📱 Mobile UI / UX Standards
- **Navbar Links:** Always use a 3-line collapsible hamburger menu (`☰`) for mobile view (`max-width: 768px`). Do NOT use `flex-wrap: wrap` for nav links, as it causes severe overlapping with headers and the Google Translate widget.
- **Search Auto-Scroll:** Never trigger `element.scrollIntoView()` on `keyup` or `input` events while the user is typing in the search bar. Auto-scroll should ONLY trigger on explicit manual actions (clicking the Search button or pressing Enter).

## 5. 📮 India Post Domain Knowledge
- **Administrative Hierarchy:** In the Indian Postal System, a "Postal Region" (e.g., Visakhapatnam Region) contains multiple independent "Postal Divisions" (e.g., Kakinada Division). 
- **User Clarification:** If a user is confused why "Visakhapatnam" shows up next to "Kakinada", clarify that it is an administrative Regional Head Office mapping, NOT a geographic village location. The JSON data is 100% correct.
