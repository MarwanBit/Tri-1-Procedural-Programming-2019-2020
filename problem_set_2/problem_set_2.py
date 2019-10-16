import re 

#use this for printing pass/fail for tests.
def grade(b):
    return "Pass" if b else "Fail"
#use this for testing floating point near equality
def closeEnough(a,b):
    return abs(a - b) < 1e-6
def isPrime(n):
    """precondition:  n is a positive integer
postcondition: return True if n is prime; otherwise return False"""
    return False

if __name__ == "__main__":
    print(grade(not isPrime(4)))
    print(grade(isPrime(5)))
    print(grade(isPrime(997)))

def smallestFactor(n):
    """precondition:  n is a positive integer, n >= 2
postcondition: return the smallest factor of n that greater than 1"""
    return n

if __name__ == "__main__":
    print(grade(smallestFactor(21) == 5))
    print(grade(smallestFactor(1001) == 7))

def primeFactors(n):
    """prec:  n is an integer
postc: returns a list of all prime factors of n in ascending
order.  If n == 1, return []."""
    return []


def getEven(x):
    """precondition: x is a non-empty list of integers
postcondition: return the sum of the even numbers in the list"""
    return 0
print(grade(getEven([1,2,3,5,7,9,10]) == 12))

def getMad(x):
    """precondition:  x is a non-empty list of integers
postcondition: return the sum of the prime numbers in the list"""
    return 0

if __name__ == "__main__":
    print(grade(getMad([3,4,5,6,7,8,9]) == 15))


def numberName(n):
    """precondition:  n is an integer between 0 and 999,999,999
postcondition: return this number out as a word"""
    return "zero"

if __name__ == "__main__":
    print(grade(numberName(100) == "one hundred"))
    print(grade(numberName(1011) == "one thousand eleven"))

def disenvowel(s):
    """precondition:  s is a string of lower-case characters or spaces
postcondition: returns a copy of s with all vowels removed, and
spaces preserved.   """
    s = list(s)
    for index, char in enumerate(s):
        if char in ['a','e','i','o','u']:
            s.remove(index)
    s = s.join('')
    return s 

def biggestWord(someString):
    """precondition: someString is a string
postcondition: returns the biggest word (contiguous
string of non-whitespace characters in someString"""
    #Solved
    some_string_list = re.split("[ ]",someString)
    max_index = 0 
    max_value = 0
    for index,k in enumerate(some_string_list):
        if len(k) > max_value:
            max_value = len(k)
            max_index = index 
    return some_string_list[max_index]

    
#Hint: use recursion. This is easy to do if the list is empty. Then
# break the list into the first element and the rest of the list.
def sumFrom(n, intList):
    """precondition: n is a positive integer and x is a list of 
integers.
postcondition: returns a sublist of x that sums to n if it exists, or 
False otherwise."""
    #The case below tests if n is in the list, making the sum easy to find
    if n in intList:
        for i in range(len(intList)):
            if intList[i] == n:
                return intList[i:i] 
    
def aboutAverage(a, b, f, n):
    """precondition:   f is a function containing [a,b], a, b are floats
with a < b and n is an integer.  returns the average value of f sampled
at n+1 equidistributed points in [a,b]
postcondition: """
    pass