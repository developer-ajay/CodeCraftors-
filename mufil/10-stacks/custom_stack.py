class CodeCraftorsStack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        

    def peek(self):
        return self.stack[-1]
    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

obj = CodeCraftorsStack()

obj.push(1)
obj.push(2)
obj.push(3)

print(obj.pop())
print(obj.peek())
print(obj.is_empty())
print(obj.size())







