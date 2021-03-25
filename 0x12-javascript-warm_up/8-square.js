#!/usr/bin/node
const argv = process.argv;
const integer = parseInt(argv[2]);
const char = 'X';
if (isNaN(integer)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < integer; i++) {
    console.log(char.repeat(integer));
  }
}
