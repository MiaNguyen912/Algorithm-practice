class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = [0] * (len(nums)+1) 

        # create a prefix sum array
        for i in range(len(nums)):
            self.prefix_sum[i+1] = self.prefix_sum[i] + nums[i]
        

    def sumRange(self, left: int, right: int) -> int:
        # Returns sum of the elements between left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
        return self.prefix_sum[right+1] - self.prefix_sum[left]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)