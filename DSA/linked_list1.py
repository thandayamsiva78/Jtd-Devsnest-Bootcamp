# class Node:
#     def __init__(self ,val ) -> None:
#         self.val = val
#         self.next = None

# class LinkedList:
#     def __init__(self) -> None:
#         self.head = None

#     def insert_at_beg(self,data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node

#     def printlinkedlist(self):
#         temp = self.head
#         while temp:
#             print(temp.val , end='-->')
#             temp = temp.next
#         print(None)

# def array_to_linkedlist(array):
#     linked_list = LinkedList()
#     for item in reversed(array):  # without reversed it give "reverse order output"
#         linked_list.insert_at_beg(item)
#     return linked_list    
    
# array = [1,2,3,4,5,6]
# linkedlist = array_to_linkedlist(array)
# linkedlist.printlinkedlist()
        
    