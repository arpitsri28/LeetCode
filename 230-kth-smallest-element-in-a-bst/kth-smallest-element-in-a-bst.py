# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.n = 0
        self.val = 0
        def helper(root, n):
            if not root:
                return
            
            helper(root.left, self.n)
            self.n += 1
            if k == self.n:
                self.val = root.val
            helper(root.right, self.n)
        
        helper(root, self.n)
        return self.val
        