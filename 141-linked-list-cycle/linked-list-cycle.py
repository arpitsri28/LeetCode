# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashNode = {}
        curr = head
        while curr:
            if curr not in hashNode:
                hashNode[curr] = curr.next
            else:
                return True
            curr = curr.next

        return False 