#!/usr/bin/node

let text = '';
const number = parseInt(process.argv[2]);
let j = 0;
if (number) {
  for (let i = 0; i < number; i++) {
    for (; j < number; j++) {
      text += 'X';
    }
    console.log(text);
  }
} else {
  console.log('Missing size');
}
