class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # return k most frequent elems, in any order
        # nums not empty, k>1 and is valid
        # It is guaranteed that the answer is unique.
        # Follow up: time complexity better than O(n log n)

        # M: dict of frequency, max heap of dict
        mp = defaultdict(int)
        for num in nums:
            mp[num] += 1
        maxh = []
        for num,freq in mp.items():
            heappush(maxh, (-freq,-num))
        output = []
        for _ in range(k):
            freq,num = heappop(maxh)
            output.append(-num)
        return output