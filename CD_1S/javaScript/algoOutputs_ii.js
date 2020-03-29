function printUpTo(x){
    if(x >= 1){
        for(var i=1; i<=1000; i++)
        console.log(i);
    } else {
        return  false;
    }
}
printUpTo(1000); 
y = printUpTo(-10);
console.log(y);

function printSum(x){
    var sum = 0;
    for(var i=0;i<=x;i++){
        console.log(i);
        sum += i;
        console.log(sum);
    }
    return sum
}
y = printSum(255)
console.log(y)