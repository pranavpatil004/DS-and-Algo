class Node:
    def __init__(self, value, next) -> None:
        self.value = value
        self.next = next
    
class Queue:
    
    def __init__(self) -> None:
        self.front = None
        self.rear = None
        self.size = 0
    
    def enqueue(self, val):
        node = Node(val, None)
        if self.front is None:
            self.front = node
        if self.rear:
            self.rear.next = node
        self.rear = node
        self.size += 1
        
    def dequeue(self):
        if self.front is not None:
            node = self.front
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            self.size -= 1
            return node.value
        else:
            print('Queue is Empty')
    
    def getFront(self):
        if self.front:
            return self.front.value
        else:
            print('Queue is empty')
    
    def getRear(self):
        if self.rear:
            return self.rear.value
        else:
            print('Queue is empty')
    
    def printQueue(self):
        front = self.front
        while front is not None:
            print(front.value, end=' -> ')
            front = front.next
        if self.front is None:
            print('Queue is empty')

callQueue = Queue()
callQueue.enqueue(1)
callQueue.enqueue(2)
callQueue.enqueue(3)
callQueue.enqueue(4)
callQueue.enqueue(5)
callQueue.printQueue()
print('Front: ', callQueue.getFront())
print('Rear: ', callQueue.getRear())
callQueue.dequeue()
callQueue.dequeue()
callQueue.dequeue()
callQueue.dequeue()
callQueue.dequeue()
callQueue.printQueue()
print('Front: ', callQueue.getFront())
print('Rear: ', callQueue.getRear())
callQueue.enqueue(6)
callQueue.enqueue(7)
callQueue.enqueue(8)
callQueue.enqueue(9)
callQueue.enqueue(10)
callQueue.printQueue()
print('Front: ', callQueue.getFront())



    

