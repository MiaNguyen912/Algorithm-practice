class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # [1,1,2,2] -> no majority, but we won't have to worry about this case as majority is guaranteed to always exist
        # Could you in O(n) time and O(1) space?

        # M1: sort -> majority element will sure to be found at the middle of nums (O(nlogn))

        # M2: use dict to store frequency -> O(n) time + space
        
        # M3: Moore Voting Algorithm (O(n) time, O(1) space)
        # fact: if there's a majority in array, it will always remain in the lead even after encountering other elements
        # consider encountering the majority elem is 1 upvote, encountering other elems is 1 downvote 
        # -> if there's a majority elem, we'll endup with a positive number of votes
        # Here, we dont know which one is majority elem to upvote, but we know that if we assume a random elem as majority,
        #   if it's not the actual majority, it'll be canceled out (downvoted to 0) by other elems or by the real majority elem;
        #   if it's the real majority, it may be canceled out by other elems, but eventually it'd still be alive no elems left to cancel it
        count = 1
        major = nums[0]
        for num in nums[1:]:
            if num == major:
                count += 1
            else:
                count -= 1
            if count == 0:
                major = num
                count = 1         
        return major