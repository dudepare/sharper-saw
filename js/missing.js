function missing(A){

    var size = A.length;
    if(size === 0)   return 1;
    var total = 0;
    var sum = 0;
    for(var j = 0; j < size; j++)
        sum += A[j];
    for(var i = 1; i <= size+1; i++)
        total += i;
    return total - sum;
}

console.log(missing([2,1]));