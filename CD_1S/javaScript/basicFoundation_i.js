// 1) Get 1 to 255 - Write a function that returns an array with all the numbers from 1 to 255.

function arrayOneTo255(x){
    var newArr = [];
    for(var i=0; i<=255; i++){
        newArr[i]=i;
    }
    newArr.shift();
    return newArr;
}

console.log(arrayOneTo255());

// 2) Get even 1000 - Write a function that would get the sum of all the even numbers from 1 to 1000.  You may use a modulus operator for this exercise.

function even1000(x){
    var sum = 0;
    for(var i=1; i<=1000; i++){
        if(i%2===0){
            sum+=i;
        }
    }
    return sum;
}

console.log(even1000());

// 3) Sum odd 5000 - Write a function that returns the sum of all the odd numbers from 1 to 5000. (e.g. 1+3+5+...+4997+4999).

function odd5000(x){
    var sum = 0;
    for(var i=1; i<=5000; i++){
        if(i%2>0){
            sum+=i;
        }
    }
    return sum;
}

console.log(odd5000());

// 4) Iterate an array - Write a function that returns the sum of all the values within an array. (e.g. [1,2,5] returns 8. [-5,2,5,12] returns 14).

var b = [23,6,90,7];
function sum(x){
    var sum = 0;
    for(var i=0; i<x.length; i++){
        sum+=x[i];
    }
    return sum;
}

var m = sum(b);
console.log(m);

// 5) Find max - Given an array with multiple values, write a function that returns the maximum number in the array. (e.g. for [-3,3,5,7] max is 7).

var c = [12,56,-81,3];
function findMax(x){
    var max = 0;
    for(var i=0; i<x.length; i++){
        if(x[i]>max){
            max=x[i];
        }
    }
    return max;
}

var n = findMax(c);
console.log(n);

// 6) Find average - Given an array with multiple values, write a function that returns the average of the values in the array. (e.g. for [1,3,5,7,20] average is 7.2).

var h = [12,13,14,15];
function findAverage(x){
    var sum = 0;
    var average = 0;
    for(var i=0; i<x.length; i++){
        sum+=x[i];
        average=sum/x.length;
    }
    return average;
}

var g = findAverage(h);
console.log(g);

// 7) Array odd - Write a function that would return an array of all the odd numbers between 1 to 50. (ex. [1,3,5, .... , 47,49]). Hint: Use 'push' method.

function arrayOdd(x){
    var newArr = [];
    var temp = 0;
    for(var i=1; i<=50; i++){
        if(i%2>0){
            newArr.push(i);
        }
    }
    return newArr;
}

var m = arrayOdd();
console.log(m);

// 8) Greater than Y - Given value of Y, write a function that takes an array and returns the number of values that are greater than Y. For example if arr = [1, 3, 5, 7] and Y = 3, your function will return 2. (There are two values in the array greater than 3, which are 5, 7).

var k = [23,31,5,67];
var g = 25;
function greaterThanG(x){
    counter = 0;
    for(var i=0; i<x.length; i++){
        if(x[i]>g){
            counter++;
        }
    }
    return counter;
}

var y = greaterThanG(k);
console.log(y);

// 9) Squares - Given an array with multiple values, write a function that replaces each value in the array with the value squared by itself. (e.g. [1,5,10,-2] will become [1,25,100,4]).

var w = [2,4,6];
function squaredArr(x){
    for(var i=0; i<x.length; i++){
        x[i]=x[i]*x[i];
    }
    return x;
}

var m = squaredArr(w);
console.log(w);

// 10) Negatives - Given an array with multiple values, write a function that replaces any negative numbers within the array with the value of 0. When the program is done the array should contain no negative values. (e.g. [1,5,10,-2] will become [1,5,10,0]).

var t = [78,-90,3,-1];
function negativeNumbers(x){
    for(var i=0; i<x.length; i++){
        if(x[i]<0){
            x[i]=0;
        }
    }
    return x;
}

var h = negativeNumbers(t);
console.log(h);

// 11) Max/Min/Avg - Given an array with multiple values, write a function that returns a new array that only contains the maximum, minimum, and average values of the original array. (e.g. [1,5,10,-2] will return [10,-2,3.5]).

var p = [12,45,3,81];
function maxMinAv(x){
    var newArr = [];
    var min = 1000;
    var max = -1000;
    var sum = 0;
    var average = 0;
    for(var i=0; i<x.length; i++){
        if(x[i]>max){
            max=x[i];
        }
        if(x[i]<min){
            min=x[i];
        }
        sum+=x[i];
    }
    average=sum/x.length;
    newArr.push(max);
    newArr.push(min);
    newArr.push(average);
    return newArr;
}

var z = maxMinAv(p);
console.log(z);

// 12) Swap Values - Write a function that will swap the first and last values of any given array. The default minimum length of the array is 2. (e.g. [1,5,10,-2] will become [-2,5,10,1]).

var e = [12,13,14,15];
function swapFirstLast(x){
    var temp = x[0];
    x[0] = x[x.length-1];
    x[x.length-1] = temp;
    return x;
}

var q = swapFirstLast(e);
console.log(q);

// 13) Number to String - Write a function that takes an array of numbers and replaces any negative values within the array with the string 'Dojo'. For example if array = [-1,-3,2], your function will return ['Dojo','Dojo',2].

var k = [0,-8,9,-15];

function replaceNegative(x){
    for(var i=0; i<x.length; i++){
        if(x[i]<0){
            x[i]="Dojo";
        }
    }
    return x;
}

var d = replaceNegative(k);
console.log(d);