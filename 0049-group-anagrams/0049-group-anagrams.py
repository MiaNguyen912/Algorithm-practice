class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # ["eat","tea","tan","ate","nat","bat"] -> [["bat"],["nat","tan"],["ate","eat","tea"]]

        # method: dict
        # words = defaultdict(list)
        # for word in strs:
        #     words["".join(sorted(list(word)))].append(word) 
        # return list(words.values())



        # ### Amazon 
        freqs = [Counter(el) for el in strs]
        groups = []
        existing_counters = []
        res = defaultdict(list)
        
        for str in strs:
            A = [0] * 26
            for c in str:
               A[ord(c) - ord('a')] += 1
            res[tuple(A)].append(str)
        return list(res.values())