#!/usr/bin/node
function factorialize (n) {
  if (n === 0 || isNaN(n)) {
    return 1;
  }
  return n * factorialize(n - 1);
}
const n = parseInt(process.argv[2]);
console.log(factorialize(n));
