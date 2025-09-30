# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 0
        curr = head
        while curr:
            i += 1
            curr = curr.next

        k = i - n
        if k == 0:
            return head.next  

        curr = head

        while k > 1:
            curr = curr.next
            k -= 1
        
        if curr.next:
            nxt = curr.next
            curr.next = nxt.next
        else:
            curr.next = None
        
        return head