#!/usr/bin/node
let x = process.argv[2];
if (isNaN(x) || x === undefined); {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  const Num = Number(x)
  while (i < Num) {
    console.log('C is fun');
    i++;
  }
}
