#!/usr/bin/node

const argv = process.argv;
const request = require('request');
const url = argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const prs = JSON.parse(body);
    const dictionary = {};
    for (const i of prs) {
      if (i.completed === true) {
        if (dictionary[i.userId] === undefined) {
          dictionary[i.userId] = 0;
        }
        dictionary[i.userId] += 1;
      }
    }
    console.log(dictionary);
  }
});
