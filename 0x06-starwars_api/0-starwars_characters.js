#!/usr/bin/node
const request = require('request');

async function getCharacter (charactersEndpoint) {
  for (let i = 0; i < charactersEndpoint.length; i++) {
    const req = new Promise((resolve, reject) => {
      request(charactersEndpoint[i], (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          resolve({ body });
        }
      });
    });
    const { body } = await req;
    console.log(JSON.parse(body).name);
  }
}

const movieId = process.argv[2];

if (!movieId) {
  process.exit();
}
const uri = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(uri, (error, response, body) => {
  if (error) {
    console.log('error: ', error);
    throw error;
  } else {
    const film = JSON.parse(body);
    getCharacter(film.characters);
  }
});
