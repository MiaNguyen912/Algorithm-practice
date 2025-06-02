class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # max subsequence length k is the k largest items
        # => find k largest items while maintaining their relative order
        # M1: store all (value, index) in max_heap -> pop k times to get k largest items
        # -> sort them by index => O(nlogn)
        # max_h = []
        # for i,num in enumerate(nums):
        #     heappush(max_h, (-num,i)) # sorted by desc num, asc i
        # top_k = []
        # for i in range(k):
        #     top_k.append(heappop(max_h))
        # top_k.sort(key=lambda pair:pair[1])
        # return [-val for val,i in top_k]
        num=[-i for i in nums]
        l=[]
        a=[]
        heapq.heapify(num)
        for i in range(k):
            l.insert(0,-heapq.heappop(num))
        for i in nums:
            if i in l:
                l.remove(i)
                a.append(i)
        return a

        # M2: build a list of (val,index), sorted by val, then get the top k items 
        # -> sort again by index => O(nlogn)
        # pairs = [(value, idx) for idx, value in enumerate(nums)]
        # pairs.sort(key=lambda pair: (pair[0], pair[1])) # [(1, 1), (2, 0), (3, 2), (3, 3)]
        # top_k = pairs[-k:]
        # top_k.sort(key=lambda pair : pair[1])
        # return [val for val,index in top_k]
