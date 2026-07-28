# Website Hosting Guide — PO ZipCode Global

## Option 1: GitHub Pages (Free, Recommended)

### Setup Steps:
1. Create a new GitHub repo: `your-username/zipcode-blogger`
2. Push the entire `zipcode-global/` folder contents
3. Go to Settings → Pages → Branch: `main` → Folder: `/ (root)`
4. Your site will be live at: `https://your-username.github.io/zipcode-blogger/`

### File Mapping on GitHub Pages:
| Local File | GitHub Pages URL |
|-----------|-----------------|
| `home/main.html` | `https://yoursite.github.io/` |
| `pages/india.html` | `https://yoursite.github.io/pages/india.html` |
| `pages/usa.html` | `https://yoursite.github.io/pages/usa.html` |
| `pages/uk.html` | `https://yoursite.github.io/pages/uk.html` |

---

## Option 2: Blogger (Blogspot)

### Method A: Embed as Blogger Page
1. Go to **Blogger Dashboard → Pages → New Page**
2. Click **HTML view** (not Compose)
3. Paste the full HTML from `pages/india.html` (or any country page)
4. Title the page: "India PIN Codes — Find Any Pincode"
5. Click **Publish**

### Method B: Custom Domain on Blogger
1. Buy a domain (e.g., `zipcodeglobal.com`) from Namecheap or GoDaddy (~$10/year)
2. Go to Blogger → Settings → Custom Domain
3. Enter your domain and follow the DNS CNAME verification

### Embedding JavaScript `fetch()` in Blogger:
Blogger widgets strip `<script>` tags by default. To fix:
1. Go to **Theme → Edit HTML**
2. Find `</body>` and add your script just before it
3. OR use a **HTML/JavaScript gadget** in the Layout

### Important Blogger Quirks:
- Blogger auto-converts `&` to `&amp;` — wrap your HTML in `<![CDATA[ ... ]]>` tags
- Images must be uploaded to Blogger's own CDN (Picasa) or use external links
- Custom CSS goes in Theme → Customize → Advanced → Add CSS

---

## Option 3: Cloudflare Pages (Best Performance)

1. Connect your GitHub repo to Cloudflare Pages
2. Build command: (none — static files)
3. Output directory: `/`
4. Free SSL + Global CDN automatically applied
5. Custom domain: Free with Cloudflare

---

## AdSense Integration

### Best Ad Placements for Zipcode Sites:
1. **Above the States Grid** — High visibility, users haven't found their data yet
2. **Between Results** — Users are engaged, likely to notice ads
3. **Footer** — Always visible, non-intrusive

### AdSense Code Placement:
```html
<!-- Paste after <body> tag -->
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-XXXXXXXXXXXXXXXX" crossorigin="anonymous"></script>

<!-- In-content ad unit -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-XXXXXXXXXXXXXXXX"
     data-ad-slot="XXXXXXXXXX"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>(adsbygoogle = window.adsbygoogle || []).push({});</script>
```

### AdSense Policy Notes:
- Each page must have original, valuable content (not just data)
- Add a 100-150 word introduction about the country/region
- Must have Privacy Policy page (already created at `pages/privacy.html`)
- Must have Contact page (already at `pages/report.html`)

---

## jsDelivr CDN Usage

All data is fetched from GitHub via jsDelivr — completely free, no limits:

```javascript
// India data (root folder)
https://cdn.jsdelivr.net/gh/chaitanyadev999/pincode-dataindia@main/telangana.json

// USA data (usa/ folder)
https://cdn.jsdelivr.net/gh/chaitanyadev999/pincode-dataindia@main/usa/California.json

// World data (world/ folder)
https://cdn.jsdelivr.net/gh/chaitanyadev999/pincode-dataindia@main/world/GB/England.json
```

**Why jsDelivr?**
- Free, unlimited requests
- Global CDN with 99.99% uptime
- Automatic cache invalidation when repo updates
- No API key required
