"""Delete the node with value 20 from the linked list  output = 10-->30-->40-->50 """ 


class Node:
    def __init__(self , data , next = None):
       self.data = data
       self.next = next
class linkedlist:
    def __init__(self):
        self.head = None
        
    def delete_node(self ,key):
        if self.head is None:
            return
        temp = self.head
        while temp and temp.next :    # traverse untill key Word
            if temp.next.data == key:
                temp.next = temp.next.next 
            temp = temp.next
        return self.head
    def display(self):
        temp = self.head
        while temp :
            print(temp.data , end= "-->")
            temp = temp.next
ll = linkedlist()
ll.head = Node(10 , Node(20 , Node(30 , Node(40 , Node(50)))))
ll.delete_node(40)
ll.display()


"""==============================================================================="""


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    # Recursive method to delete a node by key
    def delete_node_using_key(self, node, key):
        # Base case: If the node is null
        if not node:
            return None

        # If the node itself holds the key to be deleted
        if node.data == key:
            return node.next

        # Recursively call for the next node
        node.next = self.delete_node_using_key(node.next, key)
        return node

    def delete(self, key):
        self.head = self.delete_node_using_key(self.head, key)

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="-->")
            temp = temp.next
        print("Null")

ll = LinkedList()
ll.head = Node(10, Node(20, Node(30, Node(40, Node(50)))))
ll.delete(20)
ll.display()



"""Delete the node with value 20 from the linked list  output = 10-->30-->40-->50 """ 
class Node:
    def __init__(self , data , next = None):
        self.data = data
        self.next = next
class linkedlist:
    def __init__(self):
        self.head = None

        
    def delete_node_using_key(self , key):
        if self.head is None:  # if head is none return None (list is Empty)
            print("Linked list is Empty")
            return
        if self.head.data == key:  # if heads mateches the key then pointer to the haed return head
            self.head = self.head.next
            return 
        curr = self.head
        # while curr and curr.next :   # traverse untill key found
        # (OR)
        while curr.next is not None: # traverse untill key found
            if curr.next.data == key: # any data match with key ? condition
                curr.next = curr.next.next  # update next pointer
                return self.head 
            curr = curr.next
        return self.head
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data , end="-->")
            temp = temp.next
        print("Null")

ll = linkedlist()
ll.head = Node(10 , Node(20 , Node(30 , Node(40 , Node(50)))))    
ll.delete_node_using_key(20)
ll.display()



class Node:
    def __init__(self , data , next = None):
       self.data = data
       self.next = next
class linkedlist:
    def __init__(self):
        self.head = None
        
    def delete_node(self ,key):
        if self.head is None:
            return
        temp = self.head
        while temp and temp.next :    # traverse untill key Word
            if temp.next.data == key:
                temp.next = temp.next.next 
            temp = temp.next
        return self.head
    def display(self):
        temp = self.head
        while temp :
            print(temp.data , end= "-->")
            temp = temp.next
ll = linkedlist()
ll.head = Node(10 , Node(20 , Node(30 , Node(40 , Node(50)))))
ll.delete_node(40)
ll.display()
