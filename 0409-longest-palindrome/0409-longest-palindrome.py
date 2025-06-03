class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        max_len = 0
        contain_odd = False
        for c,freq in counter.items():
            max_len += (freq // 2) * 2
            if freq%2 == 1:
                contain_odd = True
        return max_len + contain_odd
        