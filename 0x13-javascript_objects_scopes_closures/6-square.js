#!/usr/bin/node
const SquareSuper = require('./5-square');

module.exports = class Square extends SquareSuper {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let i = 0;
    for (; i < this.height; i++) {
      console.log(c.repeat(this.height));
    }
  }
};
