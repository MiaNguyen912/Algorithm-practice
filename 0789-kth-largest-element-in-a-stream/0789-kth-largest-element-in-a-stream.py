class KthLargest:
    # M1: max heap
    
    def __init__(self, k: int, nums: List[int]):
        # maintains a stream of test scores 
        # use an min heap of size k to keep k highest score
        self.k = k
        self.score_heap = []
        for n in nums[:k]: # push the first k scores
            heappush(self.score_heap, n)
        for n in nums[k:]: # for remaining score, only push if it's higher than the min score in heap
            if n > self.score_heap[0]:
                heappop(self.score_heap)
                heappush(self.score_heap, n)
            

    def add(self, val: int) -> int:
        # returns the kth highest test score after a new score is added
        if len(self.score_heap) < self.k:
            heappush(self.score_heap, val)
        elif val > self.score_heap[0]:
            heappop(self.score_heap)
            heappush(self.score_heap, val)
        return self.score_heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)