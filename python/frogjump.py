
def frogjump(X, Y, D):
    return (abs(Y-X) + (D-1))//D

print(frogjump(10, 85, 30))