class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # s, t same length
        # change s to t. 
        # Changing the s[i] to t[i] costs |s[i] - t[i]| (the absolute difference of ASCII values)
        # returm max length of substr of s can be changed to corresponding substr of t, cost <= maxCost, or 0
        # ex: s = "abcd", t = "bcdf", maxCost = 3 => Output: 3 ("abc" of s can change to "bcd", which costs 3)
        
        # if we generate an array diff with diff[i] = |s[i] - t[i]| 
        # -> this problem is same as finding longest substr of diff with sum <= maxCost
        # M1: sliding window
        cost = 0
        l = 0
        max_len = 0
        for r in range(len(s)):
            cost += abs(ord(s[r]) - ord(t[r])) # ord() convert char to ascii value
            if cost > maxCost: # cut left (ascii values span from 97->122 => dont need while loop here as we'd never cut more than 1 leftmost char for each right char added)
                cost -= abs(ord(s[l]) - ord(t[l]))
                l += 1
            # at this point, s[l->r] is the longest substr that ends at r with cost <= maxCost
            if cost <= maxCost:
                max_len = max(max_len, r-l+1)
        return max_len