#!/usr/bin/node

const args = process.argv.slice(2);
const integers = args.map(Number);

if (integers.length <= 1) {
  console.log(0);
} else {
  integers.sort((a, b) => b - a);
  console.log(integers[1]);
}
