""" COMPLETE BINARY TREE   & Min heap
A binary tree is complete is all levels are fully filled except possibly for the last level 
which is filled from left to right"""

class Node:
    def __init__(self, data , left = None , right = None):
        self.data = data
        self.left = left
        self.right = right
        
def isCompleteCBT(root):
    if root is None:
        return True
    q = []
    q.append(root)
    flag = False
    while len(q) != 0:
        temp = q.pop(0)
        if temp is None:
            flag = True
        else:
            if flag:
                return False
            q.append(temp.left)
            q.append(temp.right)
    return True

def minheap(root):
    if root is None:
        return True
    if root.left and root.left.data < root.data:
        return False
    if root.right and root.right.data < root.data:
        return False
    return minheap(root.left) and minheap(root.right)

def isMinHeap(root):
    return isCompleteCBT(root) and minheap(root)

# Example usage
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
# root.right.right = Node(6)

if isMinHeap(root):
    print("Min heap")
else:
    print("Not a Min heap")
    
    
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# # root.right.right = Node(6)

# if isCompleteCBT(root) == minheap(root):
#     print("Min heap")
# else:
#     print("Not a Min heap") 
    
# # print(minheap(root))
    