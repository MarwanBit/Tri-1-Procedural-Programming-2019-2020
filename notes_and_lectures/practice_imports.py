import my_module


print(dir())

for i in range(0,100):
	string = " {0} squared is {1}, {0} cubed is {2} ".format(str(i),str(my_module.square(i)),str(my_module.cube(i)))
	string = string.center(160,'*')
	print(string) 

#Look up Python Paths in order to look for Modules in non CWD places