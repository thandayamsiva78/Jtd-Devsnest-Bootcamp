class Node:
    def __init__(self , data , next = None):
        self.data = data
        self.next = next
        
class linkedlist:
    def __init__(self):
        self.head = None
        
    def inserting_at_begening(self , val):
        new_node = Node(val)
        if self.head is None:
            new_node.next = self.head
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node
        
    def display(self):
        temp = self.head
        while temp:
            print(temp.data , end="--->")
            temp = temp.next
        print("Null")        
        
        
ll = linkedlist()
ll.head = Node(10 , Node(20 , Node(30 , Node(40 , Node(50)))))
ll.inserting_at_begening(5)
ll.display()
    