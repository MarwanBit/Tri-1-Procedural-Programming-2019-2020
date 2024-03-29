import math
import os

x = [1,2,3,4,5,6]
#Below is a list comprehensions
y = [k*k for k in x]
print(y)

#This function will take a reinmann sum
def trap(a, b, n, f):
    #a and b are the top and lower bounds of the function
    #f is the function and n is the number of rectangles.
    out = (f(a) + f(b))/2 
    h = (b - a)/n 
    x = [f(a+ k*h) for k in range(1,n)]
    out += sum(x)
    return h*out

#reinman sum of x^2 from 0 to 1
print(trap(0,1,100,lambda x:x*x))

print(trap(0,math.pi,100,math.sin))

files = os.listdir('.')
print(files)
python_files = [k for k in files if k.endswith(".py")]
print(python_files)
filtered_files = [os.path.getsize(k) for k in files if k.endswith('.py')]
print(sum(filtered_files))

#[foo(k) for k in someList if someCondition]
#Below is the structure for a dictionary comprehension....
#{k:v for (k,v) in dict.items()}

x = ['Teague','Da Monk','Brisk','King','Hunt','Rash']
filtered_list = [j.lower() for j in x if len(j) > 4]
print(filtered_list)

#sorted() vs. .sort()
#sorted returns a new sorted list while .sort() sorts the list you already have.
#Example
y = sorted(x)
print(y)
x.sort()
print(x)


def f_block_sort(input_list):
    length = len(input_list)
    for i in range(0,length-1):
        if input_list[i] > input_list[i+1]:
            input_list[i],input_list[i+1] = input_list[i+1],input_list[i]
    return input_list

#Sets in python, non-repeating, cannot contain lists 
#Try the hash function
print(hash(1))
#Hashing: is a function which takes some object and turns it into an integer, can't hash a list, 
#You can't hash lists because hashing is dependent on the object being immutable and having a type,
#lists are immutable, therefore they cannot be hashed