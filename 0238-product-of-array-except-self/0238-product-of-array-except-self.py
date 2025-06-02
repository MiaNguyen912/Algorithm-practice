class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # for each i, answer[i] is (product of items before i) * (product of items after i) 
        # => make prefix_product and postfix_product arrays
        # prefix_product[i] is product of everything before i
        # postfix_product[i] is product of everything after i
        # => answer[i] = prefix_product[i] * postfix_product[i]
        # ex: nums=[1,2,3,4] -> prefix_product=[1, 1, 2, 6]; postfix_product=[24, 12, 4, 1]

        prefix_product = [1] * len(nums)
        for i in range(1,len(nums)):
            prefix_product[i] = prefix_product[i-1] * nums[i-1]
        postfix_product = [1] * len(nums)
        answer = prefix_product
        for i in range(len(nums)-2,-1,-1):
            postfix_product[i] = postfix_product[i+1] * nums[i+1]
            answer[i] *= postfix_product[i]
        return answer