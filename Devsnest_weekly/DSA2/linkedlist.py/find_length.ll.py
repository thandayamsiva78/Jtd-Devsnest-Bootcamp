# """find the length of the linked list"""
class Node:
    def __init__(self , data , next =None):
        self.data = data
        self.next = next
        
class linkedlist:
    def __init__(self) -> None:
        self.head = None
        
    def length_of_linkedlist(self):
        temp = self.head
        count = 0
        while temp:
            count+=1
            temp = temp.next
        return count
        
    def display(self):
        temp = self.head
        while temp:
            print(temp.data , end="-->")
            temp = temp.next
            
ll  = linkedlist()
ll.head = Node(10 , Node(20 , Node(30 , Node(40))))

print(ll.length_of_linkedlist())
ll.display