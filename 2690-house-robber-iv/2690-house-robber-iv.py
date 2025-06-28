class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        # capacity: max amount steal from a house among houses
        # steal at least k houses
        # find min capacity
        # refuses to steal from adjacent homes
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