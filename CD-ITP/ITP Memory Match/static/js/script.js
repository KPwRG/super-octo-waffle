var arrOfImages = ["csharplogo.png", "csslogo.png", "htmllogo.png", "javalogo.png", "jslogo.png", "pythonlogo.png"];
// Fill these functions out using your code!
function doubleImages(arr) {
    // Your code here
}
function displayCards(arr) {
    // Your code here
}
function shuffleCards(arr) {
    // Your code here
}   
function hideACard(idx) {
    // Your code here
}
function revealCard(event) {
    // Your code here  
}

// Game logic!
console.log(doubleImages(arrOfImages));
shuffleCards(arrOfImages);
displayCards(arrOfImages);

// call on the hideACard function for each card in our array of images
for (var i = 0; i < arrOfImages.length; i++) {
    // let's call on the hideACard function we just made
    hideACard(i);
}

var cardsPicked = [];    // outside the function, we'll keep track of which cards have been picked

var cards = document.getElementsByClassName("card");    // grab all the cards
for (var i = 0; i < cards.length; i++) {
    cards[i].addEventListener("click", revealCard);
}