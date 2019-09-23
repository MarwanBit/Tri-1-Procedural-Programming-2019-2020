newline_character = ""
for i in range(0,20):
	newline_character += "\n"

#Integers don't overflow in python, they're are only limited by memory
print((2**(2**(2**2)))**2000)

#Division vs. Integer division
print("\n\n\n\n\n\n" + str(20/3)) #This is Division
print(20//3) #This is integer division

#Other cool functions
print(ord("A"))
print(ord("B"))
print(chr(56))
print(chr(1568))

#Programming Exercises (1)
print(newline_character)
print(2**(10000))
print(newline_character)

#Programming Exercises (2)
print(bin(20))
print(int(0b10100))
print(float(0b10100))
#Below is the infix binary operator (I wonder what it does?)
print(2^8)
print(0b10^0b11)
print(0b11^0b11)
#It puts both of the arguments and puts them through an XOR Gate and then adds the result in binary and then
#Converts to decimal 

#Programming Exercises (3)
print(newline_character)
#The & operator returns the lowest number
print(0b11&0b11)
print(0b11&0b01)
print(0b10&0b10)

#Programming Exercises (4)
print(newline_character)
#The operator | returns the highest number 
print(0b11|0b10)
print(0b11|0b11)
print(0b10|0b11)
print(0b00|0b10)