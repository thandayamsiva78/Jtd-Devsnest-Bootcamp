# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.prev = None
#         self.next = None

# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None

#     # Function to append a new node at the end of the list
#     def append(self, new_data):
#         new_node = Node(new_data)

#         # If the list is empty, make the new node as head
#         if self.head is None:
#             self.head = new_node
#             return

#         last = self.head

#         # Traverse to the last node
#         while last.next:
#             last = last.next

#         # Change the next of last node to new node
#         last.next = new_node

#         # Make new node as last node
#         new_node.prev = last

#     # Function to insert a new node at the front of the list
#     def insertAtFront(self, new_data):
#         new_node = Node(new_data)

#         # Make the new node as head and its prev as NULL
#         new_node.prev = None

#         # If the list is empty, also make next as NULL
#         if self.head is None:
#             new_node.next = None
#         else:
#             # Set the prev of current head to new node
#             self.head.prev = new_node

#         # Make next of new node as current head
#         new_node.next = self.head

#         # Update the head reference
#         self.head = new_node

#     # Function to insert a new node at a given position
#     def insertAtPosition(self, new_data, position):
#         # If position is 0, insert at front
#         if position == 0:
#             self.insertAtFront(new_data)
#             return

#         new_node = Node(new_data)

#         current = self.head

#         # Count until position-1 is reached
#         count = 1
#         while current and count < position:
#             current = current.next
#             count += 1

#         # If position is more than number of nodes, append at the end
#         if not current:
#             self.append(new_data)
#             return

#         # If node at position is found, link it
#         new_node.next = current.next

#         # Link previous node if it exists
#         if current.next:
#             current.next.prev = new_node

#         # Link current node to the new node
#         current.next = new_node

#         # Set prev of the new node
#         new_node.prev = current

#     # Function to insert a new node at the end of the list
#     def insertAtEnd(self, new_data):
#         self.append(new_data)

#     # Function to print the contents of the list
#     def printList(self):
#         temp = self.head
#         while temp:
#             print(temp.data, end=" -> ")
#             temp = temp.next
#         print("None")

# # Example usage
# linked_list = DoublyLinkedList()

# linked_list.append(10)
# linked_list.append(20)
# linked_list.append(30)

# print("Created linked list is: ")
# linked_list.printList()

# linked_list.insertAtFront(5)
# print("\nLinked list after insertion at front 5: ")
# linked_list.printList()

# linked_list.insertAtPosition(15, 2)
# print("\nLinked list after insertion at position 2 (15): ")
# linked_list.printList()

# linked_list.insertAtEnd(40)
# print("\nLinked list after insertion at end (40): ")
# linked_list.printList()


"""======================================================================================================================================="""
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.prev = None
#         self.next = None

# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None

#     # Function to append a new node at the end of the list
#     def append(self, new_data):
#         new_node = Node(new_data)

#         # If the list is empty, make the new node as head
#         if self.head is None:
#             self.head = new_node
#             return

#         last = self.head

#         # Traverse to the last node
#         while last.next:
#             last = last.next

#         # Change the next of last node to new node
#         last.next = new_node

#         # Make new node as last node
#         new_node.prev = last

#     # Function to print the contents of the list
#     def printList(self):
#         temp = self.head
#         while temp:
#             print(temp.data, end=" -> ")
#             temp = temp.next
#         print("None")

#     # Function to delete a node from the beginning of the list
#     def deleteFromFront(self):
#         # If list is empty, do nothing
#         if self.head is None:
#             print("List is empty, nothing to delete")
#             return

#         # If there's only one node, remove it and set head to None
#         if self.head.next is None:
#             temp = self.head
#             self.head = None
#             del temp
#             print(f"Deleted node: {temp.data}")
#             return

#         # Otherwise, move head to the next node and remove references from the old head
#         temp = self.head
#         self.head = self.head.next
#         self.head.prev = None  # Update the prev of the new head
#         del temp
#         print(f"Deleted node: {temp.data}")

#     # Function to delete a node from a specified position
#     def deleteFromPosition(self, position):
#         # If list is empty, do nothing
#         if self.head is None:
#             print("List is empty, nothing to delete")
#             return

#         # If position is 0, delete from front
#         if position == 0:
#             self.deleteFromFront()
#             return

#         current = self.head
#         count = 1

#         # Find the node
# dl = DoublyLinkedList()
# dl.append(10)
# dl.append(20)
# dl.append(30)
# dl.append(40)
# dl.deleteFromFront()

# dl.printList()