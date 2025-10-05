# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        if root:
            queue.append(root)
        output = []

        while len(queue) > 0:
            curr_lvl = []
            for i in range(len(queue)):
                curr = queue.popleft()
                curr_lvl.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            if len(curr_lvl) > 0:
                output.append(curr_lvl[-1])
        
        return output
        