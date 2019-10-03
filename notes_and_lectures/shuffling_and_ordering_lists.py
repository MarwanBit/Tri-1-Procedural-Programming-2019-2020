import random 

def is_in_order(input_list):
    'Returns true if the list is in order'
    for k in range(len(input_list) - 1):
        if input_list[k] > input_list[k+1]:
            return False 
    return True

def bozo_shuffle(input_list):
    """This sort is extremely inefficient, it works on factorial time"""
    while not is_in_order(input_list):
        random.shuffle(input_list)

def reagan_sort(input_list):
    """A Trickle down sort inspired by Reaganomics"""
    list_pointer = 1
    while list_pointer < len(input_list):
        list_pointer += 1 
        sub_list = input_list[0:list_pointer]
        if not is_in_order(input_list):
            sub_list.sort() 
            input_list[0:list_pointer] = sub_list
    return input_list

def swap(x,k,i):
    #k is a list, k and i are indices
    if k != 1:
        x[k],x[i] = x[i], x[k]

def morrisons_reagan_sort(input_list):
    """John Morrison's Reagan sort"""
    p = 1 
    while p < len(x):
        p += 1
        q = p - 1
        while q>0 and x[q] >= x[q-1]:
            swap(x,q,q-1)
            q -= 1

def least_possible(input_list):
    p = 0 
    while p < len(input_list):
        record_index = p 
        q = p 
        while q < len(input_list):
            if input_list[q] < input_list[record_index]:
                record_index = q 
            q += 1
        swap(x,record_index,p)
        record_index = p 
        q = p 
        p += 1


x= list(range(1000))
random.shuffle(x)
print(x)
least_possible(x)
print(x)
