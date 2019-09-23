#Exercise (1)
for k in range(200,300):
	print(k,hex(id(k)))
#It seems that small commonly used values/ immutable values are stored

#Exercise (2)
for k in range(-300,-200):
	print(k,hex(id(k))) 
#The same pooling of integers seems to apply for negative integers 

#Object has three attributes: State, identity, behavior 

print('''Mult-Line
	Multi-Line
	Multi-Line''')
print("jordan".capitalize())

#How to use .center()
print("Marwan!".center(50,"/"))

#Programming Exercises (P2)
string = "Marwan"
print(string.rfind('M'))
print(string.endswith("wan"))
print(string.startswith("Mar"))
print(string.lower())
print(string.upper())
string = "     Marwan    "
print(string)
print(string.strip())
string = "     Marwan    " 
print(string.lstrip()) 
string = "     Marwan    "  
print(string.rstrip()) 

motley = [True, "foo", 2, 2.0, ["cat", False, -1]]
print(motley[4][0])

#Adding lists and tuples 
print([1,2,3] + [4,5,6])
print((1,2,3) + (4,5,6))

m = "aaaaaa"
print(m.count("a"))

#Double splicing/ skips
jaq = "abcdefghijklmnopqrstuvwxyz"
print(jaq[::3])
print(jaq[5:10:3])