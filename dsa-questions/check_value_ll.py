# """Check if a value exits in a linked list"""
class Node:
    def __init__(self , data , next =None):
        self.data = data
        self.next = next   
class linkedlist:
    def __init__(self) -> None:
        self.head = None    
    def valuepresent(self , key):
        temp = self.head
        while temp and temp.next:
            if temp.next.data == key:
                return True
            temp = temp.next
        return False      
    def display(self):
        temp = self.head
        while temp:
            print(temp.data , end="-->")
            temp = temp.next        
ll  = linkedlist()
ll.head = Node(10 , Node(20 , Node(30 , Node(40, Node(50)))))
print(ll.valuepresent(20))
ll.display()