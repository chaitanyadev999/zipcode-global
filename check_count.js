const fs = require('fs');
const path = require('path');

function walkDir(dir, callback) {
    fs.readdirSync(dir).forEach(f => {
        let dirPath = path.join(dir, f);
        let isDirectory = fs.statSync(dirPath).isDirectory();
        isDirectory ? walkDir(dirPath, callback) : callback(path.join(dir, f));
    });
}

let count = 0;
let total = 0;

walkDir('./pages', function(filePath) {
    if (filePath.endsWith('.html') && !filePath.includes('about.html') && !filePath.includes('main.html')) {
        total++;
        const content = fs.readFileSync(filePath, 'utf8');
        if (content.includes('Target Audience, Use Cases')) {
            count++;
        }
    }
});

console.log(`Total files: ${total}`);
console.log(`Patched files: ${count}`);
console.log(`Remaining to patch: ${total - count}`);
