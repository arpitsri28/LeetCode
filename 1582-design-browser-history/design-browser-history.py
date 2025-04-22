class Node:
    def __init__(self, url: str, prev: 'Node' = None, next: 'Node' = None):
        self.url = url
        self. prev = prev
        self.next = next
class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = Node(homepage)

    def visit(self, url: str) -> None:
        new_node = Node(url, self.curr)
        self.curr.next = new_node
        self.curr = new_node

    def back(self, steps: int) -> str:
        i = 0
        while self.curr.prev != None:
            if i == steps:
                return self.curr.url
            i += 1
            self.curr = self.curr.prev
        return self.curr.url

    def forward(self, steps: int) -> str:
        i = 0
        while self.curr.next != None:
            if i == steps:
                return self.curr.url
            i += 1
            self.curr = self.curr.next
        return self.curr.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)