import random 

def is_in_order(input_list):
    'Returns true if the list is in order'
    for k in range(len(input_list) - 1):
        if input_list[k] > input_list[k+1]:
            return False 
    return True

#This sort is extremely inefficient, it works on factorial time
def bozo_shuffle(input_list):
    while not is_in_order(input_list):
        random.shuffle(input_list)


x= list(range(10))
random.shuffle(x)
print(x)
bozo_shuffle(x)
print(x)