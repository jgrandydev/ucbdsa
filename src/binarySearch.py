import random

class Solution:

    def generateRandom(bits=None):

        if not bits:
            bits = random.randrange(1,128)

        return random.getrandbits(bits)
    
    def binarySearchUnbounded():

        rand = Solution.generateRandom()
        lower = 0
        upper = 1
        guesses = 0
        while True:
            while lower <= upper:
                guesses += 1
                mid = (lower + upper) // 2  # with py no danger of overflow
                if mid == rand : return guesses
                if mid < rand:
                    lower = mid + 1
                else:
                    upper = mid - 1
            lower = upper + 1
            upper *= 2
    
    def binarySearchBounded(bits: int):

        # expand search range by doubling
        # 0 	1
        # 2 	2
        # 3 	4
        # 5 	8
        # 9 	16
        # 17 	32
        # 33 	64
        # 65 	128
        # 129	256
        # etc

        rand = Solution.generateRandom(bits)
        lower = 0
        upper = 2**bits - 1
        guesses = 0
        while lower <= upper:
            guesses += 1
            mid = (lower + upper) // 2  # with py no danger of overflow
            if mid == rand : return guesses
            if mid < rand:
                lower = mid + 1
            else:
                upper = mid - 1
        
        return -1