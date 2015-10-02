def missing(A):
    size = len(A)
    if size == 0:
        return 1
    total = 0
    for i in range(1, size+2):
        total +=i

    return total - sum(A)
A = [1,6,3,2,5]
print(missing(A))
