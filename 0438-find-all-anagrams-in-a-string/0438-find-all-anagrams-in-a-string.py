class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # return array of all start indices of p's anagrams in s (in any order)
        # -> use a sliding window len = len(p), check if the substr in window is an anagram of p
        p = sorted(p)
        output = []
        for i in range(len(p),len(s)+1):
            if sorted(s[i-len(p):i])==p:
                output.append(i-len(p))
        return output


