class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # nums[i] == nums[j] and abs(i - j) <= k 
        # i, j are duplicate and are close to each other
        # k can be 0, len(nums) can be 1

        # M1: sliding window, for each window size k, check if there's a duplicate -> O(n^2) time, O(1) space

        # M2: use dict to store (value:index) pairs -> O(n) time + space
        mp = defaultdict()
        for i, num in enumerate(nums):
            if num in mp and i - mp[num] <= k:
                return True
            mp[num] = i
        return False

