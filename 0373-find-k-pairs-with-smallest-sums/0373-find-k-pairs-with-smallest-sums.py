class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # sorted non-decreasing order
        # (u, v) consists of one element from the first array and one element from the second array
        # find k pairs (u1, v1),..., (uk, vk) with the smallest sums.

        # (nums1[0],nums2[0]) is always the smallest pair
        # smallest pairs always contain either nums1[0] or nums2[0]; if all pairs containing these are still less than k, then add pairs containing nums1[1] or nums2[1]; so on
        # use a maxheap size k
        minheap=[]
        for i in range(min(k,len(nums1))): # add all pairs containing nums2[0]
            heappush(minheap,(nums1[i]+nums2[0], nums1[i],nums2[0],0)) # last item is index in nums2
        result=[]
        while k>0 and minheap:
            sumi,n1,n2,j=heappop(minheap)
            result.append([n1,n2])
            k-=1

            if j < len(nums2)-1:
                next_val=nums2[j+1]
                heappush(minheap,(n1+next_val,n1,next_val,j+1))
        return result

        