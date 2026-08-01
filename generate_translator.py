import json
import os
import sys

# Append path to import generate_pages
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import generate_pages

# A basic map from country code to Google Translate language code
# Default fallback is 'en' if not found, or we map major ones explicitly.
COUNTRY_LANG_MAP = {
    "IN": "hi", "US": "en", "AD": "ca", "AE": "ar", "AI": "en", "AL": "sq", "AR": "es", "AS": "en",
    "AT": "de", "AU": "en", "AX": "sv", "AZ": "az", "BD": "bn", "BE": "nl", "BG": "bg", "BM": "en",
    "BR": "pt", "BY": "be", "CA": "en", "CC": "en", "CH": "de", "CL": "es", "CN": "zh-CN", "CO": "es",
    "CR": "es", "CX": "en", "CY": "el", "CZ": "cs", "DE": "de", "DK": "da", "DO": "es", "DZ": "ar",
    "EC": "es", "EE": "et", "ES": "es", "FI": "fi", "FK": "en", "FM": "en", "FO": "fo", "FR": "fr",
    "GB": "en", "GF": "fr", "GG": "en", "GI": "en", "GL": "kl", "GP": "fr", "GS": "en", "GT": "es",
    "GU": "en", "HK": "zh-TW", "HM": "en", "HN": "es", "HR": "hr", "HT": "ht", "HU": "hu", "ID": "id",
    "IE": "ga", "IM": "en", "IO": "en", "IS": "is", "IT": "it", "JE": "en", "JP": "ja", "KE": "sw",
    "KR": "ko", "LI": "de", "LK": "si", "LT": "lt", "LU": "lb", "LV": "lv", "MA": "ar", "MC": "fr",
    "MD": "ro", "MH": "mh", "MK": "mk", "MO": "zh-TW", "MP": "en", "MQ": "fr", "MT": "mt", "MW": "ny",
    "MX": "es", "MY": "ms", "NC": "fr", "NF": "en", "NL": "nl", "NO": "no", "NR": "na", "NU": "en",
    "NZ": "en", "PA": "es", "PE": "es", "PF": "fr", "PH": "tl", "PK": "ur", "PL": "pl", "PM": "fr",
    "PN": "en", "PR": "es", "PT": "pt", "PW": "en", "RE": "fr", "RO": "ro", "RS": "sr", "RU": "ru",
    "SE": "sv", "SG": "en", "SI": "sl", "SJ": "no", "SK": "sk", "SM": "it", "TC": "en", "TH": "th",
    "TR": "tr", "UA": "uk", "UY": "es", "VA": "it", "VI": "en", "WF": "fr", "WS": "sm", "YT": "fr",
    "ZA": "af"
}

# We also want to give India multiple languages since user asked "Indian language select chesukuni"
EXTRA_LANGS = [
    ("IN-TE", "Telugu (India)", "te"),
    ("IN-TA", "Tamil (India)", "ta"),
    ("IN-ML", "Malayalam (India)", "ml"),
    ("IN-KN", "Kannada (India)", "kn")
]

options_html = ""

# Add regular countries
for code, name, lat, lon, term, reg, sub in generate_pages.COUNTRIES:
    lang_code = COUNTRY_LANG_MAP.get(code, "en")
    flag_code = code.lower()
    options_html += f"""        <div class="lang-option" data-lang="{lang_code}" data-flag="{flag_code}" data-name="{name}">
          <img src="https://flagcdn.com/w40/{flag_code}.png" alt="{name}">
          <span>{name} ({lang_code})</span>
        </div>\n"""

# Add Indian regionals
for code, name, lang_code in EXTRA_LANGS:
    options_html += f"""        <div class="lang-option" data-lang="{lang_code}" data-flag="in" data-name="{name}">
          <img src="https://flagcdn.com/w40/in.png" alt="{name}">
          <span>{name} ({lang_code})</span>
        </div>\n"""

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Free Global Language Translator — PO ZipCode Global</title>
<meta name="description" content="Translate text instantly across 121+ countries. Free online language translator supporting English, Hindi, Telugu, Japanese, Spanish, French and more.">
<link rel="icon" type="image/png" href="/home/assets/logo.png">

<style>
:root {
  --bg: #050816;
  --card: #0a0f25;
  --p: #00d4ff;
  --p2: 0, 212, 255;
  --a: #7000ff;
  --t: #f8fafc;
  --t2: #cbd5e1;
  --t3: #94a3b8;
  --f: 'Inter', system-ui, sans-serif;
  --glow: 0 0 20px rgba(var(--p2), 0.3);
  --ease: cubic-bezier(0.16, 1, 0.3, 1);
}
  /* Google Translate styling */
  #google_translate_element { display:inline-block; margin-left: 10px; vertical-align: middle; }
  .goog-te-gadget { font-family: var(--f) !important; color: transparent !important; font-size:0; }
  .goog-te-gadget .goog-te-combo { 
    background: var(--glass); border: 1px solid var(--b); color: var(--t2); 
    padding: .4rem .9rem; border-radius: 999px; font-weight: 600; font-size: .8rem;
    cursor: pointer; transition: all .25s var(--ease); outline: none;
  }
  .goog-te-gadget .goog-te-combo:hover { background: var(--card-hi); border-color: var(--cyan); color: var(--t); }
  .goog-te-gadget .goog-te-combo option { background: #050816; color: #fff; font-weight:normal; }
  .skiptranslate iframe { display: none !important; }
  body { top: 0 !important; font-family: var(--f); background: var(--bg); color: var(--t); margin:0; padding:0; }
*,*::before,*::after{box-sizing:border-box;}
a { text-decoration: none; color: inherit; }

/* ── NAVBAR ── */
.nav{display:flex;align-items:center;justify-content:space-between;padding:1rem 2.5rem;background:rgba(5,8,22,0.85);backdrop-filter:blur(16px);border-bottom:1px solid rgba(255,255,255,0.06);position:sticky;top:0;z-index:100}
.brand{display:flex;align-items:center;gap:.75rem;font-size:1.1rem;font-weight:700;color:var(--t)}
.bmark{width:32px;height:32px;border-radius:8px;background:linear-gradient(135deg,var(--p),var(--a));display:flex;align-items:center;justify-content:center;padding:4px}
.bmark img{width:100%;height:100%;object-fit:contain}
.nav-links{display:flex;gap:.5rem;align-items:center}
.nav-btn{
  padding:.4rem .9rem;border-radius:999px;font-size:.8rem;font-weight:600;
  background:var(--glass);border:1px solid var(--b);color:var(--t2);
  transition:all .25s var(--ease);
}
.nav-btn:hover{background:var(--card-hi);border-color:var(--cyan);color:var(--t);transform:translateY(-1px)}
.nav-btn.primary{background:var(--grad);color:#000;border:none;box-shadow:0 4px 16px rgba(0,212,255,0.3)}
  @media(max-width: 680px) {
    .nav{flex-direction:column; gap:0.8rem; padding:0.8rem 1.25rem}
    .nav-links{overflow-x:auto; width:100%; padding-bottom:0.5rem; justify-content:flex-start; -ms-overflow-style:none; scrollbar-width:none;}
    .nav-links::-webkit-scrollbar { display: none; }
    .t-hero { padding: 7.5rem 1rem 2rem; }
  }

/* ── TRANSLATOR UI ── */
.t-hero { text-align:center; padding: 4rem 1rem 2rem; }
.t-hero h1 { font-size: 2.5rem; font-weight: 800; margin-bottom: 1rem; background: linear-gradient(135deg, var(--p), var(--a)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
.t-hero p { color: var(--t2); max-width: 600px; margin: 0 auto; font-size: 1.1rem; }

.container { max-width: 1000px; margin: 0 auto; padding: 2rem; }
.t-panel { background: var(--card); border: 1px solid rgba(var(--p2), 0.2); border-radius: 20px; box-shadow: var(--glow); padding: 2rem; }

.t-grid { display: grid; grid-template-columns: 1fr auto 1fr; gap: 1.5rem; align-items: stretch; margin-bottom: 2rem; }
@media(max-width: 768px) { .t-grid { grid-template-columns: 1fr; } }

.t-col { display: flex; flex-direction: column; gap: 1rem; }

/* Custom Dropdown */
.lang-select-wrap { position: relative; }
.lang-btn { width: 100%; display: flex; align-items: center; justify-content: space-between; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); padding: 1rem; border-radius: 12px; cursor: pointer; color: var(--t); font-weight: 600; font-size: 1rem; transition: all 0.2s; }
.lang-btn:hover { background: rgba(255,255,255,0.1); border-color: var(--p); }
.lang-btn img { width: 28px; border-radius: 4px; box-shadow: 0 2px 5px rgba(0,0,0,0.5); margin-right: 10px; }
.lang-btn-left { display: flex; align-items: center; }

.lang-dropdown { position: absolute; top: 110%; left: 0; width: 100%; max-height: 350px; overflow-y: auto; background: #0a0f25; border: 1px solid var(--p); border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.8); z-index: 50; display: none; }
.lang-dropdown.show { display: block; animation: slideDown 0.2s ease forwards; }
@keyframes slideDown { from { opacity: 0; transform: translateY(-10px); } to { opacity: 1; transform: translateY(0); } }

.lang-search { width: 100%; padding: 1rem; background: transparent; border: none; border-bottom: 1px solid rgba(255,255,255,0.1); color: #fff; font-size: 1rem; outline: none; }
.lang-option { padding: 0.75rem 1rem; display: flex; align-items: center; gap: 10px; cursor: pointer; transition: 0.2s; border-bottom: 1px solid rgba(255,255,255,0.05); }
.lang-option:last-child { border-bottom: none; }
.lang-option:hover { background: rgba(var(--p2), 0.2); }
.lang-option img { width: 24px; border-radius: 4px; }

/* Text Areas */
.t-area { width: 100%; height: 250px; background: rgba(0,0,0,0.3); border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; padding: 1rem; color: #fff; font-size: 1.2rem; font-family: var(--f); resize: none; outline: none; transition: 0.2s; }
.t-area:focus { border-color: var(--p); box-shadow: 0 0 15px rgba(var(--p2), 0.2); }
.t-area::placeholder { color: var(--t3); }
#outputBox { background: rgba(var(--p2), 0.05); color: var(--p); font-weight: 500; }

.swap-btn { background: linear-gradient(135deg, var(--p), var(--a)); width: 50px; height: 50px; border-radius: 50%; display: flex; align-items: center; justify-content: center; cursor: pointer; border: none; color: #fff; font-size: 1.5rem; align-self: center; box-shadow: var(--glow); transition: 0.2s; }
.swap-btn:hover { transform: rotate(180deg) scale(1.1); }
@media(max-width: 768px) { .swap-btn { transform: rotate(90deg); margin: 0 auto; } .swap-btn:hover { transform: rotate(270deg) scale(1.1); } }

.action-row { display: flex; justify-content: center; margin-top: 2rem; }
.trans-btn { background: linear-gradient(135deg, var(--p), var(--a)); color: #fff; border: none; padding: 1rem 3rem; font-size: 1.2rem; font-weight: 700; border-radius: 999px; cursor: pointer; transition: 0.3s; box-shadow: var(--glow); display: flex; align-items: center; gap: 10px; }
.trans-btn:hover { transform: translateY(-3px) scale(1.05); box-shadow: 0 10px 25px rgba(var(--p2), 0.5); }
.trans-btn:active { transform: translateY(0) scale(0.95); }

/* Loader */
.loader { display: none; width: 20px; height: 20px; border: 3px solid rgba(255,255,255,0.3); border-top-color: #fff; border-radius: 50%; animation: spin 1s infinite linear; }
@keyframes spin { 100% { transform: rotate(360deg); } }

/* Phrase Grid */
.phrases-panel { margin-top: 3rem; background: rgba(5,8,22,0.6); padding: 2.5rem; border-radius: 20px; border: 1px solid rgba(255,255,255,0.08); }
.phrases-panel h2 { text-align: center; font-size: 2rem; color: #fff; margin-bottom: 0.5rem; }
.phrases-panel p { text-align: center; color: var(--p); margin-bottom: 2rem; font-weight: 600; }
.phrase-category { margin-bottom: 2.5rem; }
.phrase-category h3 { color: var(--t2); font-size: 1.2rem; margin-bottom: 1rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem; }
.phrase-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 1rem; }
.phrase-btn { background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); color: var(--t); padding: 1rem; border-radius: 12px; font-size: 0.95rem; font-weight: 600; text-align: left; cursor: pointer; transition: all 0.2s var(--ease); font-family: var(--f); display:flex; align-items:center; line-height: 1.4; }
.phrase-btn::before { content: '💬'; margin-right: 8px; filter: grayscale(1); opacity: 0.5; transition: 0.2s; }
.phrase-btn:hover { background: rgba(var(--p2), 0.1); border-color: var(--p); transform: translateY(-3px); box-shadow: 0 5px 15px rgba(var(--p2), 0.2); }
.phrase-btn:hover::before { filter: grayscale(0); opacity: 1; }
@media(max-width:600px) { .phrases-panel { padding: 1.5rem; } .phrase-grid { grid-template-columns: 1fr; } }

/* ── FOOTER ── */
footer{border-top:1px solid rgba(255,255,255,.06);padding:2rem 1.5rem 1.5rem; text-align:center;color:var(--t3);font-size:.8rem;margin-top:2rem}

/* AD SLOT CSS */
.ad-slot-container {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 20px auto;
  width: 100%;
  max-width: 1200px;
  min-height: 0;
  overflow: hidden;
}
.ad-slot-container:empty {
  display: none;
  margin: 0;
}

@media (max-width: 768px) {
  .hide-on-mobile { display: none !important; }
}
@media (max-width: 1024px) {
  .hide-on-tab { display: none !important; }
}

.ad-sticky-bottom {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  z-index: 1000;
  background: rgba(5,8,22,0.95);
  border-top: 1px solid rgba(0,212,255,0.2);
  margin: 0;
}
</style>
</head>
<body>

<nav class="nav" id="nav">
  <a class="brand" href="/home/main.html">
    <div class="bmark"><img src="/home/assets/logo.png" alt="PO ZipCode Global Logo" loading="lazy"></div>
    <span>PO ZipCode Global</span>
  </a>
  <div class="nav-links">
    <a class="nav-btn" style="color:var(--p); border-color:var(--p)" href="/pages/translate.html">Translator</a>
    <a class="nav-btn" href="/pages/blog.html">Blog</a>
    <a class="nav-btn" href="/home/main.html">&#8592; All Countries</a>
    <div id="google_translate_element"></div>
  </div>
</nav>

  <!-- AD SLOT 1: TOP HEADER (PC, TAB, MOBILE) -->
  <div class="ad-slot-container" id="ad-slot-1">
    <!-- Insert AdSense Code Here (e.g. data-ad-format="auto"). Collapses if empty. -->
  </div>
  
  <script type="text/javascript">
function googleTranslateElementInit() {
  new google.translate.TranslateElement({pageLanguage: 'en', layout: google.translate.TranslateElement.InlineLayout.SIMPLE}, 'google_translate_element');
}
</script>
<script type="text/javascript" src="https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit" async defer></script>

<div class="t-hero">
  <h1>Global Language Translator</h1>
  <p>Translate text instantly between 120+ languages representing our global directory. Free, fast, and unlimited.</p>
</div>

<div class="container">
  <div class="t-panel">
    <div class="t-grid">
      
      <!-- FROM COLUMN -->
      <div class="t-col">
        <div class="lang-select-wrap" id="fromWrap">
          <div class="lang-btn" onclick="toggleDrop('fromDrop')">
            <div class="lang-btn-left" id="fromDisplay">
              <img src="https://flagcdn.com/w40/in.png" alt="India">
              <span>Telugu (India) (te)</span>
            </div>
            <span>▼</span>
          </div>
          <div class="lang-dropdown" id="fromDrop">
            <input type="text" class="lang-search" placeholder="Search language or country..." onkeyup="filterLangs(this)">
            <div class="lang-list" id="fromList">
              <!-- OPTIONS INJECTED HERE -->
              ___OPTIONS_HTML___
            </div>
          </div>
        </div>
        <textarea class="t-area" id="inputBox" placeholder="Type text here to translate..."></textarea>
      </div>

      <!-- SWAP BUTTON -->
      <button class="swap-btn" onclick="swapLangs()">⇄</button>

      <!-- TO COLUMN -->
      <div class="t-col">
        <div class="lang-select-wrap" id="toWrap">
          <div class="lang-btn" onclick="toggleDrop('toDrop')">
            <div class="lang-btn-left" id="toDisplay">
              <img src="https://flagcdn.com/w40/jp.png" alt="Japan">
              <span>Japan (ja)</span>
            </div>
            <span>▼</span>
          </div>
          <div class="lang-dropdown" id="toDrop">
            <input type="text" class="lang-search" placeholder="Search language or country..." onkeyup="filterLangs(this)">
            <div class="lang-list" id="toList">
              <!-- OPTIONS INJECTED HERE -->
              ___OPTIONS_HTML___
            </div>
          </div>
        </div>
          <textarea class="t-area" id="outputBox" placeholder="Translation will appear here..." readonly></textarea>
          <div id="pronunciationBox" style="display:none; margin-top: 15px; color: var(--p); font-size: 1.1rem; background: rgba(0,212,255,0.1); padding: 12px 15px; border-radius: 8px; border-left: 4px solid var(--p); font-weight: 500; letter-spacing: 0.5px; box-shadow: 0 4px 10px rgba(0,0,0,0.3);"></div>
        </div>
      
    </div>

    <!-- AD SLOT: TRANSLATOR BOTTOM -->
    <div class="ad-slot-container" id="ad-translator-bottom">
      <!-- Insert AdSense Code Here (e.g. data-ad-format="auto"). Collapses if empty. -->
    </div>
    
    <div class="action-row">
      <button class="trans-btn" onclick="doTranslate()">
        <span id="btnText">Translate Now</span>
        <div class="loader" id="loader"></div>
      </button>
    </div>
  </div>

  <div class="phrases-panel">
    <h2>Daily Life & Travel Phrases</h2>
    <p>Click any phrase below to instantly translate it into your selected language!</p>
    
    <div class="phrase-category">
      <h3>👋 Greetings & Basics</h3>
      <div class="phrase-grid">
        <button class="phrase-btn" onclick="quickTranslate('Hello')">Hello</button>
        <button class="phrase-btn" onclick="quickTranslate('How are you?')">How are you?</button>
        <button class="phrase-btn" onclick="quickTranslate('I am fine, thank you')">I am fine, thank you</button>
        <button class="phrase-btn" onclick="quickTranslate('What is your name?')">What is your name?</button>
        <button class="phrase-btn" onclick="quickTranslate('My name is...')">My name is...</button>
        <button class="phrase-btn" onclick="quickTranslate('Yes')">Yes</button>
        <button class="phrase-btn" onclick="quickTranslate('No')">No</button>
        <button class="phrase-btn" onclick="quickTranslate('Please')">Please</button>
        <button class="phrase-btn" onclick="quickTranslate('Thank you')">Thank you</button>
        <button class="phrase-btn" onclick="quickTranslate('You are welcome')">You are welcome</button>
        <button class="phrase-btn" onclick="quickTranslate('Excuse me')">Excuse me</button>
        <button class="phrase-btn" onclick="quickTranslate('I am sorry')">I am sorry</button>
        <button class="phrase-btn" onclick="quickTranslate('Good morning')">Good morning</button>
        <button class="phrase-btn" onclick="quickTranslate('Good night')">Good night</button>
        <button class="phrase-btn" onclick="quickTranslate('Goodbye')">Goodbye</button>
      </div>
    </div>

    <div class="phrase-category">
      <h3>✈️ Travel & Directions</h3>
      <div class="phrase-grid">
        <button class="phrase-btn" onclick="quickTranslate('Where is the restroom?')">Where is the restroom?</button>
        <button class="phrase-btn" onclick="quickTranslate('How much does this cost?')">How much does this cost?</button>
        <button class="phrase-btn" onclick="quickTranslate('I would like to buy this')">I would like to buy this</button>
        <button class="phrase-btn" onclick="quickTranslate('Where is the airport?')">Where is the airport?</button>
        <button class="phrase-btn" onclick="quickTranslate('I need a taxi')">I need a taxi</button>
        <button class="phrase-btn" onclick="quickTranslate('Where is the train station?')">Where is the train station?</button>
        <button class="phrase-btn" onclick="quickTranslate('Can you help me?')">Can you help me?</button>
        <button class="phrase-btn" onclick="quickTranslate('I am lost')">I am lost</button>
        <button class="phrase-btn" onclick="quickTranslate('Turn left')">Turn left</button>
        <button class="phrase-btn" onclick="quickTranslate('Turn right')">Turn right</button>
        <button class="phrase-btn" onclick="quickTranslate('Go straight')">Go straight</button>
        <button class="phrase-btn" onclick="quickTranslate('Stop here please')">Stop here please</button>
      </div>
    </div>

    <div class="phrase-category">
      <h3>🏨 Food & Accommodation</h3>
      <div class="phrase-grid">
        <button class="phrase-btn" onclick="quickTranslate('I am hungry')">I am hungry</button>
        <button class="phrase-btn" onclick="quickTranslate('I am thirsty')">I am thirsty</button>
        <button class="phrase-btn" onclick="quickTranslate('Water, please')">Water, please</button>
        <button class="phrase-btn" onclick="quickTranslate('The menu, please')">The menu, please</button>
        <button class="phrase-btn" onclick="quickTranslate('It is delicious!')">It is delicious!</button>
        <button class="phrase-btn" onclick="quickTranslate('The bill, please')">The bill, please</button>
        <button class="phrase-btn" onclick="quickTranslate('I have a reservation')">I have a reservation</button>
        <button class="phrase-btn" onclick="quickTranslate('Do you have a room?')">Do you have a room?</button>
        <button class="phrase-btn" onclick="quickTranslate('Is breakfast included?')">Is breakfast included?</button>
      </div>
    </div>

    <div class="phrase-category">
      <h3>🚨 Emergency</h3>
      <div class="phrase-grid">
        <button class="phrase-btn" onclick="quickTranslate('I need a doctor')">I need a doctor</button>
        <button class="phrase-btn" onclick="quickTranslate('Where is the hospital?')">Where is the hospital?</button>
        <button class="phrase-btn" onclick="quickTranslate('Call the police!')">Call the police!</button>
        <button class="phrase-btn" onclick="quickTranslate('I lost my passport')">I lost my passport</button>
        <button class="phrase-btn" onclick="quickTranslate('I do not understand')">I do not understand</button>
        <button class="phrase-btn" onclick="quickTranslate('Do you speak English?')">Do you speak English?</button>
      </div>
    </div>
  </div>
  
  <!-- AD SLOT 3: ABOVE FOOTER (PC, TAB) - Hides on Mobile -->
  <div class="ad-slot-container hide-on-mobile" id="ad-slot-3">
    <!-- Insert AdSense Code Here -->
  </div>
  
  <!-- AD SLOT 4: DEEP CONTENT (PC ONLY) - Hides on Tab, Mobile -->
  <div class="ad-slot-container hide-on-tab hide-on-mobile" id="ad-slot-4">
    <!-- Insert AdSense Code Here -->
  </div>
  
  <!-- AD SLOT 5: STICKY BOTTOM ANCHOR (PC ONLY) - Hides on Tab, Mobile -->
  <div class="ad-slot-container hide-on-tab hide-on-mobile ad-sticky-bottom" id="ad-slot-5">
    <!-- Insert AdSense Code Here -->
  </div>
</div>

<footer>
  <p>© 2026 PO ZipCode Global. Made for the world.</p>
</footer>

<script>
// State
let fromLang = 'te';
let fromFlag = 'in';
let fromName = 'Telugu (India)';

let toLang = 'ja';
let toFlag = 'jp';
let toName = 'Japan';

// Close dropdowns on outside click
document.addEventListener('click', e => {
  if(!e.target.closest('#fromWrap')) document.getElementById('fromDrop').classList.remove('show');
  if(!e.target.closest('#toWrap')) document.getElementById('toDrop').classList.remove('show');
});

function toggleDrop(id) {
  document.getElementById(id).classList.toggle('show');
}

function filterLangs(input) {
  let filter = input.value.toLowerCase();
  let list = input.nextElementSibling;
  let options = list.getElementsByClassName('lang-option');
  for (let opt of options) {
    let txt = opt.textContent || opt.innerText;
    opt.style.display = txt.toLowerCase().indexOf(filter) > -1 ? "flex" : "none";
  }
}

// Attach click events to options
document.querySelectorAll('#fromList .lang-option').forEach(opt => {
  opt.addEventListener('click', function() {
    fromLang = this.getAttribute('data-lang');
    fromFlag = this.getAttribute('data-flag');
    fromName = this.getAttribute('data-name');
    document.getElementById('fromDisplay').innerHTML = `<img src="https://flagcdn.com/w40/${fromFlag}.png"><span>${fromName} (${fromLang})</span>`;
    document.getElementById('fromDrop').classList.remove('show');
  });
});

document.querySelectorAll('#toList .lang-option').forEach(opt => {
  opt.addEventListener('click', function() {
    toLang = this.getAttribute('data-lang');
    toFlag = this.getAttribute('data-flag');
    toName = this.getAttribute('data-name');
    document.getElementById('toDisplay').innerHTML = `<img src="https://flagcdn.com/w40/${toFlag}.png"><span>${toName} (${toLang})</span>`;
    document.getElementById('toDrop').classList.remove('show');
  });
});
function quickTranslate(text) {
  document.getElementById('inputBox').value = text;
  document.getElementById('outputBox').value = '';
  window.scrollTo({ top: document.querySelector('.t-panel').offsetTop - 20, behavior: 'smooth' });
  doTranslate();
}

function swapLangs() {
  // Swap vars
  let tL = fromLang, tF = fromFlag, tN = fromName;
  fromLang = toLang; fromFlag = toFlag; fromName = toName;
  toLang = tL; toFlag = tF; toName = tN;
  
  // Update Displays
  document.getElementById('fromDisplay').innerHTML = `<img src="https://flagcdn.com/w40/${fromFlag}.png"><span>${fromName} (${fromLang})</span>`;
  document.getElementById('toDisplay').innerHTML = `<img src="https://flagcdn.com/w40/${toFlag}.png"><span>${toName} (${toLang})</span>`;
  
  // Swap text
  let iBox = document.getElementById('inputBox');
  let oBox = document.getElementById('outputBox');
  let temp = iBox.value;
  iBox.value = oBox.value;
  oBox.value = temp;
  document.getElementById('pronunciationBox').style.display = 'none';
}

// The Translation API Call
async function doTranslate() {
  const text = document.getElementById('inputBox').value.trim();
  if(!text) return;
  
  const btnText = document.getElementById('btnText');
  const loader = document.getElementById('loader');
  btnText.style.display = 'none';
  loader.style.display = 'block';
  document.getElementById('outputBox').value = 'Translating...';
  document.getElementById('pronunciationBox').style.display = 'none';
  
  try {
    // Using Google Translate free undocumented client API
    const url = `https://translate.googleapis.com/translate_a/single?client=gtx&sl=${fromLang}&tl=${toLang}&dt=t&dt=rm&q=${encodeURIComponent(text)}`;
    const res = await fetch(url);
    const data = await res.json();
    
    // data[0] contains array of translated sentences
    let translated = '';
    for(let i=0; i<data[0].length; i++){
      if (data[0][i][0]) {
        translated += data[0][i][0];
      }
    }
    document.getElementById('outputBox').value = translated;

    // Handle pronunciation (Romanization)
    let pron = '';
    const lastSeg = data[0][data[0].length - 1];
    if (lastSeg && lastSeg.length >= 3 && lastSeg[2]) {
      pron = lastSeg[2]; // Target language romanization
    } else if (lastSeg && lastSeg.length >= 4 && lastSeg[3] && fromLang !== 'en') {
      // In some cases (like translating FROM english), the target pronunciation might be at index 3 or it might be English
      pron = lastSeg[3]; 
    }
    
    const pBox = document.getElementById('pronunciationBox');
    let pHTML = '';
      if (pron && toLang !== 'en') {
        pHTML = '🗣️ <strong>How to Read (Pronunciation):</strong> ' + pron;
        pBox.innerHTML = pHTML;
        pBox.style.display = 'block';
      }

  } catch(e) {
    document.getElementById('outputBox').value = 'Error translating. Please try again.';
    console.error(e);
  }
  
  btnText.style.display = 'block';
  loader.style.display = 'none';
}
</script>

</body>
</html>
"""

final_html = HTML_TEMPLATE.replace("___OPTIONS_HTML___", options_html)

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pages", "translate.html")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(final_html)

print(f"Successfully generated {out_path} with {len(generate_pages.COUNTRIES) + len(EXTRA_LANGS)} languages!")
