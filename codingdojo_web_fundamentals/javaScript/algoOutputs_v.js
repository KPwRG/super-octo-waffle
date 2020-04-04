// 1) Return the given array, after setting any negative values to zero.  For example resetNegatives( [1,2,-1, -3]) should return [1,2,0,0].

var a = [1,2,-1,-3];
function resetNegatives(x){
    var newArr = [];
    for(var i=0; i<x.length; i++){
        if(x[i] < 0){
            newArr[i] = 0;
        }else{
            newArr[i] = x[i];
        }
    }
    return newArr;
}
var b = resetNegatives(a);
console.log(b);

// 2) Given an array, move all values forward by one index, dropping the first and leaving a ‘0’ value at the end.  For example moveForward( [1,2,3]) should return [2,3,0].

var n = [12,13,14];

function moveForward(x){
    var temp = 0;
    for(i=1; i<x.length; i++){
        temp = x[i];
        x[i] = x[i-1];
        x[i-1] = temp;
    }
    x.pop();
    x.push(0);
    return x;
}

console.log(moveForward(n));

// 3) Given an array, return an array with values in a reversed order.  For example, returnReversed([1,2,3]) should return [3,2,1].

var n = [12,13,14];

function returnReversed(x){
    var newArr = [];
    for( var i=0, j=x.length-1; i<x.length; i++, j--){
        newArr[i] = x[j];
    }
    return newArr;
}

console.log(returnReversed(n));

// 4) Create a function that changes a given array to list each original element twice, retaining original order.  Have the function return the new array.  For example repeatTwice( [4,”Ulysses”, 42, false] ) should return [4,4, “Ulysses”, “Ulysses”, 42, 42, false, false].

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