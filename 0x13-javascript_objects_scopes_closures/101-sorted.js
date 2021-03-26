#!/usr/bin/node
const fs = require('fs');
const data1 = fs.readFileSync(process.argv[2], { encoding: 'utf8', flag: 'r' });
const data2 = fs.readFileSync(process.argv[3], { encoding: 'utf8', flag: 'r' });
fs.writeFileSync(process.argv[4], data1 + data2);
