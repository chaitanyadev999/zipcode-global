# Cinematic Design Elements — PO ZipCode Global

## Color Palette System

### Global (used on homepage)
```css
--bg-primary: #0a0a0f;
--accent-blue: #00d4ff;
--accent-purple: #7c3aed;
--accent-gold: #fbbf24;
```

### India Page (Saffron Theme)
```css
--primary: #ff6b1a;        /* Indian Saffron */
--secondary: #f5b700;       /* Gold */
--accent: #006d77;          /* Peacock Teal */
--bg: #050816;              /* Deep Cinema Black */
```

### USA Page (Stars & Stripes Theme)
```css
--primary: #b22234;         /* American Red */
--secondary: #3c3b6e;       /* American Blue */
--accent: #fbbf24;          /* Gold Stars */
--bg: #060810;              /* Deep Navy Black */
```

### UK Page (Royal Theme)
```css
--primary: #012169;         /* Union Blue */
--secondary: #c8102e;       /* Union Red */
--accent: #ffffff;          /* White */
--bg: #050912;              /* Dark Navy */
```

### Australia Page (Aussie Theme)
```css
--primary: #00843d;         /* Australian Green */
--secondary: #ffcd00;       /* Australian Gold */
--accent: #003087;          /* Deep Blue */
--bg: #060a10;              /* Dark */
```

---

## Typography System

```css
/* Import from Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Space+Grotesk:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap');

/* Usage */
--font-display: 'Space Grotesk', sans-serif;  /* Headings, brand */
--font-body: 'Inter', system-ui, sans-serif;  /* Body text */
--font-mono: 'JetBrains Mono', monospace;     /* PIN/ZIP codes */
```

---

## Glassmorphism Components

### Glass Card:
```css
.glass-card {
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(20px) saturate(180%);
  -webkit-backdrop-filter: blur(20px) saturate(180%);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 16px;
  box-shadow: 0 24px 80px rgba(0, 0, 0, 0.6);
}
```

### Neon Glow Effect:
```css
.neon-glow {
  box-shadow: 
    0 0 20px rgba(0, 212, 255, 0.3),
    0 0 60px rgba(0, 212, 255, 0.15),
    0 0 100px rgba(0, 212, 255, 0.05);
}
```

### Gradient Text:
```css
.gradient-text {
  background: linear-gradient(135deg, #ff6b1a 0%, #f5b700 50%, #00d4ff 100%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}
```

---

## Micro-Animations

### Floating Flag Animation (Hero Section):
```css
@keyframes flag-float {
  0%, 100% { transform: translateY(0px) rotate(0deg); }
  25% { transform: translateY(-8px) rotate(1deg); }
  75% { transform: translateY(-4px) rotate(-1deg); }
}

.hero-flag {
  animation: flag-float 4s ease-in-out infinite;
}
```

### Card Reveal on Load:
```css
@keyframes card-reveal {
  from {
    opacity: 0;
    transform: translateY(20px) scale(0.98);
  }
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

.result-card {
  animation: card-reveal 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}
```

### Stagger Effect (for state buttons):
```javascript
// Add delay to each button via inline style
states.map((s, i) => 
  `<button style="transition-delay:${Math.min(i, 20) * 15}ms">...</button>`
)
```

### Pulse Dot (Live Map Indicator):
```css
@keyframes pulse-dot {
  0%, 100% { transform: scale(1); opacity: 1; box-shadow: 0 0 0 0 rgba(255, 107, 26, 0.5); }
  50% { transform: scale(1.6); opacity: 0.4; box-shadow: 0 0 0 8px rgba(255, 107, 26, 0); }
}

.pulse-dot {
  width: 8px; height: 8px;
  border-radius: 50%;
  animation: pulse-dot 1.5s ease-in-out infinite;
}
```

### Hover Lift Effect:
```css
.state-btn {
  transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
}
.state-btn:hover {
  transform: translateY(-2px);
  border-color: var(--primary);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
}
```

### Scroll Nav Blur Effect:
```javascript
window.addEventListener('scroll', () => {
  nav.classList.toggle('scrolled', window.scrollY > 50);
});
```
```css
.nav.scrolled {
  background: rgba(5, 8, 22, 0.85);
  backdrop-filter: blur(24px) saturate(180%);
  border-bottom: 1px solid rgba(255,255,255,0.1);
}
```

---

## Dark Map Styling (Leaflet)

Make the OpenStreetMap look dark/cinematic:
```css
.leaflet-tile {
  filter: brightness(0.6) invert(1) contrast(1.3) hue-rotate(200deg) saturate(0.2) brightness(0.85);
}
.leaflet-container {
  background: #0a0e27 !important;
}
```

---

## Toast Notification System

```css
.toast {
  padding: 0.875rem 1.25rem;
  background: rgba(5, 8, 22, 0.9);
  backdrop-filter: blur(20px);
  border-radius: 12px;
  transform: translateX(120%);
  transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}
.toast.show { transform: translateX(0); }
.toast.success { border-left: 3px solid #2d6a4f; }
.toast.error { border-left: 3px solid #c1272d; }
```

---

## Country-Specific Background Gradients

Each country page has a unique cinematic background:

```css
/* India */
body::before {
  background:
    radial-gradient(ellipse at 10% 20%, rgba(255, 107, 26, 0.12) 0%, transparent 50%),
    radial-gradient(ellipse at 90% 10%, rgba(245, 183, 0, 0.08) 0%, transparent 50%),
    radial-gradient(ellipse at 50% 90%, rgba(45, 106, 79, 0.10) 0%, transparent 50%);
}

/* USA */
body::before {
  background:
    radial-gradient(ellipse at 10% 20%, rgba(178, 34, 52, 0.12) 0%, transparent 50%),
    radial-gradient(ellipse at 90% 10%, rgba(74, 90, 186, 0.10) 0%, transparent 50%),
    radial-gradient(ellipse at 50% 90%, rgba(60, 59, 110, 0.10) 0%, transparent 50%);
}

/* UK */
body::before {
  background:
    radial-gradient(ellipse at 10% 20%, rgba(1, 33, 105, 0.15) 0%, transparent 50%),
    radial-gradient(ellipse at 90% 10%, rgba(200, 16, 46, 0.10) 0%, transparent 50%),
    radial-gradient(ellipse at 50% 90%, rgba(1, 33, 105, 0.12) 0%, transparent 50%);
}
```
