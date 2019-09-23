from sys import argv 

def byCharacter(fileName):
    ch = ' '
    #With assigns open(args) to fp in this case, and in the end it closes
    #The file
    with open(str(fileName),'r') as fp:
        while ch != '':
            ch = fp.read(1)
            print(ch,end='')

def foolish(fileName):
    '''
    #The line below creates an object which holds the file
    fp = open(str(fileName),'w')
    fp.close()
    '''
    pass

def byLine(fileName):
    '''prints a file by name'''
    with open(str(fileName),'r') as fp:
        #iter(obj) casts obj to an iterator, although this is redundant
        for line in iter(fp):
            print(line)

byCharacter(argv[1])