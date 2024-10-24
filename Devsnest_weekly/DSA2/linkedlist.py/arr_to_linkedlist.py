"""Convert array to linked list"""
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
         
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next: # untill None is comes
            last = last.next
        last.next = new_node
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="-->")
            temp = temp.next   
        print("Null")

ll1 = LinkedList()
ll2 = LinkedList()

arr = [10, 20, 30, 40]
for value in arr:
    ll1.append(value)
    
ll1.display()


arr1 = [10, 20, 30, 40]
for value in arr1:
    ll2.push(value)

ll2.display()  # Correctly call the display method










        
        
