class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # return array of all start indices of p's anagrams in s (in any order)
        # -> use a sliding window len = len(p), check if the substr in window is an anagram of p
        r = len(p)
        p = sorted(p)
        output = []
        while r < len(s)+1:
            if sorted(s[r-len(p):r]) == p:
                output.append(r-len(p))
            r += 1
        return output


