
"""
A stack is a fundamental data structure in computer science used to store and manage data in a specific order. It follows the Last In, First Out (LIFO) principle, meaning that the last element added to the stack is the first one to be removed.

Key Concepts of a Stack:
Push: Adds an element to the top of the stack.
Pop: Removes and returns the element from the top of the stack.
Peek/Top: Returns the element at the top of the stack without removing it.
IsEmpty: Checks if the stack is empty.
Size: Returns the number of elements in the stack.
"""


# class Stack:
#     def __init__(self) -> None:
#         self.stack = []
        
#     def size(self):
#         return len(self.stack)
        
#     def append(self , item):
#         self.stack.append(item)
        
#     def pop(self):
#         if len(self.stack) == 0:
#             return "Stack is Empty"
#         popped = self.stack.pop()
#         return popped

#     def top(self):
#         if len(self.stack) == 0:
#             return "Stack is Empty"
#         return self.stack[-1]
    
# obj = Stack()
# print("Intial Stack : ",obj.stack)

# obj.append(2)
# obj.append(3)
# obj.append(4)
# obj.append(5)

# print(obj.stack)
# print(obj.pop())
# print(obj.top())
# print("Stack Size : ",obj.size())




# implement a stack using Array
class Stack:
    def __init__(self) -> None:
        self.stack = []
        
    def is_Empty(self):
        return len(self.stack)==0
    
    def append(self, item):
        self.stack.append(item)
        
    def pop(self):
        if self.is_Empty():
            return "Stack is Empty"
        popped = self.stack.pop()
        return popped
    def top(self):
        if self.is_Empty():
            return "Stack is Empty"
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)
    
obj = Stack()
arr = [1,2,3,4,5,6,7,8]
for i in arr:
    obj.append(i)
    
print("Stack", obj.stack)
print("popped Element : " , obj.pop())
print("Stack size : " , obj.size())
print("Stack is Empty : " , obj.is_Empty())