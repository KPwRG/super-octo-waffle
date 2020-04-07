// var str1 = "Hello World!";
// var str2 = "The quick brown fox jumps over the lazy dog.";

// function reverseString(x){
//     var revStr = "";
//     for(var j=x.length-1; j>=0; j--){
//         revStr += x[j];
//     }
//     return revStr;
// }
// var m = reverseString(str1);
// console.log(m);
// var n = reverseString(str2);
// console.log(n);

// var str1 = "Hello World!";
// var str2 = "The quick brown fox jumps over the lazy dog.";

// function reverseString(x) {
//     var b = x.split("");
//     var revStr = "";
//     for (var j = b.length - 1; j >= 0; j--) {
//         revStr += b[j];
//     }
//     return revStr;
// }
// var m = reverseString(str1);
// console.log(m);
// var n = reverseString(str2);
// console.log(n);


var str1 = "Cigar? Toss it in a can. It is so tragic.";
var str2 = "The quick brown fox jumps over the lazy dog.";

function palindrome(x){
    var b = x.split("");
    var revStr = "";
    for (var j = b.length - 1; j >= 0; j--) {
        if (b[j] != " ") {
            revStr += b[j];
        }
    }
    return revStr;
}
var m = palindrome(str1);
console.log(m);
var n = palindrome(str2);
console.log(n);
