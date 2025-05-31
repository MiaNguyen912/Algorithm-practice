class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = dict() # store value:index
        for i,n in enumerate(nums):
            missing = target - n
            if missing in mp:
                return [i,mp[missing]]
            mp[n] = i
        