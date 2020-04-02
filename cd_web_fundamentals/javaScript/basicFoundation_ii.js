// 1) Biggie Size - Given an array, write a function that changes all positive numbers in the array to the string "big".  Example: makeItBig([-1,3,5,-5]) returns that same array, changed to [-1, "big", "big", -5].

var m = [1,-4,5,-8];
function biggieSize(x){
    for(var i=0; i<x.length; i++){
        if(x[i]>0){
            x[i]="big";
        }
    }
    return x;
}
var b = biggieSize(m);
console.log(b);

// 2) Print Low, Return High - Create a function that takes in an array of numbers.  The function should print the lowest value in the array, and return the highest value in the array.

var m = [34,67,98,75];
function printLowReturnHigh(x){
    var min = 1000;
    var max = -1000;
    for(var i=0; i<x.length; i++){
        if(x[i]<min){
            min=x[i];
        }
        if(x[i]>max){
            max=x[i];
        }
    }
    console.log(min);
    return max;
}
var b = printLowReturnHigh(m);
console.log(b);

// 3) Print One, Return Another - Build a function that takes in an array of numbers.  The function should print the second-to-last value in the array, and return the first odd value in the array

var a = [12,13,14,15];
function printOneReturnOne(x){
    var odd = 0;
    console.log(x[x.length-2]);
    for(var i=0; i<x.length && odd===0; i++){
        if(x[i]%2>0){
            odd=x[i];
        }
    }
    return odd;
}
var b = printOneReturnOne(a);
console.log(b);

// 4) Double Vision - Given an array (similar to saying 'takes in an array'), create    a function that returns a new array where each value in the original array has been doubled.  Calling double([1,2,3]) should return [2,4,6] without changing the original array.

var a = [12,13,14];
function doubleVision(z){
    for(var i=0; i<z.length; i++){
        z[i] = z[i]*2;
    }
    return z;
}
var d = doubleVision(a);
console.log(d);

// 5) Count Positives - Given an array of numbers, create a function to replace the last value with the number of positive values found in the array.  Example, countPositives([-1,1,1,1]) changes the original array to [-1,1,1,3] and returns it.

var g = [3,4,-5,9];
function countPositives(z){
    var sum = 0;
    for(var i=0; i<z.length; i++){
        if(z[i]>0){
            sum+=z[i];
        }
    }
    z.pop();
    z.push(sum);
    return z;
}
var r = countPositives(g);
console.log(r);

// 6) Evens and Odds - Create a function that accepts an array.  Every time that array has three odd values in a row, print "That's odd!".  Every time the array has three evens in a row, print "Even more so!".

var y = [13,15,17,1,22,34,55,79,24,64,86];
function evensOdds(z){
    var oddCounter = 0;
    var evenCounter = 0;
    for(var i=0; i<z.length; i++){
        if(z[i]%2===0){
            oddCounter=0;
            evenCounter+=1;
            if(evenCounter===3){
                console.log("Even more so!");
                evenCounter = 0;
            }
        }else if(z[i]%2>0){
            evenCounter=0;
            oddCounter+=1;
            if(oddCounter===3){
                console.log("That's odd!");
            }
        }
    }
}
evensOdds(y);

// 7) Increment the Seconds - Given an array of numbers arr, add 1 to every other element, specifically those whose index is odd (arr[1], arr[3], arr[5], etc).  Afterward, console.log each array value and return arr.

var arr = [12,13,14,15,16,17];
function incrementSeconds(z){
    for(var i=0; i<z.length; i++){
        if(i%2>0){
            z[i]+=1;
        }
        console.log(z[i]);
    }
    return z;
}
var s = incrementSeconds(arr);
console.log(s);

// 8) Previous Lengths - You are passed an array (similar to saying 'takes in an array' or 'given an array') containing strings.  Working within that same array, replace each string with a number - the length of the string at the previous array index - and return the array.  For example, previousLengths(["hello", "dojo", "awesome"]) should return ["hello", 5, 4]. Hint: Can for loops only go forward?

var a = ["hello","dojo","awesome"];
function previousLengths(z){
    var num = 0;
    var str = 0;
    for(var i=z.length-1; i>=0; i--){
        if(i>0){
            str=z[i];
            num=str.length;
            z[i]=num;
        }
    }
    return z;
}
var m = previousLengths(a);
console.log(m);

// 9) Add Seven - Build a function that accepts an array. Return a new array with all the values of the original, but add 7 to each. Do not alter the original array.  Example, addSeven([1,2,3]) should return [8,9,10] in a new array.

var a = [12,13,14];
function addSeven(z){
    var newArr = [];
    for(var i=0; i<z.length; i++){
        newArr[i]=z[i]+7;
    }
    return newArr;
}
var d = addSeven(a);
console.log(d);

// 10) Reverse Array - Given an array, write a function that reverses its values, in-place.  Example: reverse([3,1,6,4,2]) returns the same array, but now contains values reversed like so... [2,4,6,1,3].  Do this without creating an empty temporary array.  (Hint: you'll need to swap values).

function reverseArray(arr){
    var newArr = [];
    for(var i=0, j=arr.length-1; i<arr.length; i++, j--){
        newArr[i]=arr[j];
    }
    return newArr;
}
var arr = [1,2,3,4,5,6,7,8,9];
console.log(reverseArray(arr));

// 11) Outlook: Negative - Given an array, create and return a new one containing all the values of the original array, but make them all negative (not simply multiplied by -1). Given [1,-3,5], return [-1,-3,-5].

var w = [12,-13,14,15];
function negative(x){
    var newArr = [];
    for(var i=0; i<x.length; i++){
        if(x[i]>0){
        x[i]=x[i]*(-1);
        }
    newArr[i]=x[i];
    }
    return newArr;
}
var f = negative(w);
console.log(f);

// 12) Always Hungry - Create a function that accepts an array, and prints "yummy" each time one of the values is equal to "food".  If no array values are "food", then print "I'm hungry" once.

var k = [12,"food",14,"food"];
var g = [14,15,16];
function hungry(z){
    var counter = 0;
    for(var i=0; i<z.length; i++){
        if(z[i]==="food"){
            console.log("yummy");
            counter+=1;
        }
    }
    if(counter===0){
        console.log("I'm hungry");
    }
}
hungry(k);
hungry(g);

// 13) Swap Toward the Center - Given an array, swap the first and last values, third and third-to-last values, etc.  Example: swapTowardCenter([true,42,"Ada",2,"pizza"]) turns the array into ["pizza", 42, "Ada", 2, true].  swapTowardCenter([1,2,3,4,5,6]) turns the array into [6,2,4,3,5,1].  No need to return the array this time.

var m = [12,13,14,15,16,17];

function swapTowardCenter(x){
    var temp = 0;
    temp = x[0];
    x[0] = x[x.length-1];
    x[x.length-1] = temp;
    temp = x[2];
    x[2] = x[x.length-3];
    x[x.length-3] = temp;
}
swapTowardCenter(m);
console.log(m);

// 14) Scale the Array - Given an array arr and a number num, multiply all values in the array arr by the number num, and return the changed array arr.  For example, scaleArray([1,2,3], 3) should return [3,6,9].

var a = [12,13,14];
var b = 2;
function scaleArray(z,x){
    newArr = [];
    for(var i=0; i<z.length; i++){
        newArr[i]=z[i]*x;
    }
    return newArr;
}
var t = scaleArray(a,b);
console.log(t);