class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # good subarr:length >= 2, sum of the elements of the subarray is a multiple of k.
        # 0 is always a multiple of k
        # nums[i] >= 0
        # pre = [nums[0]]*len(nums)
        # mp = defaultdict(int)      
        # for i in range(1,len(nums)):
        #     pre[i] = (pre[i-1] + nums[i]) #can so %k here to make pre[] a list of remainder 
        # for i in range(len(nums)):
        #     remainder = pre[i] % k
        #     if remainder == 0 and i > 0: 
        #         return True
        #     elif remainder in mp and i > 0:
        #         if i - mp[remainder] >= 2:
        #             return True
        #     else:
        #         mp[remainder] = i
        # return False

        # better M:
        # pre = nums[0]
        # mp = defaultdict(int)   
        # mp[pre%k] = 0   
        # for i in range(1,len(nums)):
        #     pre += nums[i]
        #     remainder = pre % k
        #     if remainder == 0: 
        #         return True
        #     elif remainder in mp:
        #         if i - mp[remainder] >= 2:
        #             return True
        #     else:
        #         mp[remainder] = i
        # return False












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