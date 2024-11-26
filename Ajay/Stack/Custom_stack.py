class Custom_Stack:
    
    def __init__(self , max_size):
        self.stack = []
        self.max_size = max_size

        
    def push(self , item):
        if len(self.stack) < self.max_size:
            self.stack.append(item)
        else:
            return "Stack is full!"
        
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return "Stack is empty!"
        
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return "Stack is empty!"
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
        

stack = Custom_Stack(7)

stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
stack.push(60)
stack.push(70)

print(stack.pop())
print(stack.peek())
print(stack.is_empty())
print(stack.size())

print(stack.stack)

stack.push(80)

print(stack.stack)
