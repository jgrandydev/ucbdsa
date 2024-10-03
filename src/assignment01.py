import random
import heapq

class Solution:

    def generateRandomRange(low,high):

        return random.randrange(low,high)
    

    # O(1)
    def rotateChar(c, rotation): 
        return chr(ord(c) + rotation)
    

    # O(n)
    def rotateString(s, rotation):
        rotated = ['']*len(s)
        for i in range(len(s)):
            rotated[i] = Solution.rotateChar(s[i], rotation)
        return ''.join(rotated)
    

    # O(log N)
    def euclidean(a,b):

        if b > a:
            b,a = a,b

        while b > 0:
            r = a % b
            a = b
            b = r

        return a


    # O(n log n)
    def heapSort(a):

        minheap = []

        for i in range(len(a)):
            heapq.heappush(minheap, a[i])

        i = 0
        while minheap:
            a[i] = heapq.heappop(minheap)
            i += 1


    # O(n ^ 2)
    def bubbleSort(a):    
        start = 0
        swaps = True
        while swaps:
            swaps = False
            for i in range(len(a)-1):
                if a[i] > a[i+1]:
                    a[i],a[i+1] = a[i+1],a[i]
                    swaps = True


    # O(n + n + n) = O(3n) = O(n)
    def shuffle(n):
        
        a = [0]*n
        for i in range(1,n): a[i] = i                       # O(n)                   

        shuffled = [None]*n

        # successively randomly pick a remaining element from a[] 
        # and transfer it to the next slot in shuffled[]
        j = 0
        while j < n-1:                                      # O(n)
            while True:
                i = Solution.generateRandomRange(0,len(a))
                if a[i] != j: break                         # ensure that all elements move to a new position
            shuffled[j] = a[i]
            j += 1
            # O(1) deletion of a[i]
            if i < len(a)-1: 
                a[i] = a.pop() 
            else:
                a.pop()

        # handle the final remaining element that hasn't been added to shuffled[]
        j = 0 
        while shuffled[j] != None: j += 1                   # O(n)
        shuffled[j] = a[0]
        if shuffled[j] == j:                                     
            # need to handle case where final element was never selected randomly
            # and now has ended up in the final slot 
            # so we swap it with another random slot
            i = Solution.generateRandomRange(0,n-2)
            shuffled[j],shuffled[i] = shuffled[i],shuffled[j]

        return shuffled


    # O(log n)
    def binarySearchWithDuplicates(a,target,side):

        n = len(a)
        lower = 0
        upper = n-1
        while lower <= upper:
            mid = (lower + upper) // 2
            if a[mid] < target:
                lower = mid + 1
            elif a[mid] > target:
                upper = mid - 1
            else:   # a[mid] == target
                if side == 'left' and mid > 0 and a[mid-1] == target:
                    upper = mid - 1
                elif side == 'right' and mid < n-1 and a[mid+1] == target:
                    lower = mid + 1
                else:
                    return mid
        
        return -1

 
    # O(log n)
    def countOccurrences(a,target):

        left = Solution.binarySearchWithDuplicates(a,target,'left')
        right = Solution.binarySearchWithDuplicates(a,target,'right')
        if left < 0 or right < 0: return 0
        return right - left + 1


    # O(log n)
    def largestValueRotatedSortedArray(a):

        n = len(a)
        left = 0
        right = n-1
        while left < right:
            mid = (left + right) // 2
            if a[left] < a[mid]:
                left = mid
            elif a[left] > a[mid]:
                right = mid - 1
            else:
                left += 1
        
        if left > 0 and a[left-1] > a[left]: return a[left-1]
        return a[left]






