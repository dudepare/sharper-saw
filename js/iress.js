function solution(M, A) {
    var N = A.length;
    var count = new Array(M + 1);
    var i;
    for (i = 0; i <= M; i++)
        count[i] = 0;
    var maxOccurence = 1;
    var index = -1;
    for (i = 0; i < N; i++) {
        count[A[i]] += 1;
        if (count[A[i]] > 0) {
            var tmp = count[A[i]];
            if (tmp > maxOccurence) {
                maxOccurence = tmp;
                index = i;
            }
        }
    }
    return A[index];
}
var A = [1,2,3,1,2,2,3,3,3];
var M = 3;
console.log(solution(M, A));
