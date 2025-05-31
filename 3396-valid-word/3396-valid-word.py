class Solution:
    def isValid(self, word: str) -> bool:
        # valid: min 3 chars
        #       0-9, a-z, A-Z
        #       at least 1 vowel, 1 consonant
        if len(word)<3:
            return False
        word = word.lower()
        vowel = ['a', 'e', 'i', 'o', 'u']
        has_vowel = has_consonant = False
        for c in word:
            if not c.isalnum():
                return False
            if c in vowel:
                has_vowel = True
            else:
                if c.isalpha():
                    has_consonant = True
        return has_vowel and has_consonant
        