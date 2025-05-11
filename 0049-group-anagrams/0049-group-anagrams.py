class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # ["eat","tea","tan","ate","nat","bat"] -> [["bat"],["nat","tan"],["ate","eat","tea"]]

        # method: sort strings, return ana
        original_strs = strs.copy()
        mp = defaultdict(list) # map of sorted str and list of indexes in original array
        for i,s in enumerate(strs):
            sorted_s = sorted(s) # ['a', 'e', 't']
            sorted_s = "".join(sorted_s) 
            print(sorted_s)
            mp[sorted_s].append(i)
        # print(mp)
        output = []
        for indices_list in mp.values():
            curr_list = []
            for i in indices_list:
                curr_list.append(original_strs[i])
            output.append(curr_list)
        return output

        # print(original_strs)
        # print(strs)
        # for i,s in enumerate(strs)