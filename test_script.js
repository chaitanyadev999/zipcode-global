(function(){
'use strict';

// ── COUNTRY CONFIG ──────────────────────────────────────────────
const C = {
  name:'Japan', code:'JP', flag:'jp',
  term:'Postal Code', subtitle:'Asia · 47 Prefectures · 〒 7-digit Codes',
  lat:36.2048, lon:138.2529, region:'Asia',
  dataBase: 'JP' === 'IN' ? 'https://cdn.jsdelivr.net/gh/chaitanyadev999/pincode-dataindia@main/' : 'https://cdn.jsdelivr.net/gh/chaitanyadev999/pincode-dataindia@main/world/JP/'
};

// ── HAND-CRAFTED UNIQUE FLAG THEME COLORS FOR ALL 121 COUNTRIES ──────────────────────────
const THEMES = {
  'IN':{p:'#FF9933',a:'#138808',p2:'255,153,51'},
  'US':{p:'#B22234',a:'#3C3B6E',p2:'178,34,52'},
  'AD':{p:'#0018A8',a:'#C8102E',p2:'0,24,168'},
  'AE':{p:'#00732F',a:'#FF0000',p2:'0,115,47'},
  'AI':{p:'#00A3E0',a:'#00205B',p2:'0,163,224'},
  'AL':{p:'#E41E20',a:'#111111',p2:'228,30,32'},
  'AR':{p:'#74ACDF',a:'#F6B40E',p2:'116,172,223'},
  'AS':{p:'#00205B',a:'#C8102E',p2:'0,32,91'},
  'AT':{p:'#EF3340',a:'#C8102E',p2:'239,51,64'},
  'AU':{p:'#00008B',a:'#FF0000',p2:'0,0,139'},
  'AX':{p:'#005293',a:'#FFC61E',p2:'0,82,147'},
  'AZ':{p:'#00B5E2',a:'#50B848',p2:'0,181,226'},
  'BD':{p:'#006A4E',a:'#F42A41',p2:'0,106,78'},
  'BE':{p:'#FDDA24',a:'#EF3340',p2:'253,218,36'},
  'BG':{p:'#00966E',a:'#D62612',p2:'0,150,110'},
  'BM':{p:'#BD152B',a:'#00205B',p2:'189,21,43'},
  'BR':{p:'#009C3B',a:'#FFDF00',p2:'0,156,59'},
  'BY':{p:'#D22630',a:'#007A33',p2:'210,38,48'},
  'CA':{p:'#FF0000',a:'#C8102E',p2:'255,0,0'},
  'CC':{p:'#006633',a:'#FFCC00',p2:'0,102,51'},
  'CH':{p:'#FF0000',a:'#D52B1E',p2:'255,0,0'},
  'CL':{p:'#D52B1E',a:'#002868',p2:'213,43,30'},
  'CN':{p:'#DE2910',a:'#FFDE00',p2:'222,41,16'},
  'CO':{p:'#FCD116',a:'#003087',p2:'252,209,22'},
  'CR':{p:'#002B7F',a:'#CE1126',p2:'0,43,127'},
  'CX':{p:'#008060',a:'#FFC72C',p2:'0,128,96'},
  'CY':{p:'#D47600',a:'#4E6B34',p2:'212,118,0'},
  'CZ':{p:'#D7141A',a:'#11457E',p2:'215,20,26'},
  'DE':{p:'#FFCE00',a:'#DD0000',p2:'255,206,0'},
  'DK':{p:'#C60C30',a:'#9A001A',p2:'198,12,48'},
  'DO':{p:'#002D62',a:'#CE1126',p2:'0,45,98'},
  'DZ':{p:'#006233',a:'#D21034',p2:'0,98,51'},
  'EC':{p:'#FFD100',a:'#0033A0',p2:'255,209,0'},
  'EE':{p:'#0072CE',a:'#111111',p2:'0,114,206'},
  'ES':{p:'#AA151B',a:'#F1BF00',p2:'170,21,27'},
  'FI':{p:'#003580',a:'#00A3E0',p2:'0,53,128'},
  'FK':{p:'#00205B',a:'#C8102E',p2:'0,32,91'},
  'FM':{p:'#75B2DD',a:'#0099FF',p2:'117,178,221'},
  'FO':{p:'#0065BD',a:'#EF3340',p2:'0,101,189'},
  'FR':{p:'#0055A4',a:'#EF4135',p2:'0,85,164'},
  'GB':{p:'#012169',a:'#C8102E',p2:'1,33,105'},
  'GF':{p:'#009E49',a:'#FFD100',p2:'0,158,73'},
  'GG':{p:'#E8112D',a:'#F9D616',p2:'232,17,45'},
  'GI':{p:'#DA291C',a:'#FFC72C',p2:'218,41,28'},
  'GL':{p:'#C8102E',a:'#FF4D4D',p2:'200,16,46'},
  'GP':{p:'#00A3E0',a:'#FFC72C',p2:'0,163,224'},
  'GS':{p:'#00205B',a:'#C8102E',p2:'0,32,91'},
  'GT':{p:'#4997D0',a:'#00B5E2',p2:'73,151,208'},
  'GU':{p:'#00205B',a:'#C8102E',p2:'0,32,91'},
  'HK':{p:'#DE2910',a:'#FF4D4D',p2:'222,41,16'},
  'HM':{p:'#00205B',a:'#75B2DD',p2:'0,32,91'},
  'HN':{p:'#00B2E3',a:'#0073E6',p2:'0,178,227'},
  'HR':{p:'#FF0000',a:'#111133',p2:'255,0,0'},
  'HT':{p:'#00209F',a:'#D21034',p2:'0,32,159'},
  'HU':{p:'#CE2939',a:'#436F4D',p2:'206,41,57'},
  'ID':{p:'#CE1126',a:'#E62135',p2:'206,17,38'},
  'IE':{p:'#169B62',a:'#FF883E',p2:'22,155,98'},
  'IM':{p:'#CF142B',a:'#FFC72C',p2:'207,20,43'},
  'IO':{p:'#00205B',a:'#C8102E',p2:'0,32,91'},
  'IS':{p:'#003897',a:'#D72828',p2:'0,56,151'},
  'IT':{p:'#009246',a:'#CE2B37',p2:'0,146,70'},
  'JE':{p:'#E8112D',a:'#F9D616',p2:'232,17,45'},
  'JP':{p:'#BC002D',a:'#FF3355',p2:'188,0,45'},
  'KE':{p:'#990000',a:'#006600',p2:'153,0,0'},
  'KR':{p:'#003478',a:'#CD2E3A',p2:'0,52,120'},
  'LI':{p:'#002B7F',a:'#FFC72C',p2:'0,43,127'},
  'LK':{p:'#8D153A',a:'#FF8C00',p2:'141,21,58'},
  'LT':{p:'#FDB913',a:'#006A44',p2:'253,185,19'},
  'LU':{p:'#00A3E0',a:'#EA141D',p2:'0,163,224'},
  'LV':{p:'#9E1B32',a:'#6B1020',p2:'158,27,50'},
  'MA':{p:'#C1272D',a:'#006233',p2:'193,39,45'},
  'MC':{p:'#CE1126',a:'#FF4D4D',p2:'206,17,38'},
  'MD':{p:'#002B7F',a:'#CC0000',p2:'0,43,127'},
  'MH':{p:'#00205B',a:'#DD7500',p2:'0,32,91'},
  'MK':{p:'#D82126',a:'#FBE122',p2:'216,33,38'},
  'MO':{p:'#007A5E',a:'#FFC72C',p2:'0,122,94'},
  'MP':{p:'#00A3E0',a:'#00205B',p2:'0,163,224'},
  'MQ':{p:'#00205B',a:'#CE1126',p2:'0,32,91'},
  'MT':{p:'#C8102E',a:'#E6E6E6',p2:'200,16,46'},
  'MW':{p:'#E4002B',a:'#00A357',p2:'228,0,43'},
  'MX':{p:'#006847',a:'#CE1126',p2:'0,104,71'},
  'MY':{p:'#FFD100',a:'#000066',p2:'255,209,0'},
  'NC':{p:'#00A3E0',a:'#CE1126',p2:'0,163,224'},
  'NF':{p:'#006A4E',a:'#004B37',p2:'0,106,78'},
  'NL':{p:'#FF6600',a:'#21468B',p2:'255,102,0'},
  'NO':{p:'#EF2B2D',a:'#002868',p2:'239,43,45'},
  'NR':{p:'#00205B',a:'#FFC72C',p2:'0,32,91'},
  'NU':{p:'#FFC72C',a:'#00205B',p2:'255,199,44'},
  'NZ':{p:'#00247D',a:'#CC142B',p2:'0,36,125'},
  'PA':{p:'#005293',a:'#D21034',p2:'0,82,147'},
  'PE':{p:'#D91023',a:'#990011',p2:'217,16,35'},
  'PF':{p:'#00B5E2',a:'#CE1126',p2:'0,181,226'},
  'PH':{p:'#0038A8',a:'#FCD116',p2:'0,56,168'},
  'PK':{p:'#27AE60',a:'#01411C',p2:'39,174,96'},
  'PL':{p:'#DC143C',a:'#FF4D4D',p2:'220,20,60'},
  'PM':{p:'#00205B',a:'#00A3E0',p2:'0,32,91'},
  'PN':{p:'#00205B',a:'#008060',p2:'0,32,91'},
  'PR':{p:'#ED0000',a:'#0050F0',p2:'237,0,0'},
  'PT':{p:'#006600',a:'#FF0000',p2:'0,102,0'},
  'PW':{p:'#4AADD6',a:'#FFDE00',p2:'74,173,214'},
  'RE':{p:'#E41E20',a:'#00205B',p2:'228,30,32'},
  'RO':{p:'#002B7F',a:'#FCD116',p2:'0,43,127'},
  'RS':{p:'#C6363C',a:'#0C4076',p2:'198,54,60'},
  'RU':{p:'#0039A6',a:'#D52B1E',p2:'0,57,166'},
  'SE':{p:'#006AA7',a:'#FECC02',p2:'0,106,167'},
  'SG':{p:'#EF3340',a:'#FF6677',p2:'239,51,64'},
  'SI':{p:'#005DA4',a:'#ED1C24',p2:'0,93,164'},
  'SJ':{p:'#00205B',a:'#75B2DD',p2:'0,32,91'},
  'SK':{p:'#0B4EA2',a:'#EE1C25',p2:'11,78,162'},
  'SM':{p:'#61B2E4',a:'#0073E6',p2:'97,178,228'},
  'TC':{p:'#00A3E0',a:'#FF6F61',p2:'0,163,224'},
  'TH':{p:'#A51931',a:'#2D2A4A',p2:'165,25,49'},
  'TR':{p:'#E30A17',a:'#FFC72C',p2:'227,10,23'},
  'UA':{p:'#005BBB',a:'#FFD500',p2:'0,91,187'},
  'UY':{p:'#0038A8',a:'#FCD116',p2:'0,56,168'},
  'VA':{p:'#FFE600',a:'#D4AF37',p2:'255,230,0'},
  'VI':{p:'#00A3E0',a:'#FFC72C',p2:'0,163,224'},
  'WF':{p:'#00205B',a:'#CE1126',p2:'0,32,91'},
  'WS':{p:'#CE1126',a:'#00205B',p2:'206,17,38'},
  'YT':{p:'#0080FF',a:'#009966',p2:'0,128,255'},
  'ZA':{p:'#007A4D',a:'#FFB612',p2:'0,122,77'}
};

function getTheme(code){
  if(THEMES[code]) return THEMES[code];
  let hash = 0;
  for (let i = 0; i < code.length; i++) hash = code.charCodeAt(i) + ((hash << 5) - hash);
  const h = Math.abs(hash) % 360;
  const s = 0.85, l = 0.55;
  const c = (1 - Math.abs(2 * l - 1)) * s;
  const x = c * (1 - Math.abs((h / 60) % 2 - 1));
  const m = l - c / 2;
  let r=0,g=0,b=0;
  if (0 <= h && h < 60) { r = c; g = x; b = 0; }
  else if (60 <= h && h < 120) { r = x; g = c; b = 0; }
  else if (120 <= h && h < 180) { r = 0; g = c; b = x; }
  else if (180 <= h && h < 240) { r = 0; g = x; b = c; }
  else if (240 <= h && h < 300) { r = x; g = 0; b = c; }
  else if (300 <= h && h < 360) { r = c; g = 0; b = x; }
  const R = Math.round((r + m) * 255);
  const G = Math.round((g + m) * 255);
  const B = Math.round((b + m) * 255);
  const hex = "#" + ((1 << 24) + (R << 16) + (G << 8) + B).toString(16).slice(1);
  return { p: hex, a: '#7c3aed', p2: `${R},${G},${B}` };
}

const T = getTheme(C.code);
document.documentElement.style.setProperty('--p', T.p);
document.documentElement.style.setProperty('--a', T.a);
document.documentElement.style.setProperty('--p2', T.p2);

// ── FIELD DETECTOR ──────────────────────────────────────────────
function detectFields(records) {
  if (!records.length) return {};
  const k = Object.keys(records[0]);
  const find = (...pats) => {
    for(const p of pats){
      const match = k.find(x => p.test(x.toLowerCase()));
      if(match) return match;
    }
    return '';
  };
  return {
    pin:   find(/^pincode$/,/^postcode$/,/post.?code/,/zip.?code/,/^code$/),
    city:  find(/^city$/,/^village$/,/^town$/,/place.?name/,/office.?name/,/^locality$/,/division.?name/,/region.?name/),
    dist:  find(/district/,/county/,/admin.?name2/,/admin.?2/),
    state: find(/state.?name/,/province/,/admin.?name1/,/admin.?1/,/^state$/),
    lat:   find(/^lat/,/latitude/),
    lon:   find(/^lon/,/^lng/,/longitude/),
  };
}

// ── NAVIGATION STATE ────────────────────────────────────────────
const NAV = {
  step:0, stateFile:null, data:[], fields:{}, city:null, district:null,
  citiesList:[], cityLimit:60,
  distsList:[], distLimit:60,
  pinsList:[], pinLimit:60
};
let mainMap = null, mapMarkersGroup = null;

// ── UTILITIES ───────────────────────────────────────────────────
const $ = id => document.getElementById(id);
function show(...ids){ ids.forEach(id => $(id).style.display=''); }
function hide(...ids){ ids.forEach(id => $(id).style.display='none'); }
function setCount(id,n,label){ $(id).textContent = n+' '+label+(n!==1?'s':''); }
function toast(msg, type='info'){
  const c=$('tc'), d=document.createElement('div');
  d.className='toast '+type; d.textContent=msg; c.appendChild(d);
  requestAnimationFrame(()=>requestAnimationFrame(()=>d.classList.add('show')));
  setTimeout(()=>{d.classList.remove('show');setTimeout(()=>d.remove(),400)},2800);
}
function uniq(arr){ return [...new Set(arr.filter(x=>x&&x.trim()))].sort(); }
function val(r,f){ return f ? (r[f]||'').toString().trim() : ''; }

// ── EMOJI ICON MAPPER FOR ATTRIBUTES ─────────────────────────────
const ICON_MAP = {
  'circlename': '🏢', 'circle': '🏢',
  'regionname': '📍', 'region': '📍',
  'divisionname': '📮', 'division': '📮',
  'officename': '🏢', 'office': '🏢',
  'pincode': '🔢', 'postcode': '🔢', 'zipcode': '🔢', 'code': '🔢',
  'officetype': '🏷️', 'type': '🏷️',
  'delivery': '🚚', 'deliverystatus': '🚚',
  'district': '🏙️', 'county': '🏙️',
  'statename': '🏛️', 'state': '🏛️', 'province': '🏛️',
  'latitude': '🌐', 'lat': '🌐',
  'longitude': '🌐', 'lon': '🌐', 'lng': '🌐',
  'country': '🚩', 'countrycode': '🚩'
};

function getAttrIcon(key){
  const clean = key.toLowerCase().replace(/[^a-z]/g, '');
  return ICON_MAP[clean] || '📌';
}

// ── INITIALIZE MAIN PERSISTENT MAP ───────────────────────────────
function initMainMap(){
  if(mainMap) return;
  const mapEl = $('mainMap');
  if(!mapEl || typeof L === 'undefined') return;
  mainMap = L.map('mainMap', {zoomControl:true, attributionControl:false}).setView([C.lat, C.lon], 5);
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{maxZoom:18, noWrap:true}).addTo(mainMap);
  mapMarkersGroup = L.layerGroup().addTo(mainMap);
  
  L.circleMarker([C.lat, C.lon],{
    radius:12,fillColor:T.p,color:'#fff',weight:2.5,opacity:1,fillOpacity:.85
  }).addTo(mapMarkersGroup).bindPopup('<b>'+C.name+'</b><br>'+C.subtitle).openPopup();
}

function updateMapMarkers(records, focusLocationName){
  if(!mainMap || !mapMarkersGroup) return;
  mapMarkersGroup.clearLayers();
  
  const f = NAV.fields;
  const validPoints = [];
  
  (records||[]).forEach((r, idx)=>{
    const lat = parseFloat(val(r,f.lat));
    const lon = parseFloat(val(r,f.lon));
    const pin = val(r,f.pin)||'—';
    let place = val(r,f.city)||val(r,f.dist)||val(r,f.state)||C.name;
    let realCity = '';
    if (C.code === 'IN' && r['officename']) {
        realCity = String(r['officename']).replace(/ (B\.O|S\.O|H\.O|V\.O|Branch Office|Sub Office|Head Office)/ig, '').trim();
        realCity = realCity.replace(/[\-,]+$/, '').trim();
        if (realCity) place = realCity;
    }
    
    if(!isNaN(lat) && !isNaN(lon) && lat!==0 && lon!==0){
      validPoints.push([lat, lon]);
      const m = L.circleMarker([lat, lon],{
        radius:7,fillColor:T.p,color:'#fff',weight:1.5,opacity:0.9,fillOpacity:.75
      });
      m.bindPopup('<b>'+pin+'</b><br>'+place+'<br><button style="margin-top:.4rem;padding:.2rem .6rem;background:var(--p);color:#000;border-radius:4px;font-weight:bold;font-size:11px;" onclick="showDetail('+idx+')">View Details →</button>');
      mapMarkersGroup.addLayer(m);
    }
  });

  if(validPoints.length > 0){
    if(validPoints.length === 1){
      mainMap.flyTo(validPoints[0], 13, {duration: 1.2});
    } else {
      const bounds = L.latLngBounds(validPoints);
      mainMap.fitBounds(bounds, {padding: [30, 30], maxZoom: 14});
    }
    $('mapBadge').textContent = 'MAP: ' + (focusLocationName || C.name) + ' (' + validPoints.length + ' mapped points)';
  } else {
    mainMap.flyTo([C.lat, C.lon], 5, {duration: 1.2});
    $('mapBadge').textContent = 'MAP: ' + C.name + ' Interactive Map';
  }
}

// ── BREADCRUMB ──────────────────────────────────────────────────
function updateBC(){
  const items = [['&#127760; '+C.name, ()=>goBack(0)]];
  if(NAV.stateFile) items.push([NAV.stateFile.replace('.json','').replace(/-/g,' ').replace(/\b\w/g,x=>x.toUpperCase()), ()=>goBack(1)]);
  if(NAV.district)  items.push([NAV.district, ()=>goBack(2)]);
  if(NAV.city && !NAV.usingCitiesS1) items.push([NAV.city, ()=>goBack(3)]);
  const bc=$('bc');
  bc.innerHTML = items.map((it,i)=>{
    const isLast = i===items.length-1;
    const cls = isLast ? 'bc-item bc-cur' : 'bc-item';
    return '<span class="'+cls+'" '+(isLast?'':'')+'>'+it[0]+'</span>'+(isLast?'':' <span class="bc-sep">›</span> ');
  }).join('');
  bc.querySelectorAll('.bc-item:not(.bc-cur)').forEach((el,i)=>{
    el.addEventListener('click', items[i][1]);
  });
}

// ── STEP 0: LOAD STATES ─────────────────────────────────────────
async function loadStates(){
  try{
    const apiUrl = C.code === 'IN' ? 'https://api.github.com/repos/chaitanyadev999/pincode-dataindia/contents' : 'https://api.github.com/repos/chaitanyadev999/pincode-dataindia/contents/world/'+C.code;
      const r = await fetch(apiUrl);
    if(!r.ok) throw new Error(r.status);
    const files = await r.json();
    const states = files.filter(f=>f.name.endsWith('.json'));
    $('statRegions').textContent = states.length;
    setCount('s0cnt', states.length, 'Region');
    if(!states.length){ $('stGrid').innerHTML='<div class="err-box">No data available for this country yet.</div>'; return; }
    $('stGrid').innerHTML = states.map(f=>{
      const label = f.name.replace('.json','').replace(/-/g,' ').replace(/\b\w/g,x=>x.toUpperCase());
      return '<div class="state-card" onclick="selectState(\''+f.name+'\',\''+label+'\')">'+
        '<span class="state-name">'+label+'</span><span class="state-arr">&#8594;</span></div>';
    }).join('');
  }catch(e){
    $('stGrid').innerHTML='<div class="err-box">Could not load regions.<button class="retry-btn" onclick="loadStates()">Retry</button></div>';
  }
}

// ── SELECT STATE → LOAD DATA → SHOW CITIES ──────────────────────
async function selectState(file, label){
  NAV.stateFile = file;
  NAV.city = null; NAV.district = null;
  document.querySelectorAll('.state-card').forEach(c=>c.classList.remove('active'));
  if (event && event.currentTarget) event.currentTarget.classList.add('active');
  toast('Loading '+label+'...','info');
  hide('s1','s2','s3','s4');
  try{
    const r = await fetch(C.dataBase+file);
    if(!r.ok) throw new Error(r.status);
    NAV.data = await r.json();
    NAV.fields = detectFields(NAV.data);
    updateMapMarkers(NAV.data, label);
    showCities();
  }catch(e){ console.warn('Places unavailable'); }
}

// ── LATEST UPDATES (BLOG) ──
function loadBlogPosts() {
  const codeLower = C.code.toLowerCase();
  fetch(`https://www.blogger.com/feeds/7898864703908862562/posts/default/-/${codeLower}?alt=json&max-results=3`)
    .then(r => r.json())
    .then(data => {
      const feed = data.feed;
      if(feed && feed.entry && feed.entry.length > 0) {
        let html = '<div class="sec-hdr" style="margin-top:3rem;"><h2 class="sec-title">Latest Updates</h2></div><div class="city-grid" style="grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:1rem;">';
        feed.entry.forEach(p => {
           let title = p.title.$t;
           let link = p.link.find(l => l.rel === 'alternate').href;
           html += `<a href="${link}" target="_blank" class="city-card" style="text-align:left;display:block;"><h3 style="font-size:.95rem;margin:0 0 .5rem 0;color:var(--t);">${title}</h3><p style="font-size:.8rem;color:var(--p);margin:0;">Read more &rarr;</p></a>`;
        });
        html += '</div>';
        const d = document.createElement('div');
        d.className = 'sec';
        d.innerHTML = html;
        document.getElementById('s0').appendChild(d);
      }
    }).catch(e => console.log('No posts found.'));
}
loadBlogPosts();

  // ── INITIALIZE ──
// ── STEP 1: DISTRICTS (BATCH PAGINATION - 60 AT A TIME) ─────────────
function showCities(){
  NAV.distsList = uniq(NAV.data.map(r=>val(r,NAV.fields.dist)));
  NAV.distLimit = 60;
  const stLabel = (NAV.stateFile||'').replace('.json','').replace(/-/g,' ').replace(/\b\w/g,x=>x.toUpperCase());
  
  if(!NAV.distsList.length || (NAV.distsList.length===1 && !NAV.distsList[0])){
    NAV.distsList = uniq(NAV.data.map(r=>val(r,NAV.fields.city)));
    $('s1title').textContent = stLabel + (' — Cities');
      setCount('s1cnt', NAV.distsList.length, 'City');
    NAV.usingCitiesS1 = true;
  } else {
    $('s1title').textContent = stLabel + ' — Districts';
    setCount('s1cnt', NAV.distsList.length, 'District');
    NAV.usingCitiesS1 = false;
  }

  if(!NAV.distsList.length){
    NAV.city = 'All'; NAV.district = 'All';
    showPins(NAV.data);
    return;
  }
  renderCityBatch();
  show('s1'); hide('s2','s3','s4');
  updateBC();
  $('s1').scrollIntoView({behavior:'smooth',block:'start'});
}

function renderCityBatch(){
  const batch = NAV.distsList.slice(0, NAV.distLimit);
  $('cityGrid').innerHTML = batch.map(d=>'<div class="city-card" onclick="selectCity(\''+escQ(d)+'\')">'+d+'</div>').join('');
  if (NAV.distsList.length > NAV.distLimit) {
    const lbl = NAV.usingCitiesS1 ? 'cities' : 'districts';
    $('cityLoadWrap').innerHTML = `
      <div class="load-more-wrap">
        <button class="load-more-btn" onclick="moreCities()">Load More (+60) &#8594;</button>
        <div class="load-cnt-tag">Showing ${batch.length} of ${NAV.distsList.length} ${lbl}</div>
      </div>`;
  } else {
    $('cityLoadWrap').innerHTML = '';
  }
}

window.moreCities = function(){
  NAV.distLimit += 60;
  renderCityBatch();
};

// ── SELECT DISTRICT → SHOW CITIES (BATCH PAGINATION - 60 AT A TIME) ─────
function selectCity(dist){
  if(NAV.usingCitiesS1){
    NAV.city = dist; NAV.district = dist;
    const filtered = NAV.data.filter(r=>val(r,NAV.fields.city)===dist);
    updateMapMarkers(filtered, dist);
    showPins(filtered);
    return;
  }

  NAV.district = dist; NAV.city = null;
  const filtered = NAV.data.filter(r=>val(r,NAV.fields.dist)===dist);
  NAV.citiesList = uniq(filtered.map(r=>val(r,NAV.fields.city)));
  NAV.cityLimit = 60;
  NAV.filteredDistData = filtered;

  updateMapMarkers(filtered, dist);

  if(!NAV.citiesList.length || (NAV.citiesList.length===1 && !NAV.citiesList[0])){
    NAV.city = dist;
    showPins(filtered);
    return;
  }
  $('s2title').textContent = dist + (' — Cities');
    setCount('s2cnt', NAV.citiesList.length, 'City');
  renderDistBatch();
  show('s2'); hide('s3','s4');
  updateBC();
  $('s2').scrollIntoView({behavior:'smooth',block:'start'});
}

function renderDistBatch(){
  const batch = NAV.citiesList.slice(0, NAV.cityLimit);
  $('distGrid').innerHTML = batch.map(c=>'<div class="city-card" onclick="selectDist(\''+escQ(NAV.district)+'\',\''+escQ(c)+'\')">'+c+'</div>').join('');
  if (NAV.citiesList.length > NAV.cityLimit) {
    $('distLoadWrap').innerHTML = `
      <div class="load-more-wrap">
        <button class="load-more-btn" onclick="moreDists()">Load More (+60) &#8594;</button>
        <div class="load-cnt-tag">Showing ${batch.length} of ${NAV.citiesList.length} cities</div>
      </div>`;
  } else {
    $('distLoadWrap').innerHTML = '';
  }
}

window.moreDists = function(){
  NAV.cityLimit += 60;
  renderDistBatch();
};

// ── SELECT CITY → SHOW PINCODES ─────────────────────────────
function selectDist(dist, city){
  NAV.city = city;
  const filtered = NAV.data.filter(r=>val(r,NAV.fields.dist)===dist && val(r,NAV.fields.city)===city);
  updateMapMarkers(filtered, city);
  showPins(filtered);
}

// ── STEP 3: PINCODES (BATCH PAGINATION - 60 AT A TIME) ──────────
function showPins(records){
  NAV.pinsList = records;
  NAV.pinLimit = 60;
  $('s3title').textContent = (NAV.district||NAV.city||'') + ' — '+C.term+'s';
  setCount('s3cnt', records.length, C.term);
  renderPinBatch();
  show('s3'); hide('s4');
  updateBC();
  $('s3').scrollIntoView({behavior:'smooth',block:'start'});
}

function renderPinBatch(){
  const batch = NAV.pinsList.slice(0, NAV.pinLimit);
  const f = NAV.fields;
  $('pinGrid').innerHTML = batch.map((r,i)=>{
    const pin = val(r,f.pin)||'—';
    const place = val(r,f.city)||val(r,f.dist)||'';
    const meta = val(r,f.dist)||val(r,f.state)||'';
    return '<div class="pin-card" onclick="showDetail('+i+')">'+
      '<div class="pin-num">'+pin+'</div>'+
      (place?'<div class="pin-place">'+place+'</div>':'')+
      (meta?'<div class="pin-meta">'+meta+'</div>':'')+
    '</div>';
  }).join('');

  if (NAV.pinsList.length > NAV.pinLimit) {
    $('pinLoadWrap').innerHTML = `
      <div class="load-more-wrap">
        <button class="load-more-btn" onclick="morePins()">Load More (+60) &#8594;</button>
        <div class="load-cnt-tag">Showing ${batch.length} of ${NAV.pinsList.length} ${C.term}s</div>
      </div>`;
  } else {
    $('pinLoadWrap').innerHTML = '';
  }
}

window.morePins = function(){
  NAV.pinLimit += 60;
  renderPinBatch();
};

// ── STEP 4: FULL ATTRIBUTES DETAIL WITH ICONS ─────────────────────
function showDetail(idx){
  const r = NAV.pinsList[idx];
  if(!r) return;
  const f = NAV.fields;
  const pin   = val(r,f.pin)||'—';
  let place = val(r,f.city)||val(r,f.dist)||val(r,f.state)||C.name;
    let realCity = '';
    if (C.code === 'IN' && r['officename']) {
        realCity = String(r['officename']).replace(/ (B\.O|S\.O|H\.O|V\.O|Branch Office|Sub Office|Head Office)/ig, '').trim();
        realCity = realCity.replace(/[\-,]+$/, '').trim();
        if (realCity) place = realCity;
    }
  const lat   = parseFloat(val(r,f.lat))||null;
  const lon   = parseFloat(val(r,f.lon))||null;

  $('diPin').textContent = pin;
  $('diPlace').textContent = place;
  $('s4title').textContent = '📍 ' + C.term + ' Details: ' + pin;

  let badgesHtml = '';
  if(r['officetype']) badgesHtml += '<span class="di-badge">🏷️ Type: '+r['officetype']+'</span> ';
  if(r['delivery']) {
    const isDel = String(r['delivery']).toLowerCase().includes('delivery');
    badgesHtml += '<span class="di-badge '+(isDel?'delivery':'')+'">🚚 '+r['delivery']+'</span>';
  }
  $('diBadges').innerHTML = badgesHtml;

  // Render ALL Attributes into SIDE-BY-SIDE BOX CARDS WITH SPECIFIC EMOJI ICONS
  const keys = Object.keys(r);
  const itemsHtml = keys.map(key => {
    let value = r[key];
    if(value === null || value === undefined || value === '') value = '—';
    let label = key.replace(/_/g, ' ').replace(/([A-Z])/g, ' $1').trim();
    label = label.charAt(0).toUpperCase() + label.slice(1);
    const low = label.toLowerCase();
    if(low === 'county') label = 'District';
    if(low === 'circlename') label = 'Circle';
      if(low === 'regionname') label = 'Region';
      if(low === 'divisionname') { label = 'Division'; if(typeof value === 'string') value = value.replace(/Division/i, '').trim(); }
      if(low === 'officename') label = 'Post Office';
    if(low === 'statename') label = 'State Name';
    if(low === 'officetype') label = 'Office Type';
    
    const icon = getAttrIcon(key);
    return `<div class="di-item">
      <div class="di-item-lbl"><span>${icon}</span> ${label}</div>
      <div class="di-item-val">${value}</div>
    </div>`;
  }).join('');

  
    let realCityHtml = '';
    if (C.code === 'IN' && realCity) {
        realCityHtml = `<div class="di-item">
          <div class="di-item-lbl"><span>🏙️</span> City</div>
          <div class="di-item-val" style="color:var(--p);font-weight:600">${realCity}</div>
        </div>`;
    }
    
    $('diGrid').innerHTML = realCityHtml + itemsHtml + (C.code==='IN' ? `<div style='grid-column: 1 / -1; font-size:0.85rem; color:#888; background:rgba(255,255,255,0.03); padding:8px 12px; border-radius:6px; margin-top:5px;'><b>💡 Abbreviations:</b> B.O = Branch Office, S.O = Sub Office, H.O = Head Office, V.O = Village Office</div>` : '');

  const mapQ = encodeURIComponent(place + ' ' + pin + ' ' + C.name);
  $('diActions').innerHTML =
    (lat&&lon ? '<a class="da-btn prim" href="https://maps.google.com/?q='+lat+','+lon+'" target="_blank">🗺️ Open in Google Maps</a>' : '')+
    '<a class="da-btn sec" href="https://maps.google.com/maps?q='+mapQ+'" target="_blank">🔍 Search Location</a>';

  show('s4'); updateBC();
  $('s4').scrollIntoView({behavior:'smooth',block:'start'});

  if(lat && lon && !isNaN(lat) && !isNaN(lon)){
    updateMapMarkers([r], place + ' - ' + pin);
  }
}

// ── BACK NAVIGATION ──────────────────────────────────────────────
function goBack(fromStep){
  if(fromStep<=1){ hide('s1','s2','s3','s4'); show('s0'); NAV.stateFile=null; NAV.city=null; NAV.district=null; NAV.usingCitiesS1=false; }
  else if(fromStep===2){ hide('s2','s3','s4'); show('s1'); NAV.city=null; NAV.district=null; }
  else if(fromStep===3){ hide('s3','s4'); show('s2'); NAV.city=null; }
  else if(fromStep===4){ hide('s4'); show('s3'); }
  updateBC();
  window.scrollTo({top:0,behavior:'smooth'});
}
window.goBack = goBack;
window.selectState = selectState;
window.selectCity = selectCity;
window.selectDist = selectDist;
window.showDetail = showDetail;

// ── SEARCH ──────────────────────────────────────────────────────
function doSearch(){
  const q=$('search').value.trim().toLowerCase(); if(!q)return;
  if(!NAV.data.length){toast('Select a region first','info');return;}
  const hits = NAV.data.filter(r=>Object.values(r).some(v=>String(v).toLowerCase().includes(q)));
  if(!hits.length){toast('No results found','err');return;}
  NAV.city='Search'; NAV.district='Results';
  showPins(hits);
  updateMapMarkers(hits, 'Search: ' + q);
  toast('Found '+hits.length+' results','ok');
}
window.doSearch = doSearch;
$('search').addEventListener('keypress',e=>{if(e.key==='Enter')doSearch();});

// ── ESCAPE QUOTES ────────────────────────────────────────────────
function escQ(s){ return s.replace(/'/g,"\\'").replace(/"/g,'&quot;'); }

// ── SCROLL NAV ───────────────────────────────────────────────────
window.addEventListener('scroll',()=>$('nav').classList.toggle('sc',scrollY>50),{passive:true});
$('yr').textContent=new Date().getFullYear();
updateBC();
initMainMap();
loadStates();
})();