import itertools

#Ask Dr.Morrison if this solution is ok, having length as a parameter
def sumFrom(n, intList, length):
    """precondition: n is a positive integer and x is a list of 
integers. Length should be len(intList)
postcondition: returns a sublist of x that sums to n if it exists, or 
False otherwise."""
    #The case below tests if n is in the list, making the sum easy to find
    if n in intList:
        for i in range(len(intList)):
            if intList[i] == n:
                return_list = []
                return_list.append(intList[i])
                return return_list     
    else:
        if length >= 1:
            list_of_all_combinations_k_length = list(itertools.combinations_with_replacement(intList,length))
            for combination in list_of_all_combinations_k_length:
                if sum(combination) == n:
                    return list(combination)
            sumFrom(n,intList,length-1)
        elif length == 0: 
            return "No Such List, Sorry :("
    

#Trying a new Idea 
def sumFrom_2_0(n,intList):
    n = n 
    intList = intList 
    length = len(intList)
    return sumFrom(n,intList,length)
    
#test_list = [1,1,2,3,4,5]
#print(sumFrom(1,[1,1,2,3,4,5],len(test_list)))
#test_list = [0,1,2,3,4,5,6,777,77,7,7]
#print(sumFrom(2,[0,1,2,3,4,5,6,777,77,7,7],len(test_list)))

#test_list = [1,2,3,34,44,55,5,55,5]
#k = list(itertools.combinations_with_replacement([1,2,3,34,44,55,5,55,5], len(test_list)))
#print(dir(k))
#print(k)

test_list = [1,2,3,4,5,65,6,7,8,8,8,8,88,9,99,99,99,999,9999,99,9999,99,99,999]
print(len(test_list))
print(sumFrom_2_0(385,test_list))