# To reorder a linked list, we generally mean to rearrange it in a specific pattern. One common reordering is the "L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ..." pattern. This involves:

# Finding the middle of the linked list.
# Reversing the second half of the linked list.
# Merging the two halves in the desired order.
# Here's the code to achieve this:
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse(self, head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    def reorder_list(self):
        if not self.head or not self.head.next:
            return

        # Step 1: Find the middle of the linked list
        middle = self.find_middle()
        
        # Step 2: Reverse the second half of the linked list
        second_half = self.reverse(middle.next)
        middle.next = None  # Split the list into two halves
        
        # Step 3: Merge the two halves
        first_half = self.head
        
        while first_half and second_half:
            first_next = first_half.next
            second_next = second_half.next

            first_half.next = second_half
            second_half.next = first_next
            
            first_half = first_next
            second_half = second_next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" --> ")
            temp = temp.next
        print("None")

# Create the linked list and add nodes
ll = LinkedList()
ll.head = Node(10, Node(20, Node(30, Node(40, Node(50 , Node(60))))))

# Reorder the linked list
ll.reorder_list()

# Display the reordered linked list
ll.display()

# Step-by-Step Explanation
# Find the Middle of the Linked List:

# Use the slow and fast pointer approach. slow moves one step at a time, while fast moves two steps. When fast reaches the end, slow will be at the middle.
# Reverse the Second Half:

# Use the reverse logic as previously discussed but start from the middle node.
# Merge the Two Halves:

# Alternate between nodes from the first and second halves, adjusting pointers to achieve the desired order.
# Visual Representation of Steps
# Original Linked List:

# rust
# Copy code
# 10 -> 20 -> 30 -> 40 -> 50 -> None
# Step 1: Find the Middle:

# rust
# Copy code
# 10 -> 20 -> 30 -> 40 -> 50 -> None
#                 ^
#                middle
# Step 2: Reverse the Second Half:

# rust
# Copy code
# 10 -> 20 -> 30 -> 40 -> 50 -> None
#                 ^
#                middle

# Reversed:
# 10 -> 20 -> 30 -> None
# 50 -> 40 -> None
# Step 3: Merge Two Halves:

# rust
# Copy code
# First Half:  10 -> 20 -> 30 -> None
# Second Half: 50 -> 40 -> None

# Reordered: 10 -> 50 -> 20 -> 40 -> 30 -> None




class Node:
    def __init__(self , data , next = None):
        self.data = data
        self.next = next
        
class Linkedlist:
    def __init__(self):
        self.head = None
        
    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverse2ndhalf(self , head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
    
    def reorder(self):
        if self.head is None or self.head.next is None:
            return True
        middle = self.find_middle()
        second_half = self.reverse2ndhalf(middle.next)
        middle.next = None
        
        first_half = self.head
    
        while first_half and second_half:
            first_half.next = second_half
            second_half.next = first_half
        first_half = first_half.next
        second_half = second_half.next
        
    def display(self):
        current = self.head
        while current:
            print(current.data , end="-->")
            current = current.next
            
ll = LinkedList()
ll.head = Node(10 , Node(20 , Node(30 , Node(40 ,Node(50 ,Node(60))))))
ll.reorder_list()
ll.display()

        
            