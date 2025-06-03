# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # U:
        # - BST, not empty; node.val are unique
        # - low, high are valid
        # - find sum of values in [low, high]

        # M1: dfs, preorder recursive 
        if not root: #empty
            return 0
        total = 0
        if root.val in range(low,high+1):
            total += root.val
        if root.left:
            total += self.rangeSumBST(root.left, low, high)
        if root.right:
            total += self.rangeSumBST(root.right, low, high)
        return total

        # M2:

        

        # M: dfs, preorder recursive 
        # - base case: if not root: return 0
        # - recursive case:
        #       init sum = 0
        #       if root.val is in [low, high]: sum += root.val
        #       call self.rangeSumBST() on root.left, root.right
        # - return sum

        # if not root: 
        #     return 0
        # sum = 0
        # def sum_helper(root):
        #     nonlocal sum
        #     if not root: 
        #         return 0
        #     if root.val in range(low, high+1):
        #         sum += root.val
        #     sum_helper(root.left)
        #     sum_helper(root.right)
        # sum_helper(root)
        # return sum

        #---------------------------
        # Method 2: advanced preorder
        # - if a node.val in [low, high], add it to sum and continue traversing it's left, right
        #   elif node.val > high: only traverse it's left
        #   elif node.val < low: only traverse it's right

        def sum_helper(root):
            if not root: 
                return 0
            sum = 0
            if root.val in range(low, high+1):
                sum += root.val + sum_helper(root.left) + sum_helper(root.right)
            elif root.val > high:
                sum += sum_helper(root.left)
            else:
                sum += sum_helper(root.right)
            return sum
        return sum_helper(root)