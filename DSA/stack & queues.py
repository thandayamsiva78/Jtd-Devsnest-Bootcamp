# stack problems
# def next_greater_ele(array):
#     result = [-1]* len(array)
#     stack = []

#     for index,arr in enumerate(array):
#         while stack  and array[stack[-1]] < arr:
#             result[stack.pop()] = arr
#         stack.append(index)

#     return result
# print(next_greater_ele([2,1,2,4,3]))

## queues problems
# class Queues:
#     def __init__(self) -> None:
#         self.queue = []
       
#     def isEmpty(self):
#         return len(self.queue) == 0
    
#     def enqueue(self,value):
#         self.queue.append(value)
#         print(self.queue)

#     def dequeue(self):
#         if self.isEmpty():
#             return "queue is Empty"
#         else:
#             result = self.queue.pop(0)
#             return result

#     def size(self):
#         return len(self.queue)
    
# q = Queues()

# q.enqueue(10)
# q.enqueue(20)
# q.enqueue(30)

# print(q.isEmpty())
# print(q.dequeue())
# print(q.size())

## reverse
# from collections import deque

# def reverse(queue):
#     stack = []
#     while queue:
#         stack.append(queue.popleft())
#     while stack:
#         queue.append(stack.pop())
#     return queue

# q= deque([1,2,3,4,5])
# rev = reverse(q)
# print(rev)


# check given string is palidrome or not using queues
# from collections import deque
# def is_palidrome(s):
#     stack = []
#     queue = deque()
#     for char in s:
#         stack.append(char)
#         queue.append(char)
#     while queue:
#         if queue.popleft() != stack.pop():
#             return False
#         return True
# s = "madam"
# print(is_palidrome(s))

# class Queues:
#     def __init__(self):
#         self.queue = []

#     def isEmpty(self):
#         return len(self.queue) == 0
    
#     def enqueue(self,value):
#         self.queue.append(value)
#     def appendleft(self,value):
#         self.queue.insert(0,value)

#     def dequeue(self):
#         if self.isEmpty():
#             return "Queues is empty"
#         else:
#             result =self.queue.pop(0)
#             return result
#     def popleft(self):
#         if not self.isEmpty():
#             return self.queue.pop(0)
#         return "Queues is empty"
#     def peek(self):
#         if self.isEmpty():
#             return "Queues is empty"
#         else:
#             result =self.queue[0]
#             return result
#     def size(self):
#         return len(self.queue) == 0
    
# q = Queues()
# q.enqueue(10)
# q.enqueue(20)
# q.enqueue(30)
# q.enqueue(40)

# q.appendleft(50)

# print(q.queue)
# print(q.dequeue())
# print(q.popleft())

# print(q.peek())
# print(q.size())

                  
# stack .....
# push(2)
# pop()
# isEmpty()
# isFull()
# top()
# LIFO Last in Fist Out

# queues....
# arry is similar to queues
# push --> ENQUEUE(2)
# POP --> DEQUEUE()
# PEEK() OR FROUNT()
# FIFO  First come Fist Out
# def solve(order):
#     # CODE HERE
#     stack = []
#     next = 1
#     for el in order:
#         if el == next:
#             next+=1            
#         else:
#             stack.append(el)
#     while stack: # while the stack contains the elements
#         el = stack.pop()
#         if el==next:
#             next+=1
#         else:
#             return 0
#     return 1
# order = [5,1,2,4,3]
# # order = [3,4,2,1,5]
# print(solve(order))