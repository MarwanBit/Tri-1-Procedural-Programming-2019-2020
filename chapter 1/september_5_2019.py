

def month_name(n):
	month_list = [
	'january','febuary','march','april','may','june','july',
	'august','september','october','november','december'
	] 
	try:
		n = int(n)
	except:
		print("Wrong Input")
		quit()
	if n < 1 or n > 12:
		raise ValueError
	n -= 1
	if (n>=0) and (n<=11):
		n = month_list[n]		
	return n

#Test values
for i in range(1,13):
	j = month_name(i)
	print(j)

