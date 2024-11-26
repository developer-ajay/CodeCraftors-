from collections import deque

# Initialize a stack
stack = deque()

# Push elements onto the stack
stack.append(1)
stack.append(2)
stack.append(3)


print("Stack after pushes:", stack)

# Pop elements from the stack
print("Popped element:", stack.pop())
print("Popped element:", stack.pop())

# Stack after pops
print("Stack after pops:", stack)
