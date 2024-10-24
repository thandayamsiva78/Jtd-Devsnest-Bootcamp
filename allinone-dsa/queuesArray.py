"""
A queue is a fundamental data structure in computer science used to manage and process data in a specific order.
It follows the First In, First Out (FIFO) principle, meaning that the first element added to the queue will be the first one to be removed.

Key Concepts of a Queue:
Enqueue: Adds an element to the back (rear) of the queue.
Dequeue: Removes and returns the element from the front of the queue.
Peek/Front: Returns the element at the front of the queue without removing it.
IsEmpty: Checks if the queue is empty.
Size: Returns the number of elements in the queue.
"""

class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return "Queue is Empty"
    
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        return "Queue is Empty"
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)

# Example usage
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print("Queue:", q.queue)
print("Dequeued Element:", q.dequeue())
print("Queue after dequeue:", q.queue)
print("Front Element:", q.peek())
print("Queue size:", q.size())
print("Is Queue Empty?", q.is_empty())
