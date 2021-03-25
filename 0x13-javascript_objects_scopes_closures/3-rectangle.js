#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const charSquare = 'X';
    let i = 0;
    let j = 0;
    for (; i < this.width; i++) {
      for (; j < this.height; j++) {
        console.log(charSquare.repeat(this.width));
      }
    }
  }
}
module.exports = Rectangle;
