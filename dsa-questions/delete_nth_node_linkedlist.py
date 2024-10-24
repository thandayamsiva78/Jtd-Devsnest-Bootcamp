# Boundary conditions: Ensure that n is a valid index (i.e., 1 <= n <= count).
# Deleting the head node: If n is equal to the length of the list, it means we need to delete the head node.
# Validating the index: Ensure the correct node is being accessed and deleted.


"""Delete nth node in a Linked list"""
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Linkedlist:
    def __init__(self):
        self.head = None

    def delete_nth_node(self):
        n = int(input("Enter Delete nth Node :"))
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        # print(count)
        # Check if the value of n is valid
        if n <= 0 or n > count:
            print("Invalid node position")
            return
            # Special case: deleting the head node
        if n == count:
            self.head = self.head.next
            return
        current = self.head
        for i in range(count-n-1):
            current = current.next
        current.next = current.next.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end="-->")
            # del  current.data
            current = current.next

ll = Linkedlist()
# ll.head = Node(1, Node(2))
ll.head = Node(10, Node(20, Node(30, Node(40, Node(50, Node(60, Node(70 ,Node(80))))))))
ll.delete_nth_node()
ll.display()
