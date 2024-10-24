# Question: How do you check if the sequence of brackets is balanced using a stack in O(n) time? Ensure to handle all types of brackets: (), {}, and [].
# Input: "[{()}]"
# Output: True


def isValidparqanthes(s):
    stack = []
    brackets = {")":"(" , "]":"[" , "}":"{"}
    for char in s:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets:
            if stack and stack[-1] != brackets[char]: 
                stack.pop()
            else:
                return False
    return len(stack) == 0
    
s = "[{()}]"
result = isValidparqanthes(s)
print(result)
    
    
# Question: Given a min heap, how would you find the kth smallest element without modifying the heap? Provide the element found by traversing the heap and maintaining its properties.
# Input: [1, 3, 6, 5, 9, 8], k = 3
# Output: 5

def heapifyup(arr , i , n):
    smallest = i
    left = 2*i +1
    right = 2*i +2
    
    if left < n and arr[i] < arr[smallest]:
        smallest = left
    if right < n and arr[i] < arr[smallest]:
        smallest = right
        
    if smallest != i:
        arr[i] , arr[smallest] = arr[smallest] , arr[i]
        heapifyup(arr , smallest , n)
        
    # return arr

def createminHeap(heap , n):
    n = len(arr)
    for i in range(n//2-1,-1,-1):
        heapifyup(heap , i , n)
        
def printHeap(n):
    for i in range(n):
        print(arr[i], end=" ")
        
def kthsmallest():
    print("kth smallest element",arr[-k])
        
arr = [1 ,3,6,5,9,8]
n = len(arr)
k = 3
createminHeap(arr , n)
printHeap(n)
print()
kthsmallest()


# Question: Find the deepest left leaf node in a binary tree, ensuring to consider all levels of the tree. Provide the value of the deepest left leaf node found.
# Input: root = [1, 2, 3, null, 4, 5, null, null, 6]
# Output: 6

class TreeNode:
    def __init__(self, data=0 , left = None , right = None):
        self.data = data
        self.left = left
        self.right = right
        
class BinaryTree:
    def __init__(self):
        self.root = None
        
    # def left_skeward(self , root):
    #     if root is None:
    #         return
    #     self.left_skeward(root.left)
    #     print(root.data ,end=" ")

    def levelorder(self , root):
        q = []
        q.append(root)
        while len(q) != 0:
            root = q.pop(0)
            print(root.data , end=" ")
            if root.left is not None:
                q.append(root.left)
            if root.right is not None:
                q.append(root.right) 
        
        
        
tree = BinaryTree()
root = TreeNode(1,
                TreeNode(2,
                         TreeNode(0),
                         TreeNode(4)),
                TreeNode(3,
                         TreeNode(5,
                                  TreeNode(0),
                                  TreeNode(6)),
                         TreeNode(0)))

# tree.left_skeward(root)
tree.levelorder(root)



# Question: Detect and remove a loop in a linked list, ensuring the list is fully traversed. Demonstrate the final structure of the list with the loop removed.
# Input: 1 -> 2 -> 3 -> 4 -> 5 -> 3 (loop back to 3)
# Output: 1 -> 2 -> 3 -> 4 -> 5
print( )

class Node:
    def __init__(self, data , next = None):
        self.data = data
        self.next = next
        
class Linkedlist:
    def __init__(self) -> None:
        self.head = None
        
    def detect_cycle(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next    
        if slow == fast:
            return True
        return False
    
    def display(self):
        current = self.head
        while current:
            print(current.data , end="-->")
            current = current.next
        
ll = Linkedlist()
ll.head = Node(1,Node(2,Node(3,Node(4,Node(5)))))
ll.head.next.next.next.next.next = ll.head.next.next  

cycle = ll.detect_cycle()
print(cycle)
ll.display()

# Question: Given a sorted array of unknown length where most elements are unique except one that appears twice, find the duplicate element. Ensure to use binary search techniques to achieve the result efficiently.
# Input: [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10]
# Output: 5


# class TreeNode:
#     def __init__(self, data=0 , left = None , right = None):
#         self.data = data
#         self.left = left
#         self.right = right
        
# class BinaryTree:
#     def __init__(self):
#         self.root = None
        
#     def insert(self , root , data):
#         if root is None:
#             return TreeNode(data)
#         if data < root.data:
#             root.left = self.insert(root.left , data)
#         else:
#             root.right = self.insert(root.right , data)
#         return root
    
#     def levelorder(self , root):
#         q = []
#         q.append(root)
#         while len(q) != 0:
#             root = q.pop(0)
#             print(root.data , end=" ")
#             if root.left is not None:
#                 q.append(root.left)
#             if root.right is not None:
#                 q.append(root.right)       
        
        
# tree = BinaryTree()
# root = TreeNode(1)
# tree.insert(root , 2)
# tree.insert(root , 3)
# tree.insert(root , 4)
# tree.insert(root , 5)
# tree.insert(root , 5)
# tree.insert(root , 6)
# tree.insert(root , 7)
# tree.insert(root , 8)
# tree.insert(root , 9)

# tree.levelorder(root)

        

        

        

    
            
    