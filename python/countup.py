def faster_solution(n):
    result = 0
    for i in range(n):
        result += (i+1)
    return result


def even_faster_solution(n):
    return n * (n + 1) // 2

print(even_faster_solution(50))
print(faster_solution(50))
"""
xrange is deprecated in python 3.
range function in python 3 is actually the xrange in python 2
in python 2, range function creates the list.
the xrange function does not, it returns an xrange object"""
