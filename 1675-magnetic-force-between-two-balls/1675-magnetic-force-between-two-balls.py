class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # ith basket is at position[i]
        # distribute m balls into n baskets s.t min force between any 2 balls in maximum
        # force between 2 balls at positions x and y is |x - y|
        # return the force

        # => arrange m balls into n baskets s.t distance between 2 closest pairs is maximun
        # => to maximize the force, we'll try to put the first ball at the leftmost basket
        #   and last ball at rightmost basket
        #   Sort position, then do binary search for force from 1 to (position[-1]-position[0])/k
        #   to find the max force that we can arrange k balls in n baskets

        position.sort()
        def check(force): # check if we can arrange k-2 balls in n-2 baskets given |x-y|=force
            count = 1
            prev_pos = position[0]
            for pos in position[1:]:
                if pos - prev_pos >= force:
                    count += 1
                    prev_pos = pos
            return count >= m

        l,r = 1, (position[-1]-position[0])//(m-1) +1
        while l<=r:
            mid = (l+r)//2 # current force
            if check(mid):
                l = mid+1
            else:
                r = mid-1
        return r


