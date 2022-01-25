//Task 2
import fetch from "node-fetch";
import readline from "readline";

//Handle fetch errors
function handleFetchError(response) {
  if (!response.ok) {
      throw Error(response.statusText);
  }
  return response;
}

//Function for fetching data from API
async function fetchFunc(input) {

  //Fetching result using promise .then() for handling fetch error
  let response = await fetch(`https://newton.now.sh/api/v2/simplify/${encodeURIComponent(input)}`)
    .then(handleFetchError) //Error handling for fetch failure
    .then(response => response.json())
    .then(result => console.log(`Formula "${result.expression}" can be simplified as: "${result.result}"`))
    .catch(error => console.log(error));
}

//Create input wrapper
const frame = readline.createInterface({
  input: process.stdin,
  output: process.stdout
})

//Prompt user
frame.question(`Hello! Please enter the formulas you want to simplify:\n`, user_input => {

  //Place each formula as a element in array
  let words = user_input, wordArray = words.split('; ');

  for (var i = 0; i < wordArray.length; i++) {
    //Send each formula to our fetch functon
    fetchFunc(wordArray[i]);
  }

  frame.close();
})
