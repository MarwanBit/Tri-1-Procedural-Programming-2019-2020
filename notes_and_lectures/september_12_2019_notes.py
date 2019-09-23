def f(x,y):
    #x and y are positional arguments
    return x*y*y 

print(f(2,5))
print(f(5,2))

#when writing arguments, positional comes first, then *args, then *kwargs
def product(*args):
    product_return = 1 
    for arg in args:
        product_return *= arg 
    return product_return 
#alternate definition of product
def product_alternate(*args):
    product_return = 1
    k = 0 
    while k < len(args):
        product_return *= args[k]
        k += 1
    return product_return
def print_name(required_name_part,*optionalargs):
    #require at least one piece of the name
    print(required_name_part + " ", end='')
    k = 0
    while k < len(optionalargs):
        print(optionalargs[k] + ", ") 
        k += 1 
def kwargs_function(arg_1,**kwargs):
    print("{}: This is arg_1.".format(str(arg_1)))
    for i in kwargs.items():
        print("{}: key, {}: value".format(i[0],i[1]))

        


#Order of argument types : Positional, *args, **kwargs
kwargs_function("Arghya","y"="1","x"="2")
print_name("Jackson","\n")
print_name("Jackson", "Woodwill", "Flaglass")
print(product(1,2,3,5,5,6,3,6,3,6,3,6,3,6,3,6,6,9,20,1,14))
print(product_alternate(1,2,3,5,5,6,3,6,3,6,3,6,3,6,3,6,6,9,20,1,14))