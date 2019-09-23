from sys import setrecursionlimit

def pow(x,n):
    if n<0:
        return pow(1/x,n)
    if n == 0:
        return 1 
    elif n == 1:
        return x 
    return x * pow(x,n-1)

def kerpow(x,n):
    if n<0:
        return pow(1/x,n)
    if n == 0:
        return 1 
    elif n == 1:
        return x 
    if n%2 == 0:
        return kerpow(x*x, n//2) 
    return x * kerpow(x*x, n//2)

setrecursionlimit(10000)
print(pow(2,10)== 1024)
print(kerpow(1.0000001,10000000))
#Below is an approximation for E
print(pow(1.001,1000))

