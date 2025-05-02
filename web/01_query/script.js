"use strict";


const url = "https://opensky-network.org/api/states/all";


fetch(url)
.then(convertJSON)
.then(answer);


function convertJSON(response){
  return response.json();
}


const bodyElement = document.querySelector('body');
function answer(data) {
  for(const flight of data['states'])
  {
     const callsign = flight[1];
     
     const newElement = document.createElement('p');
     newElement.textContent = callsign;
     console.log(callsign);
     bodyElement.appendChild(newElement);
  }
}
