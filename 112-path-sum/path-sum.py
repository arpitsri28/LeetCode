# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, targetSum, total):
        if not root:
            return False
        total += root.val
        if not root.left and not root.right:
            if targetSum == total:
                return True
            else:
                return False
        if self.helper(root.right, targetSum, total):
            return True
        if self.helper(root.left, targetSum, total):
            return True
        total -= root.val
        return False

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.helper(root, targetSum, 0)

        