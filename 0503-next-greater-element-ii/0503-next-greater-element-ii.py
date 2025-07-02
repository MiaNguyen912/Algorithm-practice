class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # find the next > item for every item or -1
        # nums: circular array

        # monostack (similar to 496.Next Greater Element I (if nums is not circular))
        # double nums to represent cirlular array
        # for each item, find a range s.t it's the max value in => the next greater item is at one edge of the range
        ans = [-1] * len(nums)
        # nums.append(-inf)
        mono_st = []
    

        for i in range(len(nums)*2):

            circular_i = i % len(nums) 
            # While current number > number at the index on top of the stack
            while mono_st and nums[circular_i] > nums[mono_st[-1]]:
                min_index = mono_st.pop()
                ans[min_index] = nums[circular_i]
            if i < len(nums): #  Only push index in the first pass (to avoid overwriting)
                mono_st.append(circular_i)
        


        return ans




                
        