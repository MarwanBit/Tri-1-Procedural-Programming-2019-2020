#This file will allow you to delete files from the python compiler
from sys import argv 
import os 


if len(argv) > 2:
    raise RuntimeError("Error, more positional arguments than ability to take in.")
else:
    t = True
    while t == True:
        user_confirmation = input("are you sure you want to delete(y/n)?:")
        if user_confirmation == 'y':
            if os.path.exists(argv[1]):
                os.remove(argv[1])
                print("You're file has been deleted")
                t = False
            else: 
                raise RuntimeError("That file/directory doesn't exist!!")
        elif user_confirmation == 'n':
            print("You're file is safe!!")
            quit()
        else:
            print('Type the right input you boomer!')
    


