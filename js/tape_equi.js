function tape_equi(A)
{

    var lsum = A[0];
    var rsum = 0;
    var total = 0;
    for (var i = 0; i < A.length ; ++i)
        total += A[i];

    var min_diff = -1;

    for (var j = 0; j < A.length-1; ++j)
    {
        rsum = total - lsum;
        var current_diff = Math.abs(lsum - rsum);
        if (min_diff === -1)
            min_diff = current_diff;
        else
            min_diff = Math.min(min_diff, current_diff);
        lsum += A[j+1];
    }
    return min_diff;
}

A = [3,1,2,4,3];//[1,1];
console.log(tape_equi(A));