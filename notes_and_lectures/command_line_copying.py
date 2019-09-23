#This file allows you to copy a file to another, follow the following structure
#python command_line_copying.py <file_being_copied> <name_of_new_file>
from sys import argv

s = ''

if len(argv) > 3:
    raise("Error, only two positional arguments can be given, more than two were received!")

with open(str(argv[1]), 'r') as file_input:
    s = file_input.read()

with open(str(argv[2]),'w') as file_output:
    file_output.write(s)
    pass