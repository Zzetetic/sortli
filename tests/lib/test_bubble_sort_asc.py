import unittest
from sort.lib import bubble_sort_asc
from .helper import ListSortAscCase

class Test_case_1(ListSortAscCase, unittest.TestCase):
	def function_for_test(self, ListInst):
		bubble_sort_asc(ListInst)


if __name__ == '__main__':
    unittest.main()
