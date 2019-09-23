#We are going to chunck files instead of reading the whole thing 

fp = open('recursion.py','r')
print(type(fp))
print(fp.read(1))
print(fp.read(100))
print(fp.read(100))
print(fp.seek(50000))
print(fp.seek(30))
print(fp.read(1))
print(fp.tell())
print(fp.readline())
print(fp.readline())

hughJass = fp.readlines()
print(type(hughJass))
print(hughJass[:2])

#file.read(n) reads n characters, fp.seek(n) goes to the nth character, fp.tell() tells you which char you're in
#fp.readline() iterates through the line you are going through