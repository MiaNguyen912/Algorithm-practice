class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        # capacity: max amount steal from a house among houses
        # steal at least k houses
        # find min capacity
        # refuses to steal from adjacent homes

        # for each r, find l s.t min(nums[l->r]) is the min_capacity, and r-l+1 >= k + (k-1)
        # => find min item among all the max items for subarrs with len >= k + (k-1)

        # # use sortedlist to keep track of the min item in range l->r
        # min_cap = math.inf
        # l = 0
        # sorted_l = SortedList([])
        # for r in range(len(nums)):
        #     sorted_l.add(nums[r])
        #     if r-l+1 >= k + (k-1): 
        #         max_item = sorted_l[-1]
        #         min_cap = min(min_cap, max_item)
        # return min_cap


        # binary search: find the min capacity that satisfy condition
        # condition: r-l+1 >= k + (k-1)
        # use binary search to find a min capacity s.t that capacity is in nums and

        def check(capacity):
            # note: capacity is the max money in all houses we steal 
            # => use greedy approach: steal from the leftmost house and every other houses after if they have <= capacity money
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= capacity:
                    count += 1
                    if count >= k:
                        return True
                    i+=2
                else:
                    i+=1
            return False

            

        l,r = 0, max(nums)
        while l <= r:
            mid = (l+r)//2
            if check(mid):
                r = mid-1
            else:
                l = mid+1
        return l