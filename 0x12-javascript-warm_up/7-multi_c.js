#!/usr/bin/node
let i = 0;
const args = process.argv;
const a = 'C is fun';
const newarg = parseInt(args[2], 10);

if (isNaN(newarg) === true) {
  console.log('Missing number of occurrences');
} else {
  while (i < newarg) {
    console.log(a);
    i++;
  }
}
