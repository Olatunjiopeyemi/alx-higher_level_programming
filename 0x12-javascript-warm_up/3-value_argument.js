#!/usr/bin/node
if (process.argv[2] === undefined) { //no argument was passed
  console.log('No argument');
} else {
  console.log(process.argv[2]); // print the argument passed
}
