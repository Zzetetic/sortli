import unittest
from sort.lib import insertion_sort_desc
from .helper import ListSortDescCase

class Test_case_1(ListSortDescCase, unittest.TestCase):
	def function_for_test(self, ListInst):
		insertion_sort_desc(ListInst)

if __name__ == '__main__':
    unittest.main()
