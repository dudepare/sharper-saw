def frog_river_one(X,A):
    leaf_pos = [1] * (X+1)
    total = sum(leaf_pos)
    for i in range(len(A)):
        total -= leaf_pos[A[i]]
        leaf_pos[A[i]] = 0
        if total == 1:
            return i

    return -1

A = [1,3,1,4,2,3,5,4]
X = 5

print(frog_river_one(X, A))
