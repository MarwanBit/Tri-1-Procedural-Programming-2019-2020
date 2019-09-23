#Return ends a functions execution and returns an object 

#You specify a functions pre and post conditions

def allowed_in_pub(age):
	if age < 21:
		print("you can't enter the pub!")
	elif age >= 65:
		print("Shall I cash yer soshal, Geezer??")
	else:
		print("You can drink to your hearts content")

def abs_val(x):
	#below is a condition called a "simple x"
	if x < 0:
		x = -1*x 
	return x 

##test suite 
x = 5 
print(abs_val(x) == 5)
x = -5
print(abs_val(x) == 5)
x = 0 
print(abs_val(x) == 0)

x = input("Enter your age, baw: ")
allowed_in_pub(int(x))
print(x) 


