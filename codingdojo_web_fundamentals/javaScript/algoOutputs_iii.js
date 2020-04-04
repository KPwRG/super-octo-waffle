function printAverage(x){
    var sum = 0;
    for(var i=0; i<x.length; i++){
        sum = x[i] + sum;
    }
    return sum/x.length;
}
y = printAverage([1,2,3]);
console.log(y);

function returnOddArray(){
    oddArray = [];
    for(var i=1; i<=255; i+=2){
        oddArray.push(i); 
    }
    return oddArray;
}
y = returnOddArray();

function squareValue(x){
    for(var i=0; i<x.length; i++){
        x[i] = x[i] * x[i];
    }
    return x;
}
y = squareValue([1,2,3]);
console.log(y);
