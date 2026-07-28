# 🌍 ZipCode Global — World's #1 PIN Code Finder

**121 Countries · One World · Every Postal Code**

A cinematic, feature-rich Blogger template for finding postal codes across 121 countries. Built with Indian heritage 🇮🇳 and global reach 🌍.

## 🎯 Features

- 🌍 **121 Countries** — Each with its own dedicated page
- ⚡ **Lightning Fast** — Sub-100ms search response
- 🗺️ **Auto Map** — Every search reveals location on interactive map
- 🎙️ **Voice Search** — Speak the postal code
- ⌨️ **Command Palette** — Press Ctrl+K for instant search
- 📱 **Mobile First** — Responsive on all devices
- 🎬 **Cinematic Design** — Dark theme with saffron/gold accents
- 🔍 **Global SEO** — Optimized for search engines

## 📁 Project Structure

```
zipcode-global/
├── README.md                          # This file
├── ROADMAP.md                         # Development roadmap
├── zipcode-global-v7-homepage.xml     # Main Blogger template (paste in Template Editor)
├── pages/
│   ├── about.html                     # About page (Blogger Pages > New Page)
│   ├── privacy.html                   # Privacy Policy page
│   └── report.html                    # Report Mistake form page
└── data/                              # Pincode data (hosted on GitHub)
    ├── india/                         # 37 Indian states (from data.gov.in)
    │   ├── andhra-pradesh.json
    │   ├── bihar.json
    │   └── ...
    ├── usa/                           # 50 US states
    │   ├── California.json
    │   ├── New_York.json
    │   └── ...
    └── world/                         # 119 other countries
        ├── GB/                        # United Kingdom
        ├── JP/                        # Japan
        └── ...
```

## 🚀 Deployment Guide

### Step 1: Upload Template
1. Go to Blogger Dashboard → Theme → Edit HTML
2. Select ALL existing code → Delete
3. Paste contents of `zipcode-global-v7-homepage.xml`
4. Save

### Step 2: Create Pages
1. Go to Pages → New Page
2. Create "About" → paste `pages/about.html`
3. Create "Privacy Policy" → paste `pages/privacy.html`
4. Create "Report Mistake" → paste `pages/report.html`
5. Publish all three

### Step 3: Setup Navigation
1. Go to Layout → Add a Link List widget
2. Add links: Home, About, Privacy, Report
3. Save

### Step 4: Data Repository
1. Upload all data files to GitHub repository
2. Update `DATA_BASE` URL in template if needed

## 🎨 Design System

| Token | Color | Usage |
|-------|-------|-------|
| `--saffron` | `#ff6b1a` | Primary accent |
| `--gold` | `#f5b700` | Secondary accent |
| `--peacock-teal` | `#0a9396` | Tertiary accent |
| `--royal-indigo` | `#1a1f4d` | Deep background |
| `--cinema` | `#050816` | Base background |
| `--text` | `#f5f1e8` | Primary text |

## 📊 Data Sources

- 🇮🇳 **India**: data.gov.in (India Post)
- 🇺🇸 **USA**: USPS public data
- 🌍 **World**: Various national postal services

## 📝 License

Open source — use freely for your projects.

## 🙏 Credits

- Data: Government of India Open Data (data.gov.in)
- Maps: OpenStreetMap + Leaflet
- Fonts: Google Fonts (Inter, Space Grotesk, Cinzel)
- Built with ❤️ in Bharat 🇮🇳
