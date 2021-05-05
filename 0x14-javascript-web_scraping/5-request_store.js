#!/usr/bin/node

const argv = process.argv;
const request = require('request');
const fs = require('fs');
const url = argv[2];
const fileName = argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    fs.writeFile(fileName, data, (err) => {
      if (err) return console.log(err);
    });
  }
});
