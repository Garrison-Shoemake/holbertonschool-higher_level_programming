#!/usr/bin/node

const Square2 = require('./5-square.js');

class Square extends Square2 {
  charPrint (c) {
    let i = 0;
    if (c === undefined) {
      c = 'X';
    }
    for (i = 0; i < this.height; i++) {
      console.log(c.repeat(this.height));
    }
  }
}
module.exports = Square;
