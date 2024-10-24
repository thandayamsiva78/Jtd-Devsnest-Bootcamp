# class ListNode:
#     def __init__(self, value=0, next=None):
#         self.value = value
#         self.next = next

# def merge_two_lists(l1, l2):
#     dummy = ListNode()
#     current = dummy
#     while l1 is not None and l2 is not None:
#         if l1.value < l2.value:
#             current.next = l1
#             l1 = l1.next
#         else:
#             current.next = l2
#             l2 = l2.next
#         current = current.next
#     if l1:
#         current.next = l1
#     else:
#         current.next = l2
#     return dummy.next

# def print_list(node):
#     while node:
#         print(node.value, end=" -> ")
#         node = node.next
#     print("None")

# # Example usage
# # List 1: 1 -> 2 -> 4
# l1 = ListNode(1, ListNode(2, ListNode(4)))
# # List 2: 1 -> 3 -> 4
# l2 = ListNode(1, ListNode(3, ListNode(4)))
# # Merged list: 1 -> 1 -> 2 -> 3 -> 4 -> 4
# merged_list = merge_two_lists(l1, l2)
# print_list(merged_list)





# class Node:
#     def __init__(self , data , next = None):
#         self.data = data
#         self.next = next
        
# class linkedlist:
#     def __init__(self) -> None:
#         self.head = None
        
#     def merge(self, l2):
#         dummy = Node(0)
#         current = dummy
#         left = self.head
#         right = l2.head
        
#         while left is not None and right is not None:
#             if left.data < right.data:
#                 current.next = left
#                 left = left.next
#             else:
#                 current.next = right
#                 right = right.next
#             current = current.next
        
#         # If any elements are left in either list, append them
#         if left is not None:
#             current.next = left
#         if right is not None:
#             current.next = right
        
#         self.head = dummy.next  # Update the head of the current list
        
#     def display(self):
#         temp = self.head
#         while temp:
#             print(temp.data , end="-->")
#             temp = temp.next
    
# l1 = linkedlist()    
# l1.head = Node(10 ,Node(30 , Node(50 , Node(70))))
# print("List 1:")
# l1.display()

# print()
# l2 = linkedlist()    
# l2.head = Node(20 ,Node(40 , Node(60 , Node(80))))
# print("List 2:")
# l2.display()
# print()
# print("Merged list :")
# l1.merge(l2)
# l2.display()


class Node:
    def __init__(self , data = 0 , next = None):
        self.data = data
        self.next = next
        
def merge_linkedlist(l1 , l2):
    dummy = Node()
    current = dummy
    while l1 is not None and l2 is not None:
        if l1.data < l2.data:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    if l1:
        current.next = l1
    if l2:
        current.next = l2
    return dummy.next
def display(node):
    current =  node
    while current:
        print(current.data, end="-->")
        current = current.next
    print("Null")
      
l1 = Node(10,Node(30, Node(50, Node(60, Node(100)))))
l2 = Node(20,Node(40, Node(70, Node(80, Node(90)))))
merged = merge_linkedlist( l1 , l2)
display(merged)