class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
    def get(self, index: int) -> int:
        i = 0
        curr = self.head
        while curr and i <= index:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        i = 0
        if index == 0:
            self.addAtHead(val)
            return
        curr = self.head
        while curr:
            if i+1 == index:
                new_node = Node(val)
                new_node.next = curr.next
                curr.next = new_node
                return
            curr = curr.next
            i += 1
            
    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            if self.head:
                self.head = self.head.next
            return
        curr = self.head
        i = 0
        while curr and curr.next:
            if i+1 == index:
                if curr.next.next == None:
                    curr.next = None
                else:
                    curr.next = curr.next.next
                return
            curr = curr.next
            i += 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)