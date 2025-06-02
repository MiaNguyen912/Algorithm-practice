class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = [nums[0]] * (len(nums)) 

        # create a prefix sum array
        for i in range(1,len(nums)):
            self.prefix_sum[i] = self.prefix_sum[i-1] + nums[i]
        

    def sumRange(self, left: int, right: int) -> int:
        # Returns sum of the elements between left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
        if left == 0: return self.prefix_sum[right]
        return self.prefix_sum[right] - self.prefix_sum[left-1]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)