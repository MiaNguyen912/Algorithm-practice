class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # good subarr:length >= 2, sum of the elements of the subarray is a multiple of k.
        # 0 is always a multiple of k
        # nums[i] >= 0
        pre = [nums[0]]*len(nums)
        mp = defaultdict(int)
        # mp[0] = 1
        # if len(nums) < 2:
        #     return False
        
        for i in range(1,len(nums)):
            pre[i] = (pre[i-1] + nums[i]) #can so %k here to make pre[] a list of remainder 
        # print(pre)

        for i in range(len(nums)):
            remainder = pre[i] % k
            if remainder == 0 and i > 0: 
                return True
            elif remainder in mp and i > 0:
                if i - mp[remainder] >= 2:
                    return True
            else:
                mp[remainder] = i
            # print(mp)
        return False
