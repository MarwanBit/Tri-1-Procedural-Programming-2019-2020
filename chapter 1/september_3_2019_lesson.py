print(dir())

def square(x):
	return x*x

def noah(x):
	return x*square(x)

def print_list_of_squares_or_cubes(squares_or_cubes,upper_lim,given_function):
	for i in range(1,int(upper_lim)):
		rand_string = " {0} is the {2} of {1} ".format(str(given_function(i)),str(i),str(squares_or_cubes),str(squares_or_cubes))
		rand_string = rand_string.center(160, "*")
		print(rand_string) 



print(dir())

print_list_of_squares_or_cubes("cubes",20,noah)


#Global Symbol Table --> python's infrastructure where all the variables are hiden
#Within each scope there is a Local Symbol Table 
#Think of each of the scopes as Stacks on the Activation Table
#Think of the terminal window as a file that you write to