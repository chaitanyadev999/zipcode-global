import os

BLOG_DIR = os.path.join(os.path.dirname(__file__), "pages", "blog")
os.makedirs(BLOG_DIR, exist_ok=True)

ARTICLES = [
    {
        "slug": "india-pincode-history",
        "title": "The Fascinating History of PIN Codes in India",
        "desc": "Discover how India's 6-digit Postal Index Number system revolutionized mail delivery in 1972 and why it remains crucial today.",
        "image": "https://images.unsplash.com/photo-1524661135-423995f22d0b?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",
        "content": """
        <h2>Before 1972: A Delivery Nightmare</h2>
        <p>Imagine a time when delivering a letter in a vast, diverse country like India relied entirely on the postman's local knowledge. With hundreds of languages, identical town names across different states, and rapidly growing urban centers, the Indian postal system was facing an unprecedented crisis. Sorting letters manually without a standardized numbering system was chaotic, leading to delayed or lost mail.</p>
        <h2>The Birth of the PIN Code</h2>
        <p>On August 15, 1972, Shriram Bhikaji Velankar, an additional secretary in the Union Ministry of Communications, introduced a brilliantly simple yet powerful solution: the Postal Index Number (PIN). This 6-digit code was designed to map the entire geography of India logically.</p>
        <p>The system is incredibly elegant. The first digit represents the region (Northern, Western, Southern, or Eastern India). The second digit identifies the sub-region or state. The third digit pinpoints the sorting district within that state. Finally, the last three digits specify the exact post office responsible for final delivery.</p>
        <h2>Why It Still Matters in the Digital Age</h2>
        <p>Today, you might think email and instant messaging have made the postal system obsolete. However, the exact opposite is true. With the boom of e-commerce, food delivery apps, and digital banking (KYC verification), the PIN code has become more important than ever. It has transitioned from a simple mail-sorting tool to the backbone of modern digital logistics and location-based services in India.</p>
        """
    },
    {
        "slug": "usa-zipcode-system",
        "title": "How ZIP Codes Transformed the USA Postal System",
        "desc": "Explore the origins of the Zone Improvement Plan (ZIP) code and how it saved the US postal service from collapse in the 1960s.",
        "image": "https://images.unsplash.com/photo-1563901968864-4e94119d6917?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",
        "content": """
        <h2>The Post-War Mail Boom</h2>
        <p>Following World War II, the United States experienced a massive economic boom. Along with this prosperity came an explosion in mail volume. Businesses were sending out catalogs, bills, and advertisements by the millions. The traditional method of sorting mail—relying on clerks who had memorized the routes of thousands of streets—was breaking down under the sheer volume.</p>
        <h2>Mr. ZIP and the Zone Improvement Plan</h2>
        <p>In July 1963, the United States Postal Service (USPS) rolled out the Zone Improvement Plan, giving birth to the acronym we all know today: ZIP code. To help the public adapt to this massive change, the USPS created a cartoon character named "Mr. ZIP." With his friendly face and swift movement, Mr. ZIP appeared on posters, stamps, and even TV commercials, urging Americans to "Use ZIP Codes" for faster service.</p>
        <h2>Decoding the 5 Digits</h2>
        <p>The beauty of the ZIP code lies in its geographical logic. The first digit designates a broad area of the country, starting from zero in the Northeast (like Massachusetts) and moving westward up to nine on the West Coast (like California). The next two digits narrow down to a central post office facility, and the final two digits identify the specific local post office or delivery area.</p>
        <p>This simple 5-digit number completely revolutionized American logistics. It allowed for automated sorting machines, drastically reduced delivery times, and laid the foundational infrastructure that modern giants like Amazon and FedEx rely on today.</p>
        """
    },
    {
        "slug": "ecommerce-logistics",
        "title": "The Crucial Role of Postal Codes in Modern E-commerce",
        "desc": "Why your online shopping addiction heavily relies on accurate postal codes for lightning-fast deliveries.",
        "image": "https://images.unsplash.com/photo-1586528116311-ad8ed7c663be?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",
        "content": """
        <h2>The Hidden Engine of Online Shopping</h2>
        <p>When you click "Buy Now" on your favorite online store, you expect your package to arrive at your doorstep within days, sometimes even hours. But have you ever wondered how complex algorithms figure out exactly which warehouse to ship from, which truck to load it onto, and which driver should drop it off? The secret lies in one small string of numbers: your postal code.</p>
        <h2>Routing Optimization and Cost Calculation</h2>
        <p>For e-commerce giants, postal codes are not just address identifiers; they are critical data points for cost and time calculations. When you enter your zip code at checkout, backend systems instantly calculate shipping rates, estimate delivery dates, and even determine if a product is eligible for same-day delivery. If a postal code is entered incorrectly, the entire automated chain breaks, leading to delayed packages and frustrated customers.</p>
        <h2>The Future: Hyper-Local Delivery</h2>
        <p>As consumer expectations rise, logistics companies are moving towards hyper-local delivery models. This means using highly specific postal codes (like the US ZIP+4 or the UK's alphanumeric codes) to pinpoint delivery locations down to a single building or city block. Without these codes, the modern e-commerce miracle simply wouldn't exist.</p>
        """
    },
    {
        "slug": "global-postal-facts",
        "title": "10 Interesting Facts About Global Postal Networks",
        "desc": "From underwater post offices to mail delivered by mules, discover the quirky side of the world's postal systems.",
        "image": "https://images.unsplash.com/photo-1555529733-0e670560f7e1?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",
        "content": """
        <h2>1. The Smallest Post Office</h2>
        <p>The world's smallest post office is located in Ochopee, Florida, USA. Measuring just 61.3 square feet, this tiny shed originally served as an irrigation pipe shed for a tomato farm. Today, it has its own ZIP code (34141) and serves the local community.</p>
        <h2>2. Delivery by Mule</h2>
        <p>While drones are the talk of the town, the USPS still uses mules to deliver mail to the Havasupai Indian Reservation at the bottom of the Grand Canyon. It's the most efficient way to navigate the steep, rocky terrain.</p>
        <h2>3. The Underwater Postbox</h2>
        <p>In Vanuatu, a nation in the South Pacific, there is an official underwater post office. Scuba divers and snorkelers can purchase waterproof postcards on land and dive down to mail them in a submerged postbox!</p>
        <h2>4. The Oldest Functioning Post Office</h2>
        <p>Sanquhar Post Office in Dumfries and Galloway, Scotland, is the oldest working post office in the world. It has been operating continuously since 1712, serving its local community for over three centuries.</p>
        <p>These quirky facts remind us that despite the high-tech nature of modern logistics, the global postal network is deeply rooted in human history, culture, and sometimes, sheer adventurous ingenuity.</p>
        """
    },
    {
        "slug": "no-postal-code-countries",
        "title": "Why Some Countries Don't Use Postal Codes",
        "desc": "Discover the unique addressing systems of nations that manage just fine without ZIP or PIN codes.",
        "image": "https://images.unsplash.com/photo-1488646953014-85cb84e24328?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",
        "content": """
        <h2>Living Without the Code</h2>
        <p>In an increasingly digital and automated world, it's hard to imagine living without a postal code. Yet, several countries around the globe operate perfectly well without them. How do they manage? The answer usually lies in population density, geography, and highly structured traditional addressing methods.</p>
        <h2>The UAE's Makani System</h2>
        <p>For a long time, the United Arab Emirates did not have a standardized postal code system. Mail was delivered to central PO Boxes rather than directly to homes. To modernize direct-to-door delivery, Dubai introduced the 'Makani' system, assigning a unique 10-digit coordinate number to every building, effectively bypassing traditional zip codes altogether.</p>
        <h2>Ireland's Late Adoption</h2>
        <p>Ireland was one of the last developed nations to adopt a postal code system. Until 2015, they managed without one, relying heavily on the local knowledge of postmen and detailed street addresses. They eventually introduced "Eircodes," a unique system where every single house gets its own specific 7-character code, rather than sharing a code with a neighborhood.</p>
        <p>While the lack of postal codes can cause headaches for international shipping forms, these countries prove that there is more than one way to ensure a letter reaches its destination.</p>
        """
    },
    {
        "slug": "international-addressing",
        "title": "The Ultimate Guide to Formatting International Addresses",
        "desc": "Avoid lost packages by learning how to properly format addresses for different countries.",
        "image": "https://images.unsplash.com/photo-1596526131083-e8c633c948d2?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",
        "content": """
        <h2>The Chaos of Cross-Border Shipping</h2>
        <p>If you've ever tried to send a package overseas, you've likely stared blankly at the address fields. Should the postal code go before the city or after? Does the province matter? Formatting an international address correctly is the single most important step to prevent your package from getting lost in a foreign sorting facility.</p>
        <h2>General Best Practices</h2>
        <p>While every country has its quirks, there are universal rules to follow. Always use uppercase letters, avoid unnecessary punctuation (like commas or periods), and ensure the destination country is written on the very last line in English. This helps the sending country's automated machines route the package out of the country correctly.</p>
        <h2>Regional Variations</h2>
        <p>In Europe, the postal code usually precedes the city name (e.g., 75008 PARIS). In the United States and Canada, the city comes first, followed by the state/province abbreviation, and then the postal code (e.g., SEATTLE WA 98109). In Japan, addresses are often written in reverse order compared to the West, starting with the postal code, followed by the prefecture, city, and subarea.</p>
        <p>Taking an extra 60 seconds to verify the destination country's preferred format can save you weeks of shipping delays.</p>
        """
    },
    {
        "slug": "future-of-delivery",
        "title": "The Future of Logistics: AI, Drones, and Smart Sorting",
        "desc": "How artificial intelligence and drone technology are reinventing the way we think about postal codes and delivery.",
        "image": "https://images.unsplash.com/photo-1508614589041-895b88991e3e?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",
        "content": """
        <h2>Beyond the Postal Code</h2>
        <p>For decades, the postal code has been the ultimate geographical identifier. But as technology advances at a breakneck pace, the traditional zip code is getting a massive upgrade. Artificial Intelligence and machine learning algorithms are now taking raw address data and transforming it into hyper-optimized delivery routes that change in real-time based on traffic and weather.</p>
        <h2>The Rise of Drone Delivery</h2>
        <p>Companies like Amazon and Google's Wing are actively testing drone deliveries. For a drone, a traditional postal code is too broad. Instead, they rely on exact GPS coordinates and localized what3words mapping to drop a package safely into a specific backyard. While postal codes will still dictate the regional sorting, micro-coordinates will handle the crucial 'last mile.'</p>
        <h2>Smart Sorting Facilities</h2>
        <p>Inside massive fulfillment centers, robots glide across the floor, sorting packages at superhuman speeds. These automated systems use AI vision to instantly read handwritten postal codes, cross-reference them with digital maps, and toss them into the correct dispatch bin in milliseconds. The future of delivery isn't just fast; it's incredibly intelligent.</p>
        """
    },
    {
        "slug": "zip-plus-4",
        "title": "Understanding the Anatomy of a US ZIP+4 Code",
        "desc": "What those extra four digits mean and why they are essential for business mailers.",
        "image": "https://images.unsplash.com/photo-1550505095-81378a56fa46?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",
        "content": """
        <h2>The Evolution of the ZIP Code</h2>
        <p>In 1983, the USPS realized that the standard 5-digit ZIP code wasn't granular enough for an ever-expanding population. Enter the ZIP+4 system. While the average citizen rarely memorizes those extra four digits, they are the secret weapon of bulk mailers and modern logistics companies.</p>
        <h2>Decoding the Plus Four</h2>
        <p>The standard 5 digits get a piece of mail to a specific post office. The "+4" digits take it much further. The first two numbers of the extended code usually pinpoint a specific delivery sector—like a group of streets, several blocks of a city, or a large cluster of office buildings. The final two digits narrow it down to a "delivery segment," which could be one side of a street, a specific floor in a skyscraper, or a single large corporate department.</p>
        <h2>Why It Saves Money</h2>
        <p>If you are a business sending out thousands of catalogs, including the ZIP+4 code saves the post office sorting time. In return, the USPS offers significant bulk mailing discounts. It also drastically reduces the chance of misdelivered mail, proving that sometimes, four little numbers make a massive financial difference.</p>
        """
    },
    {
        "slug": "uk-postcode-guide",
        "title": "Navigating the Unique UK Alphanumeric Postcode System",
        "desc": "Why the UK uses letters and numbers, and how it pinpoints locations with incredible accuracy.",
        "image": "https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",
        "content": """
        <h2>A Masterpiece of Alphanumeric Design</h2>
        <p>While most of the world relies on purely numeric postal codes, the United Kingdom utilizes a complex, alphanumeric system that looks like a secret code to outsiders (e.g., SW1A 1AA). Introduced systematically between 1959 and 1974, this format is highly regarded as one of the most precise postal systems in the world.</p>
        <h2>Breaking Down the Code</h2>
        <p>A UK postcode is divided into two parts, separated by a space. The first part is the "Outward Code," which directs the mail to the correct regional sorting office. The letters represent the city or region (like 'L' for Liverpool or 'SW' for South West London), followed by numbers for the specific district. The second part, the "Inward Code," sorts the mail at the local office down to a specific sector and a delivery point—usually representing just 15 properties!</p>
        <h2>More Than Just Mail</h2>
        <p>In the UK, the postcode is ingrained in daily life. It is heavily used for GPS navigation (SatNavs), calculating car insurance premiums, determining school catchments, and analyzing demographic data. A single UK postcode holds a wealth of geographic and socio-economic information.</p>
        """
    },
    {
        "slug": "emergency-services",
        "title": "How Accurate Postal Codes Save Lives in Emergency Services",
        "desc": "When every second counts, the precision of postal data becomes a matter of life and death.",
        "image": "https://images.unsplash.com/photo-1587572236558-a3651c38d347?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",
        "content": """
        <h2>The Race Against Time</h2>
        <p>When you dial emergency services for an ambulance, police, or fire department, the dispatcher's primary goal is to locate you instantly. While GPS tracking on smartphones has improved dramatically, emergency dispatch systems (like 911 or 999) still rely heavily on verified postal addresses and zip codes to accurately route first responders.</p>
        <h2>Overcoming Address Ambiguity</h2>
        <p>Imagine living on "Main Street." In many large metropolitan areas, there could be three different "Main Streets" in neighboring suburbs. If a caller is panicking and gives an incomplete address, the postal code acts as the ultimate tie-breaker. It instantly narrows down the search radius from an entire city to a specific neighborhood block.</p>
        <h2>E-911 and GIS Integration</h2>
        <p>Modern emergency response utilizes Geographic Information Systems (GIS) that overlay postal code boundaries with real-time traffic and responder locations. Ensuring that your residential or business address is correctly mapped with the official postal code ensures that automated routing algorithms don't send an ambulance to the wrong side of the county.</p>
        """
    },
    {
        "slug": "unusual-zipcodes",
        "title": "The Most Unusual and Dedicated ZIP Codes in the World",
        "desc": "Did you know the President of the United States and Santa Claus have their own ZIP codes?",
        "image": "https://images.unsplash.com/photo-1543854589-9bd721d6f51a?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",
        "content": """
        <h2>When You're So Important You Get Your Own Code</h2>
        <p>Usually, a ZIP code covers a town or a large neighborhood. But in rare cases, a single entity receives so much mail that the postal service assigns it an exclusive code. The President of the United States, for example, receives mail at 20500—a ZIP code exclusively dedicated to the White House.</p>
        <h2>Santa Claus, Indiana</h2>
        <p>The town of Santa Claus in Indiana, USA, has a very special ZIP code: 47579. Every year, during the holiday season, the local post office is flooded with thousands of letters addressed to Santa. A group of dedicated volunteers, known as "Santa's Elves," ensures that every letter with a return address gets a reply.</p>
        <h2>Corporate Giants and Skyscrapers</h2>
        <p>Some massive buildings are essentially vertical cities. The Empire State Building in New York has its own dedicated ZIP code (10118) because it houses so many businesses. Similarly, large corporations and universities often receive unique codes to streamline the massive influx of daily correspondence.</p>
        """
    },
    {
        "slug": "shipping-costs",
        "title": "How Accurate Pin Codes Save You Money on Shipping",
        "desc": "Don't overpay for delivery! Learn how zip code validation prevents costly shipping errors.",
        "image": "https://images.unsplash.com/photo-1580674285054-bed31e145f59?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",
        "content": """
        <h2>The Hidden Cost of Typos</h2>
        <p>We've all been there: rushing through an online checkout and accidentally typing one wrong digit in the postal code field. While it seems like a minor typo, that single digit can bounce your package to the wrong side of the country. This results in "Return to Sender" fees, delayed deliveries, and restocking charges that eat into consumer and business wallets.</p>
        <h2>Zone-Based Pricing</h2>
        <p>Major carriers like FedEx, UPS, and DHL calculate shipping costs based on "zones." These zones are directly tied to postal codes. The further the destination zip code is from the origin zip code, the higher the shipping rate. Accurately validating the postal code ensures that the carrier's API quotes the correct zone rate. If a code is invalid, default maximum rates are often applied.</p>
        <h2>Address Validation Tools</h2>
        <p>This is why tools like PO ZipCode Global are so essential. By verifying your postal code before shipping a parcel, you ensure seamless integration with carrier APIs, avoiding residential surcharge errors and address correction penalties. A moment of verification leads to a lifetime of savings.</p>
        """
    },
    {
        "slug": "canadian-postal-codes",
        "title": "Demystifying the Canadian Postal Code Format",
        "desc": "Why does Canada use the A1A 1A1 format? A deep dive into one of the world's most logical postal systems.",
        "image": "https://images.unsplash.com/photo-1503899036084-c55cdd92da26?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",
        "content": """
        <h2>The A1A 1A1 Structure</h2>
        <p>Introduced gradually between 1971 and 1974, the Canadian postal code is a six-character alphanumeric string in the format ANA NAN, where 'A' is a letter and 'N' is a number. This alternating structure was chosen to be easily readable by both human eyes and early optical character recognition (OCR) sorting machines.</p>
        <h2>Forward Sortation Area (FSA)</h2>
        <p>The first three characters form the Forward Sortation Area (FSA). The very first letter represents a specific province or major geographic region. For instance, 'M' represents Metropolitan Toronto, while 'V' stands for British Columbia. The number that follows indicates whether the area is urban or rural. A '0' means a vast rural region, while numbers 1-9 indicate urban centers.</p>
        <h2>Local Delivery Unit (LDU)</h2>
        <p>The last three characters form the Local Delivery Unit (LDU). This gets incredibly specific, identifying a single city block, a large apartment building, or even a specific rural community. It is so precise that Canada Post can sort mail into the exact order the postman will walk down the street!</p>
        """
    },
    {
        "slug": "journey-of-a-letter",
        "title": "The Journey of a Letter: From Sender to Receiver",
        "desc": "Follow a piece of mail on its incredible automated journey through the modern postal network.",
        "image": "https://images.unsplash.com/photo-1594950920405-b38fae639943?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",
        "content": """
        <h2>The Drop-Off and Collection</h2>
        <p>Your letter's journey begins the moment it hits the bottom of the blue collection box. At scheduled times, postal workers collect these letters and transport them to a local sorting facility. Here, the mail is dumped onto massive conveyor belts, where machines quickly separate letters from packages and face them all in the same direction.</p>
        <h2>The Magic of OCR and Barcodes</h2>
        <p>The letters zip through an Optical Character Reader (OCR) machine at blinding speeds. The machine scans the address, looking specifically for the postal code. Once read, it prints a fluorescent barcode along the bottom edge of the envelope. If the handwriting is too messy, an image is instantly beamed to a remote worker who types the code manually.</p>
        <h2>Final Sorting and Delivery</h2>
        <p>Guided entirely by that fluorescent barcode (which represents the postal code), the letter is routed into specific bins destined for different regions. It travels by truck or plane to a destination facility, where Delivery Barcode Sorters arrange the mail in the exact sequence of the local letter carrier's daily route. The postal code is the invisible conductor orchestrating this entire symphony.</p>
        """
    },
    {
        "slug": "digital-mapping",
        "title": "How Digital Mapping is Changing the Way We Find Addresses",
        "desc": "The intersection of traditional postal codes and modern API-driven digital mapping platforms.",
        "image": "https://images.unsplash.com/photo-1524661135-423995f22d0b?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",
        "content": """
        <h2>The Transition to Polygons</h2>
        <p>Historically, a postal code was just a line on a paper map. Today, digital mapping platforms like Google Maps and Mapbox render postal codes as precise digital polygons. These geographic boundary files allow developers to visualize demographic data, map out delivery territories, and perform spatial analysis with incredible accuracy.</p>
        <h2>APIs and Real-Time Verification</h2>
        <p>Modern applications rely on Postal Code APIs to auto-complete addresses for users. When you type '90210' into a form, a digital map database instantly pings back 'Beverly Hills, California.' This reduces friction in online checkouts and prevents database corruption caused by user typos.</p>
        <h2>Bridging the Physical and Digital</h2>
        <p>As we move towards a world filled with autonomous vehicles and augmented reality, the postal code serves as the crucial bridge between physical addresses and digital coordinates. It proves that a numerical system invented in the 1960s is still entirely relevant in the era of spatial computing.</p>
        """
    }
]

# Generate blog.html (Index Page)
index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>Blog — Postal Codes, Logistics & Facts | PO ZipCode Global</title>
<meta name="description" content="Read expert articles on zip codes, postal history, logistics, and global shipping facts. Humanized, high-quality insights from PO ZipCode Global."/>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet"/>
<style>
:root{{ --bg:#050816; --t:#f0f2f8; --p:#00d4ff; --a:#7c3aed; --card:rgba(255,255,255,0.04); --glass:rgba(255,255,255,0.05); }}
body{{ font-family:'Inter',sans-serif; background:var(--bg); color:var(--t); margin:0; padding:0; }}
a{{ text-decoration:none; color:inherit; }}
.nav{{ padding:1rem 2rem; background:rgba(5,8,22,0.9); border-bottom:1px solid rgba(0,212,255,0.1); display:flex; justify-content:space-between; align-items:center; position:sticky; top:0; z-index:100; backdrop-filter:blur(10px); }}
.brand{{ font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:1.2rem; display:flex; align-items:center; gap:0.5rem; }}
.brand img{{ width:30px; border-radius:6px; }}
.nav-links a{{ margin-left:1.5rem; font-size:0.9rem; color:#94a3b8; font-weight:600; }}
.nav-links a:hover{{ color:var(--p); }}
.hero{{ text-align:center; padding:5rem 1rem 3rem; }}
.hero h1{{ font-family:'Space Grotesk',sans-serif; font-size:3rem; margin:0 0 1rem; background:linear-gradient(135deg,var(--p),var(--a)); -webkit-background-clip:text; -webkit-text-fill-color:transparent; }}
.hero p{{ color:#94a3b8; font-size:1.1rem; max-width:600px; margin:0 auto; line-height:1.6; }}
.grid{{ display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:2rem; max-width:1200px; margin:0 auto; padding:0 2rem 5rem; }}
.card{{ background:var(--card); border:1px solid rgba(0,212,255,0.1); border-radius:12px; overflow:hidden; transition:transform 0.3s, border-color 0.3s; display:flex; flex-direction:column; }}
.card:hover{{ transform:translateY(-5px); border-color:var(--p); box-shadow:0 10px 30px rgba(0,212,255,0.1); }}
.card img{{ width:100%; height:220px; object-fit:cover; }}
.card-content{{ padding:1.5rem; flex-grow:1; display:flex; flex-direction:column; }}
.card h2{{ font-family:'Space Grotesk',sans-serif; font-size:1.25rem; margin:0 0 0.8rem; line-height:1.4; color:var(--t); }}
.card p{{ color:#94a3b8; font-size:0.95rem; line-height:1.6; margin:0 0 1.5rem; flex-grow:1; }}
.card span{{ color:var(--p); font-size:0.85rem; font-weight:600; text-transform:uppercase; letter-spacing:1px; }}
@media(max-width:768px){{ .nav{{padding:1rem;}} .hero h1{{font-size:2rem;}} .grid{{grid-template-columns:1fr;}} }}
</style>
</head>
<body>
<nav class="nav">
    <a href="../home/main.html" class="brand"><img src="https://flagcdn.com/w40/un.png" alt="Logo"/> PO ZipCode Global</a>
    <div class="nav-links">
        <a href="../home/main.html">Home</a>
        <a href="blog.html" style="color:var(--p)">Blog</a>
        <a href="report.html">Report</a>
    </div>
</nav>
<div class="hero">
    <h1>Our Blog</h1>
    <p>Discover fascinating insights about global postal systems, logistics technology, and addressing standards.</p>
</div>
<div class="grid">
"""

for art in ARTICLES:
    index_html += f"""
    <a href="blog/{art['slug']}.html" class="card">
        <img src="{art['image']}" alt="{art['title']}">
        <div class="card-content">
            <h2>{art['title']}</h2>
            <p>{art['desc']}</p>
            <span>Read Article →</span>
        </div>
    </a>
    """

index_html += """
</div>
</body>
</html>
"""

with open(os.path.join(os.path.dirname(__file__), "pages", "blog.html"), "w", encoding="utf-8") as f:
    f.write(index_html)

# Generate individual blog post HTML files
for art in ARTICLES:
    post_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>{art['title']} | PO ZipCode Global Blog</title>
<meta name="description" content="{art['desc']}"/>
<meta property="og:title" content="{art['title']}"/>
<meta property="og:image" content="{art['image']}"/>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=Space+Grotesk:wght@500;700;800&display=swap" rel="stylesheet"/>
<style>
:root{{ --bg:#050816; --t:#f0f2f8; --p:#00d4ff; --a:#7c3aed; }}
body{{ font-family:'Inter',sans-serif; background:var(--bg); color:var(--t); margin:0; padding:0; line-height:1.8; }}
a{{ text-decoration:none; color:inherit; }}
.nav{{ padding:1rem 2rem; background:rgba(5,8,22,0.9); border-bottom:1px solid rgba(0,212,255,0.1); display:flex; justify-content:space-between; align-items:center; position:sticky; top:0; z-index:100; backdrop-filter:blur(10px); }}
.brand{{ font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:1.2rem; display:flex; align-items:center; gap:0.5rem; }}
.brand img{{ width:30px; border-radius:6px; }}
.nav-links a{{ margin-left:1.5rem; font-size:0.9rem; color:#94a3b8; font-weight:600; }}
.nav-links a:hover{{ color:var(--p); }}
.article{{ max-width:800px; margin:0 auto; padding:4rem 2rem 5rem; }}
.back{{ display:inline-block; margin-bottom:2rem; color:var(--p); font-weight:600; font-size:0.9rem; }}
.back:hover{{ text-decoration:underline; }}
h1{{ font-family:'Space Grotesk',sans-serif; font-size:2.8rem; margin:0 0 1.5rem; line-height:1.2; font-weight:800; }}
.desc{{ font-size:1.2rem; color:#94a3b8; margin-bottom:2.5rem; }}
.cover{{ width:100%; height:450px; object-fit:cover; border-radius:16px; margin-bottom:3rem; box-shadow:0 10px 40px rgba(0,0,0,0.5); border:1px solid rgba(255,255,255,0.05); }}
.content h2{{ font-family:'Space Grotesk',sans-serif; color:var(--p); font-size:1.8rem; margin:2.5rem 0 1rem; }}
.content p{{ font-size:1.15rem; color:#cbd5e1; margin-bottom:1.5rem; }}
@media(max-width:768px){{ h1{{font-size:2rem;}} .cover{{height:250px;}} .nav{{padding:1rem;}} .article{{padding:2rem 1rem 4rem;}} }}
</style>
</head>
<body>
<nav class="nav">
    <a href="../../home/main.html" class="brand"><img src="https://flagcdn.com/w40/un.png" alt="Logo"/> PO ZipCode Global</a>
    <div class="nav-links">
        <a href="../../home/main.html">Home</a>
        <a href="../blog.html" style="color:var(--p)">Blog</a>
    </div>
</nav>
<div class="article">
    <a href="../blog.html" class="back">← Back to Blog Index</a>
    <h1>{art['title']}</h1>
    <p class="desc">{art['desc']}</p>
    <img src="{art['image']}" alt="{art['title']}" class="cover">
    <div class="content">
        {art['content']}
    </div>
    
    <div style="margin-top:5rem; padding-top:2rem; border-top:1px solid rgba(255,255,255,0.1); text-align:center;">
        <p style="color:#94a3b8; font-size:0.9rem;">Enjoyed this article? Return to the <a href="../../home/main.html" style="color:var(--p)">Home Page</a> to find a postal code.</p>
    </div>
</div>
</body>
</html>
"""
    with open(os.path.join(BLOG_DIR, f"{art['slug']}.html"), "w", encoding="utf-8") as f:
        f.write(post_html)

print("✅ Successfully generated 15 unique blog posts and the index page!")
