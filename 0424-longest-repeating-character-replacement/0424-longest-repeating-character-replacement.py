class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # s: all uppercase letters
        # can flip at most k chars to other char (uppercase)
        # find longest substr containing same letter after at most k flips
        # => find longest substr with num of other chars besides the majority char <= k
        # -> sliding window, use a dict to store <char:count> 

        mp = defaultdict(int)
        max_len = 0
        l = 0
        for r,c in enumerate(s):
            mp[c] += 1
            while (r-l+1) - max(mp.values()) > k and l<=r: # invalid window, cut left
                mp[s[l]] -= 1
                l += 1
            max_len = max(max_len, r-l+1)
        return max_len
        
