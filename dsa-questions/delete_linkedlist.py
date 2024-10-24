class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Linkedlist:
    def __init__(self):
        self.head = None

    # def deleteList(self):
    # # initialize the current node
    #     current = self.head
    #     while current:
    #         next_to_current = current.next  # move next node
    #     # delete the current node
    #         del current
    #     # set current equals prev node
    #         current = next_to_current
    # print("List is Empty")

    def deleteList(self):
        # self.head = None
        # return self.head

        current = self.head
        while current:
            prev = current
            current = current.next
            del prev
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end="-->")
            current = current.next

ll = Linkedlist()
ll.head = Node(10, Node(20, Node(30, Node(40, Node(50, Node(60, Node(70)))))))
ll.deleteList()
ll.display()
