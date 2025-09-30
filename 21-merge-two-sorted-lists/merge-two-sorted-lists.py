# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        ptr1 = list1
        ptr2 = list2
        while ptr1 and ptr2:
            if ptr1.val <= ptr2.val:
                curr.next = ListNode(ptr1.val)
                curr = curr.next
                ptr1 = ptr1.next
            elif ptr1.val > ptr2.val:
                curr.next = ListNode(ptr2.val)
                curr = curr.next
                ptr2 = ptr2.next
        
        if ptr1:
            curr.next = ptr1
        elif ptr2:
            curr.next = ptr2
        
        return dummy.next