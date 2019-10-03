import random


##Toss the coin
def toss_coin():
	outcomes = ['H','T']
	heads_flip_false = True 
	while heads_flip_false:
		resulting_flip = random.choice(outcomes)
		if resulting_flip == 'H':
			heads_flip_false = False
			return resulting_flip 
		elif resulting_flip == 'T':
			return resulting_flip 
 

##calculate the number of times it takes to get a head
def manageTrial():
	counter = 0 
	heads = "" 
	while heads != 'H':
		counter += 1 
		heads = toss_coin() 
	return counter  


##Build dictionary and tally results into it
def DoExperiment(trials):
	data_dict = {}
	for i in range(trials):
		flip_num = manageTrial()
		if flip_num not in data_dict.keys():
			data_dict[flip_num] = 1 
		elif flip_num in data_dict.keys():
			data_dict[flip_num] = int(data_dict[flip_num]) + 1 
	#Retunrs a dict in the form flip_attempts: frequency 
	return data_dict 



##take dictionary and format as an HTML table 
def format_dictionary(data_dict):
	return_string = '<table>'
	sorted_keys = sorted(list(data_dict.keys())) 
	for k in sorted_keys:
		next_line = ''
		next_line = "<tr><td>{}</td><td>{}</td></tr>".format(k,data_dict[k])
		return_string += next_line 
	return_string += '</table>'
	return return_string 

data_dict = DoExperiment(1000000)
print(format_dictionary(data_dict)) 


