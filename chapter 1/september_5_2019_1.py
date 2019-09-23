import unittest

#import computeGrade(x)
def compute_grade(x):
	try:
		x = int(x)
	except ValueError:


class TestGradeAssignment(unittest.TestCase):

	def test_a_case(self):
		for i in range(95,101):
			grade = computeGrade(i)
			self.assertEqual("A",computeGrade(i))

	def test_b_case(self):
		pass
	def test_c_case(self):
		pass
	def test_d_case(self):
		pass

#regular import 
# import library_name 
#from library_name import * 
#from math import module, module
 