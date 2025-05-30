class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        #U:
        # - nums: sorted, unique integer array
        # - return: smallest sorted list of ranges that cover all the numbers in the array exactly
        # - Each range [a,b] in the list should be output as: "a->b" or "a" 
        # - 0 <= nums.length <= 20; -231 <= nums[i] <= 231 - 1
        # ex:  nums = [0,1,2,4,5,7] ->  Output: ["0->2","4->5","7"]
        # ex: nums = [0,2,3,4,6,8,9] -> ["0","2->4","6","8->9"]

        # M: 2 pointers (low/fast)
        # P:
        # - if len(nums) == 1: return that single item
        # - init l,f = 0,1 (which are indices)
        # - init output = []
        # - while f < len(nums): 
        #       while val(new_f) = val(old_f) + 1 -> continue to increment f
        #       if not, add "<l> -> <old_f>" or "l" to output list, update l to new_f, f to new_f.next
        #           (if old_f-l != val(old_f) - val(l)  -> add "l", else add "<l> -> <old_f>" or "l")

        #I:
        # output = []
        # if not nums:
        #     return output
        # if len(nums) == 1:
        #     output.append(str(nums[0]))
        #     return output
        # l,f = 0,1 
        # while f < len(nums): 
        #     # print(l, f)
        #     f_increased = False
        #     while f < len(nums) and nums[f] == nums[f-1] + 1:
        #         f += 1
        #         f_increased = True
        #     if not f_increased:
        #         output.append(str(nums[l]))
        #     else: 
        #         output.append(f"{nums[l]}->{nums[f-1]}")
        #     # print(output)
        #     l = f
        #     f = f+1
        #     # print("--", l,f)

        # # add the last item
        # if (l == len(nums)-1):
        #     output.append(str(nums[len(nums)-1]))
        # return output


        # l:    0     3   5
        # f:    1 2 3 4 5. 6
        # output: [0->2] [4->5]

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
