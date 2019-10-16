import unittest 
import problem_set_2 


#Challenge: Write a single-line regex to determine if a string is a parsable
#Roman numeral


class TestingGeneralFunctions(unittest.TestCase):

	def dictionary_data_set_test(self,test_data_set,func):
		for key,value in test_data_set.items():
			print(self.format_string.format(key,value,problem_set_2.biggestWord(key)))
			self.assertEqual(value, func(key))

	def test_general_functions_in_a_list(self):
		self.format_string = "Input value:{}, expected value:{}, return value:{}."
		#put the list of functions you want to test here
		self.list_of_functions = [problem_set_2.biggestWord]
		self.data_set_dictionary_keys_list = [i.__name__ for i in self.list_of_functions]
		self.dictionary_of_functions_names_to_functions = dict(zip(
			self.data_set_dictionary_keys_list,
			self.list_of_functions
			))
		#Put data sets to test in a parallel structure with the function you will be testing
		self.data_set_dictionary_values_list = [
		{
            "Logic tellacommunications J rr Kuugee Tere":
            "tellacommunications",
            "Techincal Tactical Tallibular Tachimachiumalaterakuijhatmanpuyyteerf":
            "Tachimachiumalaterakuijhatmanpuyyteerf",        
        }
		]
		self.data_set_dictionary_to_functions = zip(
			self.data_set_dictionary_keys_list,
			self.data_set_dictionary_values_list
			)
		self.list_of_functions_dict = {i.__name__:i for i in self.list_of_functions}
		self.data_set_dictionary_to_functions = dict(list(self.data_set_dictionary_to_functions))
		for i in range(len(self.list_of_functions)): 
			for global_key,global_value in self.data_set_dictionary_to_functions.items():
				self.dictionary_data_set_test(
					global_value,
					self.dictionary_of_functions_names_to_functions[global_key]
					)

unittest.main()

