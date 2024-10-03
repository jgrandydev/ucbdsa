import unittest
import assignment01

class Test_TestAssignment01(unittest.TestCase):

    def test_rotateChar1(self):
        rotated = assignment01.Solution.rotateChar('a',1)
        print('rotated ' + str(rotated))
        self.assertEqual(rotated, 'b')

    def test_rotateChar32(self):
        rotated = assignment01.Solution.rotateChar('A',32)
        print('rotated ' + str(rotated))
        self.assertEqual(rotated, 'a')

    def test_rotateString1(self):
        rotated = assignment01.Solution.rotateString('aardvark',1)
        print('rotated ' + rotated)
        self.assertEqual(rotated, 'bbsewbsl')

    def test_rotateString32(self):
        rotated = assignment01.Solution.rotateString('AARDVARK',32)
        print('rotated ' + rotated)
        self.assertEqual(rotated, 'aardvark')

    def test_euclidean(self):
        gcd = assignment01.Solution.euclidean(76,114)
        print('gcd ' + str(gcd))
        self.assertEqual(gcd,38)

    def test_heapSort(self):
        a = [747, 17, 777, 1, 666, 42] 
        assignment01.Solution.heapSort(a)
        print('a ' + str(a))
        self.assertEqual(a,[1,17,42,666,747,777])

    def test_bubbleSort(self):
        a = [747, 17, 777, 1, 666, 42] 
        assignment01.Solution.bubbleSort(a)
        print('a ' + str(a))
        self.assertEqual(a,[1,17,42,666,747,777])

    def test_shuffle(self):
        for _ in range(1000):
            a = assignment01.Solution.shuffle(20)
            print(a)
            for i in range(len(a)):
                self.assertNotEqual(a[i],i)

    def test_countOccurrences(self):

        a = [3,3,3,4,5,6]
        count = assignment01.Solution.countOccurrences(a,3)
        self.assertEqual(count,3)

        a = [0,1,2,3,3,3]
        count = assignment01.Solution.countOccurrences(a,3)
        self.assertEqual(count,3)

        a = [0,1,2,3,3,3,4,5,6]
        count = assignment01.Solution.countOccurrences(a,3)
        self.assertEqual(count,3)

        a = [0,0,1,1,2,2,3,4,4,5,5,6,6]
        count = assignment01.Solution.countOccurrences(a,3)
        self.assertEqual(count,1)

        a = [0,1,2,4,5,6]
        count = assignment01.Solution.countOccurrences(a,3)
        self.assertEqual(count,0)


    def testLargestValueRotatedSortedArray(self):

        a = [2,5]
        val = assignment01.Solution.largestValueRotatedSortedArray(a)
        self.assertEqual(val,5)

        a = [5,2]
        val = assignment01.Solution.largestValueRotatedSortedArray(a)
        self.assertEqual(val,5)

        a = [3,4,5,0,1,2]
        val = assignment01.Solution.largestValueRotatedSortedArray(a)
        self.assertEqual(val,5)

        a = [5,0,1,2,3,4]
        val = assignment01.Solution.largestValueRotatedSortedArray(a)
        self.assertEqual(val,5)

        a = [0,1,2,3,4,5]
        val = assignment01.Solution.largestValueRotatedSortedArray(a)
        self.assertEqual(val,5)


if __name__ == '__main__':
    unittest.main()



# import unittest
# class Test_TestWhatever(unittest.TestCase):

#     def test_whatever(self):
#         self.assertEqual(4, 4)

# if __name__ == '__main__':
#     unittest.main()

