
# Removing Duplicates: The remove_duplicates method removes duplicates by:
# Checking if the list is empty.
# Initializing a set to store unique values.
# Traversing the list and removing any node whose value is already in the set.

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Linkedlist:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def remove_duplicates(self):
        if self.head is None:
            return
        
        current = self.head
        unique = set()
        unique.add(current.data)
        while current.next:
            if current.next.data in unique :
                current.next = current.next.next
            else:
                unique .add(current.next.data)
                current = current.next
        # print(unique)

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="-->")
            temp = temp.next
        print("None")

ll = Linkedlist()
elements = [1, 2, 3, 4, 5, 6, 3, 4, 2]
for ele in elements:
    ll.append(ele)
print("Original list:")
ll.display()

ll.remove_duplicates()
print("List after removing duplicates:")
ll.display()


print()



class Node:
    def __init__(self , data , next = None):
        self.data = data
        self.next = next
    
class Linkedlist:
    def __init__(self):
        self.head = None
        
    def remove_duplicates(self , data):
        return list(set(data))
    
    def append(self , data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        
        
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="-->")
            temp = temp.next
    
ll = Linkedlist()
elements = [1,2,3,4,5,6,3,4,2]
unique = ll.remove_duplicates(elements)
for ele in unique:
    ll.append(ele)
ll.display()
        


print()

class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next
        
class linkedlist:
    def __init__(self) -> None:
        self.head = None
    
    def remove_duplicates(self):
        unique = set()
        current = self.head
        prev = None
        
        while current:
            if current.data in unique:
                prev.next = current.next
            else:
                unique.add(current.data)
                prev = current
            current = current.next
        return self.head
        
    def display(self):
        current = self.head
        while current:
            print(current.data, end="-->")
            current = current.next
        print("None")

ll = linkedlist()
ll.head = Node(10, Node(20, Node(30, Node(30, Node(50)))))
ll.remove_duplicates()
ll.display()



"""Remove Duplicates Using set()"""


# my_list = set()
# elemennts = [1,2,2,3,4,4,5,6,7,7,8,]
# for el in elemennts:
#     my_list.add(el)
# print(my_list)

# arr = [1,2,2,3,4,4,5,6,7,7,8,]
# unique = list(set(arr))
# print(unique)

"""Using dictionary"""

# arr = [1,2,2,3,4,4,5,6,7,7,8,]
# unque_arr = list(dict.fromkeys(arr))
# print(unque_arr)

"""Using to empty lists []"""
# unque = []
# dup = []
# elemennts = [1,2,2,3,4,4,5,6,7,7,8,]
# for el in elemennts:
#     if el in unque:
#         dup.append(el)
#     else:
#         unque.append(el)
# print(unque)
# print(dup)
