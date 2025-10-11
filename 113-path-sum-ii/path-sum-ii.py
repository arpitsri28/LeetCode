# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def dfs(root, subset, remaining):
            if not root:
                return
            subset.append(root.val)
            if not root.left and not root.right:
                if root.val == remaining:
                    res.append(subset.copy())

            dfs(root.left, subset, remaining - root.val)
            dfs(root.right, subset, remaining - root.val)
            subset.pop()
        dfs(root, [], targetSum)
        return res

            



            

        