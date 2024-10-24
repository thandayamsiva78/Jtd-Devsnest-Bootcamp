# from collections import deque
# def createQueue(stack):
#     queue = deque()
#     while stack:
#         queue.append(stack.pop())
    
#     print(queue)
    
# stack = []
# stack.append(10)
# stack.append(20)
# stack.append(30)
# stack.append(40)
# stack.append(50)
# createQueue(stack)

# from collections import deque
# def createQueue(stack):
#     queue = deque()
#     while stack:
#         queue.append(stack.pop())
#     return queue
# # Initialize the stack
# stack = []
# stack.append(10)  # stack: [10]
# stack.append(20)  # stack: [10, 20]
# stack.append(30)  # stack: [10, 20, 30]
# stack.append(40)  # stack: [10, 20, 30, 40]
# stack.append(50)  # stack: [10, 20, 30, 40, 50]
# # Create the queue from the stack
# queue = createQueue(stack)
# # Print the queue
# print(queue)  # Output: deque([50, 40, 30, 20, 10])
    

"""Removing the 1st Kth elements"""
# from collections import deque
# def reverse_kth(queue , k):
#     if k > len(queue) or k <= 0:
#         return queue
#     stack = []
#     for _ in range(k):  # push the kth elements in the list
#         stack.append(queue.popleft())
#     while stack: # Enqueue the stack elements in the queue
#         queue.append(stack.pop())
#     for i in range(len(queue)-k): # enqueue the remaining elements in the list
#         queue.append(queue.popleft())
#     return queue

# queue = deque([1,2,3,4,5,6,7,8,9,10])
# k = 5
# print(reverse_kth(queue , k))

"""REVERSE AN QUEUE USING DEQUEUE"""
# from collections import deque  # deque follows FIFO order
# def reversequeue(queue):
#     stack = []
#     while queue: # push the elements into the stack using popleft which means fifo
#         stack.append(queue.popleft())
#     while stack: # enqueue the elements into the queue using pop which means lifo
#         queue.append(stack.pop())
#     return queue
# queue = deque([1,2,3,4,5,6,7,8,9,10])
# # print(reverse_queue(queue))
# res = reversequeue(queue)
# print(list(res))