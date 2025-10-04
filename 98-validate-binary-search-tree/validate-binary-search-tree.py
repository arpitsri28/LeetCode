# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, arr):
        if not root:
            return arr
        
        self.helper(root.left, arr)
        arr.append(root.val)
        self.helper(root.right, arr)
        return arr

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        output = self.helper(root, [])
        prev = output[0]
        i = 0
        while i < len(output) - 1:
            if output[i] >= output[i+1]:
                return False
            i += 1
        
        return True



        