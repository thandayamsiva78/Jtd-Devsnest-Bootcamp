# reverse a linked list in group of given size #
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LL:
    def __init__(self):
        self.head = None

    def reverse(self, head, k):
        if head == None:
            return None
        curr = head
        next = None
        prev = None
        count = 0

        while(curr is not None and count < k): #3<3
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            count += 1

        if next is not None:
            head.next = self.reverse(next, k)
        return prev
    
    # def push(self, new_data):
    #     new_node = Node(new_data)
    #     new_node.next = self.head
    #     self.head = new_node
    
    def append(self , values):
        new_node = Node(values)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    
    def printLL(self):
        temp = self.head
        while(temp):
            print(temp.data, end = " ")
            temp = temp.next

llist = LL()
elements = [1,2,3,4,5,6,7,8,9]
for el in elements:
    llist.append(el)
    
# llist.push(9)
# llist.push(8)
# llist.push(7)
# llist.push(6)
# llist.push(5)
# llist.push(4)
# llist.push(3)
# llist.push(2)
# llist.push(1)

print("Given linked list")
llist.printLL()
llist.head = llist.reverse(llist.head, 3)
print()
print("Reversed Linked List")
llist.printLL()