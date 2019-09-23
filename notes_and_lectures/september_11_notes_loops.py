import math

n = 10 
while n > 0:
    print(n)
    n -= 1

def factorial(n):
    if n == 0:
        return 1
    factorial_sum = 1
    while n>0:
        factorial_sum *= n 
        n = n-1 

def makeTable(some_list):
    out = "<table>\n"
    k = 0 
    while k < len(some_list):
        out += "<tr><td>{}</td><td>{}</td></tr>\n".format(k,some_list[k])
        k += 1
    out += "</table>\n" 
    return out

def summer(f, n):
    k = 1 
    out = 0 
    while k<=n:
        out += f(k)
        k += 1 
    return out

print(summer(factorial,10))

#Project Euler
#You sign up and it gives you computational problems