class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # U:
        # - return a list of list [i,j,k], solution set must not contain duplicate triplets
        # - nums[i] + nums[j] + nums[k] == 0
        # - len(nums) >= 3 (valid)
        # - nums[i] can be negative 
        # - is nums sorted? No
        # - ex: [-1,0,1,2,-1,-4] -> [[-1,-1,2],[-1,0,1]]
        #       [0,1,1] -> []
        #       [0,0,0] -> [[0,0,0]]

        # M:
        # - METHOD 1: brute force -> O(n^3), O(n) space
        #       + traverse the array, for each item, found 2 other items that add up to negative of the current item's value
        #       + do this by:   init result_list
        #                       for i in range(len(nums)): => O(n^2)
        #                           init j = i+1, remain = 0-nums[i]-nums[j]
        #                           search nums for an item equal to remain, then add to result_list [nums[i], nums[j], remain]
        #                           increase j and do it again
        #                       return result_list
        # 
        # result = set() # use set to prevent duplication
        # for i in range(len(nums)-2):
        #     for j in range(i+1, len(nums)-1):
        #         remain_num = 0 - nums[i] - nums[j]
        #         for k in range(j+1, len(nums)):
        #             if nums[k] == remain_num:
        #                 result.add(tuple(sorted((nums[i], nums[j], nums[k])))) # tuple is hashable
        #                         # if dont sort the tuple, (-1, 0, 1) and (0, 1, -1) are considered different; O(1) since only 3 items
        # return [list(item) for item in result] # this solution is correct but too inefficient and cause time limit exceeded


        # METHOD 2: sort, hashmap -> O(n^2)
        # nums.sort()
        # if nums[0] > 0:
        #     return []
        # hashMap = {}
        # for i, num in enumerate(nums):
        #     hashMap[num] = i # init hashmap with indexes
        # answer = []
        # i = 0
        # while i < len(nums) - 2:
        #     if nums[i] > 0:
        #         break
        #     j = i + 1
        #     while j < len(nums) - 1:
        #         required = 0 - (nums[i] + nums[j])
        #         if required in hashMap and hashMap[required] > j:
        #             answer.append([nums[i], nums[j], required])
        #         j = hashMap[nums[j]] +1 
        #     i = hashMap[nums[i]] + 1
        # return answer




        # METHOD 3: sort array, use 2 pointers (left,right) -> O(n^2) time, O(1) space
        #           + sort -> O(nlogn) time, O(n) space
        #           + init result_list
        #           + init pointer i fixed at index 0, j next to i, k at the rightmost 
        #             [-4,-1,-1,0,1,2]
        #               i  j        k
        #           + if nums[j] + nums[k] + nums[i] == 0, add to result_list, increment j, decrement k
        #             if < 0, increment j
        #             if > 0, decrement k, do this until j>=k
        #           + increment i, j next to i, k at right most
        
        res = set() # use set to prevent duplication
        nums.sort()
        if nums[0] > 0:
            return []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    res.add((nums[i], nums[j], nums[k])) # tuple is hashable so can be added to set
                    j += 1
                    k -= 1
        return [list(item) for item in res] # return a list of list
