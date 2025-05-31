class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # return array of all start indices of p's anagrams in s (in any order)
        # -> use a sliding window len = len(p), check if the substr in window is an anagram of p
        l,r = 0,0
        for i in range(len(p)): # move r len(p) steps away from l
            r += 1 
        sorted_p = sorted(p)
        output = []
        while r < len(s)+1:
            if sorted(s[l:r]) == sorted_p:
                output.append(l)
            l += 1
            r+= 1
        return output

