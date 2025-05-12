class Solution:
    def romanToInt(self, s: str) -> int:
        # I can be placed before V (5) and X (10) to make 4 and 9. 
        # X can be placed before L (50) and C (100) to make 40 and 90. 
        # C can be placed before D (500) and M (1000) to make 400 and 900.
        # they can also be placed after to increase value
        
        # M1: check each char and add value to sum 
        # if char is 'V' or 'X' and prev_char is 'I' -> add -2
        # if char is 'L' or 'C' and prev_char is 'X' -> add -20
        # if char is 'D' or 'M' and prev_char is 'C' -> add -200
        # => O(n) time, O(1) space
        # hashmap = {'I':1, 'V':5, 'X':10, 'L':50,'C':100, 'D':500, 'M':1000}
        # sum = hashmap[s[0]]
        # for i,c in enumerate(s[1:], start=1):
        #     sum += hashmap[c]
        #     if c in "VX" and s[i-1] == "I":
        #         sum -= 2
        #     elif c in "LC" and s[i-1] == "X":
        #         sum -= 20
        #     elif c in "DM" and s[i-1] == "C":
        #         sum -= 200
        #     print(sum, hashmap[c])
        # return sum

        # M2: apply general rule of roman number
        symbol = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000, '&' : 0}
        s += '&'
        result = 0
        for i in range(len(s)-1):
            if symbol[s[i]] >= symbol[s[i+1]] :
                result += symbol[s[i]]
            else:
                result -= symbol[s[i]]
        return result