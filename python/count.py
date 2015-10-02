# tallies numbers as they appear assuming numbers belongs to a known set
"""
0 - 0
1 - 1
2 - 3
3 - 1
4 - 4
5 - 2
"""
def counting(A, m):
    n = len(A)
    # create an array with m+1 elements
    count = [0] *(m+1)
    # traverse the array
    for k in range(n):
        number = A[k]
        count[number] += 1
    return count

A = [1,4,3,4,4,5,2,5,4]
B = [3,4,1,4,4,5,2,5,4]
m = 5
#counting(A, m)

def slow_solution(A,B, m):
    n = len(A)
    sum_a = sum(A)
    print("sum_a {0}".format(sum_a))
    sum_b = sum(B)
    print("sum_b {0}".format(sum_b))
    for i in range(n):
        for j in range(n):
            change = B[j] - A[i]
            sum_a += change
            sum_b -= change
            if(sum_a == sum_b):
                print(i,j)
                return True
            sum_a -= change
            sum_b += change
    return False

print(slow_solution(A,B,m))

def fast_solution(A,B, m):
    n = len(A)
    sum_a = sum(A)
    sum_b = sum(B)
    d = sum_b - sum_a
    if(d%2) == 1:
        return False
    d //= 2
    count = counting(A,m)
    for i in range(n):
        number = B[i] - d
        if 0 <= number and number <= m and count[number] > 0:
            print(number)
            return True
    return False

print(fast_solution(A,B,m))