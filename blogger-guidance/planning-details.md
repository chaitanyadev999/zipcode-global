# Planning Details — SEO & Content Strategy

## Target Keywords by Country

### India (High Priority)
| Keyword | Monthly Searches | Difficulty |
|---------|-----------------|------------|
| india pincode | 500K+ | High |
| pincode finder | 200K+ | Medium |
| india postal code | 150K+ | Medium |
| telangana pincode | 80K+ | Low |
| andhra pradesh pin code | 60K+ | Low |
| pin code by area | 100K+ | Medium |

### USA (High Priority)
| Keyword | Monthly Searches | Difficulty |
|---------|-----------------|------------|
| zip code lookup | 2M+ | High |
| us zip code finder | 800K+ | High |
| zip code by city | 600K+ | High |
| california zip codes | 200K+ | Medium |
| texas zip codes | 180K+ | Medium |
| zip code search | 1M+ | High |

### UK
| Keyword | Monthly Searches | Difficulty |
|---------|-----------------|------------|
| uk postcode finder | 400K+ | High |
| postcode lookup | 300K+ | Medium |
| england postcodes | 100K+ | Low |

---

## Page Title Formulas

### Country Pages:
```
{Country} {Term} Directory — Find {Term} by State | PO ZipCode Global

Examples:
- India PIN Code Directory — Find Pincode by State | PO ZipCode Global
- USA ZIP Code Directory — Find ZIP Code by State | PO ZipCode Global
- UK Postcode Directory — Find Postcode by Region | PO ZipCode Global
```

### Meta Description Formula:
```
Find {term} for all {count} {states/regions} of {country}. 
Search by {city/district/area}. Free, instant lookup with interactive map. 
{count}+ {terms} in our database.

Example:
Find PIN codes for all 36 states and UTs of India. 
Search by district, city or area name. Free, instant lookup with interactive map. 
155,000+ pincodes in our database.
```

---

## JSON-LD Schema Markup

Add this to each country page `<head>` for rich search results:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebApplication",
  "name": "PO ZipCode Global — India",
  "url": "https://zipcodeglobal.com/p/india.html",
  "description": "Find any PIN code in India. 36 States & UTs. 155,000+ records.",
  "applicationCategory": "UtilitiesApplication",
  "operatingSystem": "Any",
  "offers": {
    "@type": "Offer",
    "price": "0",
    "priceCurrency": "USD"
  },
  "author": {
    "@type": "Organization",
    "name": "PO ZipCode Global",
    "url": "https://zipcodeglobal.com"
  }
}
</script>
```

---

## URL Structure

### Recommended URL Pattern for Blogger:
```
/p/india.html         → India page
/p/usa.html           → USA page
/p/uk.html            → UK page
/p/australia.html     → Australia page
/p/canada.html        → Canada page
/p/germany.html       → Germany page
... (121 country pages total)
/p/about.html         → About
/p/privacy.html       → Privacy Policy
/p/report.html        → Report/Contact
```

### For GitHub Pages:
```
/pages/india.html
/pages/usa.html
/pages/uk.html
```

---

## Content Strategy for Each Country Page

Each country page should have:

1. **H1 Heading:** "{Country} {Postal Code Term} by State/Region"
2. **Introduction paragraph (100-150 words):** Explain what the page does, mention the country, total count
3. **States Grid:** Interactive buttons for each state/region
4. **Search Box:** With ZIP/PIN code input and voice search
5. **Results Section:** Dynamic cards with postal data
6. **Interactive Map:** Leaflet.js with markers
7. **Footer:** Internal links to other country pages

---

## XML Sitemap Structure

Create a `sitemap.xml` file:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://zipcodeglobal.com/</loc>
    <priority>1.0</priority>
    <changefreq>weekly</changefreq>
  </url>
  <url>
    <loc>https://zipcodeglobal.com/p/india.html</loc>
    <priority>0.9</priority>
    <changefreq>monthly</changefreq>
  </url>
  <url>
    <loc>https://zipcodeglobal.com/p/usa.html</loc>
    <priority>0.9</priority>
    <changefreq>monthly</changefreq>
  </url>
  <!-- Add all 121 country pages -->
</urlset>
```

Submit to Google Search Console at: https://search.google.com/search-console

---

## Internal Linking Strategy

On India page, add links to nearby countries:
```
"Also explore: Pakistan, Bangladesh, Sri Lanka, Nepal, Bhutan"
```

On USA page:
```
"Also explore: Canada, Mexico, Puerto Rico"
```

This creates a natural internal link network that boosts SEO.

---

## Content Calendar

| Week | Task |
|------|------|
| Week 1 | Launch India + USA pages, submit to GSC |
| Week 2 | Add UK + Australia + Canada pages |
| Week 3 | Add Germany + France + Japan + UAE |
| Week 4 | Add remaining 114 country pages |
| Month 2 | Apply for Google AdSense |
| Month 3 | Build backlinks from travel/expat blogs |
