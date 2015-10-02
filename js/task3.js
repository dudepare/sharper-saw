function solution(A) {
    var N = A.length;
    var result = 0;
    for (var i = 0; i < N * N; i++){
        var y = Math.floor(i/N);
        var x = i % N;
        if(A[x] == A[y])
            result = Math.max(result, Math.abs(x-y));
    }
    return result;
}
A =  [4, 6, 2, 2, 0, 0, 6];

console.log(solution(A));