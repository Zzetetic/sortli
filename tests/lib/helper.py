class ListSortAscCase():
	def function_for_test(self, ListInst):
		pass
	
	def test_1(self):
		UnSortList = [3, 5, 2, 4, 1]
		SortList = [1, 2, 3, 4, 5]
		self.function_for_test(UnSortList)
		self.assertEqual(UnSortList, SortList)

	def test_2(self):
		UnSortList = [0, 1, 4, 2, 3]
		SortList = [0, 1, 2, 3, 4]
		self.function_for_test(UnSortList)
		self.assertEqual(UnSortList, SortList)

	def test_3(self):		
		UnSortList = [1, 0, 2, 3, 4]
		SortList = [0, 1, 2, 3, 4]
		self.function_for_test(UnSortList)
		self.assertEqual(UnSortList, SortList)

	def test_4(self):		
		UnSortList = [0, 1, 2, 3, 4]
		SortList = [0, 1, 2, 3, 4]
		self.function_for_test(UnSortList)
		self.assertEqual(UnSortList, SortList)
		
	def test_5(self):		
		UnSortList = [4 , 3, 2, 1, 0]
		SortList = [0 , 1, 2, 3, 4]
		self.function_for_test(UnSortList)
		self.assertEqual(UnSortList, SortList)

	def test_6(self):		
		UnSortList = [5, 5, 5]
		SortList = [5, 5, 5]
		self.function_for_test(UnSortList)
		self.assertEqual(UnSortList, SortList)

	def test_7(self):
		UnSortList = [0, 0, 0]
		SortList = [0, 0, 0]
		self.function_for_test(UnSortList)
		self.assertEqual(UnSortList, SortList)

	def test_8(self):		
		UnSortList = [5, 5, 7, 6, 6, 34]
		SortList = [5, 5, 6, 6, 7, 34]
		self.function_for_test(UnSortList)
		self.assertEqual(UnSortList, SortList)
		


class ListSortDescCase():
	def function_for_test(self, ListInst):
		pass
	
	def test_1(self):
		UnSortList = [3, 5, 2, 4, 1]
		SortList = [5, 4, 3, 2, 1]
		self.function_for_test(UnSortList)
		self.assertEqual(UnSortList, SortList)

	def test_2(self):
		UnSortList = [0, 1, 4, 2, 3]
		SortList = [4, 3, 2, 1, 0]
		self.function_for_test(UnSortList)
		self.assertEqual(UnSortList, SortList)

	def test_3(self):		
		UnSortList = [1, 0, 2, 3, 4]
		SortList = [4, 3, 2, 1, 0]
		self.function_for_test(UnSortList)
		self.assertEqual(UnSortList, SortList)

	def test_4(self):		
		UnSortList = [0, 1, 2, 3, 4]
		SortList = [4, 3, 2, 1, 0]
		self.function_for_test(UnSortList)
		self.assertEqual(UnSortList, SortList)
		
	def test_5(self):		
		UnSortList = [4, 3, 2, 1, 0]
		SortList = [4, 3, 2, 1, 0]
		self.function_for_test(UnSortList)
		self.assertEqual(UnSortList, SortList)

	def test_6(self):		
		UnSortList = [5, 5, 5]
		SortList = [5, 5, 5]
		self.function_for_test(UnSortList)
		self.assertEqual(UnSortList, SortList)

	def test_7(self):
		UnSortList = [0, 0, 0]
		SortList = [0, 0, 0]
		self.function_for_test(UnSortList)
		self.assertEqual(UnSortList, SortList)

	def test_8(self):		
		UnSortList = [5, 5, 7, 6, 6, 34]
		SortList = [34, 7, 6, 6, 5, 5]
		self.function_for_test(UnSortList)
		self.assertEqual(UnSortList, SortList)
