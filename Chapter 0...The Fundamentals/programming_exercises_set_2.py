#Exercise (1) if you try 5 = x Python will say can't assign
#to literal 

a = 1
b = 2 
c = 3 
a,b,c = b,c,a 
print(a)
print(b)
print(c)

#Exercise (3) if you try a,b,c = c it will say TypeError: cannot
#unpack non-iterable int object 

#Pooling and the use of the "is" operator
x = 5 
y = 5
print(x is y)
name = "String"
Ella = "String"
print(name is Ella) 
#The following line evaluates if (6*4 == 5*50) "is" false
print(False is (6*4 == 5*50)) 


#.center, .find, .capitalize, .rfind() len()

print(name.rfind("g"))
sid = "sid_is_dumb"
print(min(sid))
print(max(sid))
print(sid.count("_"))