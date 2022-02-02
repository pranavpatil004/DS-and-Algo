class Node:
    def __init__(self, value, next) -> None:
        self.value = value
        self.next = next


class Stack:
    head = None
    size = 0
        
    def push(self, value):
        n = Node(value, self.head)
        self.head = n
        self.size += 1
    
    def pop(self):
        if self.head:
            n = self.head
            self.head = n.next
            self.size -= 1
            return n.value
    
    def top(self):
        return self.head.value if self.head else None
    
    def isEmpty(self):
        return not (self.head)
    
    def getSize(self):
        return self.size


s = Stack()
s.push(4)
s.push(5)
s.push(3)
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
s.push(9)
print(s.top())
print(s.isEmpty())
print(s.getSize())




