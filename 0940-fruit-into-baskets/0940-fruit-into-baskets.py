class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # fruits[i] is the type of fruit the ith tree produces.
        # collect as much fruit as possible
        # rules: only have 2 baskets, each hold 1 type of fruit, no limit
        #       can start from any tree, but must pick 1 fruit from each free from that, the picked fruit must fit in 1 basket
        #       If reach a tree with non-fit fruit, stop
        # find max num of fruit

        # => find longest subarr with only 2 types of fruit (2 distinct values)
        # => use sliding window

        num_fruits = defaultdict(int) # hold type and count of fruits
        l = 0
        max_fruits = 0
        for r in range(len(fruits)):
            num_fruits[fruits[r]] += 1 
            while len(num_fruits.keys()) > 2: # invalid window -> cut left
                num_fruits[fruits[l]] -= 1
                if num_fruits[fruits[l]] == 0:
                    del num_fruits[fruits[l]] # remove from dict
                l += 1
            # at this point, num_fruits holds the longest subarr ending at r that only has 2 types of fruit
            max_fruits = max(max_fruits, sum(num_fruits.values()))
        return max_fruits
            



        

