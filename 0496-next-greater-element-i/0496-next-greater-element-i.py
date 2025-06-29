class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # nums1 is a subset of nums2.
        # For each 0 <= i < nums1.length, find j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2 or -1.
        # Return array ans of length nums1.length such that ans[i] is the next greater element as described above.
        # next greater element of x is the first greater element to the right of x 

        # plan 1: for each item in nums2, find the next greater item of it, then return the corresponding answer for each item in nums1 (O(n^2))

        # plan 2: monotonic stack (O(n))
        # create the decreasing monostack to record the subarr that each item in num2 is the max of

        mp = {n:i for i,n in enumerate(nums1)}
        N = len(nums2)
        ans = [0] * (len(nums1))
        nums2 = nums2 + [math.inf]
        monostack = [] # decreasing monostack
        
        for i in range(len(nums2)):
            while monostack and nums2[monostack[-1]] < nums2[i]: # while the last item in monostack < curr item
                last_index = monostack.pop()
                r = i-1
                if nums2[last_index] in mp:
                    ans[mp[nums2[last_index]]] = nums2[r+1] if r < N-1 else -1
            monostack.append(i)
        # ex: nums2 = [1,3,4,2] => max_arr = [[0, 0], [0, 1], [0, 3], [3, 3]]

        return ans

