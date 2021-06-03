#!/usr/bin/node
let i = 0;
const args = process.argv;
const newarg = parseInt(args[2], 10);

if (isNaN(newarg) === true) {
  console.log('Missing size');
} else {
  while (i < newarg) {
    console.log('X'.repeat(newarg));
    i++;
  }
}
