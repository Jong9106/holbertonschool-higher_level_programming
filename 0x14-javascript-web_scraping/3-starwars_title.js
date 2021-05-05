#!/usr/bin/node

const request = require('request');
const argv = process.argv;
const url = 'https://swapi-api.hbtn.io/api/films/';

request(url + argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
