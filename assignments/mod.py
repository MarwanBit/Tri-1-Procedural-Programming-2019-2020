#O(n) at worst proportional to n 

class Mod(object):
    #Modular arithmetic is cyclic, you increment and the 
    #Successor of the last element in the set is the first element of 
    #The set.
    #The length of the set is determined by the mod object you're using
    def __init__(self,k,modulus):
        if (k < 0 or modulus < 0):
            raise ValueError 
        self.k = k 
        self.modulus = modulus
    #These double underline methods are called "hooks" and they're are many of them
    def __str__(self):
        '''This method controls the behavior when you call str(Mod(arg1,arg2))'''
        return "{} mod {}".format(self.k, self.modulus)
    def __add__(self,other):
        '''This tells you what to do when: Mod1 + Mod2'''
        #The add method is applied to the first object, using the secondary object 
        #As the argument
        if self.modulus != other.modulus:
            raise ValueError 
        return Mod((self.k + other.k) % self.modulus,self.modulus)
    def __sub__(self,other):
        if self.modulus != other.modulus:
            raise ValueError 
        return Mod(self.k + self.modulus - other.k, self.modulus)
    def __mul__(self,other):
        if self.modulus != other.modulus:
            raise ValueError 
        return Mod((self.k * other.k) % self.modulus,self.modulus)
    def multiplicative_inverse(self):
        chocula = 1 
        cumulative = self.k
        if self.k == 1:
            return Mod(1,self.modulus)
        while (cumulative != 0) and (cumulative % self.modulus != 1): 
            cumulative = (cumulative + self.k) % self.modulus
            chocula += 1 
        if cumulative == 0:
            raise ValueError("No Multiplicative inverse")
        return Mod(chocula, self.modulus)
    def __div__(self,other):
        return self * other.multiplicative_inverse()


#In Modular arithmetic their are two types of numbers: units which have a multiplicative inverse
#And 

m = Mod(3,16)
n = Mod(13,16)
print(m+n)
print(m.__add__(n))
for k in range(16):
    print(Mod(k,16) + Mod(16 - k,16))
a = Mod(3,16)
b = Mod(11,16)
print(a*b)
print("Test multiplicative inverse".center(80,"*"))
for k in range(1,5):
    print(Mod(k,5).multiplicative_inverse())

k = Mod(12,24)
print(str(k).center(80,"*"))

#Research Euclidian Algorithm for Modular arithmetic (Open Puzzle to write a function for this)