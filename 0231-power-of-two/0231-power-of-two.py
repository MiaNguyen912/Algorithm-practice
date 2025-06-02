class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # power of 2: must be even, > 0

        # M1: -2^31 <= n <= 2^31 - 1  -> x can be from 0->30 -> check if n == 2^x
        # if n <=0:
        #     return False
        # product = 1/2 # init to 1/2 so that in the first loop when x=0, product = 1
        # for x in range(31):
        #     product *= 2
        #     if n == product:
        #         return True
        # return False

        # M2: bit manipulation

        # M3: recursion
        if n == 1:
            return True
        if n<1:
            return False
        
        return self.isPowerOfTwo(n/2)


