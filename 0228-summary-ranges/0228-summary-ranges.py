class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        #U:
        # - nums: sorted, unique integer array
        # - return: smallest sorted list of ranges that cover all the numbers in the array exactly
        # - Each range [a,b] in the list should be output as: "a->b" or "a" 
        # - 0 <= nums.length <= 20; -231 <= nums[i] <= 231 - 1
        # ex:  nums = [0,1,2,4,5,7] ->  Output: ["0->2","4->5","7"]
        # ex: nums = [0,2,3,4,6,8,9] -> ["0","2->4","6","8->9"]

        # M: 2 pointers (start/end)
        if not nums:
            return []
        start, end = 0,0
        output = []
        while end < len(nums)-1:
            if nums[end+1] == nums[end] + 1:
                end += 1
            else:
                if start == end:
                    output.append(str(nums[start]))
                else:
                    output.append(f"{nums[start]}->{nums[end]}")
                end += 1
                start = end 
        # at this point, we haven't added the last range
        if start == end:
            output.append(str(nums[start]))
        else:
            output.append(f"{nums[start]}->{nums[end]}")
        
        return output
