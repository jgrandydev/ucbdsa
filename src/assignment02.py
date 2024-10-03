import heapq
import random
import re

from collections import deque
from unicodedata import numeric


class Stack:

    s = []
    count = 0

    def __init__(self,capacity):
        self.s = [None]*capacity
        self.count = 0

    def resizeUp(self):
        capacityCurrent = len(self.s)
        if self.count == capacityCurrent:
            capacityNew = capacityCurrent * 2
            s1 = [None]*capacityNew
            for i in range(self.count):
                s1[i] = self.s[i]
            self.s = s1

    def resizeDown(self):
        capacityCurrent = len(self.s)
        if self.count < capacityCurrent // 4:
            capacityNew = capacityCurrent // 2
            s1 = [None]*capacityNew
            for i in range(self.count):
                s1[i] = self.s[i]
            self.s = s1

    def count(self):
        return self.count

    def push(self,e):
        if self.count == len(self.s):
            self.resizeUp()
        self.s[self.count] = e
        self.count += 1

    def pop(self):
        if self.count == 0: raise Exception("Pop failed - stack is empty")
        val = self.s[self.count-1]
        self.count -= 1
        if self.count < len(self.s) // 4:
            self.resizeDown()
        return val

    def read(self):
        if self.count == 0: raise Exception("Read failed - stack is empty")
        return self.q[self.count-1]


class Queue:

    q = []
    count = 0

    def __init__(self,capacity):
        self.q = [None]*capacity
        self.count = 0

    def resizeUp(self):
        capacityCurrent = len(self.q)
        if self.count == capacityCurrent:
            capacityNew = capacityCurrent * 2
            q1 = [None]*capacityNew
            for i in range(self.count):
                q1[i] = self.q[i]
            self.q = q1

    def resizeDown(self):
        capacityCurrent = len(self.q)
        if self.count < capacityCurrent // 4:
            capacityNew = capacityCurrent // 2
            q1 = [None]*capacityNew
            for i in range(self.count):
                q1[i] = self.q[i]
            self.q = q1

    def count(self):
        return self.count
            
    def enqueue(self,e):
        if self.count == len(self.q):
            self.resizeUp()
        self.q[self.count] = e
        self.count += 1

    def dequeue(self):
        if self.count == 0: raise Exception("Queue is empty")
        val = self.q[0]
        for i in range(1,self.count):
            self.q[i-1] = self.q[i] 
        self.count -= 1
        if self.count < len(self.q) // 4:
            self.resizeDown()
        return val

    def read(self):
        if self.count == 0: raise Exception("Queue is empty")
        return self.q[0]


class Solution:

    # Question 1 iterative
    def rotateDequeIterative(q:  deque, n):

        if n == 0: return
        if n > 0:
            for _ in range(n):
                q.appendleft(q.pop())
        else:
            for _ in range(abs(n)):
                q.append(q.popleft())


    # Question 1 recursive
    def rotateDequeRecursive(q: deque, n):

        if n == 0: return
        if n > 0:
            q.appendleft(q.pop())
            Solution.rotateDequeRecursive(q,n-1)
        else:
            q.append(q.popleft())
            Solution.rotateDequeRecursive(q,n+1)


    # Question 2 using deque iterative
    def reverseDequeIterative(q):
    
        n = len(q)

        if n <= 1: return

        for i in range(n // 2):
            print("i=" + str(i))
            q[i],q[n-1-i] = q[n-1-i],q[i]

        # this solution is not very deque-esque !

            
    # Question 2 using deque recursive
    def reverseDequeRecursive(q):

        if len(q) <= 1: return

        left = q.popleft()
        right = q.pop()
        
        Solution.reverseDequeRecursive(q)

        q.appendleft(right)
        q.append(left)


    # Question 2 using Queue iterative
    def reverseQueueIterative(q: Queue):
        
        if q.count <= 1: return

        s = Stack(q.count)

        while q.count > 0:
            s.push(q.dequeue())

        while s.count > 0:
            q.enqueue(s.pop())

        # this solution is not very Queue-esque !


    # Question 2 using Queue recursive
    def reverseQueueRecursive(q):
        
        if q.count <= 1: return

        e = q.dequeue()
        
        Solution.reverseQueueRecursive(q)

        q.enqueue(e)


    # Question 2 using Stack iterative and temp array
    def reverseStackIterativeWithArray(s):
        
        if s.count <= 1: return

        n = s.count
        a = []
        for _ in range(n):
            a.append(s.pop())
        
        for i in range(n):
            s.push(a[i])

        # this solution is not very Stack-esque !


    # Question 2 using Stack iterative and extra temp stacks
    # O(3N) = O(N)
    def reverseStackIterativeWithStacks(s):
        
        if s.count <= 1: return

        temp1 = Stack(s.count)
        temp2 = Stack(s.count)

        while s.count > 0:
            temp1.push(s.pop())

        while temp1.count > 0:
            temp2.push(temp1.pop())

        while temp2.count > 0:
            s.push(temp2.pop())


    # Question 2 using Stack recursive
    def reverseStackRecursive(s):

        if s.count <= 1: return

        # how to do this ? 


    def towerOfHanoi(n,a,b,c):

        if n == 1:
            b.push(a.pop())
            return

        Solution.towerOfHanoi(n-1,a,c,b)
        b.push(a.pop())
        Solution.towerOfHanoi(n-1,c,b,a)


    # Question 3 recursive
    def binarySearchRecursive(a, target, left=None, right=None):
        
        #[1,3,5,7,9,11,13,15,17,19]

        if left is None or right is None:
            left = 0
            right = len(a) - 1

        mid = (left + right) // 2
        val = a[mid]

        if val == target: return mid

        if target < val:
            right = mid - 1
        else:
            left = mid + 1

        if left > right: return -1

        return Solution.binarySearchRecursive(a,target,left,right)


    # Question 4
    def balancedBraces(equation):

        total = ['{','(','[','}',')',']']
        open = ['{','(','[']
        close = ['}',')',']']

        s = []

        for c in equation:
            if c in total: 
                if c in open:
                    s.append(c)
                elif c in close: 
                    if ( s[-1] == open[0] and c == close[0]) or ( s[-1] == open[1] and c == close[1]) or ( s[-1] == open[2] and c == close[2]):
                        s.pop()
                    else:
                        return False
                    
        if len(s) > 0: return False
                    
        return True


    # Question 4
    def balancedBracesStack(equation):

        braces = {'{':'}','(':')','[':']'}

        s = Stack()

        for c in equation:
            if c not in braces.keys() and c not in braces.values():
                continue
            elif c in braces:
                s.append(c)
            else:
                if c != braces[s.pop()]:
                    return False
                    
        if len(s) > 0: return False
                    
        return True
    

    # Question 5
    def evaluatePostfix(equation):

        def evaluatePostfixStackRecursive(s):

            if not s: return None

            s1 = s.pop()

            if len(s1) == 1 and s1 in operators:
                op = s1

                s2 = s[-1]
                if len(s2) == 1 and s2 in operators:
                    n2 = evaluatePostfixStackRecursive(s)
                else: 
                    s.pop()
                    if s2.isnumeric(): 
                        n2 = int(s2)
                    else:
                        n2 = float(s2)

                n1 = evaluatePostfixStackRecursive(s)
                
                if op == '+':
                    return n1 + n2
                elif op == '-':
                    return n1 - n2
                elif op == '*':
                    return n1 * n2
                elif op == '/':
                    return n1 / n2
                
            else:
                if s1.isnumeric(): 
                    n = int(s1)
                else:
                    n = float(s1)
                return n


        operators = ['+', '-', '*', '/']
        s = []

        segments = re.findall(r'\S+',equation)

        for segment in segments:
            s.append(segment)

        return evaluatePostfixStackRecursive(s)

        

    # Question 5
    def evaluatePostfixStack(equation):
        operators = ['+', '-', '*', '/']
        segments = equation.split()
        s = Stack(len(segments))
        for segment in segments:
            if len(segment) == 1 and segment in operators:
                operator = segment
                operand2 = s.pop()
                operand1 = s.pop()
                result = None
                if operator == '+':
                    result = operand1 + operand2
                elif operator == '-':
                    result = operand1 - operand2
                elif operator == '*':
                    result = operand1 * operand2
                elif operator == '/':
                    result = operand1 / operand2
                if s.count == 0: return result
                s.push(result)
            else: 
                operand = float(segment)
                s.push(operand)

