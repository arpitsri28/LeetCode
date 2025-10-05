# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        output = []
        if root:
            queue.append(root)
        
        while len(queue) > 0:
            curr_out = []
            for i in range(len(queue)):
                curr = queue.popleft()
                curr_out.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            output.append(curr_out)
        
        return output
            

        