class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # ith pile has piles[i] bananas. 
        # guards come back in h hours.
        # Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them and will not eat any more bananas during this hour.
        # Return the minimum k such that she can eat all the bananas within h hours.

        # plan: find a speed from 1 -> max(piles)
        # 

        def check_time_condition(mid):
            num_piles = 0
            for p in piles:
                num_piles += ceil(p/mid)
                if num_piles > h:
                    return False
            return True

        l, r = 1, max(piles)
        while l<=r: #O(n * log(max(piles))), worst test case O(log(10**9) * 10^4)
            # find time eating all piles
            mid = (l+r)//2 # mid
            if check_time_condition(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l
            
