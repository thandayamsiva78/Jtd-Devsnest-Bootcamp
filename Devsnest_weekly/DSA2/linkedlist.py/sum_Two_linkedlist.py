"""Sum Two linked lists"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy_head = ListNode(0)  # Step 1: Initialize dummy head
    current = dummy_head      # Pointer to build the result list
    carry = 0                 # Initialize carry to 0
    
    while l1 is not None or l2 is not None:  # Step 2: Traverse both lists
        x = l1.val if l1 is not None else 0  # Get value from l1, 0 if l1 is None
        y = l2.val if l2 is not None else 0  # Get value from l2, 0 if l2 is None
        sum = carry + x + y                  # Calculate sum of values and carry
        carry = sum // 10                    # Update carry
        current.next = ListNode(sum % 10)    # Create new node with current digit
        current = current.next               # Move to the next node
        
        if l1 is not None: l1 = l1.next      # Move l1 to the next node
        if l2 is not None: l2 = l2.next      # Move l2 to the next node
    
    if carry > 0:                            # Step 3: Handle remaining carry
        current.next = ListNode(carry)       # Create a new node with carry
    
    return dummy_head.next

def display(node):
    temp = node
    while temp:
        print(temp.val , end="-->")
        temp = temp.next

l1 = ListNode(2, ListNode(3, ListNode(5 )))
l2 = ListNode(2, ListNode(3, ListNode(5 )))

result = addTwoNumbers(l1 , l2)
display(result)


print()

class Node:
    def __init__(self , data , next = None) -> None:
        self.data = data
        self.next = next
        
def sumTwolinkedlist( l1 , l2):
    if l1 is None and l2 is None:
        return
    dummy_head = Node(0)
    current = dummy_head
    carry = 0
    
    while l1 is not None and l2 is not None:
        x = l1.data if l1 is not None else 0
        y = l2.data if l2 is not None else 0
        sum = carry + x + y
        carry = (sum//10)
        current.next = Node(sum % 10)
        current = current.next
        
        if l1 is not None:
            l1 = l1.next
        if l2 is not None:
            l2 = l2.next
            
    if carry > 0:
        current.next = Node(carry)
        current = current.next
            
    return dummy_head.next
    
def display(node):
    temp = node
    while temp:
        print(temp.data , end="-->")
        temp = temp.next
    
l1 = Node(2, Node(3 ,Node(5)))
l2 = Node(2, Node(3 ,Node(5)))

result = sumTwolinkedlist(l1 , l2)
display(result)


        
        
        
print()
print(10//10)
print(10%10)    