class Solution:
    def minAnagramLength(self, s: str) -> int:
        # s: concatenation of anagrams of some string t.
        # find min possible length of t
        
        # M1: brute force, increase the anagram size from 1->n to check (O(n^2 logn))
        s = list(s)
        n = len(s)
        for size in range(1, n):
            if n % size == 0: # only care if n % size_of_anagram == 0
                anagram = sorted(s[:size])
                for j in range(size, n, size): # step of size
                    temp = sorted(s[j:j+size])
                    if anagram != temp: 
                        break
                else:
                    return size         
        return n


        # M2: same as M1, but using Counter() to get the hashable value of string instead of sort() it (O(n^2))
        # s = list(s)
        # n = len(s)
        # ans = n
        # for size in range(1, n):
        #     if n % size == 0: 
        #         count = Counter(s[:size]) # O(n)
        #         for j in range(size, n, size):
        #             temp = Counter(s[j:j+size])
        #             if count != temp:
        #                 break
        #         else:
        #             return size
        # return ans











         # Get the length of the input string 's'
        n = len(s)

        # Define a helper function to calculate the greatest common divisor (GCD)
        def gcd(a, b):
            # Euclidean algorithm to find GCD
            while b != 0:
                temp = b
                b = a % b
                a = temp
            return a

        # Count the occurrences of each character in 's' using Counter
        hashmap = Counter(s)

        # Initialize the divisor with the count of the first character in 's'
        div = hashmap[s[0]]

        # Iterate over the counts of characters in the hashmap
        for key, value in hashmap.items():
            # Update the divisor by finding the GCD of the current count and the previous divisor
            div = gcd(div, value)
        
        # Return the minimum length of 't', which is the length of 's' divided by the divisor
        return n // div