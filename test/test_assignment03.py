import unittest
from collections import deque

import assignment03
from assignment03 import LinkedList
from assignment03 import DoublyLinkedList
from assignment03 import Queue
from assignment03 import Dictionary

class Test_TestAssignment03(unittest.TestCase):


    def testInsertionSortIterative(self):
         
        a = []
        assignment03.Solution.insertionSortIterative(a)
        print(a)
        self.assertEqual(a,[])

        a = [0,1,2,3,4,5,6,7,8,9]
        assignment03.Solution.insertionSortIterative(a)
        print(a)
        self.assertEqual(a,[0,1,2,3,4,5,6,7,8,9])

        a = [9,8,7,6,5,4,3,2,1,0]
        assignment03.Solution.insertionSortIterative(a)
        print(a)
        self.assertEqual(a,[0,1,2,3,4,5,6,7,8,9])

        a = [8,4,2,5,7,9,3,1,6,0]
        assignment03.Solution.insertionSortIterative(a)
        print(a)
        self.assertEqual(a,[0,1,2,3,4,5,6,7,8,9])


    def testInsertionSortRecursive(self):
         
        a = []
        assignment03.Solution.insertionSortRecursive(a,len(a)-1)
        print(a)
        self.assertEqual(a,[])

        a = [0,1,2,3,4,5,6,7,8,9]
        assignment03.Solution.insertionSortRecursive(a,len(a)-1)
        print(a)
        self.assertEqual(a,[0,1,2,3,4,5,6,7,8,9])

        a = [9,8,7,6,5,4,3,2,1,0]
        assignment03.Solution.insertionSortRecursive(a,len(a)-1)
        print(a)
        self.assertEqual(a,[0,1,2,3,4,5,6,7,8,9])

        a = [8,4,2,5,7,9,3,1,6,0]
        assignment03.Solution.insertionSortRecursive(a,len(a)-1)
        print(a)
        self.assertEqual(a,[0,1,2,3,4,5,6,7,8,9])
         

    def testfindMissingNumbers(self):
         
        a = []
        m = assignment03.Solution.findMissingNumbers(a)
        print(m)
        self.assertEqual(m,[])

        a = [0,1,2,3,5,5,6,7,8,9]
        m = assignment03.Solution.findMissingNumbers(a)
        print(m)
        self.assertEqual(m,[4])

        a = [9,8,7,6,5,5,3,2,1,0]
        m = assignment03.Solution.findMissingNumbers(a)
        print(m)
        self.assertEqual(m,[4])

        a = [1,3,5,7,9,1,3,5,7,]
        m = assignment03.Solution.findMissingNumbers(a)
        print(m)
        self.assertEqual(m,[0,2,4,6,8])

        a = [0,3,6,7,3,3,0,4]
        m = assignment03.Solution.findMissingNumbers(a)
        print(m)
        self.assertEqual(m,[1,2,5])


    def testFindLongestConsecutiveSubsequence(self):
         
        a = []
        s = assignment03.Solution.findLongestConsecutiveSubsequence(a)
        print(s)
        self.assertEqual(s,[])

        a = [1,2,3,5,6,7]
        s = assignment03.Solution.findLongestConsecutiveSubsequence(a)
        print(s)
        self.assertEqual(s,[1,2,3])

        a = [7,6,5,3,2,1]
        s = assignment03.Solution.findLongestConsecutiveSubsequence(a)
        print(s)
        self.assertEqual(s,[5,6,7])
                 
        a = [0,-1,2,1,3,4]
        s = assignment03.Solution.findLongestConsecutiveSubsequence(a)
        print(s)
        self.assertEqual(s,[-1,0,1,2,3,4])

        a = [0,1,2,3,5,0]
        s = assignment03.Solution.findLongestConsecutiveSubsequence(a)
        print(s)
        self.assertEqual(s,[0,1,2,3])

        a = [3,4,2,3,6]
        s = assignment03.Solution.findLongestConsecutiveSubsequence(a)
        print(s)
        self.assertEqual(s,[2,3,4])

        a = [20,21,1,2,7,5,40]
        s = assignment03.Solution.findLongestConsecutiveSubsequence(a)
        print(s)
        self.assertEqual(s,[20,21])

        a = [10,1,8,5,15]
        s = assignment03.Solution.findLongestConsecutiveSubsequence(a)
        print(s)
        self.assertEqual(s,[10])

        a = [32,34,2,33,6,30,36,35]
        s = assignment03.Solution.findLongestConsecutiveSubsequence(a)
        print(s)
        self.assertEqual(s,[32, 33, 34, 35, 36])

        a = [5, 5, 5, 5]
        s = assignment03.Solution.findLongestConsecutiveSubsequence(a)
        print(s)
        self.assertEqual(s,[5])


    def testFindLongestSubarraySumTarget_SlidingWindow(self):
        
        a = [3,1,-1,2,-1,5,-2,3]
        max = assignment03.Solution.findLongestSubarraySumTarget_SlidingWindow(a,3)
        print(max)
        self.assertEqual(max,5)

        #[3, 1, -1, 2, -1, 5, -2, 3] and a target value of 3, the longest subarray length is 5 ([-1, 2, -1, 5, -2])

        a = [0,1,2,3,4,5,6,7,8,9]
        max = assignment03.Solution.findLongestSubarraySumTarget_SlidingWindow(a,45)
        print(max)
        self.assertEqual(max,10)


    def testFindLongestSubarraySumTarget_PrefixSum(self):
        
        a = [3,1,-1,2,-1,5,-2,3]
        max = assignment03.Solution.findLongestSubarraySumTarget_PrefixSum(a,3)
        print(max)
        self.assertEqual(max,5)

        #[3, 1, -1, 2, -1, 5, -2, 3] and a target value of 3, the longest subarray length is 5 ([-1, 2, -1, 5, -2])

        a = [0,1,2,3,4,5,6,7,8,9]
        max = assignment03.Solution.findLongestSubarraySumTarget_PrefixSum(a,45)
        print(max)
        self.assertEqual(max,10)

