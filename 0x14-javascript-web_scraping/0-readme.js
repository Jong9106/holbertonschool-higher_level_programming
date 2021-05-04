#!/usr/bin/node

const fs = require('fs');
const argv = process.argv;

fs.readFile(argv[2], 'utf8', function (err, fd) {
  if (err) {
    return console.error(err);
  }

  console.log(fd);
});
