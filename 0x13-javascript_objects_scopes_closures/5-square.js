#!/usr/bin/node

const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  constructor (length) {
    super(length, length);
  }
}
module.exports = Square;
