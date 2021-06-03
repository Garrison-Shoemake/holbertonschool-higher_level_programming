#!/usr/bin/node
const a = 'No argument';
const b = 'Argument found';
const c = 'Arguments found';

if (process.argv.length === 2) {
  console.log(a);
}
if (process.argv.length === 3) {
  console.log(b);
}
if (process.argv.length > 3) {
  console.log(c);
}
