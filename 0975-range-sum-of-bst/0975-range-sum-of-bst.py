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