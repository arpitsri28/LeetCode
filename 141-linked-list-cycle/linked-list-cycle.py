# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        flag = False
        hashMap = defaultdict(ListNode)
        while flag == False:
            if head == None:
                return flag
            if head in hashMap:
                flag = True
            else:
                hashMap[head] = head.next
                head = head.next
        
        return flag

        