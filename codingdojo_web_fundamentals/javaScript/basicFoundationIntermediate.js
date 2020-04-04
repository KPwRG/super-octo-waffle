// 1) Sigma - Implement function sigma(num) that, given a number, returns the sum of all positive integers up to the given number (inclusive).  Ex: sigma(3) = 6 (or 1+2+3); sigma(5) = 15 (or 1+2+3+4+5).;

var h = 10;
function sigma(x){
    var b = 0;
    for(var i=0; i<=x; i++){
        b += i;
    }
    return b;
}
y = sigma(h);
console.log(y);

// 2) Factorial - Write a function factorial(num) that, given a number, returns the product (multiplication) of all positive integers from 1 up to the given number (inclusive).  For example, factorial(3) = 6 (or 1*2*3); factorial(5) = 120 (or 1*2*3*4*5).

var h = 5;
function factorial(x){
    var b = 1;
    for(var i=1; i<=x; i++){
        b *= i;
    }
    return b;
}
y = factorial(h);
console.log(y);

// 3) Fibonacci - Create a function to generate Fibonacci numbers.  In this famous mathematical sequence, each number is the sum of the previous two, starting with values 0 and 1.  Your function should accept one argument, an index into the sequence (where 0 corresponds to the initial value, 4 corresponds to the value four later, etc).  Examples: fibonacci(0) = 0 (given), fibonacci(1) = 1 (given), fibonacci(2) = 1 (fib(0)+fib(1), or 0+1), fibonacci(3) = 2 (fib(1) + fib(2)3, or 1+1), fibonacci(4) = 3 (1+2), fibonacci(5) = 5 (2+3), fibonacci(6) = 8 (3+5), fibonacci(7) = 13 (5+8).  Do this without using recursion first.  If you don't know what a recursion is yet, don't worry as we'll be introducing this concept in Part 2 of this assignment.

var r = 5;
function fibonacci(x){
    var fib = 0;
    var prevFib = 1;
    var temp = 0;
    for(var i=0; i<=x; i++){
        temp = prevFib;
        prevFib = prevFib + fib;
        fib = temp;
    }
    return fib;
}
var m = fibonacci(r);
console.log(m);

// 4) Array: Second-to-Last: Return the second-to-last element of an array. Given [42, true, 4, "Liam", 7], return "Liam".  If array is too short, return null.

var y = [42,true,4,"Liam",7];
var p = [42];
function secondToLast(x){
    if(x.length===1){
        return null;
    }
    return x[x.length-2];
}
var m = secondToLast(y);
console.log(m);
var n = secondToLast(p);
console.log(n);

// 5) Array: Nth-to-Last: Return the element that is N-from-array's-end.  Given ([5,2,3,6,4,9,7],3), return 4.  If the array is too short, return null.

var v = [5,2,3,6,4,9,7];
var r = 3;
var c = 10;
function nthToLast(x,y){
    if(x.length<y){
        return null;
    }
    return x[x.length-y];
}
var b = nthToLast(v,r);
console.log(b);
var n = nthToLast(v,c);
console.log(n);

// 6) Array: Second-Largest: Return the second-largest element of an array. Given [42,1,4,3.14,7], return 7.  If the array is too short, return null.

var r = [42,1,4,3.14,7];
var t = [12,12,12,12,12];
var w = [34];
function secondLargest(x){
    var largest = 0;
    var secondLargestVal = 0;
    var temp = 0;
    for(var i=0; i<x.length; i++){
        temp = x[i];
        if(largest<temp){
            largest = temp;
        }if(x.length===x.length){
            temp = 0;
        }
    }
    for(var i=0; i<x.length; i++){
        temp = x[i];
        if(temp<largest && temp>secondLargestVal){
            secondLargestVal = temp;
        }
    }
    if(secondLargestVal===0){
        return null;
    }
    return secondLargestVal;
}
var m = secondLargest(r);
console.log(m);
var n = secondLargest(t);
console.log(n);
var b = secondLargest(w);
console.log(b);

// 7) Double Trouble: Create a function that changes a given array to list each existing element twice, retaining original order.  Convert [4, "Ulysses", 42, false] to [4,4, "Ulysses", "Ulysses", 42, 42, false, false]

var m = [4,"Ulysses",42,false];

function repeatTwice(x){
    var newArr = [];
    for(var i=0; i<x.length; i++){
        newArr.push(x[i]);
        newArr.push(x[i]);
    }
    return newArr;
}

console.log(repeatTwice(m));