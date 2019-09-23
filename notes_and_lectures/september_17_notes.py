from sys import argv
#To print anything from the command line type python file_name things_to_print
#argv is everything in a list which contains all the arguments typed into the command line
print('My name is {} and I have just run.'.format(argv[1]))
print(argv)
for i in argv:
    print(i)
