// 1) Given an array and a value Y, count and print the number of array values greater than Y.

var x = [23,4,89,9,3];
var y = 13;
var count = 0;
    for(var i=0; i<x.length; i++){
        if(x[i] > y){
        console.log(x[i]);
        count++;
        }
    }
console.log(count);

// 2) Given an array, print the max, min and average values for that array.

var w = [3,5,6,90,102];
var max = -1000;
var min = 1000;
var average = 0;
var sum = 0;

    for (var i=0; i<w.length; i++){
        if(w[i] > max){
        max = w[i];
        }
        if(w[i] < min){
        min = w[i];
        }
    sum += w[i]; 
    }

average = sum/w.length;
console.log(max, min, average);

// 3) Given an array of numbers, create a function that returns a new array where negative values were replaced with the string ‘Dojo’.   For example, replaceNegatives( [1,2,-3,-5,5]) should return [1,2, "Dojo", "Dojo", 5].

var n = [3,9,-10,8,-1,0];

function replaceNegatives(x){
    var newArr = [];
    for(var i=0; i<x.length; i++){
        if(x[i]<0){
        newArr[i] = "Dojo";
        }else{
        newArr[i] = x[i];
        }
    }
    return newArr;
}

var m = replaceNegatives(n);
console.log(m);



// 4) Given array, and indices start and end, remove values in that index range, working in-place (hence shortening the array).  For example, removeVals([20,30,40,50,60,70],2,4) should return [20,30,70].

var b = [20,30,40,50,60,70];
var startingRemovedIndex = 2;
var endingRemovedIndex = 4;
function removeVals(x,y,z){
    var newArray = [];
    for (i=0; i<x.length; i++){
        if (i<y || i>z){
            newArray.push(x[i]);
        }
    }
    return newArray;
}
var d = removeVals(b,startingRemovedIndex,endingRemovedIndex);
console.log(d);