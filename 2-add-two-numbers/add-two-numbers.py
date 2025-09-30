# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        ptr1 = l1
        ptr2 = l2
        carry = 0
        while ptr1 and ptr2:
            val = ptr1.val + ptr2.val + carry
            carry = 0
            if val >= 10:
                carry = 1
                val -= 10
            curr.next = ListNode(val)
            curr = curr.next
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        if ptr1:
            while ptr1:
                val = ptr1.val + carry
                carry = 0
                if val >= 10:
                    carry = 1
                    val -= 10
                curr.next = ListNode(val)
                curr = curr.next
                ptr1 = ptr1.next
        elif ptr2:
            while ptr2:
                val = ptr2.val + carry
                carry = 0
                if val >= 10:
                    carry = 1
                    val -= 10
                curr.next = ListNode(val)
                curr = curr.next
                ptr2 = ptr2.next
        if carry == 1:
            curr.next = ListNode(1)
            curr = curr.next
        
        return dummy.next


        