class Node:
    def __init__(self , data , next = None):
        self.data = data
        self.next = next
        
class linkedlist:
    def __init__(self):
        self.head = None
        
    def detect_cycle(self):
        temp  = self.head
        slow = temp
        fast = temp.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        
    def display(self):
        temp = self.head
        while temp:
            print(temp.data , end="-->")
            temp = temp.next
        print("Null")
        
ll = linkedlist()
ll.head = Node(10 , Node(20 , Node(30 , Node(40 , Node(20)))))
ll.head.next.next.next.next.next = ll.head.next
print(ll.detect_cycle())
# ll.display()  # infinity
    


