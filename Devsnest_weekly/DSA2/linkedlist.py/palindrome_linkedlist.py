class Node:
    def __init__(self , data , next = None):
        self.data = data
        self.next = next
        
class Linkedlist:
    def __init__(self):
        self.head = None
        
    def palindrome(self):
        temp = []
        currrent = self.head
        while currrent:
            temp.append(currrent.data)
            currrent = currrent.next
        return temp == temp[::-1]
    
        # if temp == temp[::-1]:
        #     return True
        # else:
        #     return False
            
    def display(self):
        current = self.head
        while current:
            print(current.data, end="-->")
            current = current.next
        print("None")

ll = Linkedlist()
ll.head = Node(1, Node(2, Node(3, Node(3, Node(2, Node(1))))))
print(ll.palindrome())
ll.display()


"""Palindrome or not"""
# def is_palindrome(arr):
#     if not arr:
#         return True
#     left = 0
#     right = len(arr) - 1
#     while left < right:
#         if arr[left] != arr[right]:
#             return False
#         left += 1
#         right -= 1
#     return True
# # Example usage:
# arr1 = [1, 2, 3, 2, 1]
# arr2 = [1, 2, 3, 4, 5]

# print(is_palindrome(arr1))  # True
# print(is_palindrome(arr2))  # False


class Node:
    def __init__(self , data , next = None):
        self.data = data
        self.next = next
        
class Linkedlist:
    def __init__(self):
        self.head = None
        
        
    def palindrome(self):
        stack = []
        temp = self.head
        while temp:
            stack.append(temp.data)
            temp = temp.next
        
        temp = self.head
        while temp:
            if temp.data != stack.pop():
                return False
            temp = temp.next
        return True
            
    def display(self):
        current = self.head
        while current:
            print(current.data, end="-->")
            current = current.next
        print("None")

ll = Linkedlist()
ll.head = Node(1, Node(2, Node(3, Node(3, Node(2, Node(1))))))
print(ll.palindrome())
ll.display()






















        
            