import random

#Problem 1: write a function which prints out all the entries in the list passed through it
def print_list(input_list):
    k = 0 
    while k < int(len(input_list)):
        try: 
            i = str(input_list[k])
            print(i)
        except:
            raise("Everything must be castable to a string!!!")
        k += 1

#Problem 2: Write a function called untilDoubles that repeatedly rolls a pair of dice until you get doubles. Print the rolls as they occur. 
# If you get double ones, print "Snake Eyes!" and if you get double sixes, print "Boxcars!"
def until_doubles():
    #This function rolls doubles
    t = True
    while t:
        dice_1 = random.randint(1,6) 
        dice_2 = random.randint(1,6)
        string_roll = "Dice 1 rolled {}, Dice 2 rolled {}.".format(str(dice_1),str(dice_2))
        print(string_roll)
        if dice_1 == dice_2:
            print("Doubles")
            if dice_1 == 6:
                print("Boxcars!")
            elif dice_1 == 1:
                print("Snake Eyes!")
            t = False


#Write a function called until5Heads that repeatedly tosses a fair coin until you get five heads in a row. 
# return the tosses in a string like this: "HTHHHTTTHTTTHHHTTTTTHHHHH".
def until5heads():
    t = True
    head_roll = 0
    string_of_rolls = ""
    while t:
        dice = random.randint(0,1)
        if dice == 0:
            string_of_rolls += "H"
            head_roll += 1
        elif dice == 1:
            string_of_rolls += "T"
            head_roll = 0 
        if head_roll == 5:
            return string_of_rolls 

print('\n'*5)
list_to_print = ['121','Marwan Bit',1,5,4,6,[1,24,5,6],'0b101101']
print_list(list_to_print)
print('\n'*5)
until_doubles()
print('\n'*5)
print(until5heads())
