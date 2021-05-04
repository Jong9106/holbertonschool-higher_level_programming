#!/usr/bin/node

const argv = process.argv;
const request = require('request');

request(argv[2], function (error, response) {
  if (error) {
    console.error('code:', error);
  } else {
    console.log('code:', response.statusCode);
  }
});
