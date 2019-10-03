#Universe of Discourse, all of what is being mentioned set-wise 
#Sets are collections of things!

#x (element of) a 
j = set()
j.add("a")
j.add("piranah")
j.add(False) 
print(j)

#Testing if somethings in the set J 
print("a" in j)
#Testing if somethings not in the set J 
print("a" not in j)

#To find the union of two sets
k = set()
k.add("a")
k.add("b")
k.add("c")
print(j.union(k)) 
#You can do the same thing with a|b 
print(j|k)

#How to do the intersection of two sets 
print(j.intersection(k))
#The same thing can be done with x&y 
print(j&k) 

#below are the commands for set difference 
print(j.difference(k))
print(j-k)

#xor is or except both cannot be true 
#xor --> x^y

#A delta b is a set's symetric difference, all non-intersecting values
print(j.symmetric_difference(k)) 

#Disjoint sets are sets with no intersecting value 
print(j.isdisjoint(k))

#Subsets and proper subsets
#The lines below describe subsets
print(j.issubset(k)) 
#Or....
print(j <= k) 

#The lines below describe how to find a proper subset
print(j < k) 


print((j for j in range(100)))
#
