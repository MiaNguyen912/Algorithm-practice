class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # good subarr:length >= 2, sum of the elements of the subarray is a multiple of k.
        # 0 is always a multiple of k
        # nums[i] >= 0

        # pre[r] - pre[l] = n*k => (pre[r]%k - pre[l]%k)%k == 0
        # => pre[l]%k == pre[r]%k, and r-l>=2
        # ex: [5 0 0 0],k=3 -> pre=[5 5 5 5], mp={0:-1, 2:0}, valid range is arr[1:3] (=[0,0])
        pre = 0
        mp = dict() # store <(sum of items up to i)%k : i>
        mp[0] = -1 # <sum of [] : -1>
        for r,curr in enumerate(nums):
            pre += curr
            target = pre%k
            # print(target, r,mp)
            if target in mp:
                if r-mp[target] >= 2: #[5 0 0],k=3->valid range:[0 0] -> r-l>=2
                    return True
            else:
                mp[target] = r # only store the leftmost index of mp[target]
        return False