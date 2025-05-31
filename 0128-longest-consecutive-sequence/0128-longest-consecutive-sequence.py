class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # convert nums to set to remove duplicate
        # for each number, while num+1 is in set, increase num and check if num+1 in in set, also remove that num from set to avoid looping through it again

        nums_set = set(nums)
        max_len = 0
        curr_len = 0
        for num in nums:
            if num in nums_set:
                curr_len = 0
                d = num
                while num in nums_set:
                    curr_len += 1
                    nums_set.remove(num)
                    num += 1
                num = d-1
                while num in nums_set:
                    curr_len += 1
                    nums_set.remove(num)
                    num -= 1
                max_len = max(max_len, curr_len)
        return max_len
                