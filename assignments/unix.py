import os
######### Free code ############
def getOctalPermissionsString(fileName):
    stat = os.stat(fileName).st_mode
    o = stat & 7
    stat //=8
    g = stat & 7
    stat //=8
    u = stat & 7
    return "{}{}{}".format(u,g,o)
print(getOctalPermissionsString("unix.py"))
###########end free code############
def ls(fileName="."):
    """prec:  fileName is a file or directory
postc:
    if fileName is an exist file, show its name
    if not, produce an error message about no such file or directory

    if fileNam is a directory, list its contents"""
    pass
def fancyLs(fileName="."):
    """ modify the ls function so that if fileName is an existing file
    its permission string (-rx-r--r) is shown, then the file's size,
    and finally the filename is shown.  It's a "junior" version of ls -l
    """
def pwd():
    """prec: none
postc: print the current working directory to the screen"""
    pass
def cat(*fileNames):
    """prec: none
    postc:  show contents of files to the screen in seriatum
    """
    pass
def loookFor(searchString, fileName):
    """prec:  none
    postc:  print out all lines containing the searchString in the
    file fileName with a line number at the beginning of each."""
    pass
def sizeOfRegularFIles(someDir = "."):
    """prec:  none
    postc: if someDir is not a directory, print an error message
    otherwise, compute the total size of the regular files in the directory."""
    pass
def head(fileName, howMany = 10):
    """prec: none
    postc: if the file does not exist, error out.
    Otherwise, show the first howMany lines of the file  If howMany is too
    large, just show the entire file."""
    with open(str(fileName),'r') as fp:
        for i in range(0,howMany):
            print(fp.readline())
#TestCode for head()
print(head('unix.py'))
print(head('unix.py',20))
#
def tail(fileName, howMany = 10):
    """prec: none
    postc: if the file does not exist, error out.
    Otherwise, show the last howMany lines of the file  If howMany is too
    large, just show the entire file."""
    with open(str(fileName),'r') as fp:
        tail_chunk_of_file = fp.readlines()[-howMany:]
    for i in tail_chunk_of_file:
        print(i)
#testcode for tail
tail('unix.py')
tail('unix.py',15)

    
