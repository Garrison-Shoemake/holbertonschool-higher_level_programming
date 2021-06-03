#!/usr/bin/node
const argv = process.argv;

const newarg = parseInt(argv[2], 10);

if (isNaN(newarg) === true) {
  console.log('Not a number');
} else {
  console.log('My number: ' + newarg);
}
