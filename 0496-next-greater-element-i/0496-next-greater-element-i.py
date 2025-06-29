class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # nums1 is a subset of nums2.
        # For each 0 <= i < nums1.length, find j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2 or -1.
        # Return array ans of length nums1.length such that ans[i] is the next greater element as described above.
        # next greater element of x is the first greater element to the right of x 

        # plan 1: for each item in nums2, find the next greater item of it, then return the corresponding answer for each item in nums1 (O(n^2))

        # plan 2: monotonic stack (O(n))
        # create the decreasing monostack to record the subarr that each item in num2 is the max of

        # mp = {n:i for i,n in enumerate(nums1)}
        # N = len(nums2)
        # ans = [0] * (len(nums1))
        # nums2 = nums2 + [math.inf]
        # monostack = [] # decreasing monostack
        
        # for i in range(len(nums2)):
        #     while monostack and nums2[monostack[-1]] < nums2[i]: # while the last item in monostack < curr item
        #         last_index = monostack.pop()
        #         r = i-1
        #         if nums2[last_index] in mp:
        #             ans[mp[nums2[last_index]]] = nums2[r+1] if r < N-1 else -1
        #     monostack.append(i)
        # # ex: nums2 = [1,3,4,2] => max_arr = [[0, 0], [0, 1], [0, 3], [3, 3]]

        # return ans




        #----------------------
        """
        We use a monotonic decreasing stack to efficiently find the next greater number for each element in nums2.

        We scan from left to right through nums2.
        At each index i, we compare nums2[i] with the top of the stack:
            If nums2[i] > stack[-1], we found the next greater number for stack[-1].
            So we pop the top, and record nums2[i] as its next greater element.
        We continue popping until the stack is empty or nums2[i] <= stack[-1].
        Then we push nums2[i] onto the stack.

        \U0001f4a1 Why does this work?
        The stack only contains elements that haven’t yet found their next greater element.
        We maintain a monotonically decreasing stack, so the moment we see a larger number, we know it’s the next greater for all smaller numbers before it.

        \U0001f525 Why Not an Increasing Stack?
        If we used an increasing stack, the top of the stack would be the largest seen so far.
        When we encounter a new number, we’d be comparing it to larger or equal numbers => this won’t tell us whether it is the next greater for previous element.
        """


        # Step 1: Build a map from number in nums2 -> its next greater element
        next_greater = {}  # key: number, value: next greater number
        stack = []  # monotonic decreasing stack (stores nums)

        for num in nums2:
            # While current num is greater than top of stack -> found next greater for stack[-1]
            while stack and num > stack[-1]:
                prev = stack.pop()
                next_greater[prev] = num  # map prev to current num as next greater
            stack.append(num)  # push current num to wait for its next greater

        # All remaining elements in stack have no next greater
        while stack:
            next_greater[stack.pop()] = -1

        # Step 2: Build result for nums1 using the map
        return [next_greater[num] for num in nums1]