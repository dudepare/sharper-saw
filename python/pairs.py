
def pairs(A):
    pairs = 0
    for i in range(len(A)):
        head = A[i]
        for j in range(i+1, len(A)):
            if head == A[j]:
                pairs += 1
    return pairs

A = [3, 5, 6, 3, 3, 5, 6, 0, -2, 400, 34, -2]
print(pairs(A))