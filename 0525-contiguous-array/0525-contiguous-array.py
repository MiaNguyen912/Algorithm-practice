class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
         #
        # mp = defaultdict(lambda: len(nums))
        # a=b=0
        # pre = 0
        # for i in range(len(nums)):
        #     pre += nums[i]
        #     diff = 2*pre - (i+1)
        #     if diff == 0:
        #         a,b = 0,i
        #     elif diff in mp and (i - (mp[diff] + 1)) > b-a: # find max
        #         a = mp[diff] + 1
        #         b = i
        #     mp[diff] = min(mp[diff], i)
        #     # print(nums[a:b+1]) # slicing is [a,b) so need to +1 to b
        # return b-a+1 if a!=b else 0

        # M2:
        mp = dict() # mp[i]
        mp[0] = -1 # for empty array [], numbers of 0 and 1 are equal
        pre = 0
        result = 0 # len of result array
        for i in range(len(nums)):
            pre += 1 if nums[i]==1 else -1 # pre is diff of 1 and 0
            if pre in mp:
                result = max(result, i - mp[pre]) # find the longest subarr
            else:
                mp[pre] = i # pre[i] store (num of 1s - num of 0s) upto index i
        return result