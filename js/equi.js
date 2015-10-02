function equi(A){
    var lsum;
    var rsum;
    for(var k = 0; k < A.length; k++)
    {
        lsum = 0;
        rsum = 0;
        for(var m = 0 ; m < k; m++)
            lsum += A[m];

        for(var n = k+1; n < A.length; n++)
            rsum += A[n];

        if (lsum == rsum) return k;
    }

    return -1;
}

function equi2(A){
    if(A.length === 0) return -1;

    // calculate sum
    sum = 0;
    for(var i = 0; i < A.length; i++)
        sum += A[i];

    var rsum = 0;
    var lsum = 0;
    for(var j = 0; j < A.length; j++){
        // calculate rsum by sum - lsum
        rsum = sum - lsum - A[j];
        if(lsum == rsum)
            return j;
        lsum += A[j];
    }
    return -1;
}

var A = [-7,1,5,2,-4,3,0];
console.log(equi(A));
console.log(equi2(A));

