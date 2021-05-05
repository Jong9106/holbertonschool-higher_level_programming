#!/usr/bin/node

const argv = process.argv;
const request = require('request');
const fs = require('fs');
const url = argv[2];
const fileName = argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    fs.writeFile(fileName, body, 'utf8', function (err) {
      if (err) return console.log(err);
    });
  }
});
