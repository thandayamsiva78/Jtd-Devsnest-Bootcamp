# # Create a Node
# class Node:
#     def __init__(self , data , next = None):
#         self.data = data
#         self.next = next
# # Link the all nodes in Linked List
# class Linkedlist:
#     def __init__(self):
#         self.head = None
     
#     def insert_at_begining(self , val):
#         new_node = Node(val)  # 1 .create Node
#         new_node.next = self.head  # 2 . store  the head address in newNode.next
#         self.head = new_node # 3 . update the head as a newNode
        
#     def insert_at_end(self , val):
#         new_node = Node(val)
#         current = self.head
        
#         while current.next: # traverse end of the linked list 
#             current = current.next # find last untill update 
#         current.next = new_node  # ofter loop considerd as its means finded the last node and its having None  so itiliazing newnode into last node.next   
        
#     def insert_at_pos(self ,val , pos):
#         new_node = Node(val)
#         current = self.head
#         for i in range(pos- 1):
#             current = current.next
#         new_node.next = current.next 
#         current.next  =  new_node
                
#     def insert_at_middle(self , val):
#         new_node = Node(val)
#         current = self.head
#         count = 0
#         while current:
#             count+=1
#             current = current.next
#         mid = count//2
#         # print(mid)
#         self.insert_at_pos(val , mid)

        
#     def display(self):
#         current = self.head  # store the head in a temporary variable
#         while current:  # if all nodes as long as
#             print(current.data , end="-->")  # print the node.data
#             current = current.next # as long as move next one by one
#         print("Null")    # ofter loop exits print()    
    
# ll = Linkedlist()

# ll.head = Node(10 , Node(20 , Node(30 , Node(40 , Node(50 , Node(60 ,Node(70)))))))
# ll.insert_at_begining(5)
# ll.insert_at_end(100)
# ll.insert_at_pos(25 , 3)
# ll.insert_at_middle(55)
# ll.display()



"""==================================================================================="""



class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        
    def insert_at_end(self, val):
        new_node = Node(val)
        if self.head is None:  # case 1. list is EMpty or head is Empty then update newnode to head
            self.head = new_node
            return
        current = self.head
        while current.next:  # case 2. list is not empty find last node and update the new node to last node 
            current = current.next
        current.next = new_node
        
    def insert_at_pos(self, val, pos):
        new_node = Node(val)
        current = self.head
        if pos == 0:  # case 1. if pos is <=1  its means insert starting just update newnode.next to head
            new_node.next = self.head
            self.head = new_node
            return
        for _ in range(pos - 1): # case 2. >=2 run the loop untill the given position 
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
        new_node.next = current.next # ofter loop exists update newnode.next to currnt next  then update current next to newnode
        current.next = new_node
            
    def insert_at_middle(self, val):
        current = self.head
        count = 0  # find length of the linked list
        while current:
            count += 1
            current = current.next
        mid = count // 2  # find middle node at the linked list
        self.insert_at_pos(val, mid) # call the another function which is inserting at particular pos

    def delete_at_pos(self, pos):
        if self.head is None:
            print("List is empty")
            return
        
        current = self.head
        
        if pos == 1:
            self.head = current.next
            current = None
            return
        
        for i in range(pos - 2):
            if current.next is None:
                print("Position out of range")
                return
            current = current.next
            # print(i, end=" ")
        
        if current.next is None or current.next.next is None:
            print("Position out of range")
            return
        
        current.next = current.next.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end="-->")
            current = current.next
        print("Null")

# Testing the LinkedList
ll = Linkedlist()
ll.head = Node(10, Node(20, Node(30, Node(40, Node(50)))))
ll.insert_at_beginning(5)
ll.insert_at_end(60)
ll.insert_at_pos(25, 3)
ll.insert_at_middle(55)
ll.display()
ll.delete_at_pos(3)
ll.display()
ll.delete_at_pos(1)
ll.display()
ll.delete_at_pos(10)  # Out of range test
ll.display()


