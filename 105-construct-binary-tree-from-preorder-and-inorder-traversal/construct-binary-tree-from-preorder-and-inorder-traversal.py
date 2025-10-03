# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        root_p = preorder[0]
        for i in range(len(inorder)):
            if inorder[i] == root_p:
                root_i = i
                break
        root = TreeNode(root_p)
        root.left = self.buildTree(preorder[1:1 + root_i], inorder[0:root_i])
        root.right = self.buildTree(preorder[1 + root_i :], inorder[root_i + 1:len(inorder)])
        return root




        