#!/usr/bin/node
const argv = process.argv;
const integer = parseInt(argv[2]);
const integer2 = parseInt(argv[3]);
if (isNaN(integer) && isNaN(integer2)) {
  console.log('NaN');
} else {
  const result = (integer + integer2);
  console.log(result);
}
