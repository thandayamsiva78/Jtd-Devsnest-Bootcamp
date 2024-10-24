"""Reverse a Linked list """
# 1 . Iterative 
# 2 . Recursive
# 3 . Using stacks
# 4 . TailRecursive approach

class Node:
    def __init__(self , data , next = None):
        self.data = data
        self.next = next
        
class linkedlist:
    def __init__(self) -> None:
        self.head = None
        
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        return self.head

    def display(self):
        temp = self.head
        while temp:
            print(temp.data , end="-->")
            temp = temp.next
    
ll = linkedlist()    
ll.head = Node(10 ,Node(20 , Node(30 , Node(40))))
ll.reverse()
ll.display()




"""Reverse Linked list using swapping method"""
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def reverse_ll(self):
        # Collect all node data in an array
        arr = []
        temp = self.head
        while temp:
            arr.append(temp.data)
            temp = temp.next
        # print(arr) # [10,20,30,40,50]
        
        # Swap the data in the array
        left = 0
        right = len(arr) - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        # [50,40,30,20,10]
        
        # Assign the swapped data back to the nodes
        temp = self.head
        for data in arr:
            temp.data = data
            temp = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" --> ")
            temp = temp.next
        print("None")

# Create the linked list and add nodes
ll = LinkedList()
ll.head = Node(10, Node(20, Node(30, Node(40, Node(50)))))
# Reverse the linked list using swapping method
ll.reverse_ll()
# Display the reversed linked list
ll.display()



