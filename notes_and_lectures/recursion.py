import sys
#Here you can set a recursion limit
sys.setrecursionlimit(10001)

def factorial(n):
	#Below is the base case. This stops the recursion.
	if n == 0 or n == 1:
		return 1 
	#This is the recursion step.
	return factorial(n-1)*n 

def missTree(ch,n):
	if n == 0:
		return
	print(ch*n)
	missTree(ch, n-1)

def missTreePuzzler(ch,n):
	if n == 0:
		return
	print(ch*1)
	for i in range(1,n):
		print(ch*i)

def missTreePuzzler2(ch,n):
	if n == 0:
		return
	missTree(ch, n-1)
	print(ch*n)	

#Very inefficient use of recursion
def fib_num(n):
	if n == 0 or n == 1:
		return n 
	return fib_num(n - 1) + fib_num(n - 2)

def main():
	if __name__ == "__main__":
		#Recursion limit is (999)
		#for i in range(1004):
		#	print("{} factorial is equal to {}".format(i,factorial(i)))
		missTreePuzzler("*",10)
		print(fib_num(12))
main()