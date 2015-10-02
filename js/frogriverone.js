function sum(arr){
    var total = 0;
    for(var i = 0; i < arr.length; i++)
        total += arr[i];
    return total;
}

function frog_river_one(X, A){
    n = A.length;
    var leaf_pos = new Array(X+1);
    for(var i = 0; i < leaf_pos.length; i++)
        leaf_pos[i] = 1;
    var total = sum(leaf_pos);
    for(var j = 0; j < n; j++)
    {
        total -= leaf_pos[A[j]];
        leaf_pos[A[j]] = 0;
        if(total == 1)
            return j;
    }
    return -1;
}

var A = [1,3,1,4,2,3,5,4];
var X = 5;

console.log(frog_river_one(X, A));