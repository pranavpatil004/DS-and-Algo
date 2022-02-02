class Stack:
    stk = []
    def push(self, val):
        self.stk.append(val)
    def pop(self):
        if len(self.stk)>0:
            return self.stk.pop()
    def top(self):
        return self.stk[-1]
    def isEmpty(self):
        return len(self.stk) == 0

stack = Stack()
print(stack.pop())
print(stack.stk)
stack.push(5)
print(stack.stk)
stack.push(6)
stack.push(4)
print(stack.stk)
print(stack.pop())
print(stack.stk)
stack.push(7)
print(stack.stk)