import unittest
import binarySearch 

class Test_TestBinarySearch(unittest.TestCase):

    def test_binarySearchBounded(self):
        guesses = binarySearch.Solution.binarySearchBounded(128)
        print('guesses ' + str(guesses))
        self.assertNotEqual(guesses, -1)

    def test_binarySearchUnbounded(self):
        guesses = binarySearch.Solution.binarySearchUnbounded()
        print('guesses ' + str(guesses))
        self.assertNotEqual(guesses, -1)

if __name__ == '__main__':
    unittest.main()



# import unittest
# class Test_TestWhatever(unittest.TestCase):

#     def test_whatever(self):
#         self.assertEqual(4, 4)

# if __name__ == '__main__':
#     unittest.main()

