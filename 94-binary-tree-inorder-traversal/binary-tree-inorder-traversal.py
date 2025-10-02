# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        output = self.helper(root, [])
        return output
    
    def helper(self, root, lst):
        if not root:
            return
        self.helper(root.left, lst)
        lst.append(root.val)
        self.helper(root.right, lst)
        return lst