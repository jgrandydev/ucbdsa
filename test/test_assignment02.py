import unittest
import assignment02
from collections import deque
from assignment02 import Queue

class Test_TestAssignment02(unittest.TestCase):

    def testRotateDequeIterative(self):

        a = deque([1,2,3,4,5])

        assignment02.Solution.rotateDequeIterative(a,1)
        print(a)
        self.assertEqual(a, deque([5,1,2,3,4]))

        assignment02.Solution.rotateDequeIterative(a,3)
        print(a)
        self.assertEqual(a, deque([2,3,4,5,1]))

        assignment02.Solution.rotateDequeIterative(a,1)
        print(a)
        self.assertEqual(a, deque([1,2,3,4,5]))

        assignment02.Solution.rotateDequeIterative(a,-1)
        print(a)
        self.assertEqual(a, deque([2,3,4,5,1]))

        assignment02.Solution.rotateDequeIterative(a,-3)
        print(a)
        self.assertEqual(a, deque([5,1,2,3,4]))

        assignment02.Solution.rotateDequeIterative(a,-1)
        print(a)
        self.assertEqual(a, deque([1,2,3,4,5]))


    def testRotateDequeRecursive(self):

        a = deque([1,2,3,4,5])

        assignment02.Solution.rotateDequeRecursive(a,1)
        print(a)
        self.assertEqual(a, deque([5,1,2,3,4]))

        assignment02.Solution.rotateDequeRecursive(a,3)
        print(a)
        self.assertEqual(a, deque([2,3,4,5,1]))

        assignment02.Solution.rotateDequeRecursive(a,1)
        print(a)
        self.assertEqual(a, deque([1,2,3,4,5]))

        assignment02.Solution.rotateDequeRecursive(a,-1)
        print(a)
        self.assertEqual(a, deque([2,3,4,5,1]))

        assignment02.Solution.rotateDequeRecursive(a,-3)
        print(a)
        self.assertEqual(a, deque([5,1,2,3,4]))

        assignment02.Solution.rotateDequeRecursive(a,-1)
        print(a)
        self.assertEqual(a, deque([1,2,3,4,5]))


    def testReverseDequeIterative(self):

        a = deque([1,2,3,4,5])
        assignment02.Solution.reverseDequeIterative(a)
        print(a)
        self.assertEqual(a, deque([5,4,3,2,1]))


    def testReverseDequeRecursive(self):

        a = deque([1,2,3,4,5])
        assignment02.Solution.reverseDequeRecursive(a)
        print(a)
        self.assertEqual(a, deque([5,4,3,2,1]))


    def testReverseQueueIterative(self):

        q = assignment02.Queue(5)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        q.enqueue(5)
        self.assertEqual(q.count, 5)
        assignment02.Solution.reverseQueueIterative(q)
        self.assertEqual(q.count, 5)
        self.assertEqual(q.dequeue(), 5)
        self.assertEqual(q.dequeue(), 4)
        self.assertEqual(q.dequeue(), 3)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.count, 0)


    def testReverseQueueRecursive(self):

        q = assignment02.Queue(5)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        q.enqueue(5)
        self.assertEqual(q.count, 5)
        assignment02.Solution.reverseQueueRecursive(q)
        self.assertEqual(q.dequeue(), 5)
        self.assertEqual(q.dequeue(), 4)
        self.assertEqual(q.dequeue(), 3)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.count, 0)


    def testReverseStackIterativeWithArray(self):

        s = assignment02.Stack(5)
        s.push(1)
        s.push(2)
        s.push(3)
        s.push(4)
        s.push(5)
        self.assertEqual(s.count, 5)
        assignment02.Solution.reverseStackIterativeWithArray(s)
        self.assertEqual(s.pop(), 1)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 3)
        self.assertEqual(s.pop(), 4)
        self.assertEqual(s.pop(), 5)
        self.assertEqual(s.count, 0)


    def testReverseStackIterativeWithStacks(self):

        s = assignment02.Stack(5)
        s.push(1)
        s.push(2)
        s.push(3)
        s.push(4)
        s.push(5)
        self.assertEqual(s.count, 5)
        assignment02.Solution.reverseStackIterativeWithStacks(s)
        self.assertEqual(s.count, 5)
        self.assertEqual(s.pop(), 1)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 3)
        self.assertEqual(s.pop(), 4)
        self.assertEqual(s.pop(), 5)
        self.assertEqual(s.count, 0)


    def testBinarySearchRecursive(self):

        a = [1,3,5,7,9,11,13,15,17,19]
        index = assignment02.Solution.binarySearchRecursive(a, 5)
        print('index=' + str(index))
        self.assertEqual(index,2)


    def testBalancedBraces(self):

        # For example, this function should return True for the following: 

        # [ ]
        # {}{}[]()
        # [{()}]
        # (()[[[()({})]]])

        equation = '[ ]'
        result = assignment02.Solution.balancedBraces(equation)
        print('result=' + str(result))
        self.assertEqual(result,True)

        equation = '{}{}[]()'
        result = assignment02.Solution.balancedBraces(equation)
        print('result=' + str(result))
        self.assertEqual(result,True)

        equation = '[{()}]'
        result = assignment02.Solution.balancedBraces(equation)
        print('result=' + str(result))
        self.assertEqual(result,True)

        equation = '(()[[[()({})]]])'
        result = assignment02.Solution.balancedBraces(equation)
        print('result=' + str(result))
        self.assertEqual(result,True)

        # It should return False for the following:

        # [ ] [
        # {{}[](})
        # [{)}]
        # (()[()({})]]])

        equation = '[ ] ['
        result = assignment02.Solution.balancedBraces(equation)
        print('result=' + str(result))
        self.assertEqual(result,False)

        equation = '{{}[](})'
        result = assignment02.Solution.balancedBraces(equation)
        print('result=' + str(result))
        self.assertEqual(result,False)

        equation = '[{)}]'
        result = assignment02.Solution.balancedBraces(equation)
        print('result=' + str(result))
        self.assertEqual(result,False)

        equation = '(()[()({})]]])'
        result = assignment02.Solution.balancedBraces(equation)
        print('result=' + str(result))
        self.assertEqual(result,False)

        equation = '(1+3)*{2-7}+({6-5}+[14/3])'
        result = assignment02.Solution.balancedBraces(equation)
        print('result=' + str(result))
        self.assertEqual(result,True)

        equation = '(1+3)*({2-7)}+({6-5}+[14/3])'
        result = assignment02.Solution.balancedBraces(equation)
        print('result=' + str(result))
        self.assertEqual(result,False)


    def testEvaluatePostfix(self):

# Input: "3 4 +" Output: 7.0
# Input: "10 2 /" Output: 5.0
# Input: "5 1 2 + 4 * + 3 -" Output: 14.0

        equation = '3 4 +'
        result = assignment02.Solution.evaluatePostfix(equation)
        print('result=' + str(result))
        self.assertEqual(result,7)

        equation = '10 2 /'
        result = assignment02.Solution.evaluatePostfix(equation)
        print('result=' + str(result))
        self.assertEqual(result,5)

        equation = '5 1 2 + 4 * + 3 -'
        result = assignment02.Solution.evaluatePostfix(equation)
        print('result=' + str(result))
        self.assertEqual(result,14)

        equation = '68 4 5 6 * + /'
        result = assignment02.Solution.evaluatePostfix(equation)
        print('result=' + str(result))
        self.assertEqual(result,2)

        equation = '10 5 18 3 6 * / + -'
        result = assignment02.Solution.evaluatePostfix(equation)
        print('result=' + str(result))
        self.assertEqual(result,4)


    def testEvaluatePostfixStack(self):

# Input: "3 4 +" Output: 7.0
# Input: "10 2 /" Output: 5.0
# Input: "5 1 2 + 4 * + 3 -" Output: 14.0

        equation = '3 4 +'
        result = assignment02.Solution.evaluatePostfixStack(equation)
        print('result=' + str(result))
        self.assertEqual(result,7)

        equation = '10 2 /'
        result = assignment02.Solution.evaluatePostfixStack(equation)
        print('result=' + str(result))
        self.assertEqual(result,5)

        equation = '5 1 2 + 4 * + 3 -'
        result = assignment02.Solution.evaluatePostfixStack(equation)
        print('result=' + str(result))
        self.assertEqual(result,14)

        equation = '68 4 5 6 * + /'
        result = assignment02.Solution.evaluatePostfixStack(equation)
        print('result=' + str(result))
        self.assertEqual(result,2)

        equation = '10 5 18 3 6 * / + -'
        result = assignment02.Solution.evaluatePostfixStack(equation)
        print('result=' + str(result))
        self.assertEqual(result,4)



    def testTowerOfHanoi(self):

        n = 5

        # setup
        a = assignment02.Stack(n)
        b = assignment02.Stack(n)
        c = assignment02.Stack(n)

        for i in range(n,0,-1):
            a.push(i)

        assignment02.Solution.towerOfHanoi(n,a,b,c)
        print(b)
        self.assertEqual(b.pop(),1)
        self.assertEqual(b.pop(),2)
        self.assertEqual(b.pop(),3)
        self.assertEqual(b.pop(),4)
        self.assertEqual(b.pop(),5)


if __name__ == '__main__':
    unittest.main()



# import unittest
# class Test_TestWhatever(unittest.TestCase):

#     def test_whatever(self):
#         self.assertEqual(4, 4)

# if __name__ == '__main__':
#     unittest.main()

