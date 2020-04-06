//1) Given an array and a value Y, count and print the number of array values greater than Y.

// var t = 10;
// var z = [13,6,78,90,1];
// function greaterThanY(x,y){
//     for(var i=0; i<x.length; i++){
//         if(x[i] > 10){
//             console.log(x[i]);
//         }
//     }
// }
// greaterThanY(z,t);

//2) Given an array, print the max, min and average values for that array.

// var q = [43,35,6,17];
// function maxMinAverage(x){
//     var max = -100;
//     var min = 100;
//     var sum = 0;
//     var average = sum/x.length;
//     for(var i=0; i<x.length; i++){
//         if(x[i] > max){
//             max = x[i];
//         }
//         if(x[i] < min){
//             min = x[i];
//         }
//         sum += i;
//     }
//     console.log("The max is"+" "+max);
//     console.log("The min is"+" "+min);
//     console.log("The average is"+" "+average);
// }
// maxMinAverage(q);

//3) Given an array of numbers, create a function that returns a new array where negative values were replaced with the string ‘Dojo’.   For example, replaceNegatives( [1,2,-3,-5,5]) should return [1,2, "Dojo", "Dojo", 5].

// var e = [-8,4,0,-9,10];
// function replacedNegatives(x){
//     var n = [];
//     for(var i=0; i<x.length; i++){
//         if(x[i] < 0){
//             n[i] = "Dojo";
//         }else{
//             n[i] = x[i];
//         }
//     }
//     return n;
// }
// var m = replacedNegatives(e);
// console.log(m);

//4) Given array, and indices start and end, remove values in that index range, working in-place (hence shortening the array).  For example, removeVals([20,30,40,50,60,70],2,4) should return [20,30,70].

// var q = [12,13,14,15,16,17,18,19];
// var w = 3;
// var r = 6;
// function shorteningArray(x,y,z){
//     var c = [];
//     for(var i=0; i<x.length; i++){
//         if(i < w){
//             c.push(x[i]);
//         }
//         if(i > r){
//             c.push(x[i]);
//         }
//     }
//     return c;
// }
// var m = shorteningArray(q,w,r);
// console.log(m);

//1) Return the given array, after setting any negative values to zero.  For example resetNegatives( [1,2,-1, -3]) should return [1,2,0,0].

//2) Given an array, move all values forward by one index, dropping the first and leaving a ‘0’ value at the end.  For example moveForward( [1,2,3]) should return [2,3,0].

//3) Given an array, return an array with values in a reversed order.  For example, returnReversed([1,2,3]) should return [3,2,1].

//4) Create a function that changes a given array to list each original element twice, retaining original order.  Have the function return the new array.  For example repeatTwice( [4,”Ulysses”, 42, false] ) should return [4,4, “Ulysses”, “Ulysses”, 42, 42, false, false].

// 1) Get 1 to 255 - Write a function that returns an array with all the numbers 	     from 1 to 255.

// 2) Get even 1000 - Write a function that would get the sum of all the even numbers    from 1 to 1000.  You may use a modulus operator for this exercise.

// 3) Sum odd 5000 - Write a function that returns the sum of all the odd numbers    from 1 to 5000. (e.g. 1+3+5+...+4997+4999).

// 4) Iterate an array - Write a function that returns the sum of all the values    within an array. (e.g. [1,2,5] returns 8. [-5,2,5,12] returns 14).

// 5) Find max - Given an array with multiple values, write a function that returns    the maximum number in the array. (e.g. for [-3,3,5,7] max is 7).

// 6) Find average - Given an array with multiple values, write a function that    returns the average of the values in the array. (e.g. for [1,3,5,7,20] average    is 7.2).

// 7) Array odd - Write a function that would return an array of all the odd numbers    between 1 to 50. (ex. [1,3,5, .... , 47,49]). Hint: Use 'push' method.

// 8) Greater than Y - Given value of Y, write a function that takes an array and    returns the number of values that are greater than Y. For example if arr = [1,    3, 5, 7] and Y = 3, your function will return 2. (There are two values in the    array greater than 3, which are 5, 7).

// 9) Squares - Given an array with multiple values, write a function that replaces    each value in the array with the value squared by itself. (e.g. [1,5,10,-2]    will become [1,25,100,4]).

// 10) Negatives - Given an array with multiple values, write a function that     replaces any negative numbers within the array with the value of 0. When the     program is done the array should contain no negative values. (e.g. [1,5,10,-2]     will become [1,5,10,0]).

// 11) Max/Min/Avg - Given an array with multiple values, write a function that     returns a new array that only contains the maximum, minimum, and average     values of the original array. (e.g. [1,5,10,-2] will return [10,-2,3.5]).

// 12) Swap Values - Write a function that will swap the first and last values of any     given array. The default minimum length of the array is 2. (e.g. [1,5,10,-2]     will become [-2,5,10,1]).

// 13) Number to String - Write a function that takes an array of numbers and     replaces any negative values within the array with the string 'Dojo'. For     example if array = [-1,-3,2], your function will return ['Dojo','Dojo',2].

// 1) Biggie Size - Given an array, write a function that changes all positive numbers in the array to the string "big".  Example: makeItBig([-1,3,5,-5]) returns that same array, changed to [-1, "big", "big", -5].

// 2) Print Low, Return High - Create a function that takes in an array of numbers.  The function should print the lowest value in the array, and return the highest value in the array.

// 3) Print Low, Return High - Create a function that takes in an array of numbers.  The function should print the lowest value in the array, and return the highest value in the array.

// 4) Double Vision - Given an array (similar to saying 'takes in an array'), create    a function that returns a new array where each value in the original array has    been doubled.  Calling double([1,2,3]) should return [2,4,6] without changing    the original array.

// 5) Count Positives - Given an array of numbers, create a function to replace the last value with the number of positive values found in the array.  Example, countPositives([-1,1,1,1]) changes the original array to [-1,1,1,3] and returns it.

// 6) Evens and Odds - Create a function that accepts an array.  Every time that array has three odd values in a row, print "That's odd!".  Every time the array has three evens in a row, print "Even more so!".

// 7) Increment the Seconds - Given an array of numbers arr, add 1 to every other element, specifically those whose index is odd (arr[1], arr[3], arr[5], etc).  Afterward, console.log each array value and return arr.

// 8) Previous Lengths - You are passed an array (similar to saying 'takes in an array' or 'given an array') containing strings.  Working within that same array, replace each string with a number - the length of the string at the previous array index - and return the array.  For example, previousLengths(["hello", "dojo", "awesome"]) should return ["hello", 5, 4]. Hint: Can for loops only go forward?

// 9) Add Seven - Build a function that accepts an array. Return a new array with all the values of the original, but add 7 to each. Do not alter the original array.  Example, addSeven([1,2,3]) should return [8,9,10] in a new array.

// 10) Reverse Array - Given an array, write a function that reverses its values, in-place.  Example: reverse([3,1,6,4,2]) returns the same array, but now contains values reversed like so... [2,4,6,1,3].  Do this without creating an empty temporary array.  (Hint: you'll need to swap values).

// 11) Outlook: Negative - Given an array, create and return a new one containing all the values of the original array, but make them all negative (not simply multiplied by -1). Given [1,-3,5], return [-1,-3,-5].

// 1) Sigma - Implement function sigma(num) that, given a number, returns the sum of all positive integers up to the given number (inclusive).  Ex: sigma(3) = 6 (or 1+2+3); sigma(5) = 15 (or 1+2+3+4+5).

// 2) Factorial - Write a function factorial(num) that, given a number, returns the product (multiplication) of all positive integers from 1 up to the given number (inclusive).  For example, factorial(3) = 6 (or 1*2*3); factorial(5) = 120 (or 1*2*3*4*5).

// 3) Fibonacci - Create a function to generate Fibonacci numbers.  In this famous mathematical sequence, each number is the sum of the previous two, starting with values 0 and 1.  Your function should accept one argument, an index into the sequence (where 0 corresponds to the initial value, 4 corresponds to the value four later, etc).  Examples: fibonacci(0) = 0 (given), fibonacci(1) = 1 (given), fibonacci(2) = 1 (fib(0)+fib(1), or 0+1), fibonacci(3) = 2 (fib(1) + fib(2)3, or 1+1), fibonacci(4) = 3 (1+2), fibonacci(5) = 5 (2+3), fibonacci(6) = 8 (3+5), fibonacci(7) = 13 (5+8).  Do this without using recursion first.  If you don't know what a recursion is yet, don't worry as we'll be introducing this concept in Part 2 of this assignment.

// 4) Array: Second-to-Last: Return the second-to-last element of an array. Given [42, true, 4, "Liam", 7], return "Liam".  If array is too short, return null.

// 5) Array: Nth-to-Last: Return the element that is N-from-array's-end.  Given ([5,2,3,6,4,9,7],3), return 4.  If the array is too short, return null.

// 6) Array: Second-Largest: Return the second-largest element of an array. Given [42,1,4,3.14,7], return 7.  If the array is too short, return null.

// 7) Double Trouble: Create a function that changes a given array to list each existing element twice, retaining original order.  Convert [4, "Ulysses", 42, false] to [4,4, "Ulysses", "Ulysses", 42, 42, false, false].











//1) Given an array and a value Y, count and print the number of array values greater than Y.

//2) Given an array, print the max, min and average values for that array.

//3) Given an array of numbers, create a function that returns a new array where negative values were replaced with the string ‘Dojo’.   For example, replaceNegatives( [1,2,-3,-5,5]) should return [1,2, "Dojo", "Dojo", 5].

//4) Given array, and indices start and end, remove values in that index range, working in-place (hence shortening the array).  For example, removeVals([20,30,40,50,60,70],2,4) should return [20,30,70].

//1) Return the given array, after setting any negative values to zero.  For example resetNegatives( [1,2,-1, -3]) should return [1,2,0,0].

//2) Given an array, move all values forward by one index, dropping the first and leaving a ‘0’ value at the end.  For example moveForward( [1,2,3]) should return [2,3,0].

//3) Given an array, return an array with values in a reversed order.  For example, returnReversed([1,2,3]) should return [3,2,1].

//4) Create a function that changes a given array to list each original element twice, retaining original order.  Have the function return the new array.  For example repeatTwice( [4,”Ulysses”, 42, false] ) should return [4,4, “Ulysses”, “Ulysses”, 42, 42, false, false].

// 1) Get 1 to 255 - Write a function that returns an array with all the numbers 	     from 1 to 255.

// 2) Get even 1000 - Write a function that would get the sum of all the even numbers    from 1 to 1000.  You may use a modulus operator for this exercise.

// 3) Sum odd 5000 - Write a function that returns the sum of all the odd numbers    from 1 to 5000. (e.g. 1+3+5+...+4997+4999).

// 4) Iterate an array - Write a function that returns the sum of all the values    within an array. (e.g. [1,2,5] returns 8. [-5,2,5,12] returns 14).

// 5) Find max - Given an array with multiple values, write a function that returns    the maximum number in the array. (e.g. for [-3,3,5,7] max is 7).

// 6) Find average - Given an array with multiple values, write a function that    returns the average of the values in the array. (e.g. for [1,3,5,7,20] average    is 7.2).

// 7) Array odd - Write a function that would return an array of all the odd numbers    between 1 to 50. (ex. [1,3,5, .... , 47,49]). Hint: Use 'push' method.

// 8) Greater than Y - Given value of Y, write a function that takes an array and    returns the number of values that are greater than Y. For example if arr = [1,    3, 5, 7] and Y = 3, your function will return 2. (There are two values in the    array greater than 3, which are 5, 7).

// 9) Squares - Given an array with multiple values, write a function that replaces    each value in the array with the value squared by itself. (e.g. [1,5,10,-2]    will become [1,25,100,4]).

// 10) Negatives - Given an array with multiple values, write a function that     replaces any negative numbers within the array with the value of 0. When the     program is done the array should contain no negative values. (e.g. [1,5,10,-2]     will become [1,5,10,0]).

// 11) Max/Min/Avg - Given an array with multiple values, write a function that     returns a new array that only contains the maximum, minimum, and average     values of the original array. (e.g. [1,5,10,-2] will return [10,-2,3.5]).

// 12) Swap Values - Write a function that will swap the first and last values of any     given array. The default minimum length of the array is 2. (e.g. [1,5,10,-2]     will become [-2,5,10,1]).

// 13) Number to String - Write a function that takes an array of numbers and     replaces any negative values within the array with the string 'Dojo'. For     example if array = [-1,-3,2], your function will return ['Dojo','Dojo',2].

// 1) Biggie Size - Given an array, write a function that changes all positive numbers in the array to the string "big".  Example: makeItBig([-1,3,5,-5]) returns that same array, changed to [-1, "big", "big", -5].

// 2) Print Low, Return High - Create a function that takes in an array of numbers.  The function should print the lowest value in the array, and return the highest value in the array.

// 3) Print Low, Return High - Create a function that takes in an array of numbers.  The function should print the lowest value in the array, and return the highest value in the array.

// 4) Double Vision - Given an array (similar to saying 'takes in an array'), create    a function that returns a new array where each value in the original array has    been doubled.  Calling double([1,2,3]) should return [2,4,6] without changing    the original array.

// 5) Count Positives - Given an array of numbers, create a function to replace the last value with the number of positive values found in the array.  Example, countPositives([-1,1,1,1]) changes the original array to [-1,1,1,3] and returns it.

// 6) Evens and Odds - Create a function that accepts an array.  Every time that array has three odd values in a row, print "That's odd!".  Every time the array has three evens in a row, print "Even more so!".

// 7) Increment the Seconds - Given an array of numbers arr, add 1 to every other element, specifically those whose index is odd (arr[1], arr[3], arr[5], etc).  Afterward, console.log each array value and return arr.

// 8) Previous Lengths - You are passed an array (similar to saying 'takes in an array' or 'given an array') containing strings.  Working within that same array, replace each string with a number - the length of the string at the previous array index - and return the array.  For example, previousLengths(["hello", "dojo", "awesome"]) should return ["hello", 5, 4]. Hint: Can for loops only go forward?

// 9) Add Seven - Build a function that accepts an array. Return a new array with all the values of the original, but add 7 to each. Do not alter the original array.  Example, addSeven([1,2,3]) should return [8,9,10] in a new array.

// 10) Reverse Array - Given an array, write a function that reverses its values, in-place.  Example: reverse([3,1,6,4,2]) returns the same array, but now contains values reversed like so... [2,4,6,1,3].  Do this without creating an empty temporary array.  (Hint: you'll need to swap values).

// 11) Outlook: Negative - Given an array, create and return a new one containing all the values of the original array, but make them all negative (not simply multiplied by -1). Given [1,-3,5], return [-1,-3,-5].

// 1) Sigma - Implement function sigma(num) that, given a number, returns the sum of all positive integers up to the given number (inclusive).  Ex: sigma(3) = 6 (or 1+2+3); sigma(5) = 15 (or 1+2+3+4+5).

// 2) Factorial - Write a function factorial(num) that, given a number, returns the product (multiplication) of all positive integers from 1 up to the given number (inclusive).  For example, factorial(3) = 6 (or 1*2*3); factorial(5) = 120 (or 1*2*3*4*5).

// 3) Fibonacci - Create a function to generate Fibonacci numbers.  In this famous mathematical sequence, each number is the sum of the previous two, starting with values 0 and 1.  Your function should accept one argument, an index into the sequence (where 0 corresponds to the initial value, 4 corresponds to the value four later, etc).  Examples: fibonacci(0) = 0 (given), fibonacci(1) = 1 (given), fibonacci(2) = 1 (fib(0)+fib(1), or 0+1), fibonacci(3) = 2 (fib(1) + fib(2)3, or 1+1), fibonacci(4) = 3 (1+2), fibonacci(5) = 5 (2+3), fibonacci(6) = 8 (3+5), fibonacci(7) = 13 (5+8).  Do this without using recursion first.  If you don't know what a recursion is yet, don't worry as we'll be introducing this concept in Part 2 of this assignment.

// 4) Array: Second-to-Last: Return the second-to-last element of an array. Given [42, true, 4, "Liam", 7], return "Liam".  If array is too short, return null.

// 5) Array: Nth-to-Last: Return the element that is N-from-array's-end.  Given ([5,2,3,6,4,9,7],3), return 4.  If the array is too short, return null.

// 6) Array: Second-Largest: Return the second-largest element of an array. Given [42,1,4,3.14,7], return 7.  If the array is too short, return null.

// 7) Double Trouble: Create a function that changes a given array to list each existing element twice, retaining original order.  Convert [4, "Ulysses", 42, false] to [4,4, "Ulysses", "Ulysses", 42, 42, false, false].


var arr = [1,2,3,4,5,6,7,8,9];
function reverseArray(x){
    var newArr = [];
    for(var i=0, j=x.length-1; i<x.length; i++, j--){
        newArr[i] = x[j];
    }
    return newArr;
}
var m = reverseArray(arr);
console.log(m);

var myArr = [5,4,3,0];
function revArray(x){
    var temp = 0;
    for(var i=0; i<x.length/2; i++){
        temp = x[i];
        x[i] = x[x.length-1-i];
        x[x.length-1-i] = temp;
    }
    return x;
}
var n = revArray(myArr);
console.log(n);
