""" COMPLETE BINARY TREE
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
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
# root.right.right = Node(6)

if isCompleteCBT(root) == True:
    print("Complete Binary Tree")
else:
    print("NOT Complete Binary Tree")        



# # A binary tree node has data, pointer to left child and a
# # pointer to right child
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
 
# # Given a binary tree, return true if the tree is complete
# # else false
# def isCompleteBT(root: Node) -> bool:
#     # Base Case: An empty tree is complete Binary Tree
#     if root is None:
#         return True
 
#     # Create an empty queue
#     q = []
#     q.append(root)
#     # Create a flag variable which will be set true
#     # when a non full node is seen
#     flag = False
 
#     # Do level order traversal using queue.
#     while len(q) != 0:
#         temp = q.pop(0)
 
#         if temp is None:
#             # If we have seen a NULL node, we set the flag
#             # to true
#             flag = True
#         else:
#             # If that NULL node is not the last node then
#             # return false
#             if flag:
#                 return False
#             # Push both nodes even if there are null
#             q.append(temp.left)
#             q.append(temp.right)
 
#     # If we reach here, then the tree is complete Binary
#     # Tree
#     return True
 
# # Helper function that allocates a new node with the
# # given data and NULL left and right pointers.
# def newNode(data: int) -> Node:
#     temp = Node(data)
#     return temp
 
# # Driver code
# if __name__ == '__main__':
#     # Let us construct the following Binary Tree which
#     # is not a complete Binary Tree
#     #        1
#     #       / \
#     #      2   3
#     #     / \   \
#     #    4   5   6
#     root = newNode(1)
#     root.left = newNode(2)
#     root.right = newNode(3)
#     root.left.left = newNode(4)
#     root.left.right = newNode(5)
#     root.right.right = newNode(6)

# #     root = Node(1)
# #     root.left = Node(2)
# #     root.right = Node(3)
# #     root.left.left = Node(4)
# #     root.left.right = Node(5)
# #     root.right.right = Node(6)
 
#     if isCompleteBT(root) == True:
#         print("Complete Binary Tree")
#     else:
#         print("NOT Complete Binary Tree")