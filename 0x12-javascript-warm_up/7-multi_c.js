#!/usr/bin/node
const argv = process.argv;
const integer = parseInt(argv[2]);
if (isNaN(integer)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < integer; i++) { console.log('C is fun'); }
}
