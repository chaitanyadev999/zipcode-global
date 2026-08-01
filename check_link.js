function safeFilename(name) {
    if (!name) return 'unknown';
    return name.replace(/[^a-zA-Z0-9\s-]/g, '').trim().toLowerCase().replace(/\s+/g, '-');
}
console.log(safeFilename('ANDHRA PRADESH'));
console.log(safeFilename('Kakinada'));
console.log(safeFilename('Los Angeles'));
console.log(safeFilename('British Columbia'));
