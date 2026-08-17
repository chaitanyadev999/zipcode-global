
// Auto clean cache every 24 hours
(function() {
    try {
        const lastClear = localStorage.getItem('last_cache_clear');
        const now = Date.now();
        if (!lastClear || now - parseInt(lastClear) > 86400000) {
            localStorage.clear();
            sessionStorage.clear();
            localStorage.setItem('last_cache_clear', now.toString());
            window.location.reload(true);
        }
    } catch(e) {}
})();

function getBasePath() {
    const path = window.location.pathname;
    const idx = path.indexOf("/pages/");
    return idx !== -1 ? path.substring(0, idx + 1) : "/";
}
(function() {
  'use strict';
  const SCRIPT_URL = document.currentScript ? document.currentScript.src : getBasePath() + 'pages/shared_pseo.js';

  // ====================================================
  // DYNAMIC COUNTRY LOADER - reads ?code=XX from URL
  // ====================================================
  const COUNTRY_DB = {
    'IN':{name:'India',lat:20.5937,lon:78.9629,region:'Asia'},
    'US':{name:'United States',lat:37.0902,lon:-95.7129,region:'Americas'},
    'AD':{name:'Andorra',lat:42.5063,lon:1.5218,region:'Europe'},
    'AE':{name:'United Arab Emirates',lat:23.4241,lon:53.8478,region:'Asia'},
    'AI':{name:'Anguilla',lat:18.2206,lon:-63.0686,region:'Americas'},
    'AL':{name:'Albania',lat:41.1533,lon:20.1683,region:'Europe'},
    'AR':{name:'Argentina',lat:-38.4161,lon:-63.6167,region:'Americas'},
    'AS':{name:'American Samoa',lat:-14.2710,lon:-170.1322,region:'Oceania'},
    'AT':{name:'Austria',lat:47.5162,lon:14.5501,region:'Europe'},
    'AU':{name:'Australia',lat:-25.2744,lon:133.7751,region:'Oceania'},
    'AX':{name:'Aland Islands',lat:60.1785,lon:19.9156,region:'Europe'},
    'AZ':{name:'Azerbaijan',lat:40.1431,lon:47.5769,region:'Asia'},
    'BD':{name:'Bangladesh',lat:23.6850,lon:90.3563,region:'Asia'},
    'BE':{name:'Belgium',lat:50.5039,lon:4.4699,region:'Europe'},
    'BG':{name:'Bulgaria',lat:42.7339,lon:25.4858,region:'Europe'},
    'BM':{name:'Bermuda',lat:32.3078,lon:-64.7505,region:'Americas'},
    'BR':{name:'Brazil',lat:-14.2350,lon:-51.9253,region:'Americas'},
    'BY':{name:'Belarus',lat:53.7098,lon:27.9534,region:'Europe'},
    'CA':{name:'Canada',lat:56.1304,lon:-106.3468,region:'Americas'},
    'CC':{name:'Cocos Islands',lat:-12.1642,lon:96.8710,region:'Oceania'},
    'CH':{name:'Switzerland',lat:46.8182,lon:8.2275,region:'Europe'},
    'CL':{name:'Chile',lat:-35.6751,lon:-71.5430,region:'Americas'},
    'CN':{name:'China',lat:35.8617,lon:104.1954,region:'Asia'},
    'CO':{name:'Colombia',lat:4.5709,lon:-74.2973,region:'Americas'},
    'CR':{name:'Costa Rica',lat:9.7489,lon:-83.7534,region:'Americas'},
    'CX':{name:'Christmas Island',lat:-10.4475,lon:105.6904,region:'Oceania'},
    'CY':{name:'Cyprus',lat:35.1264,lon:33.4299,region:'Europe'},
    'CZ':{name:'Czech Republic',lat:49.8175,lon:15.4730,region:'Europe'},
    'DE':{name:'Germany',lat:51.1657,lon:10.4515,region:'Europe'},
    'DK':{name:'Denmark',lat:56.2639,lon:9.5018,region:'Europe'},
    'DO':{name:'Dominican Republic',lat:18.7357,lon:-70.1627,region:'Americas'},
    'DZ':{name:'Algeria',lat:28.0339,lon:1.6596,region:'Africa'},
    'EC':{name:'Ecuador',lat:-1.8312,lon:-78.1834,region:'Americas'},
    'EE':{name:'Estonia',lat:58.5953,lon:25.0136,region:'Europe'},
    'ES':{name:'Spain',lat:40.4637,lon:-3.7492,region:'Europe'},
    'FI':{name:'Finland',lat:61.9241,lon:25.7482,region:'Europe'},
    'FK':{name:'Falkland Islands',lat:-51.7963,lon:-59.5236,region:'Americas'},
    'FM':{name:'Micronesia',lat:7.4256,lon:150.5508,region:'Oceania'},
    'FO':{name:'Faroe Islands',lat:61.8926,lon:-6.9118,region:'Europe'},
    'FR':{name:'France',lat:46.2276,lon:2.2137,region:'Europe'},
    'GB':{name:'United Kingdom',lat:55.3781,lon:-3.4360,region:'Europe'},
    'GF':{name:'French Guiana',lat:3.9339,lon:-53.1258,region:'Americas'},
    'GG':{name:'Guernsey',lat:49.4657,lon:-2.5853,region:'Europe'},
    'GI':{name:'Gibraltar',lat:36.1408,lon:-5.3536,region:'Europe'},
    'GL':{name:'Greenland',lat:71.7069,lon:-42.6043,region:'Americas'},
    'GP':{name:'Guadeloupe',lat:16.2650,lon:-61.5510,region:'Americas'},
    'GS':{name:'South Georgia',lat:-54.4296,lon:-36.5879,region:'Americas'},
    'GT':{name:'Guatemala',lat:15.7835,lon:-90.2308,region:'Americas'},
    'GU':{name:'Guam',lat:13.4443,lon:144.7937,region:'Oceania'},
    'HK':{name:'Hong Kong',lat:22.3193,lon:114.1694,region:'Asia'},
    'HM':{name:'Heard Island',lat:-53.0818,lon:73.5042,region:'Oceania'},
    'HN':{name:'Honduras',lat:15.2000,lon:-86.2419,region:'Americas'},
    'HR':{name:'Croatia',lat:45.1000,lon:15.2000,region:'Europe'},
    'HT':{name:'Haiti',lat:18.9712,lon:-72.2852,region:'Americas'},
    'HU':{name:'Hungary',lat:47.1625,lon:19.5033,region:'Europe'},
    'ID':{name:'Indonesia',lat:-0.7893,lon:113.9213,region:'Asia'},
    'IE':{name:'Ireland',lat:53.1424,lon:-7.6921,region:'Europe'},
    'IM':{name:'Isle of Man',lat:54.2361,lon:-4.5481,region:'Europe'},
    'IO':{name:'British Indian Ocean Territory',lat:-6.3432,lon:71.8765,region:'Asia'},
    'IS':{name:'Iceland',lat:64.9631,lon:-19.0208,region:'Europe'},
    'IT':{name:'Italy',lat:41.8719,lon:12.5674,region:'Europe'},
    'JE':{name:'Jersey',lat:49.2144,lon:-2.1313,region:'Europe'},
    'JP':{name:'Japan',lat:36.2048,lon:138.2529,region:'Asia'},
    'KE':{name:'Kenya',lat:-0.0236,lon:37.9062,region:'Africa'},
    'KR':{name:'South Korea',lat:35.9078,lon:127.7669,region:'Asia'},
    'LI':{name:'Liechtenstein',lat:47.1660,lon:9.5554,region:'Europe'},
    'LK':{name:'Sri Lanka',lat:7.8731,lon:80.7718,region:'Asia'},
    'LT':{name:'Lithuania',lat:55.1694,lon:23.8813,region:'Europe'},
    'LU':{name:'Luxembourg',lat:49.8153,lon:6.1296,region:'Europe'},
    'LV':{name:'Latvia',lat:56.8796,lon:24.6032,region:'Europe'},
    'MA':{name:'Morocco',lat:31.7917,lon:-7.0926,region:'Africa'},
    'MC':{name:'Monaco',lat:43.7384,lon:7.4246,region:'Europe'},
    'MD':{name:'Moldova',lat:47.4116,lon:28.3699,region:'Europe'},
    'MH':{name:'Marshall Islands',lat:7.1315,lon:171.1845,region:'Oceania'},
    'MK':{name:'North Macedonia',lat:41.6086,lon:21.7453,region:'Europe'},
    'MO':{name:'Macao',lat:22.1987,lon:113.5439,region:'Asia'},
    'MP':{name:'Northern Mariana Islands',lat:17.3308,lon:145.3847,region:'Oceania'},
    'MQ':{name:'Martinique',lat:14.6415,lon:-61.0242,region:'Americas'},
    'MT':{name:'Malta',lat:35.9375,lon:14.3754,region:'Europe'},
    'MW':{name:'Malawi',lat:-13.2543,lon:34.3015,region:'Africa'},
    'MX':{name:'Mexico',lat:23.6345,lon:-102.5528,region:'Americas'},
    'MY':{name:'Malaysia',lat:4.2105,lon:101.9758,region:'Asia'},
    'NC':{name:'New Caledonia',lat:-20.9043,lon:165.6180,region:'Oceania'},
    'NF':{name:'Norfolk Island',lat:-29.0408,lon:167.9547,region:'Oceania'},
    'NL':{name:'Netherlands',lat:52.1326,lon:5.2913,region:'Europe'},
    'NO':{name:'Norway',lat:60.4720,lon:8.4689,region:'Europe'},
    'NR':{name:'Nauru',lat:-0.5228,lon:166.9315,region:'Oceania'},
    'NU':{name:'Niue',lat:-19.0544,lon:-169.8672,region:'Oceania'},
    'NZ':{name:'New Zealand',lat:-40.9006,lon:174.8860,region:'Oceania'},
    'PA':{name:'Panama',lat:8.5380,lon:-80.7821,region:'Americas'},
    'PE':{name:'Peru',lat:-9.1900,lon:-75.0152,region:'Americas'},
    'PF':{name:'French Polynesia',lat:-17.6797,lon:-149.4068,region:'Oceania'},
    'PH':{name:'Philippines',lat:12.8797,lon:121.7740,region:'Asia'},
    'PK':{name:'Pakistan',lat:30.3753,lon:69.3451,region:'Asia'},
    'PL':{name:'Poland',lat:51.9194,lon:19.1451,region:'Europe'},
    'PM':{name:'Saint Pierre and Miquelon',lat:46.8852,lon:-56.3159,region:'Americas'},
    'PN':{name:'Pitcairn',lat:-24.7036,lon:-127.4393,region:'Oceania'},
    'PR':{name:'Puerto Rico',lat:18.2208,lon:-66.5901,region:'Americas'},
    'PT':{name:'Portugal',lat:39.3999,lon:-8.2245,region:'Europe'},
    'PW':{name:'Palau',lat:7.5150,lon:134.5825,region:'Oceania'},
    'RE':{name:'Reunion',lat:-21.1151,lon:55.5364,region:'Africa'},
    'RO':{name:'Romania',lat:45.9432,lon:24.9668,region:'Europe'},
    'RS':{name:'Serbia',lat:44.0165,lon:21.0059,region:'Europe'},
    'RU':{name:'Russia',lat:61.5240,lon:105.3188,region:'Europe'},
    'SE':{name:'Sweden',lat:60.1282,lon:18.6435,region:'Europe'},
    'SG':{name:'Singapore',lat:1.3521,lon:103.8198,region:'Asia'},
    'SI':{name:'Slovenia',lat:46.1512,lon:14.9955,region:'Europe'},
    'SJ':{name:'Svalbard and Jan Mayen',lat:77.5536,lon:23.6703,region:'Europe'},
    'SK':{name:'Slovakia',lat:48.6690,lon:19.6990,region:'Europe'},
    'SM':{name:'San Marino',lat:43.9424,lon:12.4578,region:'Europe'},
    'TC':{name:'Turks and Caicos Islands',lat:21.6940,lon:-71.7979,region:'Americas'},
    'TH':{name:'Thailand',lat:15.8700,lon:100.9925,region:'Asia'},
    'TR':{name:'Turkey',lat:38.9637,lon:35.2433,region:'Asia'},
    'UA':{name:'Ukraine',lat:48.3794,lon:31.1656,region:'Europe'},
    'UY':{name:'Uruguay',lat:-32.5228,lon:-55.7658,region:'Americas'},
    'VA':{name:'Vatican City',lat:41.9029,lon:12.4534,region:'Europe'},
    'VI':{name:'US Virgin Islands',lat:18.3358,lon:-64.8963,region:'Americas'},
    'WF':{name:'Wallis and Futuna',lat:-13.7687,lon:-177.1561,region:'Oceania'},
    'WS':{name:'Samoa',lat:-13.7590,lon:-172.1046,region:'Oceania'},
    'YT':{name:'Mayotte',lat:-12.8275,lon:45.1662,region:'Africa'},
    'ZA':{name:'South Africa',lat:-30.5595,lon:22.9375,region:'Africa'}
  };

  // Read URL param - special redirect for IN and US
  let urlCode = '';
  let isPseo = false;

  if (window.PSEO_COUNTRY) {
    // We are in a generated PSEO page
    isPseo = true;
    urlCode = window.PSEO_COUNTRY.toLowerCase();
  } else {
    urlCode = new URLSearchParams(window.location.search).get('code');
    if (!urlCode) {
      const match = window.location.pathname.match(/\/pages\/([a-zA-Z0-9-]+)\.html/);
      if (match && match[1] && match[1] !== 'layout' && match[1] !== 'country-template') {
        const urlName = match[1].toLowerCase().replace(/-/g, ' ');
        
        // Special fallbacks for India and USA
        if (urlName === 'usa') { urlCode = 'us'; }
        else if (urlName === 'india') { urlCode = 'in'; }
        else if (urlName === 'united states') { urlCode = 'us'; }
        else {
            for (const [code, meta] of Object.entries(COUNTRY_DB)) {
              if (meta.name.toLowerCase() === urlName || code.toLowerCase() === urlName) {
                urlCode = code.toLowerCase();
                break;
              }
            }
        }
      }
    }
  }

  if (!urlCode) {
    if (!isPseo && (window.location.pathname.includes('/pages/') || window.location.pathname.includes('\\pages\\'))) {
       // fallback for india if on india.html but not matched
       urlCode = 'in';
    } else {
       urlCode = 'in';
    }
  }

  urlCode = urlCode.toUpperCase();
  const META = COUNTRY_DB[urlCode];
  if (!META) {
    console.error('Unknown country code: ' + urlCode);
  }

  // Build COUNTRY object skeleton (states filled async)
  const CDN_RAW = 'https://raw.githubusercontent.com/chaitanyadev999/pincode-dataindia/main/';
  const COUNTRY = {
    name: META.name,
    code: urlCode.toUpperCase(),
    flagCode: urlCode.toLowerCase(),
    subtitle: META.region + ' \u00b7 Postal Code Directory \u00b7 PO ZipCode Global',
    lat: META.lat,
    lon: META.lon,
    dataPath: CDN_RAW,
    dataPrefix: 'world/' + urlCode.toUpperCase() + '/',
    states: []
  };
  if (urlCode === 'IN') {
    COUNTRY.dataPath = 'https://raw.githubusercontent.com/chaitanyadev999/pincode-dataindia/main/';
    COUNTRY.dataPrefix = '';
  }


  // Async load states from GitHub Contents API
  async function loadStates() {
    try {
      let apiUrl = 'https://api.github.com/repos/chaitanyadev999/pincode-dataindia/contents/world/' + COUNTRY.code; if (COUNTRY.code === 'IN') apiUrl = 'https://api.github.com/repos/chaitanyadev999/pincode-dataindia/contents/'; const resp = await fetch(apiUrl);
      const files = await resp.json();
      if (Array.isArray(files)) {
        COUNTRY.states = files
          .filter(f => f.name.endsWith('.json') && f.name !== 'pincode-map.json' && f.name !== 'package.json' && f.name !== 'data.json')
          .map(f => ({ name: f.name.replace('.json', '').replace(/-/g, ' '), file: f.name }));
      }
    } catch (e) {
      COUNTRY.states = [{ name: 'All Regions', file: 'data.json' }];
    }
    if (COUNTRY.states.length === 0) {
      COUNTRY.states = [{ name: 'Coming Soon', file: '' }];
    }
    initPage();
  }

  const $ = (id) => document.getElementById(id);
  const dataCache = new Map();

  let map = null;
  let mapMarkers = [];
  let mapInitialized = false;

  // Toast
  function showToast(msg, type) {
    const c = $('toastContainer');
    const t = document.createElement('div');
    t.className = 'toast ' + (type || 'info');
    const icon = type === 'success' ? '\u2713' : type === 'error' ? '\u2715' : '\u2139';
    t.innerHTML = '<span class="toast-icon">' + icon + '</span><span>' + msg + '</span>';
    c.appendChild(t);
    setTimeout(() => t.classList.add('show'), 10);
    setTimeout(() => { t.classList.remove('show'); setTimeout(() => t.remove(), 400); }, 3500);
  }

  // Copy
  function copyPin(text) {
    if (navigator.clipboard) {
      navigator.clipboard.writeText(text).then(() => showToast('Copied: ' + text, 'success'));
    }
  }

  // Scroll nav
  let scrollTimeout;
  window.addEventListener('scroll', () => {
    if (scrollTimeout) return;
    scrollTimeout = setTimeout(() => {
      $('countryNav').classList.toggle('scrolled', window.scrollY > 50);
      scrollTimeout = null;
    }, 10);
  }, { passive: true });

  function initPage() {
    if (!window.PSEO_CITY) {
      // Set page title and meta dynamically for normal pages
      document.title = COUNTRY.name + ' Postal Codes \u2014 PO ZipCode Global';
      const ogTitle = document.querySelector('meta[property="og:title"]');
      if (ogTitle) ogTitle.content = COUNTRY.name + ' Postal Codes \u2014 PO ZipCode Global';
      const ogDesc = document.querySelector('meta[property="og:description"]');
      if (ogDesc) ogDesc.content = 'Find any postal code in ' + COUNTRY.name + '. ' + COUNTRY.states.length + ' regions. Instant lookup with interactive map.';
    }

    // Init hero with flagcdn.com image
    $('heroFlag').innerHTML = '<img src="https://flagcdn.com/w160/' + COUNTRY.flagCode + '.png" alt="' + COUNTRY.name + ' Flag" style="width:120px;height:auto;border-radius:10px;box-shadow:0 8px 32px rgba(0,0,0,0.6);display:inline-block;"/>';
    
    if (window.PSEO_CITY) {
      const toTitleCase = (str) => {
        if (!str) return '';
        return str.replace(/\w\S*/g, t => t.charAt(0).toUpperCase() + t.substr(1).toLowerCase());
      };
      const cityStr = window.PSEO_CITY ? toTitleCase(window.PSEO_CITY) + ', ' : '';
      const stateStr = window.PSEO_STATE_LABEL ? toTitleCase(window.PSEO_STATE_LABEL) : '';
      $('heroTitle').textContent = cityStr + stateStr + (stateStr ? ' - ' : '') + COUNTRY.name;
      $('heroSubtitle').textContent = 'List of all post offices and postal codes';
      $('statesTitle').textContent = 'Post Offices in ' + window.PSEO_CITY;
    } else {
      $('heroTitle').textContent = COUNTRY.name;
      $('heroSubtitle').textContent = COUNTRY.subtitle;
      $('statesTitle').textContent = COUNTRY.name + ' \u2014 States & Regions';
    }
    
    $('year').textContent = new Date().getFullYear();

    // Stats
    $('heroStats').innerHTML =
      '<div class="stat"><span class="stat-num">' + COUNTRY.states.length + '</span><span class="stat-label">Regions</span></div>' +
      '<div class="stat"><span class="stat-num">' + COUNTRY.code + '</span><span class="stat-label">Country Code</span></div>' +
      '<div class="stat"><span class="stat-num">' + META.region + '</span><span class="stat-label">Continent</span></div>';

    renderStates();
  }

  // Render states
  function renderStates() {
    $('statesGrid').innerHTML = COUNTRY.states.map((s, i) =>
      '<button class="state-btn" data-file="' + s.file + '" data-name="' + s.name + '" style="transition-delay:' + Math.min(i, 20) * 15 + 'ms">' + s.name + '</button>'
    ).join('');

    document.querySelectorAll('.state-btn').forEach(btn => {
      btn.addEventListener('click', async () => {
        const file = btn.dataset.file;
        const name = btn.dataset.name;
        const url = COUNTRY.dataPath + COUNTRY.dataPrefix + file;

        btn.classList.add('loading');
        btn.textContent = '⏳ Loading...';

        try {
          let data;
          if (dataCache.has(url)) {
            data = dataCache.get(url);
          } else {
            const res = await fetch(url);
            if (!res.ok) throw new Error('Failed');
            data = await res.json();
            dataCache.set(url, data);
          }

          const query = $('searchInput').value.trim();
          let results = data;
          if (query) {
            const lowerQuery = query.toLowerCase();
            const fields = ['pincode', 'ZipCode', 'zipcode', 'postcode', 'postalcode', 'Postcode', 'code'];
            results = data.filter(item => {
              for (let i = 0; i < fields.length; i++) {
                const val = item[fields[i]];
                if (val && String(val).toLowerCase().includes(lowerQuery)) return true;
              }
              return false;
            });
          }

          renderResults(results, COUNTRY.name + ' — ' + name, query ? 'code: ' + query : null);
          btn.textContent = name;
          btn.classList.remove('loading');
        } catch (err) {
          showToast('Failed to load ' + name, 'error');
          btn.textContent = name;
          btn.classList.remove('loading');
        }
      });
    });
  }

  // Search across all states
  async function searchAll(query) {
    if (!query) { showToast('Enter a postal code', 'error'); return; }

    $('resultsList').innerHTML = '<div class="spinner"></div>';
    $('resultsTitle').textContent = 'Searching...';
    $('resultsCount').textContent = '';
    $('resultsSection').classList.add('visible');

    const allMatches = [];
    const fields = ['pincode', 'ZipCode', 'zipcode', 'postcode', 'postalcode', 'Postcode', 'code', 'officename', 'OfficeName', 'City', 'district', 'Districtname', 'County', 'statename', 'State'];
    const lowerQuery = query.toLowerCase();

    for (const state of COUNTRY.states) {
      try {
        const url = COUNTRY.dataPath + COUNTRY.dataPrefix + state.file;
        let data;
        if (dataCache.has(url)) data = dataCache.get(url);
        else {
          const res = await fetch(url);
          if (res.ok) { data = await res.json(); dataCache.set(url, data); }
        }
        if (data) {
          for (let i = 0; i < data.length; i++) {
            const item = data[i];
            for (let j = 0; j < fields.length; j++) {
              const val = item[fields[j]];
              if (val && String(val).toLowerCase().includes(lowerQuery)) {
                allMatches.push(item);
                break;
              }
            }
          }
        }
      } catch (e) {}
    }

    window.CURRENT_PAGE_DATA = allMatches;
    renderResults(allMatches, COUNTRY.name + ' — Search: ' + query, null);
    
    const normalizedQuery = lowerQuery.replace(/-/g, ' ');
    const stateMatches = COUNTRY.states.filter(s => s.name.toLowerCase().includes(normalizedQuery));
    if (stateMatches.length > 0) {
      const statesHtml = '<div style="margin-bottom:2.5rem; padding-bottom:1.5rem; border-bottom:1px solid rgba(var(--p2),0.2);"><h3 style="color:var(--t); margin-bottom:1.25rem; font-size:1.2rem; display:flex; align-items:center; gap:0.5rem;"><span style="color:var(--p)">📍</span> Matching Regions / States</h3><div class="states-grid" style="display:grid; grid-template-columns:repeat(auto-fill, minmax(180px, 1fr)); gap:1rem;">' +
        stateMatches.map((s) =>
          '<button class="state-btn" onclick="window.location.href=\'' + getBasePath() + 'pages/' + COUNTRY.code.toLowerCase() + '/' + s.file.replace('.json', '.html') + '\'" style="width:100%; text-align:center; padding:1rem; background:var(--card-hi); border:1px solid var(--p); box-shadow:var(--glow); border-radius:12px; color:var(--t); font-weight:600; cursor:pointer; font-family:var(--fd); transition:all 0.2s;">' + s.name + '</button>'
        ).join('') +
        '</div></div>';
      
      const resultsList = $('resultsList');
      // Prepend to results list if empty state wasn't rendered
      if (resultsList.querySelector('.empty-state') && allMatches.length === 0) {
        resultsList.innerHTML = statesHtml;
      } else {
        resultsList.insertAdjacentHTML('afterbegin', statesHtml);
      }
    }
  }

  // Voice search
  function startVoice() {
    if (!('webkitSpeechRecognition' in window || 'SpeechRecognition' in window)) {
      showToast('Voice search not supported in this browser', 'error');
      return;
    }
    const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
    const recognition = new SR();
    recognition.lang = 'en-US';
    recognition.interimResults = false;
    recognition.maxAlternatives = 1;

    const btn = $('voiceBtn');
    btn.classList.add('listening');
    showToast('Listening...', 'info');

    recognition.onresult = (event) => {
      const transcript = event.results[0][0].transcript;
      $('searchInput').value = transcript;
      btn.classList.remove('listening');
      searchAll(transcript);
    };
    recognition.onerror = () => { btn.classList.remove('listening'); showToast('Voice error — try again', 'error'); };
    recognition.onend = () => { btn.classList.remove('listening'); };
    recognition.start();
  }

  function initMap() {
    if (mapInitialized) return;
    map = L.map('map', { zoomControl: true, scrollWheelZoom: false, preferCanvas: true }).setView([COUNTRY.lat, COUNTRY.lon], 4);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { attribution: '© OpenStreetMap', maxZoom: 19 }).addTo(map);
    mapInitialized = true;
  }

  function makePin(c1, c2) {
    return L.divIcon({
      className: 'custom-marker',
      html: '<div style="background:linear-gradient(135deg,' + c1 + ',' + c2 + ');width:28px;height:28px;border-radius:50% 50% 50% 0;transform:rotate(-45deg);box-shadow:0 4px 16px ' + c1 + '80;border:3px solid white;"></div>',
      iconSize: [28, 28], iconAnchor: [14, 28]
    });
  }

  function showMap(results) {
    initMap();
    mapMarkers.forEach(m => map.removeLayer(m));
    mapMarkers = [];
    const withCoords = results.filter(r => r.latitude != null && r.longitude != null);
    if (withCoords.length === 0) { $('mapSection').classList.remove('visible'); return; }

    const MAX_MARKERS = window.innerWidth <= 768 ? 100 : 300;
    const markersToRender = withCoords.slice(0, MAX_MARKERS);
    const isValidCoords = (lat, lon) => {
      if (isNaN(lat) || isNaN(lon) || (lat === 0 && lon === 0) || lat < -90 || lat > 90 || lon < -180 || lon > 180) return false;
      let latDiff = Math.abs(lat - COUNTRY.lat);
      let lonDiff = Math.abs(lon - COUNTRY.lon);
      if (lonDiff > 180) lonDiff = 360 - lonDiff;
      return latDiff <= 50 && lonDiff <= 120;
    };

    markersToRender.forEach(item => {
      const lat = parseFloat(item.latitude), lon = parseFloat(item.longitude);
      if (!isValidCoords(lat, lon)) return;
      const office = item.officename || item.OfficeName || item.City || item.PlaceName || 'Unknown';
      const pin = item.pincode || item.ZipCode || item.Postcode || '';
      const dist = item.district || item.District || item.County || '';
      const popup = `<b>${office}</b><br>${pin}<br>${dist}<br><a href="https://www.google.com/maps?q=${lat},${lon}" target="_blank">Google Maps</a>`;
      let colors = ['#00d4ff', '#0055ff'];
      if (item.officetype === 'HO') colors = ['#ff0055', '#ff9900'];
      else if (item.officetype === 'SO') colors = ['#00ff88', '#0099ff'];
      const m = L.marker([lat, lon], { icon: makePin(...colors) }).addTo(map).bindPopup(popup);
      mapMarkers.push(m);
    });
    
    if (markersToRender.length > 0) {
      const firstValid = markersToRender.find(r => isValidCoords(parseFloat(r.latitude), parseFloat(r.longitude)));
      if (firstValid) {
        const lat = parseFloat(firstValid.latitude), lon = parseFloat(firstValid.longitude);
        map.setView([lat, lon], 6, { animate: true });
      }
    }

    let valid = markersToRender.filter(r => isValidCoords(parseFloat(r.latitude), parseFloat(r.longitude)));
    if (valid.length > 2) {
      const lats = valid.map(r => parseFloat(r.latitude)).sort((a,b)=>a-b);
      const lons = valid.map(r => parseFloat(r.longitude)).sort((a,b)=>a-b);
      const mLat = lats[Math.floor(lats.length/2)], mLon = lons[Math.floor(lons.length/2)];
      const madLat = valid.map(r => Math.abs(parseFloat(r.latitude)-mLat)).sort((a,b)=>a-b)[Math.floor(valid.length/2)];
      const madLon = valid.map(r => Math.abs(parseFloat(r.longitude)-mLon)).sort((a,b)=>a-b)[Math.floor(valid.length/2)];
      const tLat = Math.max(madLat * 4, 2), tLon = Math.max(madLon * 4, 2);
      valid = valid.filter(r => Math.abs(parseFloat(r.latitude)-mLat) <= tLat && Math.abs(parseFloat(r.longitude)-mLon) <= tLon);
    }
    if (valid.length > 0) {
      map.fitBounds(valid.map(r => [parseFloat(r.latitude), parseFloat(r.longitude)]), { padding: [50, 50], maxZoom: 6 });
    }
    
    let badgeText = markersToRender.length + ' location' + (markersToRender.length > 1 ? 's' : '');
    if (withCoords.length > MAX_MARKERS) badgeText += ' (showing top ' + MAX_MARKERS + ')';
    $('mapBadgeText').textContent = badgeText;
    
    $('mapSection').classList.add('visible');
    setTimeout(() => map.invalidateSize(), 400);
  }

  // Results
  function renderResults(results, title, subtitle) {
    if (results && results.length > 0) {
      results.forEach(r => {
        if (r.latitude === undefined && (r.Latitude !== undefined || r.lat !== undefined)) {
          r.latitude = r.Latitude !== undefined ? r.Latitude : r.lat;
        }
        if (r.longitude === undefined && (r.Longitude !== undefined || r.lon !== undefined || r.lng !== undefined)) {
          r.longitude = r.Longitude !== undefined ? r.Longitude : (r.lon !== undefined ? r.lon : r.lng);
        }
      });
    }
    if ($('statesSection')) $('statesSection').style.display = 'none';
    if (!results || results.length === 0) {
      $('resultsList').innerHTML = '<div class="empty-state"><div class="empty-icon">🔍</div><p>No results found.' + (subtitle ? ' Try a different code.' : '') + '</p></div>';
      $('resultsCount').textContent = '0 found';
      $('resultsTitle').textContent = title;
      $('resultsSection').classList.add('visible');
      $('mapSection').classList.remove('visible');
      return;
    }
    $('resultsTitle').textContent = title;
    $('resultsCount').textContent = results.length + ' found';
    
    const resultsList = $('resultsList');
    resultsList.innerHTML = '';
    const CHUNK_SIZE = 100;
    let chunkIndex = 0;
    
    function renderChunk() {
      const chunk = results.slice(chunkIndex, chunkIndex + CHUNK_SIZE);
      if (chunk.length === 0) return;
      
      const html = chunk.map((item, idx) => {
        let globalIdx = chunkIndex + idx;
        let stateLbl = 'State';
        let distLbl = 'City / District';
        if (['US','GB','IE'].includes(COUNTRY.code)) distLbl = 'County';
        else if (COUNTRY.code === 'JP') { stateLbl = 'Prefecture'; distLbl = 'City/Ward'; }
        else if (COUNTRY.code === 'CA') { stateLbl = 'Province'; distLbl = 'County/City'; }
        else if (COUNTRY.code === 'CN') { stateLbl = 'Province'; distLbl = 'Prefecture'; }
        else if (COUNTRY.code === 'FR') { stateLbl = 'Region'; distLbl = 'Department'; }
        else if (COUNTRY.code === 'IT') { stateLbl = 'Region'; distLbl = 'Province'; }
        else if (COUNTRY.code === 'ES') { stateLbl = 'Community'; distLbl = 'Province'; }
        else if (COUNTRY.code === 'AU') { stateLbl = 'State'; distLbl = 'Region'; }
        else if (COUNTRY.code === 'BR') { stateLbl = 'State'; distLbl = 'Municipality'; }
        else if (COUNTRY.code === 'ZA') { stateLbl = 'Province'; distLbl = 'Municipality'; }
        else if (COUNTRY.code === 'RU') { stateLbl = 'Republic/Oblast'; distLbl = 'District'; }
        else if (COUNTRY.code !== 'IN') { stateLbl = 'Province/State'; distLbl = 'County/City'; }

        const pin = item.pincode || item.ZipCode || item.zipcode || 'N/A';
        const office = item.officename || item.OfficeName || item.City || 'Location';
        const state = item.statename || item.State || '';
        const district = item.district || item.Districtname || item.County || item.City || item.Taluk || item.divisionname || '';
        const region = item.regionname || item.Country || '';
        const division = item.divisionname || '';
        const hasCoords = item.latitude != null && item.longitude != null;
        
        let animDelay = Math.min(globalIdx * 10, 1000);
        return '<div class="result-card" data-idx="' + globalIdx + '" style="animation-delay:' + animDelay + 'ms">'  +
          '<div class="result-pin"><span class="result-pin-num">' + pin + '</span><button class="copy-btn" data-pin="' + pin + '">📋</button></div>' +
          '<div class="result-office">' + office + '</div>' +
          '<div class="result-meta">' +
            '<div class="meta-item"><span class="meta-label">' + stateLbl + '</span><span class="meta-value">' + (state || 'N/A') + '</span></div>' +
            '<div class="meta-item"><span class="meta-label">' + distLbl + '</span><span class="meta-value">' + (district || 'N/A') + '</span></div>' +
            '<div class="meta-item"><span class="meta-label">Region</span><span class="meta-value">' + (region || 'N/A') + '</span></div>' +
            '<div class="meta-item"><span class="meta-label">Division</span><span class="meta-value">' + (division || 'N/A') + '</span></div>' +
          '</div>' +
          '<div class="result-actions">' +
            (hasCoords ? '<button class="action-btn" data-lat="' + item.latitude + '" data-lon="' + item.longitude + '" data-label="' + office + '">🗺️ Focus</button>' : '') +
            '<a class="action-btn" href="https://www.google.com/maps?q=' + (item.latitude || '') + ',' + (item.longitude || '') + '" target="_blank" rel="noopener">🌍 Google</a>' +
            '<a class="action-btn" href="' + getBasePath() + 'pages/report.html?country=' + encodeURIComponent(COUNTRY.name) + '&office=' + encodeURIComponent(office) + '&pin=' + encodeURIComponent(pin) + '">⚠️ Report</a>' +
          '</div></div>';
      }).join('');

      resultsList.insertAdjacentHTML('beforeend', html);
      chunkIndex += CHUNK_SIZE;
      
      if (chunkIndex < results.length) {
        requestAnimationFrame(renderChunk);
      } else {
        const moreHtml = `
          <div style="margin-top: 2rem; display: flex; flex-wrap: wrap; gap: 1rem; justify-content: center;">
            <a href="${getBasePath()}pages/${COUNTRY.flagCode}.html" class="action-btn" style="background: linear-gradient(135deg, #ff6b1a 0%, #f5b700 100%); color: #000; padding: 0.8rem 1.5rem; font-weight: bold; border-radius: 8px; text-decoration: none;">🔍 Find More Pincodes in ${COUNTRY.name}</a>
            <a href="https://www.google.com/search?q=${encodeURIComponent(title + ' postal code')}" target="_blank" class="action-btn" style="background: #333; color: #fff; padding: 0.8rem 1.5rem; font-weight: bold; border-radius: 8px; text-decoration: none;">🌍 Google Search</a>
          </div>
        `;
        resultsList.insertAdjacentHTML('beforeend', moreHtml);
      }

    }
    
    requestAnimationFrame(renderChunk);

    $('resultsSection').classList.add('visible');
    showMap(results);
    setTimeout(() => $('resultsSection').scrollIntoView({ behavior: 'smooth', block: 'start' }), 100);
  }

  // Event listeners
  const searchBtnNode = $('searchBtn');
  const searchInputNode = $('searchInput');
  if (searchBtnNode && searchInputNode) {
    searchBtnNode.addEventListener('click', () => searchAll(searchInputNode.value.trim()));
    searchInputNode.addEventListener('keypress', (e) => { if (e.key === 'Enter') searchBtnNode.click(); });
    
    // Auto-search on input
    let searchTimeout = null;
    searchInputNode.addEventListener('input', (e) => {
      clearTimeout(searchTimeout);
      const val = e.target.value.trim();
      searchTimeout = setTimeout(() => searchAll(val), 300);
    });
    
    const voiceBtn = $('voiceBtn');
    if (voiceBtn) voiceBtn.addEventListener('click', startVoice);
  }

  // Global event delegation for results list (Optimized DOM handling)
  document.addEventListener('click', (e) => {
    const copyBtn = e.target.closest('.copy-btn');
    if (copyBtn) {
      e.stopPropagation();
      copyPin(copyBtn.dataset.pin);
      copyBtn.classList.add('copied'); copyBtn.textContent = '✓';
      setTimeout(() => { copyBtn.classList.remove('copied'); copyBtn.textContent = '📋'; }, 1500);
      return;
    }
    const focusBtn = e.target.closest('.action-btn[data-lat]');
    if (focusBtn) {
      e.stopPropagation();
      showMap([{ latitude: focusBtn.dataset.lat, longitude: focusBtn.dataset.lon, officename: focusBtn.dataset.label }]);
      return;
    }
    const card = e.target.closest('.result-card');
    if (card && !e.target.closest('.action-btn') && !e.target.closest('.copy-btn')) {
      const idx = card.dataset.idx;
      if (idx !== undefined && window.CURRENT_PAGE_DATA && window.CURRENT_PAGE_DATA[idx]) {
          showPinDetails(window.CURRENT_PAGE_DATA[idx]);
      } else {
          card.classList.toggle('expanded');
      }
    }
  });

  window.showPinDetails = function(pinObj) {
    $('resultsList').style.display = 'none';
    if ($('pagination')) $('pagination').style.display = 'none';
    if ($('mapSection')) $('mapSection').style.display = 'none';
    
    let d = $('pinDetails');
    if (!d) {
       d = document.createElement('div');
       d.id = 'pinDetails';
       d.style.padding = '20px';
       d.style.textAlign = 'center';
       $('resultsSection').appendChild(d);
    }
    d.style.display = 'block';
    
    let html = '<button class="action-btn" style="margin-bottom:15px;background:#333;color:#fff;" onclick="document.getElementById(\'pinDetails\').style.display=\'none\';document.getElementById(\'resultsList\').style.display=\'\';if(document.getElementById(\'mapSection\'))document.getElementById(\'mapSection\').style.display=\'\';">🔙 Back to List</button>';
    html += '<div class="pin-card highlight" style="max-width:600px;margin:0 auto;text-align:left;">';
    for(let k in pinObj){
        html += '<div style="margin-bottom:8px;"><strong>'+String(k).toUpperCase()+':</strong> '+pinObj[k]+'</div>';
    }
    const office = pinObj.officename || pinObj.City || pinObj.OfficeName || '';
    const state = pinObj.statename || pinObj.State || '';
    const pin = pinObj.pincode || pinObj.zip || pinObj.ZipCode || '';
    const query = encodeURIComponent(office + ' ' + pin);
    
    html += '<div style="margin-top:15px;display:flex;gap:10px;flex-wrap:wrap;">';
    html += '<a href="https://www.google.com/maps/search/?api=1&query='+query+'" target="_blank" class="action-btn" style="background:#4285F4;color:#fff;">📍 Maps</a>';
    html += '<a href="https://www.google.com/search?q='+encodeURIComponent('About ' + office + ' ' + state)+'" target="_blank" class="action-btn" style="background:linear-gradient(135deg, #10a37f, #0d8a6a);color:#fff;">📖 About '+office+'</a>';
    html += '</div></div>';
    
    d.innerHTML = html;
  }

  // Init removed

  // ==========================================
  // PSEO INJECTION & AD LOGIC
  // ==========================================
  function injectAdSlots() {
    const isMobile = window.innerWidth <= 768;
    const isTab = window.innerWidth > 768 && window.innerWidth <= 1024;
    const isPC = window.innerWidth > 1024;

    const ads = [
      { id: 'ad-slot-1', types: ['mobile', 'tab', 'pc'] },
      { id: 'ad-slot-2', types: ['mobile', 'tab', 'pc'] },
      { id: 'ad-slot-3', types: ['pc', 'tab'] },
      { id: 'ad-slot-4', types: ['pc'] },
      { id: 'ad-slot-5', types: ['pc'] }
    ];

    ads.forEach(ad => {
      const el = document.getElementById(ad.id);
      if (!el) return;
      if (
        (isMobile && !ad.types.includes('mobile')) ||
        (isTab && !ad.types.includes('tab')) ||
        (isPC && !ad.types.includes('pc'))
      ) {
        return; // hide
      }
      
      if (!el.innerHTML.includes('ins class="adsbygoogle"')) {
        el.innerHTML = '<ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-6426743918933227" data-ad-slot="1234567890" data-ad-format="auto" data-full-width-responsive="true"></ins>';
        try { (window.adsbygoogle = window.adsbygoogle || []).push({}); } catch (e) { console.error('AdSense error', e); }
      }
    });
  }

  async function loadCityData() {
    const url = COUNTRY.dataPath + COUNTRY.dataPrefix + window.PSEO_STATE;
    const query = window.PSEO_CITY ? window.PSEO_CITY.toLowerCase() : '';
    
    try {
      $('resultsList').innerHTML = '<div class="spinner"></div>';
      $('resultsTitle').textContent = 'Loading ' + (window.PSEO_CITY || window.PSEO_STATE_LABEL) + '...';
      $('resultsSection').classList.add('visible');
      
      const res = await fetch(url);
      let data = await res.json();
      
      let results = data;
      if (query) {
        results = data.filter(item => {
          const office = String(item.officename || item.OfficeName || item.City || '').toLowerCase();
          const district = String(item.district || item.Districtname || item.County || '').toLowerCase();
          const state = String(item.statename || item.State || '').toLowerCase();
          
          return office.includes(query) || district.includes(query) || state.includes(query);
        });
      }
      
      window.CURRENT_PAGE_DATA = results;
      const title = window.PSEO_CITY ? (window.PSEO_CITY + ' — ' + window.PSEO_STATE_LABEL) : window.PSEO_STATE_LABEL;
      renderResults(results, title, window.PSEO_CITY ? 'City Search' : 'State Search');
    } catch (e) {
      console.error('Failed to load data', e);
      $('resultsList').innerHTML = '<div class="empty-state">Failed to load data</div>';
    }
  }

  function performLocalSearch(q) {
    const toTitleCase = (str) => {
      if (!str) return '';
      return str.replace(/\w\S*/g, t => t.charAt(0).toUpperCase() + t.substr(1).toLowerCase());
    };
    
    if (window.CURRENT_PAGE_DATA && q) {
      const titleCity = window.PSEO_CITY ? toTitleCase(window.PSEO_CITY) : '';
      const titleState = window.PSEO_STATE_LABEL ? toTitleCase(window.PSEO_STATE_LABEL) : '';
      const titleStr = titleCity ? (titleCity + ' — ' + titleState) : titleState;
      document.title = titleStr + ' | PO ZipCode Global';
    }

    if (!window.CURRENT_PAGE_DATA) return;
    if (!q) {
      const titleCity = window.PSEO_CITY ? toTitleCase(window.PSEO_CITY) : '';
      const titleState = window.PSEO_STATE_LABEL ? toTitleCase(window.PSEO_STATE_LABEL) : '';
      const title = titleCity ? (titleCity + ' — ' + titleState) : titleState;
      renderResults(window.CURRENT_PAGE_DATA, title, window.PSEO_CITY ? 'City Search' : 'State Search');
      return;
    }
    const query = q.toLowerCase();
    const fields = ['pincode', 'ZipCode', 'zipcode', 'postcode', 'postalcode', 'Postcode', 'code', 'officename', 'OfficeName', 'City', 'district', 'Districtname', 'County', 'statename', 'State'];
    const results = window.CURRENT_PAGE_DATA.filter(item => {
      for (let i = 0; i < fields.length; i++) {
        const val = item[fields[i]];
        if (val && String(val).toLowerCase().includes(query)) return true;
      }
      return false;
    });
    renderResults(results, 'Search Results for "' + q + '"', '');
  }

  async function startApp() {
    if (window.PSEO_CITY || window.PSEO_IS_STATE) {
      try {
        let templatePath = SCRIPT_URL.replace('shared_pseo.js', 'country-template.html');
        if (window.location.protocol === 'file:') {
            templatePath = getBasePath() + 'pages/country-template.html';
        }
        const res = await fetch(templatePath);
        let html = await res.text();
        
        const styleMatch = html.match(/<style[^>]*>([\s\S]*?)<\/style>/ig);
        if (styleMatch) {
            styleMatch.forEach(styleTag => {
                document.head.insertAdjacentHTML('beforeend', styleTag);
            });
        }
        
        const bodyMatch = html.match(/<body[^>]*>([\s\S]*)<\/body>/i);
        if (bodyMatch) html = bodyMatch[1];
        
        const app = document.getElementById('app');
        const logoEl = document.querySelector('.logo');
        if (logoEl && !logoEl.innerHTML.includes('img')) {
            logoEl.innerHTML = '<img src="' + getBasePath() + 'home/assets/logo.png" alt="PO ZipCode Global Logo" style="height:40px; vertical-align:middle; margin-right:8px; border-radius:4px;"> PO ZipCode Global';
        }
        
        const bp = getBasePath();
        html = html.replace(/href="\.\.\/home\//g, 'href="' + bp + 'home/');
        html = html.replace(/href="\.\.\/pages\//g, 'href="' + bp + 'pages/');
        html = html.replace(/src="\.\.\/home\//g, 'src="' + bp + 'home/');
        html = html.replace(/href="report\.html"/g, 'href="' + bp + 'pages/report.html"');
        html = html.replace(/href="\/"/g, 'href="' + bp + '"');
        
        if (app) app.innerHTML = html;
        else document.body.innerHTML = html;
        document.body.className = 'theme-' + COUNTRY.code.toLowerCase();
          applyDynamicCountryTheme(COUNTRY.code);
          
        // Dynamic Navbar Active Highlight
        const currentPath = window.location.pathname;
        document.querySelectorAll('.nav-btn, .nav-links a').forEach(el => {
            const href = el.getAttribute('href');
            if (href && !href.startsWith('#') && currentPath.includes(href.split('/').pop())) {
                el.style.color = 'var(--p)';
                el.style.borderColor = 'var(--p)';
            }
        });
        
        setTimeout(() => {
          let seoText = document.querySelector('.seo-text');
          const resultsHeader = document.querySelector('.results-header');
          
          if (!seoText && window.PSEO_STATE_LABEL) {
              seoText = document.createElement('div');
              seoText.className = 'seo-text';
              seoText.style.padding = '20px';
              seoText.style.background = 'rgba(255,255,255,0.05)';
              seoText.style.margin = '20px auto';
              seoText.style.maxWidth = '800px';
              seoText.style.borderRadius = '8px';
              seoText.style.color = '#ccc';
              seoText.style.lineHeight = '1.6';
              seoText.style.textAlign = 'center';
              seoText.style.fontSize = '14px';
              
              let term = window.PSEO_COUNTRY === 'US' ? 'ZIP Code' : (window.PSEO_COUNTRY === 'IN' ? 'PIN Code' : 'Postal Code');
              seoText.innerHTML = `This page provides a comprehensive list of all ${term}s and Post Offices in <strong>${window.PSEO_CITY}</strong>, <strong>${window.PSEO_STATE_LABEL}</strong>. Use our interactive map and directory to find post office locations, delivery areas, and branch details for <strong>${window.PSEO_CITY}</strong>.`;
          }
          
          if (seoText && resultsHeader) {
            seoText.style.display = 'block';
            resultsHeader.parentNode.insertBefore(seoText, resultsHeader.nextSibling);
          }
        }, 100);
        
        $('searchBtn').addEventListener('click', () => performLocalSearch($('searchInput').value.trim()));
        $('searchInput').addEventListener('keypress', (e) => { if (e.key === 'Enter') $('searchBtn').click(); });
        
        let localSearchTimeout = null;
        $('searchInput').addEventListener('input', (e) => {
            clearTimeout(localSearchTimeout);
            const val = e.target.value.trim();
            localSearchTimeout = setTimeout(() => performLocalSearch(val), 200);
        });
        
        const vBtn = $('voiceBtn');
        if(vBtn) vBtn.addEventListener('click', startVoice);
        
        if (typeof injectAdSlots === 'function') injectAdSlots();
        
        if (!window.L) {
            const script = document.createElement('script');
            script.src = 'https://unpkg.com/leaflet@1.9.4/dist/leaflet.js';
            script.onload = () => {
              loadStates();
              loadCityData();
            };
            document.head.appendChild(script);
        } else {
            loadStates();
            loadCityData();
        }
      } catch (e) { console.error('Failed to load layout'); }
    }
  }

  if (window.PSEO_CITY || window.PSEO_IS_STATE) {
    startApp();
  } else {
    // Normal country page
    loadStates();
  }

})();




function applyDynamicCountryTheme(code) {
  const customThemes = {
    'IN': ['#ff9933', '#138808'],
    'US': ['#b22234', '#3c3b6e'],
    'GB': ['#c8102e', '#012169'],
    'CA': ['#ff0000', '#ff0000'],
    'AU': ['#ffcd00', '#00843D']
  };
  let p, s;
  if(customThemes[code]) { p = customThemes[code][0]; s = customThemes[code][1]; }
  else {
    let h = 0; for(let i=0; i<code.length; i++) h = code.charCodeAt(i) + ((h<<5)-h);
    let hue = Math.abs(h) % 360;
    p = 'hsl('+hue+', 80%, 55%)'; s = 'hsl('+((hue+45)%360)+', 70%, 45%)';
  }
  document.documentElement.style.setProperty('--grad-cinema', 'linear-gradient(135deg, '+p+', '+s+')');
  document.documentElement.style.setProperty('--saffron', p);
  document.documentElement.style.setProperty('--bg-card', 'color-mix(in srgb, '+p+' 5%, rgba(255,255,255,0.035))');
}











window.addEventListener('DOMContentLoaded', () => {
  setTimeout(() => {
    try{
      const q = new URLSearchParams(window.location.search).get('q');
      if(q && document.getElementById('search') && window.doSearch) {
        document.getElementById('search').value = q;
        window.doSearch();
      }
    }catch(e){}
  }, 500);
});
