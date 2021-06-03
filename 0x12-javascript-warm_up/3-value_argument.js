#!/usr/bin/node
const a = 'No argument';

if (process.argv.length === 2) {
  console.log(a);
}
if (process.argv.length > 2) {
  console.log(process.argv[2]);
}
