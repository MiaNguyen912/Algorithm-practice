class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefix sum
        # generate a prefix sum array of nums with pre[i] = sum of items in nums upto index i
        # for each pre[i], we'd want to find how many indices x s.t pre[x] = pre[i] - k and x <= i
        # => we'll use a map to record number of occurence of items in pre upto the current i
        # count = 0
        # pre = [0] * len(nums)
        # for i in range(len(nums)):
        #     if i == 0:
        #         pre[i] = nums[i]
        #     else:
        #         pre[i] = pre[i-1] + nums[i]
        # mp = defaultdict(int)
        # mp[0] = 1
        # for i in range(len(nums)):
        #     remainder = pre[i] - k
        #     count += mp[remainder]
        #     mp[pre[i]] += 1
        # return count

        count = 0
        pre = 0
        mp = defaultdict(int) # stores <sum([:i]): count>
        mp[0] = 1 # <sum([]) : 1>
        for i in range(len(nums)):
            pre += nums[i]
            target = pre - k
            count += mp[target]
            mp[pre] += 1
        return count

