# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root: #empty
            return 0
        elif not root.left and not root.right: # leaf
            return root.val if low<=root.val<=high else 0
        total = self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
        if root.val in range(low,high+1):
            total += root.val
        return total