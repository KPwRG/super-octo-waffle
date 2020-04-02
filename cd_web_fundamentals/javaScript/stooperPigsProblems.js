// Bubble sort

var q = [4, 6, 7, 3, 1];
var w = [6, 4, 7, 3, 1];
function largestLast(x) {
    var swapped = true;
    for (var j = 0; j < x.length && swapped; j++) {
        var temp = 0;
        swapped = false;
        for (var i = 0; i < x.length; i++) {
            if (x[i - 1] > x[i]) {
                temp = x[i - 1];
                x[i - 1] = x[i];
                x[i] = temp
                swapped = true;
            }
        }
    }
    return x;
}
var b = largestLast(q);
console.log(b);
var n = largestLast(w);
console.log(n);