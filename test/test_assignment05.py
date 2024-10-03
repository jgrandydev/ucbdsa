import unittest

from assignment05 import BinaryNode
from assignment05 import BinarySearchTree 
from assignment05 import HeapNode
from assignment05 import MinHeap
from assignment05 import MaxHeap
from assignment05 import Trie
#from assignment05 import CharFrequencyHeap
from assignment05 import CharFrequencyHeapArray
from assignment05 import CharFrequencyHeapq
from assignment05 import LongestCommonPrefixForWords
from assignment05 import ShortestUniquePrefixesForWords

class Test_TestAssignment05(unittest.TestCase):

    def testCompleteTree(self):

        #                 100
        #     50                      150
        # 25      75              125     175          

        root = BinaryNode(100)
        root.left = BinaryNode(50)
        root.right = BinaryNode(150)
        root.left.left = BinaryNode(25)
        root.left.right = BinaryNode(75)
        root.right.left = BinaryNode(125)
        root.right.right = BinaryNode(175)
        bst = BinarySearchTree(root)

        self.assertEqual(bst.LastItem(), 175)

        #                 100
        #     50                      150
        # 25      75              125    


        root = BinaryNode(100)
        root.left = BinaryNode(50)
        root.right = BinaryNode(150)
        root.left.left = BinaryNode(25)
        root.left.right = BinaryNode(75)
        root.right.left = BinaryNode(125)
        bst = BinarySearchTree(root)

        self.assertEqual(bst.LastItem(), 125)


# Question 2
# Write a function that accepts a string and returns an array of the characters in the string sorted by frequency 
# (from most frequent to least frequent).
# You must use a heap to sort the characters. You can use the heap in the dsa package, Python's heapq package or write your own. 
# Example: 
# The input
#  "abracadabra"
# should return:
# ['a', 'b', 'r', 'c', 'd']
# Note: characters that have the same frequency can appear in any order


    # def testCharFrequencyHeap(self):
    #     s = "abracadabra"
    #     # a 5
    #     # b 2
    #     # c 1
    #     # d 1
    #     # r 1
    #     result = CharFrequencyHeap(s)
    #     print(result)
    #    self.assertEqual(result,['a','r','b','d','c'])


    def testCharFrequencyHeapArray(self):
        s = "abracadabra"
        # a 5
        # b 2
        # c 1
        # d 1
        # r 1
        result = CharFrequencyHeapArray(s)
        print(result)                                                            
        self.assertEqual(result,['a','r','b','d','c'])

        s = "open sesame"
        # e 3
        # s 2
        # p 1
        # o 1                                                           
        # a 1
        # m 1
        # e 1
        result = CharFrequencyHeapArray(s)
        print(result)
        self.assertEqual(result,['e','s','p','o','a','m','e'])

        s = "she sells seashells by the seashore"
        # s 8
        # h 4
        # e 7
        # l 4
        # a 2
        # b 1
        # y 1
        # t 1
        # o 1
        # r 1
        # space 5
        result = CharFrequencyHeapArray(s)
        print(result)
        self.assertEqual(result,['s', 'e', ' ', 'l', 'h', 'a', 'y', 't', 'r', 'o', 'b'])


    def testCharFrequencyHeapq(self):
        s = "abracadabra"
        # a 5
        # b 2
        # c 1
        # d 1
        # r 1
        result = CharFrequencyHeapq(s)
        print(result)
        self.assertEqual(result,['a','b','r','c','d'])

        s = "she sells seashells by the seashore"
        # s 8
        # h 4
        # e 7
        # l 4
        # a 2
        # b 1
        # y 1
        # t 1
        # o 1
        # r 1
        # space 5
        result = CharFrequencyHeapq(s)
        print(result)
        self.assertEqual(result,['s', 'e', ' ', 'h', 'l', 'a', 'b', 'o', 'r', 't', 'y'])


# Question 3
# Write a function that accepts an array of words, stores them in a trie and returns the longest common prefix. Write it so that it performs efficiently.
# For example, given the array
# words = ["apple", "appetite", "apparatus", "appliance"]
# The function should return
# "app"

    def testLongestCommonPrefixForWords(self):
        words = ["apple", "appetite", "apparatus", "appliance"]
        self.assertEqual(LongestCommonPrefixForWords(words),'app')



# 4. Write a function that accepts an array of words and then returns the shortest unique prefix of each word. 
# For example:
# words = ['apple', 'banana', 'cherry', 'cranberry', 'grape', 'grapefruit'] 
# # 'apple' returns 'a'
# # 'banana' returns 'b'
# # 'cherry' returns 'ch'
# # 'cranberry' returns 'cr'
# # 'grape' returns 'grape'
# # 'grapefruit' returns 'grapef'
# # returns:
# ['a', 'b', 'ch', 'cr', 'grape', 'grapef']

    def testShortestUniquePrefixesForWords(self):
        words = ['apple', 'banana', 'cherry', 'cranberry', 'grape', 'grapefruit'] 
        prefixes = ShortestUniquePrefixesForWords(words)
        print(prefixes)
        self.assertEqual(prefixes,['a', 'b', 'ch', 'cr', 'grape', 'grapef'])

        words = ['apple', 'applesauce', 'apply', 'applicant', 'applicants', 'application', 'applications', 'applicable', 'applicability'] 
        prefixes = ShortestUniquePrefixesForWords(words)
        print(prefixes)
        self.assertEqual(prefixes,['apple', 'apply', 'appli'])



# 5. Write a search function or method for a Trie data structure. 
# The search word may contain the dot character '.' to represent any single letter.
# 15 points maximum if the function returns True or False for each search query
# (more challenging) 20 points maximum if the function returns an array of words that match the wildcard search
# Examples:i
# Assume that the Trie has the following words:
# apple, apply, application, banana
# trie.search("apple")  # Returns: True
# trie.search("app")    # Returns: False
# trie.search("appl.")  # Returns: True
# trie.search("ap.le")  # Returns: True
# trie.search_all("app.e")  # Returns: ["apple"]
# trie.search_all("ap.l.")  # Returns: ["apple", "apply"]


    def testSearch(self):
        words = ['apple', 'applesauce', 'apply', 'applicant', 'applicants', 'application', 'applications', 'applicable', 'applicability'] 
        trie = Trie(words)
        self.assertEqual(trie.Search('applicable'),['applicable'] )

        words = ['apple', 'apply', 'application', 'banana'] 
        trie = Trie(words)
        self.assertEqual(trie.Search('apple'),['apple'])
        self.assertEqual(trie.Search('app'),[] )
        self.assertEqual(trie.Search('appl.'),['apple','apply'] )
        self.assertEqual(trie.Search('ap.le'),['apple'] )
        self.assertEqual(trie.Search('app.e'),['apple'] )
        self.assertEqual(trie.Search('ap.l.'),['apple','apply'] )