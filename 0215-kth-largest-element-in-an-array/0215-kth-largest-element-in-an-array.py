class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # solve without sorting
        # k >= 1, 1-indexed

        # M1: max heap
        import heapq
        maxh = []
        for num in nums:
            heapq.heappush(maxh, -num)
        # print(maxh) # [-6, -5, -4, -5, ...] -> it's a binary heap (special kind of binary tree) -> cannot do 'return -maxh[k-1]'
        for _ in range(k - 1):
            heapq.heappop(maxh) 
        return -heapq.heappop(maxh)  
