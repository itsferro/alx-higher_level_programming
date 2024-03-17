#!/usr/bin/node

const text = 'C is fun';
const number = parseInt(process.argv[2]);
if (number) {
  for (let i = 0; i < number; i++) {
    console.log(text);
  }
} else {
  console.log('Missing number of occurrences');
}
