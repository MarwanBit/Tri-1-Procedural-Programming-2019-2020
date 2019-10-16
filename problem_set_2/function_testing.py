import re
import problem_set_2

def foo(x,y,z):
	return x,y,z

print(foo.__name__)
print(dir(foo))

for i in (dir(foo)):
	print(foo.i)

list_1 = [0,1,2,3,4,5]
list_2 = ['ob_1','ob_2','ob_3','ob_4','ob_5','ob_6']
dictionary = zip(list_1,list_2)
dictionary = list(dictionary)
dictionary = dict(dictionary)
print(dictionary)


