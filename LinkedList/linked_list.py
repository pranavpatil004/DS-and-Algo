class Node:
    def _init_(self,value,node):
        self.value = value
        self.next  = node

class LinkedList:
    def _init_(self):
        self.head = None
        self.size = 0
        
    def insert(self,pos,ele):
        if pos > self.size:
            print("Can not insert because position is out of reach")
            return
        if self.head == None:
            node = Node(ele,None)
            self.head = node 
        else:
            if pos==0:
                node = Node(ele,self.head)
                self.head = node
            else:
                pointer = self.head
                for i in range(pos-1):
                    pointer = pointer.next
                node = Node(ele,pointer.next)
                pointer.next = node
        self.size += 1
                
    def delete_pos(self,pos):
        if self.head == None or pos >= self.size:
            print("Either list is empty or position is out of reach")
            return 
        if pos==0:
            pointer = self.head.next
            self.head = pointer
        else:
            pointer = self.head
            for i in range(pos-1):
                pointer = pointer.next
            pointer.next = pointer.next.next
        self.size -= 1
    
    def print_ll(self):
        if self.head == None:
            return
        pointer = self.head
        while pointer.next != None:
            print(pointer.value, end = ' ')
            pointer = pointer.next
        print(pointer.value)
        
    def get_size(self):
        return self.size
        
    
l = LinkedList()
l.print_ll()
l.insert(0,5)
l.insert(1,6)
l.insert(0,7)
l.print_ll()
print(l.get_size())
l.delete_pos(0)
print(l.get_size())
l.print_ll()
l.insert(0,7)
l.print_ll()