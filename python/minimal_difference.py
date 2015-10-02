def min_diff(A):
    lsum = A[0]
    rsum = 0
    total = sum(A)
    min_diff = -1

    for i in range(1, len(A)):
        rsum = total - lsum
        diff = abs(rsum - lsum)
        if min_diff == -1:
            min_diff = diff
        else:
            min_diff = min(min_diff, diff)
        lsum += A[i]
    return min_diff

A = [3,1,2,4,3]
print(min_diff(A))