var str1 = "Hello World!";
var str2 = "The quick brown fox jumps over the lazy dog.";

function reverseString(x){
    x.split("");
    var revStr = "";
    for(var i=0, j=x.length-1; i<x.length; i++, j--){
        revStr += x[j];
    }
    return revStr;
}
var m = reverseString(str1);
console.log(m);
var n = reverseString(str2);
console.log(n);


// var str1 = "Cigar? Toss it in a can. It is so tragic.";
// var str2 = "The quick brown fox jumps over the lazy dog.";

// funtion palindrome(x){
//     x.split("");
//     var revStr = "";
//     for(var i=0, j=x.length-1; i<x.length; i++, j--){
        
//     }
// }