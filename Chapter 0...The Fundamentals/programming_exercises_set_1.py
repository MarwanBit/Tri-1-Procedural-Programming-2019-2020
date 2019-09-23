newline_character = "\n"
for i in range(0,10):
	newline_character += "\n"

#These prints the nth digit of 3/7 where n is in the string "{:.nf}"" Exercise (1)
print("{:.3f}".format(3/7))
print("{:.2f}".format(3/7))
print("{:.1f}".format(3/7))

#This prints the number in scientific notation Exercise (2)
print("{:.1e}".format(3/7))
print("{:.8e}".format(3/7))
print("{:.9e}".format(3/7))

#Exercise (3)
print("{:.8f}".format(2))
print("{:40.8f}".format(2))

#Exercise (4)
print("{:5.1f}".format(3/7))
print("{:1.3f}".format(3/7))
print("{:-1.3f}".format(3/7))
print("{:-20.3f}".format(3/7))

#Exercise 5
print("My name is {}, {}".format("Marwan","Bit"))
print("My name is {1}, {0}".format("Marwan","Bit"))

#Multiplying Strings
print("*"*20) #we are printing the asterisks 20 times using String multiplication
# if "string"*n when n is <= 0, an empty string is returned 

#Boolean order of operations --> not, and, or 

#Every object in python has its own ID, below is an example
print(hex(id(1)))
print(hex(id(2)))
print(hex(id(newline_character)))

#Variables don't store the value you assign to them, they store the address of the 
#value you assign to them
print(newline_character)
print(hex(id(5)))
x = 5
print(hex(id(5)))

#Look at the following variable assignment (the following code switches the values)
a = 4
b = 5
a,b = b,a 
print(a)
print(b)

print("*"*80)
print(80*"*")
print(hex(id("sid is sus")))
print(ord("J"))
