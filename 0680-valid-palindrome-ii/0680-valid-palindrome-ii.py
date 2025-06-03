class Solution:
    def validPalindrome(self, s: str) -> bool:
        # U:
        # - return true if s can be palindrome after deleting at most 1 character
        # - s is not empty; consists of lowercase letters
        # - ex: "aba" -> T; "abca"->T; "abc"-> F
        
        # M: 2 pointers left/right (O(n) time, O(1) space)
        # - implement a helper function exactPalindrome(s) that check if s is exact palindrome(without removing a char)
        #       init left, right = 0, len(s)-1
        #       while left<right:
        #            if s[left] == s[right]: increment left, decrement right
        #            else: return False
        #       return True
        # - init left, right = 0, len(s)-1
        # - while left<right:
        #      if s[left] == s[right]: increment left, decrement right
        #      else:
        #           return exactPalindrome(s[left+1 : right+1]) or exactPalindrome(s[left : right])
        
        def exactPalindrome(s):
            left, right = 0, len(s)-1
            while left<right:
                if s[left] == s[right]: 
                    left, right = left+1, right-1
                else: 
                    return False
            return True
        left, right = 0, len(s)-1
        while left<right:
            if s[left] == s[right]: 
                left, right = left+1, right-1
            else:
                return exactPalindrome(s[left+1 : right+1]) or exactPalindrome(s[left : right])
        return True
        