
const document = { 
  getElementById: (id) => { 
    if(id === 'heroSearch') return { value: 'india', addEventListener: ()=>{} }; 
    return {addEventListener: ()=>{}, scrollIntoView: ()=>{}}; 
  }, 
  querySelectorAll: () => [] 
}; 
const window = { location: { href: '' }, addEventListener: ()=>{} }; 
let curSearch = ''; 
function renderAll(){} 
let globalIndex = { cities: { india: 'pages/moldova/Grigoriopol_Tr..html' }, states: {}, pincodes: {} }; 
async function loadGlobalIndex() {} 
const ALL=[{name: 'India', code: 'IN'}]; 

(function(){
'use strict';

const COUNTRIES = [
  {code:'IN',name:'India',region:'asia',term:'PIN Code',phone:'+91', lat:20.5937,lon:78.9629},
  {code:'US',name:'United States',region:'americas',term:'ZIP Code',phone:'+1', lat:39.8283,lon:-98.5795},
  {code:'GB',name:'United Kingdom',region:'europe',term:'Postcode',phone:'+44', lat:55.3781,lon:-3.4360},
  {code:'AU',name:'Australia',region:'oceania',term:'Postcode',phone:'+61', lat:-25.2744,lon:133.7751},
  {code:'CA',name:'Canada',region:'americas',term:'Postal Code',phone:'+1', lat:56.1304,lon:-106.3468},
  {code:'DE',name:'Germany',region:'europe',term:'Postal Code',phone:'+49', lat:51.1657,lon:10.4515},
  {code:'FR',name:'France',region:'europe',term:'Code Postal',phone:'+33', lat:46.2276,lon:2.2137},
  {code:'JP',name:'Japan',region:'asia',term:'Postal Code',phone:'+81', lat:36.2048,lon:138.2529},
  {code:'AE',name:'UAE',region:'asia',term:'Postal Code',phone:'+971', lat:23.4241,lon:53.8478},
  {code:'SG',name:'Singapore',region:'asia',term:'Postal Code',phone:'+65', lat:1.3521,lon:103.8198},
  {code:'BR',name:'Brazil',region:'americas',term:'CEP',phone:'+55', lat:-14.2350,lon:-51.9253},
  {code:'CN',name:'China',region:'asia',term:'Postal Code',phone:'+86', lat:35.8617,lon:104.1954},
  {code:'KR',name:'South Korea',region:'asia',term:'Postal Code',phone:'+82', lat:35.9078,lon:127.7669},
  {code:'MX',name:'Mexico',region:'americas',term:'Código Postal',phone:'+52', lat:23.6345,lon:-102.5528},
  {code:'NZ',name:'New Zealand',region:'oceania',term:'Postcode',phone:'+64', lat:-40.9006,lon:174.8860},
  {code:'BD',name:'Bangladesh',region:'asia',term:'Postal Code',phone:'+880', lat:23.6850,lon:90.3563},
  {code:'LK',name:'Sri Lanka',region:'asia',term:'Postal Code',phone:'+94', lat:7.8731,lon:80.7718},
  {code:'TH',name:'Thailand',region:'asia',term:'Postal Code',phone:'+66', lat:15.8700,lon:100.9925},
  {code:'MY',name:'Malaysia',region:'asia',term:'Postcode',phone:'+60', lat:4.2105,lon:101.9758},
  {code:'PH',name:'Philippines',region:'asia',term:'Postal Code',phone:'+63', lat:12.8797,lon:121.7740},
  {code:'RU',name:'Russia',region:'europe',term:'Postal Code',phone:'+7', lat:61.5240,lon:105.3188},
  {code:'IT',name:'Italy',region:'europe',term:'CAP',phone:'+39', lat:41.8719,lon:12.5674},
  {code:'ES',name:'Spain',region:'europe',term:'Postal Code',phone:'+34', lat:40.4637,lon:-3.7492},
  {code:'NL',name:'Netherlands',region:'europe',term:'Postal Code',phone:'+31', lat:52.1326,lon:5.2913},
  {code:'PT',name:'Portugal',region:'europe',term:'Postal Code',phone:'+351', lat:39.3999,lon:-8.2245},
  {code:'PK',name:'Pakistan',region:'asia',term:'Postal Code',phone:'+92', lat:30.3753,lon:69.3451},
    {code:'PL',name:'Poland',region:'europe',term:'Postal Code',phone:'+48', lat:51.9194,lon:19.1451},
  {code:'ZA',name:'South Africa',region:'africa',term:'Postal Code',phone:'+27', lat:-30.5595,lon:22.9375},
  {code:'TR',name:'Turkey',region:'asia',term:'Postal Code',phone:'+90', lat:38.9637,lon:35.2433},
  {code:'AR',name:'Argentina',region:'americas',term:'Postal Code',phone:'+54', lat:-38.4161,lon:-63.6167},
  {code:'AD',name:'Andorra',region:'europe',term:'Postal Code',phone:'+376', lat:42.5063,lon:1.5218},
  {code:'AI',name:'Anguilla',region:'americas',term:'Postal Code',phone:'+1', lat:18.2206,lon:-63.0686},
  {code:'AL',name:'Albania',region:'europe',term:'Postal Code',phone:'+355', lat:41.1533,lon:20.1683},
  {code:'AS',name:'American Samoa',region:'oceania',term:'ZIP Code',phone:'+1', lat:-14.2710,lon:-170.1322},
  {code:'AT',name:'Austria',region:'europe',term:'Postal Code',phone:'+43', lat:47.5162,lon:14.5501},
  {code:'AX',name:'Aland Islands',region:'europe',term:'Postal Code',phone:'+358', lat:60.1785,lon:19.9156},
  {code:'AZ',name:'Azerbaijan',region:'asia',term:'Postal Code',phone:'+994', lat:40.1431,lon:47.5769},
  {code:'BE',name:'Belgium',region:'europe',term:'Postal Code',phone:'+32', lat:50.5039,lon:4.4699},
  {code:'BG',name:'Bulgaria',region:'europe',term:'Postal Code',phone:'+359', lat:42.7339,lon:25.4858},
  {code:'BM',name:'Bermuda',region:'americas',term:'Postal Code',phone:'+1', lat:32.3078,lon:-64.7505},
  {code:'BY',name:'Belarus',region:'europe',term:'Postal Code',phone:'+375', lat:53.7098,lon:27.9534},
  {code:'CC',name:'Cocos Islands',region:'oceania',term:'Postal Code',phone:'+61', lat:-12.1642,lon:96.8710},
  {code:'CH',name:'Switzerland',region:'europe',term:'Postal Code',phone:'+41', lat:46.8182,lon:8.2275},
  {code:'CL',name:'Chile',region:'americas',term:'Postal Code',phone:'+56', lat:-35.6751,lon:-71.5430},
  {code:'CO',name:'Colombia',region:'americas',term:'Postal Code',phone:'+57', lat:4.5709,lon:-74.2973},
  {code:'CR',name:'Costa Rica',region:'americas',term:'Postal Code',phone:'+506', lat:9.7489,lon:-83.7534},
  {code:'CX',name:'Christmas Island',region:'oceania',term:'Postal Code',phone:'+61', lat:-10.4475,lon:105.6904},
  {code:'CY',name:'Cyprus',region:'europe',term:'Postal Code',phone:'+357', lat:35.1264,lon:33.4299},
  {code:'CZ',name:'Czech Republic',region:'europe',term:'Postal Code',phone:'+420', lat:49.8175,lon:15.4730},
  {code:'DK',name:'Denmark',region:'europe',term:'Postal Code',phone:'+45', lat:56.2639,lon:9.5018},
  {code:'DO',name:'Dominican Republic',region:'americas',term:'Postal Code',phone:'+1', lat:18.7357,lon:-70.1627},
  {code:'DZ',name:'Algeria',region:'africa',term:'Postal Code',phone:'+213', lat:28.0339,lon:1.6596},
  {code:'EC',name:'Ecuador',region:'americas',term:'Postal Code',phone:'+593', lat:-1.8312,lon:-78.1834},
  {code:'EE',name:'Estonia',region:'europe',term:'Postal Code',phone:'+372', lat:58.5953,lon:25.0136},
  {code:'FI',name:'Finland',region:'europe',term:'Postal Code',phone:'+358', lat:61.9241,lon:25.7482},
  {code:'FK',name:'Falkland Islands',region:'americas',term:'Postal Code',phone:'+500', lat:-51.7963,lon:-59.5236},
  {code:'FM',name:'Micronesia',region:'oceania',term:'ZIP Code',phone:'+691', lat:7.4256,lon:150.5508},
  {code:'FO',name:'Faroe Islands',region:'europe',term:'Postal Code',phone:'+298', lat:61.8926,lon:-6.9118},
  {code:'GF',name:'French Guiana',region:'americas',term:'Code Postal',phone:'+594', lat:3.9339,lon:-53.1258},
  {code:'GG',name:'Guernsey',region:'europe',term:'Postcode',phone:'+44', lat:49.4657,lon:-2.5853},
  {code:'GI',name:'Gibraltar',region:'europe',term:'Postcode',phone:'+350', lat:36.1408,lon:-5.3536},
  {code:'GL',name:'Greenland',region:'americas',term:'Postal Code',phone:'+299', lat:71.7069,lon:-42.6043},
  {code:'GP',name:'Guadeloupe',region:'americas',term:'Code Postal',phone:'+590', lat:16.2650,lon:-61.5510},
  {code:'GS',name:'South Georgia',region:'americas',term:'Postal Code',phone:'+500', lat:-54.4296,lon:-36.5879},
  {code:'GT',name:'Guatemala',region:'americas',term:'Postal Code',phone:'+502', lat:15.7835,lon:-90.2308},
  {code:'GU',name:'Guam',region:'oceania',term:'ZIP Code',phone:'+1', lat:13.4443,lon:144.7937},
  {code:'HK',name:'Hong Kong',region:'asia',term:'Postal Code',phone:'+852', lat:22.3193,lon:114.1694},
  {code:'HM',name:'Heard Island',region:'oceania',term:'Postal Code',phone:'+672', lat:-53.0818,lon:73.5042},
  {code:'HN',name:'Honduras',region:'americas',term:'Postal Code',phone:'+504', lat:15.2000,lon:-86.2419},
  {code:'HR',name:'Croatia',region:'europe',term:'Postal Code',phone:'+385', lat:45.1000,lon:15.2000},
  {code:'HT',name:'Haiti',region:'americas',term:'Postal Code',phone:'+509', lat:18.9712,lon:-72.2852},
  {code:'HU',name:'Hungary',region:'europe',term:'Postal Code',phone:'+36', lat:47.1625,lon:19.5033},
  {code:'ID',name:'Indonesia',region:'asia',term:'Postal Code',phone:'+62', lat:-0.7893,lon:113.9213},
  {code:'IE',name:'Ireland',region:'europe',term:'Eircode',phone:'+353', lat:53.1424,lon:-7.6921},
  {code:'IM',name:'Isle of Man',region:'europe',term:'Postcode',phone:'+44', lat:54.2361,lon:-4.5481},
  {code:'IO',name:'British Indian Ocean',region:'asia',term:'Postal Code',phone:'+246', lat:-6.3432,lon:71.8765},
  {code:'IS',name:'Iceland',region:'europe',term:'Postal Code',phone:'+354', lat:64.9631,lon:-19.0208},
  {code:'JE',name:'Jersey',region:'europe',term:'Postcode',phone:'+44', lat:49.2144,lon:-2.1313},
  {code:'KE',name:'Kenya',region:'africa',term:'Postal Code',phone:'+254', lat:-0.0236,lon:37.9062},
  {code:'LI',name:'Liechtenstein',region:'europe',term:'Postal Code',phone:'+423', lat:47.1660,lon:9.5554},
  {code:'LT',name:'Lithuania',region:'europe',term:'Postal Code',phone:'+370', lat:55.1694,lon:23.8813},
  {code:'LU',name:'Luxembourg',region:'europe',term:'Postal Code',phone:'+352', lat:49.8153,lon:6.1296},
  {code:'LV',name:'Latvia',region:'europe',term:'Postal Code',phone:'+371', lat:56.8796,lon:24.6032},
  {code:'MA',name:'Morocco',region:'africa',term:'Code Postal',phone:'+212', lat:31.7917,lon:-7.0926},
  {code:'MC',name:'Monaco',region:'europe',term:'Code Postal',phone:'+377', lat:43.7384,lon:7.4246},
  {code:'MD',name:'Moldova',region:'europe',term:'Postal Code',phone:'+373', lat:47.4116,lon:28.3699},
  {code:'MH',name:'Marshall Islands',region:'oceania',term:'ZIP Code',phone:'+692', lat:7.1315,lon:171.1845},
  {code:'MK',name:'North Macedonia',region:'europe',term:'Postal Code',phone:'+389', lat:41.6086,lon:21.7453},
  {code:'MO',name:'Macao',region:'asia',term:'Postal Code',phone:'+853', lat:22.1987,lon:113.5439},
  {code:'MP',name:'N. Mariana Islands',region:'oceania',term:'ZIP Code',phone:'+1', lat:17.3308,lon:145.3847},
  {code:'MQ',name:'Martinique',region:'americas',term:'Code Postal',phone:'+596', lat:14.6415,lon:-61.0242},
  {code:'MT',name:'Malta',region:'europe',term:'Postal Code',phone:'+356', lat:35.9375,lon:14.3754},
  {code:'MW',name:'Malawi',region:'africa',term:'Postal Code',phone:'+265', lat:-13.2543,lon:34.3015},
  {code:'NC',name:'New Caledonia',region:'oceania',term:'Code Postal',phone:'+687', lat:-20.9043,lon:165.6180},
  {code:'NF',name:'Norfolk Island',region:'oceania',term:'Postal Code',phone:'+672', lat:-29.0408,lon:167.9547},
  {code:'NO',name:'Norway',region:'europe',term:'Postal Code',phone:'+47', lat:60.4720,lon:8.4689},
  {code:'NR',name:'Nauru',region:'oceania',term:'Postal Code',phone:'+674', lat:-0.5228,lon:166.9315},
  {code:'NU',name:'Niue',region:'oceania',term:'Postal Code',phone:'+683', lat:-19.0544,lon:-169.8672},
  {code:'PA',name:'Panama',region:'americas',term:'Postal Code',phone:'+507', lat:8.5380,lon:-80.7821},
  {code:'PE',name:'Peru',region:'americas',term:'Postal Code',phone:'+51', lat:-9.1900,lon:-75.0152},
  {code:'PF',name:'French Polynesia',region:'oceania',term:'Code Postal',phone:'+689', lat:-17.6797,lon:-149.4068},
  {code:'PM',name:'St Pierre & Miquelon',region:'americas',term:'Code Postal',phone:'+508', lat:46.8852,lon:-56.3159},
  {code:'PN',name:'Pitcairn',region:'oceania',term:'Postal Code',phone:'+870', lat:-24.7036,lon:-127.4393},
  {code:'PR',name:'Puerto Rico',region:'americas',term:'ZIP Code',phone:'+1', lat:18.2208,lon:-66.5901},
  {code:'PW',name:'Palau',region:'oceania',term:'ZIP Code',phone:'+680', lat:7.5150,lon:134.5825},
  {code:'RE',name:'Reunion',region:'africa',term:'Code Postal',phone:'+262', lat:-21.1151,lon:55.5364},
  {code:'RO',name:'Romania',region:'europe',term:'Postal Code',phone:'+40', lat:45.9432,lon:24.9668},
  {code:'RS',name:'Serbia',region:'europe',term:'Postal Code',phone:'+381', lat:44.0165,lon:21.0059},
  {code:'SE',name:'Sweden',region:'europe',term:'Postal Code',phone:'+46', lat:60.1282,lon:18.6435},
  {code:'SI',name:'Slovenia',region:'europe',term:'Postal Code',phone:'+386', lat:46.1512,lon:14.9955},
  {code:'SJ',name:'Svalbard & Jan Mayen',region:'europe',term:'Postal Code',phone:'+47', lat:77.5536,lon:23.6703},
  {code:'SK',name:'Slovakia',region:'europe',term:'Postal Code',phone:'+421', lat:48.6690,lon:19.6990},
  {code:'SM',name:'San Marino',region:'europe',term:'Postal Code',phone:'+378', lat:43.9424,lon:12.4578},
  {code:'TC',name:'Turks & Caicos',region:'americas',term:'Postal Code',phone:'+1', lat:21.6940,lon:-71.7979},
  {code:'UA',name:'Ukraine',region:'europe',term:'Postal Code',phone:'+380', lat:48.3794,lon:31.1656},
  {code:'UY',name:'Uruguay',region:'americas',term:'Postal Code',phone:'+598', lat:-32.5228,lon:-55.7658},
  {code:'VA',name:'Vatican City',region:'europe',term:'Postal Code',phone:'+39', lat:41.9029,lon:12.4534},
  {code:'VI',name:'US Virgin Islands',region:'americas',term:'ZIP Code',phone:'+1', lat:18.3358,lon:-64.8963},
  {code:'WF',name:'Wallis & Futuna',region:'oceania',term:'Code Postal',phone:'+681', lat:-13.7687,lon:-177.1561},
  {code:'WS',name:'Samoa',region:'oceania',term:'Postal Code',phone:'+685', lat:-13.7590,lon:-172.1046},
  {code:'YT',name:'Mayotte',region:'africa',term:'Code Postal',phone:'+262', lat:-12.8275,lon:45.1662},
  {code:'IT',name:'Italy',region:'europe',term:'CAP',phone:'+39', lat:41.8719,lon:12.5674},
];

// deduplicate
const seen=new Set(), ALL=[];
COUNTRIES.forEach(c=>{ if(!seen.has(c.code)){seen.add(c.code);ALL.push(c);} });

const PRIORITY=['IN','US','GB','AU','CA','DE','FR','JP','AE','SG','BR','CN','KR','MX','NZ','BD','LK','TH','MY','PH','RU','IT','ES','NL','PT','PL','ZA','TR','AR'];
const SPECIAL={'IN':'../pages/india.html', 'US':'../pages/usa.html'};

function pageUrl(code){ return SPECIAL[code]||('/pages/'+code.toLowerCase()+'.html'); }
function fSrc(code,w){ return 'https://flagcdn.com/w'+(w||80)+'/'+code.toLowerCase()+'.png'; }
function fImg(code,cls,w){
  return '<img src="'+fSrc(code,w||80)+'" class="'+cls+'" alt="'+code+'" onerror="this.style.display=\'none\'">';
}

function cardNav(c){
  showToast('Opening '+c.name+'...','info');
  document.getElementById('globeMount').scrollIntoView({behavior:'smooth',block:'center'});
  
    window.location.href=pageUrl(c.code);
  
}

// ── RENDER CARDS ──
let curFilter='all', curSearch='';

function filterCountries(){
  return ALL.filter(c=>{
    const matchReg = curFilter==='all' || c.region===curFilter;
    const matchSearch = !curSearch ||
      c.name.toLowerCase().includes(curSearch.toLowerCase()) ||
      c.code.toLowerCase().includes(curSearch.toLowerCase()) ||
      c.term.toLowerCase().includes(curSearch.toLowerCase());
    return matchReg && matchSearch;
  });
}

function renderPriority(){
  const pList = ALL.filter(c=>PRIORITY.includes(c.code)).slice(0,12);
  const grid = document.getElementById('priorityGrid');
  grid.innerHTML = pList.map(c=>`
    <div class="pcard" onclick="cardNav({code:'${c.code}',name:'${c.name.replace(/'/g,"\\'")} ',lat:${c.lat},lon:${c.lon},term:'${c.term}'})">
      <div class="pcard-top">
        ${fImg(c.code,'pcard-flag',100)}
        <div>
          <div class="pcard-name">${c.name}</div>
          <div class="pcard-term">${c.term} <span style="margin-left:8px; color:var(--p2); background:rgba(0,0,0,0.4); padding:2px 6px; border-radius:4px; font-size:0.7rem;">${c.phone}</span></div>
        </div>
      </div>
      <div class="pcard-meta">Explore states, cities & postal codes</div>
      <div class="pcard-btn">Browse ${c.name} &#8594;</div>
    </div>
  `).join('');
}

function renderAll(){
  const list = filterCountries();
  const grid = document.getElementById('allGrid');
  if(!list.length){
    grid.innerHTML='<div style="grid-column:1/-1;text-align:center;padding:3rem;color:var(--t3)">No countries match your search.</div>';
    return;
  }
  grid.innerHTML = list.map(c=>`
    <a class="citem" href="${pageUrl(c.code)}">
      <div class="citem-flag-wrap">
        ${fImg(c.code,'citem-flag',320)}
      </div>
      <div class="citem-info">
        <div class="citem-name">${c.name}</div>
        <div class="citem-term">${c.term} Directory</div>
      </div>
      <span class="citem-arr">&#8594;</span>
    </a>
  `).join('');
}

function renderPopular(){
  const pop = PRIORITY.slice(0,10).map(code=>ALL.find(c=>c.code===code)).filter(Boolean);
  document.getElementById('popularChips').innerHTML = pop.map(c=>`
    <div class="lchip" onclick="cardNav({code:'${c.code}',name:'${c.name.replace(/'/g,"\\'")} ',lat:${c.lat},lon:${c.lon},term:'${c.term}'})">
      ${fImg(c.code,'',40)} ${c.name}
    </div>
  `).join('');
}

window.filterBy=function(r,btn){
  curFilter=r;
  document.querySelectorAll('.filter-strip .fb').forEach(b=>b.classList.remove('on'));
  btn.classList.add('on');
  renderAll();
};

window.filterRegion=function(r,chip){
  curFilter=r;
  document.querySelectorAll('#regionChips .lchip').forEach(b=>b.classList.remove('on'));
  chip.classList.add('on');
  document.querySelectorAll('.filter-strip .fb').forEach(b=>{
    b.classList.toggle('on',b.textContent.toLowerCase().startsWith(r)||r==='all');
  });
  renderAll();
  document.getElementById('allSec').scrollIntoView({behavior:'smooth',block:'start'});
};

let globalIndex = null;
async function loadGlobalIndex() {
  if (!globalIndex) {
     try {
       const res = await fetch('assets/search_index.json');
       if (res.ok) globalIndex = await res.json();
     } catch (e) {
       console.error("Failed to load global index", e);
     }
  }
}
document.getElementById('heroSearch').addEventListener('focus', loadGlobalIndex);

window.doSearch = async function() {
  const q = document.getElementById('heroSearch').value.trim().toLowerCase();
  if (!q) {
      curSearch = '';
      renderAll();
      return;
  }

  // Exact Country match has absolute highest priority!
  const lowerV = q.replace(/[^a-z0-9\s-]/g, '').trim();
  if (typeof ALL !== 'undefined') {
      for (let i = 0; i < ALL.length; i++) {
          if (ALL[i].name.toLowerCase() === lowerV || ALL[i].code.toLowerCase() === lowerV) {
              let pageName = ALL[i].code.toLowerCase();
              if (pageName === 'in') pageName = 'india';
              if (pageName === 'us') pageName = 'usa';
              window.location.href = '/pages/' + pageName + '.html';
              return;
          }
      }
  }
  
  if (!globalIndex) {
      await loadGlobalIndex();
  }

  if (globalIndex) {
    if (globalIndex.pincodes && globalIndex.pincodes[q]) {
      window.location.href = '/' + globalIndex.pincodes[q];
      return;
    }
    const cKey = q.replace(/[^a-z0-9\s-]/g, '').trim().replace(/\s+/g, '-');
    if (globalIndex.cities && globalIndex.cities[cKey]) {
      window.location.href = '/' + globalIndex.cities[cKey];
      return;
    }
    const sKey = q.replace(/[^a-z0-9\s-]/g, '').trim().replace(/\s+/g, ' ');
    if (globalIndex.states && globalIndex.states[sKey]) {
      window.location.href = '/' + globalIndex.states[sKey];
      return;
    }

    // Partial match fallback
    if (q.length >= 2) {
        
        // Match Country (partial)
        if (typeof ALL !== 'undefined') {
            for (let i = 0; i < ALL.length; i++) {
                if (ALL[i].name.toLowerCase().includes(lowerV)) {
                    let pageName = ALL[i].code.toLowerCase();
                    if (pageName === 'in') pageName = 'india';
                    if (pageName === 'us') pageName = 'usa';
                    window.location.href = '/pages/' + pageName + '.html';
                    return;
                }
            }
        }
        
        if (globalIndex.cities) {
            const cityMatchTerm = lowerV.replace(/\s+/g, '-');
            for (const key in globalIndex.cities) {
                if (key.includes(cityMatchTerm)) {
                    window.location.href = '/' + globalIndex.cities[key];
                    return;
                }
            }
        }
        if (globalIndex.states) {
            const stateMatchTerm = lowerV.replace(/\s+/g, ' ');
            for (const key in globalIndex.states) {
                if (key.includes(stateMatchTerm)) {
                    window.location.href = '/' + globalIndex.states[key];
                    return;
                }
            }
        }
        if (globalIndex.pincodes) {
            for (const key in globalIndex.pincodes) {
                if (key.includes(lowerV)) {
                    window.location.href = '/' + globalIndex.pincodes[key];
                    return;
                }
            }
        }
    }
  }

  curSearch = q;
  renderAll();
  document.getElementById('allSec').scrollIntoView({behavior:'smooth',block:'start'});
};

document.getElementById('heroSearch').addEventListener('keypress',e=>{if(e.key==='Enter')window.doSearch();});
document.getElementById('heroSearch').addEventListener('input', async e => {
    const v = e.target.value.trim();
    const suggBox = document.getElementById('searchSuggestions');
    if (!v) { 
        curSearch = ''; renderAll(); 
        suggBox.classList.remove('show');
        return; 
    }
    
    if (!globalIndex) await loadGlobalIndex();
    
    if (globalIndex && v.length >= 2) {
        const lowerV = v.toLowerCase().replace(/[^a-z0-9\s-]/g, '').trim();
        let matches = [];
        
        // Search Countries first
        if (typeof ALL !== 'undefined') {
            for (let i = 0; i < ALL.length; i++) {
                if (ALL[i].name.toLowerCase().includes(lowerV) || ALL[i].code.toLowerCase().includes(lowerV)) {
                    let pageName = ALL[i].code.toLowerCase();
                    if (pageName === 'in') pageName = 'india';
                    if (pageName === 'us') pageName = 'usa';
                    matches.push({ name: ALL[i].name, path: 'pages/' + pageName + '.html', type: 'Country' });
                }
                if (matches.length > 3) break;
            }
        }

        if (globalIndex.cities && matches.length < 5) {
            const cityMatchTerm = lowerV.replace(/\s+/g, '-');
            let count = 0;
            for (const key in globalIndex.cities) {
                if (key.includes(cityMatchTerm)) {
                    matches.push({ name: key.replace(/-/g, ' '), path: globalIndex.cities[key], type: 'City' });
                    count++;
                }
                if (count > 5) break;
            }
        }
        
        if (globalIndex.states && matches.length < 8) {
            const stateMatchTerm = lowerV.replace(/\s+/g, ' ');
            let count = 0;
            for (const key in globalIndex.states) {
                if (key.includes(stateMatchTerm)) {
                    matches.push({ name: key, path: globalIndex.states[key], type: 'State' });
                    count++;
                }
                if (count > 8) break;
            }
        }
        
        if (globalIndex.pincodes && matches.length < 10) {
            let count = 0;
            for (const key in globalIndex.pincodes) {
                if (key.includes(lowerV)) {
                    matches.push({ name: key, path: globalIndex.pincodes[key], type: 'Code' });
                    count++;
                }
                if (count > 10) break;
            }
        }
        
        if (matches.length > 0) {
            suggBox.innerHTML = matches.map(m => 
                `<div class="suggestion-item" onclick="window.location.href='/${m.path}'">
                    <span style="text-transform:capitalize">${m.name}</span>
                    <span class="suggestion-type">${m.type}</span>
                </div>`
            ).join('');
            suggBox.classList.add('show');
        } else {
            suggBox.innerHTML = `<div class="suggestion-item" style="cursor:default">No exact matches found</div>`;
            suggBox.classList.add('show');
        }
    } else {
        suggBox.classList.remove('show');
    }
});

function showToast(msg,type){
  const w=document.getElementById('toastWrap');
  const t=document.createElement('div');
  t.className='toast '+(type||'info');t.textContent=msg;
  w.appendChild(t);
  requestAnimationFrame(()=>requestAnimationFrame(()=>t.classList.add('show')));
  setTimeout(()=>{t.classList.remove('show');setTimeout(()=>t.remove(),400);},2500);
}

window.addEventListener('scroll',()=>document.getElementById('mainNav').classList.toggle('scrolled',window.scrollY>40),{passive:true});
document.getElementById('yr').textContent=new Date().getFullYear();

window.ALL=ALL;

renderPriority();
renderAll();
renderPopular();



// ── MARQUEE INITIALIZATION ──
function initMarquee() {
  const t1 = document.getElementById('mqTrack1');
  const t2 = document.getElementById('mqTrack2');
  if(!t1 || !t2) return;
  
  // Shuffle ALL array so it looks random
  const flags = [...ALL].sort(() => 0.5 - Math.random());
  const htmlStr = flags.map(c => `
    <a href="${pageUrl(c.code)}" class="mq-card">
      <img src="https://flagcdn.com/w80/${c.code.toLowerCase()}.png" alt="${c.name} Flag"/>
      <span>${c.name}</span>
    </a>
  `).join('');
  
  t1.innerHTML = htmlStr;
  t2.innerHTML = htmlStr;
}

// ── HERO FLAGS BACKGROUND ──
function initHeroFlags() {
  const container = document.getElementById('heroBgFlags');
  if(!container) return;
  
  // Create 10 rows (increased from 6 to cover background)
  let rowsHtml = '';
  for(let r = 0; r < 10; r++) {
    const shift = (r * 15) % ALL.length;
    // Wrap around to guarantee we always get 25 flags even if shift is near the end
    const wrappedAll = [...ALL.slice(shift), ...ALL.slice(0, shift)];
    const rowFlags = wrappedAll.slice(0, 25);
    
    const flagsHtml = rowFlags.map(c => `<img src="https://flagcdn.com/w80/${c.code.toLowerCase()}.png" decoding="async" style="width:60px; height:40px; border-radius:6px; object-fit:cover; margin:0 5px; will-change:transform;" alt=""/>`).join('');
    
    const duration = 1200 + (r % 3)*100;
    const dir = r % 2 === 0 ? 'scrollXHero' : 'scrollXHeroRev';
    
    rowsHtml += `
      <div style="display:flex; width:max-content; animation: ${dir} ${duration}s linear infinite; will-change:transform;">
        <div style="display:flex;">${flagsHtml}</div>
        <div style="display:flex;">${flagsHtml}</div>
      </div>
    `;
  }
  
  // Add animation styles dynamically
  const style = document.createElement('style');
  style.innerHTML = `
    @keyframes scrollXHero { 0% { transform: translateX(0) translateZ(0); } 100% { transform: translateX(-50%) translateZ(0); } }
    @keyframes scrollXHeroRev { 0% { transform: translateX(-50%) translateZ(0); } 100% { transform: translateX(0) translateZ(0); } }
  `;
  document.head.appendChild(style);
  
  container.innerHTML = rowsHtml;
}

if(document.readyState==='complete'){
  initMarquee();
  initHeroFlags();
}else{
  window.addEventListener('load',()=>{
    initMarquee();
    initHeroFlags();
  });
}

})();

window.doSearch().then(() => console.log('Final HREF:', window.location.href));
