#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === undefined); {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  const Num = Number(process.argv[2]);
  while (i < Num) {
    console.log('C is fun');
    i++;
  }
}
