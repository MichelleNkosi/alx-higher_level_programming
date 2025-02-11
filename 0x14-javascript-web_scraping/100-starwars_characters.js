#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    const characters = data.characters;

    characters.forEach(characterUrl => {
      request(characterUrl, (err, res, body) => {
        if (err) {
          console.log(err);
        } else {
          const character = JSON.parse(body);
          console.log(character.name);
        }
      });
    });
  }
});
