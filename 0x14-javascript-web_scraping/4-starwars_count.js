#!/usr/bin/node

const argv = process.argv;
const request = require('request');
const characterID = 18;

let k = 0;

request(argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const prs = JSON.parse(body);
    for (const i of prs.results) {
      for (const j of i.characters) {
        if (j.search(characterID) > 0) {
          k++;
        }
      }
    }
    console.log(k);
  }
});
