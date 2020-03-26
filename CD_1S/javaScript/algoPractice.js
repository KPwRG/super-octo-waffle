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

var a = [1,2,3];
function returnReversed(x){
    newArr = [];
    for(i=0; i<x.length; i++){
        for(j=x.lenght-1; j<x.length; j--){
            newArr = x[j];
        }
    }
    return newArr;
}
var b = returnReversed(a);
console.log(b);