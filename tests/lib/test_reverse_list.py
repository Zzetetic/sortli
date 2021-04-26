import unittest
from sort.lib import reverse_list


class Test_case_1(unittest.TestCase):

	def test_1(self):
		UnSortList = [3 , 5, 2, 4, 1]
		SortList = [1, 4, 2, 5, 3]
		reverse_list(UnSortList)
		self.assertEqual(UnSortList, SortList)

	def test_2(self):
		UnSortList = [0, 1, 4, 2, 3]
		SortList = [3, 2, 4, 1, 0]
		reverse_list(UnSortList)
		self.assertEqual(UnSortList, SortList)

	def test_3(self):		
		UnSortList = [1 , 0, 2, 3, 4]
		SortList = [4, 3, 2, 0, 1]
		reverse_list(UnSortList)
		self.assertEqual(UnSortList, SortList)

	def test_4(self):		
		UnSortList = [0 , 1, 2, 3, 4]
		SortList = [4, 3, 2, 1, 0]
		reverse_list(UnSortList)
		self.assertEqual(UnSortList, SortList)
		
	def test_5(self):		
		UnSortList = [4 , 3, 2, 1, 0]
		SortList = [0, 1, 2, 3, 4]
		reverse_list(UnSortList)
		self.assertEqual(UnSortList, SortList)

	def test_6(self):		
		UnSortList = [5, 5, 5]
		SortList = [5, 5, 5]
		reverse_list(UnSortList)
		self.assertEqual(UnSortList, SortList)

	def test_7(self):
		UnSortList = [0, 0, 0]
		SortList = [0, 0, 0]
		reverse_list(UnSortList)
		self.assertEqual(UnSortList, SortList)

	def test_8(self):		
		UnSortList = [5, 5, 7, 6, 6, 34]
		SortList = [34, 6, 6, 7, 5, 5]
		reverse_list(UnSortList)
		self.assertEqual(UnSortList, SortList)


if __name__ == '__main__':
    unittest.main()
