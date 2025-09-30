"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashMap = {}
        curr = head
        while curr:
            new_node = Node(curr.val)
            hashMap[curr] = new_node
            curr = curr.next
        curr = head
        while curr:
            if curr.next:
                hashMap[curr].next = hashMap[curr.next]
            else:
                hashMap[curr].next = None
            if curr.random:
                hashMap[curr].random = hashMap[curr.random]
            else:
                hashMap[curr].random = None
            curr = curr.next
        
        if head:
            output = hashMap[head]
        else:
            output = None
        return output
        
        