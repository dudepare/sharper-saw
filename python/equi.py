def equi(A):
    for k in range(len(A)):
        rsum = 0
        lsum = 0
        for m in range(k):
            lsum += A[m]
        for n in range(k+1, len(A)-1):
            rsum += A[n]
        if lsum == rsum:
            return k
    return -1


def equi2(A):
    if len(A) == 0:
        return -1
    
    sum = 0
    # compute for the sum
    for i in range(len(A)):
        sum += A[i]

    lsum = 0
    for k in range(len(A)):
        rsum = sum - lsum - A[k]
        if rsum == lsum:
            return k
        lsum += A[k]

    return -1

if __name__ == '__main__':
    A = [-7,1,5,2,-4,3,0]
    B = [-1, 3, -4, 5, 1, -6, 2, 1]
    print(equi(A))
    print(equi2(A))
    print(equi(B))
    print(equi2(B))