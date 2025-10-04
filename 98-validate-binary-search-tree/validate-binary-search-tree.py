# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.prev = None
    def helper(self, root):
        if not root:
            return True
        
        if not self.helper(root.left):
            return False
        
        if self.prev is not None and root.val <= self.prev:
            return False
        self.prev = root.val
        
        return self.helper(root.right)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root)



        