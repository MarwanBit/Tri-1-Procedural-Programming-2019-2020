import re 
import math
import itertools

#Custom Function made for one of the problems
def get_factor_list(n):
    '''returns list of all factors of n from [1,n]'''
    list_of_factors = []
    for i in range(1,n+1):
        if n%i == 0: 
            list_of_factors.append(i)
    return list_of_factors


#use this for printing pass/fail for tests.
def grade(b):
    #Provided
    return "Pass" if b else "Fail"
#use this for testing floating point near equality
def closeEnough(a,b):
    #Provided
    return abs(a - b) < 1e-6

def isPrime(n):
    """precondition:  n is a positive integer
postcondition: return True if n is prime; otherwise return False"""
    #Works!
    if n == 1:
        return False
    for i in range(1,n):
        if (n % i == 0) and i != 1:
            return False
    return True

if __name__ == "__main__":
    print(grade(not isPrime(4)))
    print(grade(isPrime(5)))
    print(grade(isPrime(997)))

def smallestFactor(n):
    """precondition:  n is a positive integer, n >= 2
postcondition: return the smallest factor of n that greater than 1"""
    #Works
    factor_list = get_factor_list(n)
    del factor_list[0] #deletes 1 from the factor list 
    return min(factor_list)


if __name__ == "__main__":
    print(grade(smallestFactor(21) == 3))
    print(grade(smallestFactor(1001) == 7))

def primeFactors(n):
    """prec:  n is an integer
postc: returns a list of all prime factors of n in ascending
order.  If n == 1, return []."""
    #Works, but ask if primeFactors(5) should give you 5 and 1 
    if n == 1: 
        return [] 
    factors_list = get_factor_list(n)
    prime_factors = [] 
    for i in factors_list:
        if isPrime(i):
            prime_factors.append(i) 
    return prime_factors


def getEven(x):
    #Works!!!
    """precondition: x is a non-empty list of integers
postcondition: return the sum of the even numbers in the list"""
    list_of_evens = []
    for i in x:
        if i % 2 == 0: 
            list_of_evens.append(i)
    out = sum(list_of_evens)
    return out

if __name__ == "__main__":    
    print(grade(getEven([1,2,3,5,7,9,10]) == 12))

def getMad(x):
    """precondition:  x is a non-empty list of integers
postcondition: return the sum of the prime numbers in the list"""
    #Works
    out = 0 
    for i in x:
        if isPrime(i):
            out += i
    return out

if __name__ == "__main__":
    print(grade(getMad([3,4,5,6,7,8,9]) == 15))


def numberName(n):
    #Solved, needs to be optimized
    """precondition:  n is an integer between 0 and 999,999,999
postcondition: return this number out as a word"""

    list_of_numbers_between_10_and_20_exclusive = [
        'eleven','twelve','thirteen','fourteen','fifteen',
        'sixteen','seventeen','eighteen','nineteen'
    ]
    list_of_tens_multiples = [
        'ten','twenty','thirty','fourty','fifty',
        'sixty','seventy','eighty','ninety'
    ]
    list_of_one_digit_numbers = [
        'zero','one','two','three','four','five','six',
        'seven','eight','nine'
    ]
    list_of_hundreds = [
        "one hundred", "two hundred", "three hundred", "four hundred", "five hundred",
        "six hundred", "seven hundred", "eight hundred", "nine hundred"
    ]
    list_of_thousands = [
        "one thousand", "two thousand", "three thousand", "four thousand", "five thousand", 
        "six thousand", "seven thousand", "eight thousand", "nine thousand"
    ]
    list_of_ten_thousands = [ 
        "ten thousand", "twenty thousand", "thirty thousand", "fourty thousand", "fifty thousand", 
        "sixty thousand", "seventy thousand", "eighty thousand", "ninety thousand"
    ]
    list_of_hundred_thousands = [
        "one hundred thousand", "two hundred thousand", "three hundred thousand", "four hundred thousand", 
        'five hundred thousand', 'six hundred thousand', 'seven hundred thousand', 'eight hundred thousand', 
        'nine hundred thousand'
    ]
    list_of_millions = [
        "one million", "two million", "three million", "four million", "five million", "six million", 
        "seven million", "eight million", "nine million"
    ]
    list_of_tens_of_millions = [
        "ten million", "twenty million", "thirty million", "fourty million", "fifty million", "sixty million", 
        'seventy million', 'eighty million', 'ninety million'
    ]
    list_of_hundrds_of_millions = [
        "one hundred million", "two hundred million", "three hundred million", "four hundred million", 
        "five hundred million", "six hundred million", "seven hundred million", "eight hundred million", 
        "nine hundred million"
    ]
    if len(str(n)) == 1:
        return list_of_one_digit_numbers[int(n)]
    elif len(str(n)) == 2: 
        if n == 10:
            return list_of_tens_multiples[0] 
        elif (int(str(n)[0]) == 1) and (int(str(n)[1]) > 0): 
            return list_of_numbers_between_10_and_20_exclusive[int(str(n)[1])-1]
        elif int(str(n)[0]) >= 2 and (int(str(n)[1]) > 0): 
            return list_of_tens_multiples[int(str(n)[0])-1] + numberName(int(str(n)[1])) 
        elif int(str(n)[0]) >= 2 and (int(str(n)[1]) == 0):
            return list_of_tens_multiples[int(str(n)[0])-1]
    elif len(str(n)) == 3: 
        if int(str(n)[0]) > 0 and (int(str(n)[1]) == 0 and int(str(n)[2]) == 0):
            return list_of_hundreds[int(str(n)[0])-1] 
        else:
            return list_of_hundreds[int(str(n)[0])-1] + numberName(int(str(n)[1:]))
    elif len(str(n)) == 4: 
        if int(str(n)[0]) > 0 and (int(str(n)[1]) == 0 and int(str(n)[2]) == 0 and int(str(n)[3]) == 0):
            return list_of_thousands[int(str(n)[0])-1] 
        else:
            return list_of_thousands[int(str(n)[0])-1] + numberName(int(str(n)[1:]))
    elif len(str(n)) == 5: 
        if (
            int(str(n)[0]) > 0 and int(str(n)[1]) == 0 and int(str(n)[2]) == 0 and 
            int(str(n)[3]) == 0 and int(str(n)[4]) == 0
        ):
            return list_of_ten_thousands[int(str(n)[0])-1] 
        else:
            return list_of_ten_thousands[int(str(n)[0])-1] + numberName(int(str(n)[1:]))
    elif len(str(n)) == 6: 
        if (
            int(str(n)[0]) > 0 and int(str(n)[1]) == 0 and int(str(n)[2]) == 0 and 
            int(str(n)[3]) == 0 and int(str(n)[4]) == 0 and int(str(n)[5]) == 0
        ):
            return list_of_hundred_thousands[int(str(n)[0])-1] 
        else:
            return list_of_hundred_thousands[int(str(n)[0])-1] + numberName(int(str(n)[1:]))
    elif len(str(n)) == 7: 
        if (
            int(str(n)[0]) > 0 and int(str(n)[1]) == 0 and int(str(n)[2]) == 0 and 
            int(str(n)[3]) == 0 and int(str(n)[4]) == 0 and int(str(n)[5]) == 0 and 
            int(str(n)[6]) == 0
        ):
            return list_of_millions[int(str(n)[0])-1] 
        else:
            return list_of_millions[int(str(n)[0])-1] + numberName(int(str(n)[1:]))
    elif len(str(n)) == 8: 
        if (
            int(str(n)[0]) > 0 and int(str(n)[1]) == 0 and int(str(n)[2]) == 0 and 
            int(str(n)[3]) == 0 and int(str(n)[4]) == 0 and int(str(n)[5]) == 0 and 
            int(str(n)[6]) == 0 and int(str(n)[7]) == 0
        ):
            return list_of_tens_of_millions[int(str(n)[0])-1] 
        else:
            return list_of_tens_of_millions[int(str(n)[0])-1] + numberName(int(str(n)[1:]))
    elif len(str(n)) == 9: 
        if (
            int(str(n)[0]) > 0 and int(str(n)[1]) == 0 and int(str(n)[2]) == 0 and 
            int(str(n)[3]) == 0 and int(str(n)[4]) == 0 and int(str(n)[5]) == 0 and 
            int(str(n)[6]) == 0 and int(str(n)[7]) == 0 and int(str(n)[8]) == 0
        ):
            return list_of_hundrds_of_millions[int(str(n)[0])-1] 
        else:
            return list_of_hundrds_of_millions[int(str(n)[0])-1] + numberName(int(str(n)[1:]))
    
    


if __name__ == "__main__":
    print(grade(numberName(100) == "one hundred"))
    print(grade(numberName(1011) == "one thousand eleven"))

def disenvowel(s):
    """precondition:  s is a string of lower-case characters or spaces
postcondition: returns a copy of s with all vowels removed, and
spaces preserved.   """
    #Solved
    s = list(s)
    for index, char in enumerate(s):
        if char in ['a','e','i','o','u']:
            del s[index]
    string = ''
    for i in s:
        string += str(i)
    return string

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

    
def check_easy_sumFrom_cases(n,intList):
    '''check the easy cases of sumFrom'''
    return_list = []
    if sum(intList) < n: 
        return return_list
    elif n in intList: 
        return_list.append(n)
        return return_list
    
def check_cases_of_n_length(length,intList,n):
    '''checks cases for sum from of length: length'''
    combinations = itertools.combinations(intList,length)
    for i in combinations:
        if sum(i) == n:
            return list(i)

#Hint: use recursion. This is easy to do if the list is empty. Then
# break the list into the first element and the rest of the list.
def sumFrom(n, intList):
    """precondition: n is a positive integer and x is a list of 
integers.
postcondition: returns a sublist of x that sums to n if it exists, or 
False otherwise."""
    #Checks easy cases 
    if check_easy_sumFrom_cases(n,intList) != None: 
        return check_easy_sumFrom_cases(n,intList)
    length_variable = 2 
    while length_variable <= len(intList): 
        if check_cases_of_n_length(length_variable,intList,n) != None:
            return check_cases_of_n_length(length_variable,intList,n)
        length_variable += 1

    

    
def aboutAverage(a, b, f, n):
    """precondition:   f is a function containing [a,b], a, b are floats
with a < b and n is an integer.  returns the average value of f sampled
at n+1 equidistributed points in [a,b]
postcondition: """
    #Solved
    distance_between_points = (a+b)/n 
    distance_from_a = 0 
    list_of_x_data_points = []
    for i in range(n+1):
        list_of_x_data_points.append(a+distance_from_a)
        distance_from_a += distance_between_points
    list_of_y_data_points = [f(i) for i in list_of_x_data_points]
    return sum(list_of_y_data_points)/(n+1)
