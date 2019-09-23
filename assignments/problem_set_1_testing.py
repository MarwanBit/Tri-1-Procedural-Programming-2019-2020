import problem_set_1 
import unittest 
import datetime


class TestingMeanie(unittest.TestCase):

	#This class is used to test the function meanie() in problem_set_1.py
	#This Function is Done!!
	def test_meanie_with_data_set_1(self):
		print('\n' + "Testing the Meanie() Function".center(80))
		self.meanie = problem_set_1.meanie
		self.meanie_test_prompt = "for the data set: {}, the expected value is {}, the resulting value is {}"
		self.data_set_1 = [1,2,4,8,-15]
		test_data = self.meanie(self.data_set_1)
		self.assertEqual(test_data,0)
	def test_meanie_with_data_set_2(self):
		self.meanie = problem_set_1.meanie
		self.meanie_test_prompt = "for the data set: {}, the expected value is {}, the resulting value is {}"
		self.data_set_2 = [1,2,3,4,5,6]
		test_data = self.meanie(self.data_set_2)
		self.assertEqual(test_data,3.5)
	def test_meanie_with_data_set_3(self):
		self.meanie = problem_set_1.meanie
		self.meanie_test_prompt = "for the data set: {}, the expected value is {}, the resulting value is {}"
		self.data_set_3 = [0]
		test_data = self.meanie(self.data_set_3)
		self.assertEqual(test_data,0)
	def test_meanie_with_data_set_4(self):
		self.meanie = problem_set_1.meanie
		self.meanie_test_prompt = "for the data set: {}, the expected value is {}, the resulting value is {}"
		self.data_set_4 = [-1,-1,-1,-1,-1,-1]
		test_data = self.meanie(self.data_set_4)
		self.assertEqual(test_data,-1)
	def test_meanie_with_data_set_5(self):
		self.meanie = problem_set_1.meanie
		self.meanie_test_prompt = "for the data set: {}, the expected value is {}, the resulting value is {}"
		self.data_set_5 = [0,0,0,0,0]
		test_data = self.meanie(self.data_set_5)
		self.assertEqual(test_data,0)



class TestingDatePlus(unittest.TestCase):
	def test_data_ddmmyy(self):
		self.datePlus = problem_set_1.datePlus
		self.date_plus_test_prompt = "for the input {}, the expected value is {}, the resulting values is {}"
		self.data_set = {
			"08/04/2003":2015,"09/04/2002":2015,
			"08-04-2003":2015,"09-04-2002":2015,
			"08042003":2015, "080403":2015, 
			"08/04/03":2015,"08-04-03":2015
			}
		print('\n' + "Testing the DatePlus() Function".center(80))
		for i in self.data_set.items():
			i = list(i)
			print(i)
			self.assertEqual(self.datePlus(i[0]),i[1])
			print(self.date_plus_test_prompt.format(i[0],i[1],self.datePlus(i[0])))

class TestingDayInYear(unittest.TestCase):

	def test_day_in_year(self):
		self.prompt_string = "for the input {}, the expected value is {}, the resulting values is {}"
		self.test_data_set = {
			(2019,9,20) : 263,
			(2019,9,21) : 264,
			(2019,3,11) : 70,
			(2019,4,9) : 99
		}
		print("Testing the DayInYear() Function".center(80))
		for i in self.test_data_set.items():
			i = list(i)
			self.assertEqual(problem_set_1.dayInYear(i[0][0],i[0][1],i[0][2]),i[1])
			print(self.prompt_string.format(i[0],i[1],problem_set_1.dayInYear(i[0][0],i[0][1],i[0][2])))


class TestingDaysLeftInYear(unittest.TestCase):
	def test_days_left_in_year(self):
		self.prompt_string = "for the input {}, the expected value is {}, the resulting values is {}"
		self.test_data_set = {
			(2019,1,1) : 364,
			(2019,12,30) : 1,
			(2019,1,2) : 363,
			(2019,1,28) : 337,
		}
		print("Testing the DaysLeftInYear() Function".center(80))
		for i in self.test_data_set.items():
			i = list(i)
			self.assertEqual(problem_set_1.daysLeftInYear(i[0][0],i[0][1],i[0][2]),i[1])
			print(self.prompt_string.format(i[0],i[1],problem_set_1.daysLeftInYear(i[0][0],i[0][1],i[0][2])))


class TestingDaysToGraduation(unittest.TestCase):
	def test_days_to_graduation(self):
		self.prompt_string = "for the input {}, the expected value is {}, the resulting values is {}"
		self.test_data_set = {
			(2021,5,25) : 0,
			(2021,5,24) : 1,
			(2020,5,25) : 365,
			(2020,5,24) : 366,
		}
		print("Testing the DaysToGraduation() Function".center(80))
		for i in self.test_data_set.items():
			i = list(i)
			self.assertEqual(problem_set_1.daysToGraduation(i[0][1],i[0][2],i[0][0]),datetime.timedelta(i[1]))
			print(self.prompt_string.format(i[0],i[1],problem_set_1.daysToGraduation(i[0][1],i[0][2],i[0][0])))

class TestingDHMS(unittest.TestCase):
	def testing_dhms(self):
		self.prompt_string = "for the input {}, the expected value is {}, the resulting values is {}"
		self.test_data_set = {
			6000000 : "69:10:40:00",
			60 : "00:00:01:00",
			600 : "00:00:10:00",
			645 : "00:00:10:45",
			3601 : "00:01:00:01",
			3661 : "00:01:01:01",
			43534 : "00:12:05:05",
			3600 : "00:01:00:00",
			86400 : "01:00:00:00",
		}
		print("Testing the dhms() Function".center(80))
		for i in self.test_data_set.items():
			i = list(i)
			self.assertEqual(problem_set_1.dhms(i[0]),i[1])
			print(self.prompt_string.format(i[0],i[1],problem_set_1.dhms(i[0])))

class TestingWaterCloset(unittest.TestCase):
	def test_water_closet(self):
		self.prompt_string = "for the input {}, the expected value is {}, the resulting values is {}"
		self.test_data_set = {
			'''This is the String I am testing 
			This is the third line.''' : (48, 12, 2),
		}
		print("Testing the WaterCloset() Function".center(80))
		for i in self.test_data_set.items():
			i = list(i)
			self.assertEqual(problem_set_1.waterCloset(i[0]),i[1])
			print(self.prompt_string.format(i[0],i[1],problem_set_1.waterCloset(i[0])))

class TestingMathCase(unittest.TestCase):
	def test_math_case(self):
		self.prompt_string = "for the input {}, the expected value is {}, the resulting values is {}"
		self.data_set = {
			5:1, -6:-1, 2:0, 1:0
		}
		for i in self.data_set.items():
			i = list(i)
			self.assertEqual(problem_set_1.mathCase(i[0]),i[1])
			print(self.prompt_string.format(i[0],i[1],problem_set_1.mathCase(i[0])))


unittest.main()