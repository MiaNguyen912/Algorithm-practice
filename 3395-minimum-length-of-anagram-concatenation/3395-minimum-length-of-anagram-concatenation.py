class Solution:
    def minAnagramLength(self, s: str) -> int:
        # s: concatenation of anagrams of some string t.
        # find min possible length of t
        
        # M1: brute force, increase the anagram size from 1->n to check (O(n^2 logn))
        # s = list(s)
        # n = len(s)
        # for size in range(1, n):
        #     if n % size == 0: # only care if n % size_of_anagram == 0
        #         anagram = sorted(s[:size])
        #         for j in range(size, n, size): # step of size
        #             temp = sorted(s[j:j+size])
        #             if anagram != temp: 
        #                 break
        #         else:
        #             return size         
        # return n

        #---------------------------------
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




        # M3: use the characteristic of number to find possible number x in range 1->n s.t n%x==0
        # - x is [1, sqrt(n)] + all numbers i = n/a for a in [1, sqrt(n)]

        sqrt_n = math.sqrt(len(s))
        n = len(s)
        consider = []
        for i in range(1,math.ceil(sqrt_n)+1):
            if n%i == 0:
                consider.append(i)
        temp = []
        for num in consider:
            temp.append(n//num)
        consider += temp[::-1]
        print(consider)
        for anagram_len in consider:
            anagram = s[:anagram_len]
            valid = True
            for j in range(anagram_len, len(s), anagram_len):
                if sorted(s[j:j+anagram_len]) != sorted(anagram):
                    valid = False
                    break
            if valid:
                return anagram_len






        #---------------------------------
        # M3: find Greatest common divisor (GCD) between s and t
        # - gcd(a mod b,b) = gcd(a,b).
       

        # counter = Counter(s)
        
        # counts = [v for k,v in counter.items()]
        
        # def gcd_of_list(numbers):
        #     result = numbers[0]
        #     for num in numbers[1:]:
        #         result = math.gcd(result, num)
        #     return result
    
        # g = gcd_of_list(counts)
        
        # total = 0
        # for c in counts:
        #     total += c//g
        
        # return total

