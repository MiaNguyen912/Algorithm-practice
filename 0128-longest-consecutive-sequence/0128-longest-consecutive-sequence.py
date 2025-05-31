class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # convert nums to set to remove duplicate
        # for each number, while num+1 is in set, increase num and check if num+1 in in set, also remove that num from set to avoid looping through it again

        # O(n), since we only pass each number once
        nums_set = set(nums)
        max_len = 0
        for num in nums:
            if num in nums_set: # check if num hasn't been removed from set
                curr_len = 0 # reset
                temp = num 
                while num in nums_set: # check all numbers consecutive to num (on the right side, including num)
                    curr_len += 1
                    nums_set.remove(num) # remove from set so we wont need to consider this number again later
                    num += 1 # increment num
                num = temp-1 # reset 
                while num in nums_set: # check all numbers consecutive to num (on the left side)
                    curr_len += 1
                    nums_set.remove(num)
                    num -= 1
                max_len = max(max_len, curr_len)
        return max_len
                


        #-----------------------
        # key: a number from the input array, 
        # value: length of a consecutive sequence with that number as either the upper or lower bound of the sequence.
        nums = set(nums)
        table = {}
        maxval = 0
        for num in nums:
            x = table.get(num - 1, 0) # get len of consecutive sequence that end at num-1
            y = table.get(num + 1, 0) # get len of consecutive sequence that begins at num+1
            val = x + y + 1 # combine the 2 sequences above and include num
            table[num - x] = val # store the len of sequence at the beginning of sequence
            table[num + y] = val # store the len of sequence at the end of sequence
            maxval = max(maxval, val) 
        return maxval