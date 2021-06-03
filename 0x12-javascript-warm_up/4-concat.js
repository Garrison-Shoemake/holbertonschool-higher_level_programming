#!/usr/bin/node
const argv = process.argv;
let i = 0;

while (argv[i] !== undefined) {
  i++;
}
console.log(argv[2] + ' is ' + argv[3]);
