import sys

x = range(5)
print(type(x))
y = iter(x)
print(y)
print(next(y))
print(next(y))
random_list = []
for k in range(10):random_list.append(k)
print(random_list)
random_list = []
for k in range(5,10): random_list.append(k)
print(random_list)
random_list = []
for k in range(2,150,7): random_list.append(k)
print(random_list)
random_list = []
for k in range(10,-1,-1): random_list.append(k)
print(random_list)
random_list = []

#anything you want to use a for loop on requires an iterator, test using the iter() function
#New Objects: range object, iterator object
#Lists, ranges, tuples, and strings are all iterable

for k in []: print(k)
for k in '': print(k)

def triangle(n):
    #n is a non negative integer, returns 1 + 2 + 3 .... 
    sum = 0
    for i in range(0,n+1):
        sum += i 
    return sum 

print(triangle(4)==10,",",triangle(10)==55)
print(triangle(0)==0)

def filterForStrings(x):
    '''x is a list, returns a list with all strings element in x'''
    filtered_list = []
    for i in x:
        if type(i) == str:
            filtered_list.append(i)
    return filtered_list 

test_list = ['a','b','c',1,2,4,5,'cd']
print(filterForStrings(test_list) == ['a','b','c','cd'])

def fib(n):
    '''prec n is a nonnegative integer, returns the nth fibonnaci number'''
    if n == 0:
        return 0 
    elif n == 1:
        return 1 
    else: 
        return fib(n-1) + fib(n-2)

print(fib(0)==0,fib(1)==1,fib(2) == 1, fib(3) == 2)

def fib1(n):
    '''prec n is a nonnegative integer, returns the nth fibonnaci number'''
    fib_1 = [0,1]
    if n < 2:
        return fib_1[n]
    else:
        for i in range(n-1):
            fib_1.append(sum(fib_1))
            del fib_1[0]
        return fib_1[1]

for i,k in enumerate(range(10)):
    print('fib({}) = {}'.format(i, fib(k)))

def easterEgg(x):
    '''x is a list of numbers, returns nothing but squares every number in the list'''
    strings_in_x = filterForStrings(x)
    x -= strings_in_x
    squares_list = []
    for item in x:
        item = item**2
        squares_list.append(item)
    return squares_list


#research enumerate
print(enumerate(range(10)))
def explicitPrintList(x):
    #Imagine enumrate as a list of tuples
    for i, item in enumerate(x):
        print("x[{}] == {}".format(i,item))
explicitPrintList(['1','2','3','4','5'])