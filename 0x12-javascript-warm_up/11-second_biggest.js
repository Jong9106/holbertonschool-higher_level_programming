#!/usr/bin/node
const argv = process.argv;
let max;
const arraycopy = [];

function SecondMax (array) {
  if (array.length <= 3) {
    return 0;
  } else {
    for (let i = 2; i < array.length; i++) {
      arraycopy.push(parseInt(array[i]));
    }
    max = Math.max.apply(null, arraycopy);
    arraycopy.splice(arraycopy.indexOf(max), 1);
    return Math.max.apply(null, arraycopy);
  }
}
console.log(SecondMax(argv));
