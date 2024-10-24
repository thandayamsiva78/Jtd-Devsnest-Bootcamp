# Finding the Middle Node: The find_middle method uses the two-pointer technique:
# Both pointers start at the head.
# The slow pointer moves one step at a time, while the fast pointer moves two steps at a time.
# When the fast pointer reaches the end, the slow pointer will be at the middle node.


"""Find middle node in a linked list"""
# Use Two pointer Technique
class Node:
    def __init__(self , data , next = None):
        self.data = data
        self.next = next
        
class Linkedlist:
    def __init__(self):
        self.head = None
        
    def find_middle(self):
        # Edge case: if the list is empty or has only one element
        if self.head is None or self.head.next is None:
            return None
        
        slow = self.head
        fast = self.head
        
        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow.data
        
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="-->")
            temp = temp.next
    
ll = Linkedlist()
ll.head = Node(10, Node(20, Node(30, Node(40, Node(50,Node(60, Node(70 , Node(80 ,Node(90 , Node(100))))))))))
mid = ll.find_middle()
print(mid)
ll.display()


# Step 0: slow=10, fast=10
# Step 1: slow=20, fast=30
# Step 2: slow=30, fast=50
# Step 3: slow=40, fast=70
# Step 4: slow=50, fast=90
# Step 5: slow=60, fast=100
print()


"""Find middle element Using count(ll) // 2 idx"""

class Node:
    def __init__(self , data , next = None):
        self.data = data
        self.next = next
        
class Linkedlist:
    def __init__(self):
        self.head = None
        
    def find_middle(self):
        temp = self.head
        count = 0
        while temp :
            count+=1
            temp  = temp.next
        mid = count//2
        temp = self.head
        for i in range(mid):
            temp = temp.next
        return temp.data
    
    def delete_middle(self):
         # Edge case: if the list is empty or has only one element
        if self.head is None or self.head.next is None:
            return None
        temp = self.head
        count = 0
        while temp :
            count+=1
            temp  = temp.next
        mid = count//2
        temp = self.head
        for i in range(mid-1):
            temp = temp.next
        temp.next = temp.next.next

    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="-->")
            temp = temp.next
    
ll = Linkedlist()
ll.head = Node(1, Node(3, Node(4, Node(7, Node(1,Node(2, Node(6 )))))))
print(ll.find_middle())
ll.delete_middle()

ll.display()
