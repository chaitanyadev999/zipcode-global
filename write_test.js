const fs = require('fs');
let js = `
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
`;
js += fs.readFileSync('test_main.js','utf8');
js += `\nwindow.doSearch().then(() => console.log('Final HREF:', window.location.href));\n`;
fs.writeFileSync('test_run.js', js);
