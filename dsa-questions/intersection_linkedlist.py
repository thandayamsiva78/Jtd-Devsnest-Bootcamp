# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
    
# class Linkedlist:
#     def __init__(self):
#         self.head = None
        
#     def intersection(self, head1, head2 , head3):
#         l1 = []
#         l2 = []
#         l3 = []
#         temp1, temp2 , temp3= head1, head2 , head3
        
#         while temp1:
#             l1.append(temp1.data)
#             temp1 = temp1.next
            
#         while temp2:
#             l2.append(temp2.data)
#             temp2 = temp2.next
        
#         while temp3:
#             l3.append(temp3.data)
#             temp3 = temp3.next
#         return list(set(l1) & set(l2) & set(l3))
        
#     def display(self, head):
#         temp = head
#         while temp:
#             print(temp.data, end="-->")
#             temp = temp.next
#         print("None")

# # Create linked lists
# l1 = Node(10, Node(20, Node(30, Node(90))))
# l2 = Node(10, Node(20, Node(50, Node(90))))
# l3 = Node(10, Node(20, Node(70, Node(90))))

# ll = Linkedlist()
# intersection_result = ll.intersection(l1, l2 ,l3)
# print("Intersection:", intersection_result)

# print("List 1:")
# ll.display(l1)
# print("List 2:")
# ll.display(l2)
# print("List 3:")
# ll.display(l3)
        
      
      
      
      
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
class Linkedlist:
    def __init__(self):
        self.head = None
        
        
    def intersection(self , head1 , head2):
        l1 = []
        l2 = []
        
        temp1 , temp2 = head1 , head2
        while temp1:
            l1.append(temp1.data)
            temp1 = temp1.next
            
        while temp2:
            l2.append(temp2.data)
            temp2 = temp2.next
            
        return list(set(l1) & set(l2))
    
    def display(self, head):
        temp = head
        while temp:
            print(temp.data, end="-->")
            temp = temp.next
    
ll = Linkedlist()
l1 = Node(10, Node(20, Node(30, Node(90))))
l2 = Node(10, Node(20, Node(50, Node(90))))
intersection = ll.intersection(l1 ,l2)
print(intersection)
