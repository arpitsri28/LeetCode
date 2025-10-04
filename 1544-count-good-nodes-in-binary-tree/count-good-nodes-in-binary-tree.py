# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, val):
        if not root:
            return 0
        count = 0
        if root.val >= val:
            count += 1
            val = root.val
        return count + self.helper(root.left, val) + self.helper(root.right, val)
        
    def goodNodes(self, root: TreeNode) -> int:
        maxval = root.val
        return 1 + self.helper(root.left, maxval) + self.helper(root.right, maxval)
    


        