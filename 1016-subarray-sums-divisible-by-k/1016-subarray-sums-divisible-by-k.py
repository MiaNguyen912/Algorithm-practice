class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # find num of subarr with sum divisible by k
        # => prefix sum
        # for each r, find how many l such that sum of subarr divisible by k
        # (pre[r] - pre[l-1]) % k == 0
        # => pre[l-1]%k = pre[r]%k
        # => use a map to store pre[r]%k
        count = 0
        n = len(nums)
        pre = [0] * (n+1)
        pre[1] = nums[0]
        for i in range(2,n+1):
            pre[i] = pre[i-1] + nums[i-1]
        # print(pre)
        mp = defaultdict(int)

        for r in range(n+1):
            target = pre[r]%k
            count += mp[target]
            mp[target] += 1
        return count


        