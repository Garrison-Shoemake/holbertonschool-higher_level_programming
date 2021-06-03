#!/usr/bin/node
const a = 'No argument';
const args = process.argv;
let i = 0;

while (args[i] !== undefined) {
  i++;
}
if (i === 2) {
  console.log(a);
}
if (i > 2) {
  console.log(args[2]);
}
