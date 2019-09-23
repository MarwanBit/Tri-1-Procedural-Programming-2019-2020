from sys import argv 
'''
Make a command which takes <search string> <file name> <0(for false) or 1(for true)>
it searches for all lines in file which contains the search string, <0 or 1>
makes it case insensitive or case sensitive
'''

case_sensitive = str(argv[3])
string_in_file = False
search_string = argv[1]

if len(argv) > 4:
    raise RuntimeError("To many arguments provided!!")
else:
    with open(str(argv[2]),'r') as file_to_read:
        for line in file_to_read:
            line = line.strip()
            if case_sensitive == '1':
                line = str(line).lower()  
                search_string = search_string.lower()
            if search_string in line:
                string_in_file = True
                print(line)
    print("String in file: {}".format(str(string_in_file)))

