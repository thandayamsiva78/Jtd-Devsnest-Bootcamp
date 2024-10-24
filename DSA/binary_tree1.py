# creating simple tree   ---->  TREE NODE CLASS
# class TreeNode:
#     def __init__(self,val) -> None:
#         self.val = val
#         self.left = self.right = None

# a = TreeNode(1)
# b = TreeNode(2)
# c = TreeNode(3)

# a.left , a.right = b , c
# print(a.val , a.left.val , a.right.val)
#---------------------------------------------------------------------------------------------------------------------------
# ---> Traversal  1. recursive(stack) called as DFS  
#                 2. iterative (queue)called as BFS

# from collections import deque

# #--------> creating simple tree   ---->  TREE NODE CLASS
# class TreeNode:
#     def __init__(self,val , left = None , right = None) -> None:
#         self.val = val
#         self.left = left
#         self.right = right

# def postorder(root):
#     if root== None:
#         return
#     postorder(root.left)
#     postorder(root.right)
#     print(root.val, end= "-")

# def inorder(root):
#     if root == None:
#         return
#     inorder(root.left)
#     print(root.val, end= "-")
#     inorder(root.right)

# def preorder(root):
#     if root == None:
#         return
#     print(root.val , end= "-")
#     preorder(root.left)
#     preorder(root.right)

# def levelorder(root):
#     if not root:
#         return
#     queue = deque([root])
#     while queue:
#         ele = queue.pop()
#         print(ele.val)
#         if ele.left:
#             queue.appendleft(ele.left)
#         if ele.right:
#             queue.appendleft(ele.right)

# def levelorder2(root):
#     if not root:
#         return
#     queue = deque([None ,root])
#     while queue:
#         el = queue.pop()
#         if el:
#             print(el.val)
#             if el.left:
#                 queue.appendleft(el.left)
#             if el.right:
#                 queue.appendleft(el.right)
#         else:
#             print("-")
#             if queue:
#                 queue.appendleft(None)
# ####--------> Constructing root tree type 1

# # root = TreeNode("A",
# #                 TreeNode("B",
# #                         TreeNode("D"),
# #                         TreeNode("E")),
# #                 TreeNode("C",
# #                         TreeNode("F",
# #                                 TreeNode("H"),
# #                                 TreeNode("I")),
# #                         TreeNode("G")))

# ####--------> Constructing root tree type 1
# root = TreeNode("A")
# root.left = TreeNode('B')
# root.right = TreeNode("C")
# root.left.left = TreeNode("D")
# root.left.right = TreeNode("E")
# root.right.left = TreeNode("F")
# root.right.right = TreeNode("G")
# root.right.left.left = TreeNode("H")
# root.right.left.right = TreeNode("I")
# print("postorder --> ")
# postorder(root)
# print()
# print("inorder -->")
# inorder(root)
# print()
# print("preorder -->")
# preorder(root)
# print("level order -->")
# levelorder(root)
# print("levelorder2 -->")
# levelorder2(root)
"""=============================================================================================================================================================="""
'''Inserting a Binaryy tree in Level order'''
# #         Before                  Ofter Inserting 12
# #           10                        10
# #         /   \                     /    \
# #        11    9                    11     9
# #       /    /  \                 /  \   /  \
# #      7    15   8               7   12 15   8

# class Node:
#     def __init__(self ,data) -> None:
#         self.val = data
#         self.left = None
#         self.right = None
  
# def inorder(root):
#     if not root:
#         return
#     inorder(root.left)
#     print(root.val , end= " ")
#     inorder(root.right)
    
# def insert(root, key):
#     if root is None:
#         root = Node(key)
#         return
#     q = []
#     q.append(root)
#     while len(q) > 0:
#         root = q.pop(0)
#         print(root.val)
        
#         if root.left is None:
#             root.left = Node(key)
#             break
#         else:
#             q.append(root.left)
#         if root.right is None:
#             root.right = Node(key)
#             break
#         else:
#             q.append(root.right)
            
# root = Node(10)
# root.left = Node(11)
# root.left.left = Node(7)
# root.right = Node(9)
# root.right.left = Node(15)
# root.right.right = Node(8)

# print("Inorder traversal before insertion --->", end= " ")
# inorder(root)
# key = 12
# insert(root , key)
# print()
# print("Inorder  traversal ofter insertion -->" , end= " ")
# inorder(root)
        
"""=============================================================================================================================================================="""
""" LEFT SKEWARD AND RIGHT SKEWARD BINARY  TREE"""
"""  LEFT SKEWARD BINARY SEARCH TREE"""
# class Node:
#     def __init__(self , data) -> None:
#         self.val = data
#         self.left = None
# class BinarySearchTree:
#     def __init__(self):
#         self.root = None

#     def insert(self, key):
#         if self.root is None:
#             self.root = Node(key)
#         else:
#             self._insert(self.root, key)

#     def _insert(self, root_node, key):
#         if key < root_node.val:
#             if root_node.left is None:
#                 root_node.left = Node(key)
#             else:
#                 self._insert(root_node.left, key)
#         # No right insertions to keep it left-skewed

#     def inorder_traversal(self, root):
#         if root is None:
#             return
#         self.inorder_traversal(root.left)
#         print(root.val, end=' ') # -----------------

# # Example usage
# bst = BinarySearchTree()

# # Insert nodes to form a left-skewed binary tree
# bst.insert(5)
# bst.insert(3)
# bst.insert(2)
# bst.insert(1)

# # Inorder traversal to display the tree structure
# bst.inorder_traversal(bst.root)  # Output: 1 2 3 5

"""RIGHT SKEWARD BINARY SEARCHH TREE"""
# class Node:
#     def __init__(self , data) -> None:
#         self.val = data
#         self.right = None
# class BinarySearchTree:
#     def __init__(self):
#         self.root = None

#     def insert(self, key):
#         if self.root is None:
#             self.root = Node(key)
#         else:
#             self._insert(self.root, key)

#     def _insert(self, root_node, key):
#         if key > root_node.val:
#             if root_node.right is None:
#                 root_node.right = Node(key)
#             else:
#                 self._insert(root_node.right, key)
#         # Since it's right-skewed, we don't need to handle left insertion

#     def inorder_traversal(self, root):
#         if root is None:
#             return
#         print(root.val, end=' ') #----------------------------
#         self.inorder_traversal(root.right)
        

# # Example usage
# bst = BinarySearchTree()

# # Insert nodes to form a right-skewed binary tree
# bst.insert(1)
# bst.insert(2)
# bst.insert(3)
# bst.insert(4)

# # Inorder traversal to display the tree structure
# bst.inorder_traversal(bst.root)  # Output: 1 2 3 4

"""=============================================================================================================================================================="""

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
# from collections import deque
# ## TREE NODE  Class
# class TreeNode:
#     def __init__(self , data) -> None:
#         self.data = data
#         self.left = self.right = None

# ## BINARY TREE Class
# class BinaryTree:
#     def CreateNode(self ,data) -> None:
#         return TreeNode(data)

#     def insert_recursivley(self, node , data):
#         if node is None:
#             return self.CreateNode(data)
#         if data < node.data :
#             node.left = self.insert_recursivley(node.left , data)
#         else:
#             node.right = self.insert_recursivley(node.right , data)
#         return node
    
#     def traverse_inorder(self, root):
#         if root is not None:
#             self.traverse_inorder(root.left)
#             print(root.data)
#             self.traverse_inorder(root.right)

#     def levelorder(self,root):
#         if not root:
#             return
#         queue = deque([root])
#         while queue:
#             ele = queue.pop()
#             print(ele.data)
#             if ele.left:
#                 queue.appendleft(ele.left)
#             if ele.right:
#                 queue.appendleft(ele.right)


#     def levelorder2(self ,root):
#         if not root:
#             return
#         queue = deque([None ,root])
#         while queue:
#             el = queue.pop()
#             if el:
#                 print(el.data)
#                 if el.left:
#                     queue.appendleft(el.left)
#                 if el.right:
#                     queue.appendleft(el.right)
#             else:
#                 print("-")
#                 if queue:
#                     queue.appendleft(None)

#     def sum1(self, root):
#         if root is None:
#             return 0
#         return root.data + self.sum1(root.left) + self.sum1(root.right)
#     def count(self,root):
#         if root is None:
#             return 0
#         return 1 + self.count(root.left) + self.count(root.right)
# tree = BinaryTree()
# root= tree.CreateNode(10)
# tree.insert_recursivley(root, 5)
# tree.insert_recursivley(root, 15)
# tree.insert_recursivley(root, 20)
# tree.insert_recursivley(root, 8)
# tree.insert_recursivley(root, 30)
# tree.insert_recursivley(root, 45)
# tree.insert_recursivley(root, 19)
# print("Inorder --->")
# tree.traverse_inorder(root)
# print("Level order --->")
# tree.levelorder(root)
# print("Levelorder 2 --->")
# tree.levelorder2(root)
# print("SUM of the tree Node --->")
# print(tree.sum1(root))
# print("COunt the tree Nodes--->")
# print(tree.count(root))


####-------------------------------------------PROBLEMS---------------------------------------------------------------
####---------- Symmetric Tree
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

# class BinaryTree:
#     def is_symmetric(self, left, right):
#         if not left and not right:
#             return True
#         if not left or not right:
#             return False
#         if left.data != right.data:
#             return False
#         return self.is_symmetric(left.left, right.right) and self.is_symmetric(left.right, right.left)

#     def solve(self, root):
#         if not root:
#             return True
#         return self.is_symmetric(root.left, root.right)
# # Example usage:
# # Create a symmetric tree
# #         1
# #       /   \
# #      2     2
# #     / \   / \
# #    3   4 4   3

# root = Node(1)
# root.left = Node(2)
# root.right = Node(2)
# root.left.left = Node(3)
# root.left.right = Node(4)
# root.right.left = Node(4)
# root.right.right = Node(3)
# tree = BinaryTree()
# # print(tree.isSymmetric(root))  # Output: True
# print(tree.solve(root))
""""============================================================================================================================================"""
###----------------------------------------------------------------------------------------------------------------------------------------------
"""Question 2: Implement a function to perform a level order traversal on a binary tree.

Input: 	Binary Tree:
        1
       / \
      2   3
     / \   \
    4   5   6
Output: Level order traversal: [1, 2, 3, 4, 5, 6]"""

# from collections import deque

# class TreeNode:
#     def __init__(self , data ) -> None:
#         self.data = data
#         self.left = None
#         self.right = None


# def leverorder(root):
#     if not root:
#         return
#     queue = deque([root])
#     while queue:
#         ele = queue.pop()
#         if ele.data %2 != 0:
#             print(ele.data , end= ' ')
#         if ele.left is not None:
#             queue.appendleft(ele.left)
#         if ele.right is not None:
#             queue.appendleft(ele.right)
    
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# root.right.right = TreeNode(6)
# print("Level order traversal  ---->")
# leverorder(root)

"""Question 3: Implement a function to convert a binary tree to its mirror tree.

Input:   Binary Tree:
               4
       	      / \
      		 2   7
            / \ / \
           1  3 6  9


Output:    Mirror Tree:
        4
       / \
      7   2
     / \ / \
    9  6 3  1
    """
# from collections import deque

# class TreeNode:
#     def __init__(self , data ) -> None:
#         self.data = data
#         self.left = None
#         self.right = None

# def inorder(root):
#     if root:
#         inorder(root.left)
#         print(root.data , end= " ")
#         inorder(root.right)

# def mirror(root):
#     if root is None:
#         return
#     root.left , root.right = root.right , root.left
#     mirror(root.left)
#     mirror(root.right)
#     return root

# def leverorder(root):
#     if not root:
#         return
#     queue = deque([root])
#     while queue:
#         ele = queue.pop()
#         print(ele.data , end= ' ')
#         if ele.left is not None:
#             queue.appendleft(ele.left)
#         if ele.right is not None:
#             queue.appendleft(ele.right)
    
# root = TreeNode(4)
# root.left = TreeNode(2)
# root.right = TreeNode(7)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(3)
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(9)
# print('Before  Normal Tree --- Inorder Traversal--->')
# inorder(root)
# mirror(root)
# print()
# print("Ofter change Mirror Tree--->")
# leverorder(root)


"""Question 1: Question 1: Implement a function to find the lowest common ancestor (LCA) of two nodes in a binary tree.

Input: Binary Tree:
        3
       / \
      5   1
     / \ / \
    6  2 0  8
      / \
     7   4

Nodes: 5, 1

Output:  LCA: 3
The LCA of 5 and 1 is 6
The LCA of nodes 5 and 2 is 5 , since a node can be a descendant of itself accordingly to the LCA defination


"""
# class TreeNode:
#     def __init__(self , data  , left = None , right = None) -> None:
#         self.data = data
#         self.left = left
#         self.right = right

# def lowest_common_ancestor(root ,node1 , node2):
#     if not root or root == node1 or root == node2:
#         return root
#     left = lowest_common_ancestor(root.left , node1 , node2)
#     right = lowest_common_ancestor(root.right , node1 , node2)
#     if left and right :
#         return root.data
#     return left if left else right

# root = TreeNode(3)
# root.left = TreeNode(5)
# root.right = TreeNode(1)
# root.left.left = TreeNode(6)
# root.left.right = TreeNode(2)
# root.right.left = TreeNode(0)
# root.right.right = TreeNode(8)
# root.left.right.left = TreeNode(7)
# root.left.right.right = TreeNode(4)

# p = root.left
# q = root.right
# lca = lowest_common_ancestor(root ,p , q)
# print(lca)


"""Question 4: Implement a function to check if a given binary tree is a min-heap.

Input: Binary tree:
              1
 		     / \
            3   6
           / \ / \
          5  9 8 10


Output: Is min-heap: False"""


"""=============================================================================================================================="""


# total 8 session of 2-3 hours
# linked lists - 1
# binary trees - 1
# binary search trees - 1
# heaps -1
# graphs - 2/3
# backtracking - 1
# dp/string pattern searching - 1 (0 if graphs takes 3)

"""TOP VIEW BINARY TREE"""
# class TreeNode:
#     def __init__(self, data ) -> None:
#         self.data = data
#         self.left = None
#         self.right = None
#         self.level = None
        
# class BinaryTree:
#     def createNode(self,data):
#         return  TreeNode(data)
        
#     def insert(self, root_node , data):
#         if root_node is None:
#             return self.createNode(data)
#         if data < root_node.data:
#             root_node.left = self.insert(root_node.left , data)
#         if data > root_node.data:
#             root_node.right = self.insert(root_node.right , data)
#         return root_node
    
#     def traverse_inorder(self, root):
#         if root:
#             self.traverse_inorder(root.left)
#             print(root.data , end= " ")
#             self.traverse_inorder(root.right)
            
#     def levelOrder(self, root):
#         if root is None:
#             return
#         q = []
#         q.append(root)
#         while len(q) > 0:
#             current = q.pop(0)
#             print(current.data , end= " ")
#             if current.left is not None:
#                 q.append(current.left)
#             if current.right is not None:
#                 q.append(current.right)
                
#     def Topview(self,root):
#         q = []
#         dic = dict()
#         root.level = 0
#         q.append(root)
#         while len(q) != 0:
#             root = q.pop(0)
#             if root.level not in dic:
#                 dic[root.level] = root.data
#             if root.left is not None:
#                 q.append(root.left)
#                 root.left.level = root.level -1
#             if root.right is not None:
#                 q.append(root.right)
#                 root.right.level = root.level +1
#         print(*sorted(dic.values()))
                
# tree = BinaryTree()
# root = tree.createNode(5)
# tree.insert(root , 20)
# tree.insert(root , 15)
# tree.insert(root , 25)
# tree.insert(root , 13)
# tree.insert(root , 45)
# tree.insert(root , 8)
# tree.traverse_inorder(root)
# print()
# tree.levelOrder(root)
# print()
# tree.Topview(root)

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def find_leaf_nodes(root):
#     if not root:
#         return []
#     if not root.left and not root.right:
#         return [root.val]  # Only return the value
#     leaves = []
#     if root.left:
#         leaves.extend(find_leaf_nodes(root.left))
#     if root.right:
#         leaves.extend(find_leaf_nodes(root.right))
#     return leaves

# def are_similar_leaf_nodes(root1, root2):
#     # Find leaf nodes of both trees
#     leaves1 = find_leaf_nodes(root1)
#     leaves2 = find_leaf_nodes(root2)

#     # Sort the leaf nodes to ensure they can be compared
#     leaves1.sort()
#     leaves2.sort()

#     # Compare the leaf nodes
#     return 1 if leaves1 == leaves2 else 0

# # Example usage:
# root1 = TreeNode(10,
#                 TreeNode(5, TreeNode(3, TreeNode(2)), TreeNode(7)),
#                 TreeNode(20, TreeNode(15, None, TreeNode(18)), TreeNode(25)))

# root2 = TreeNode(10,
#                 TreeNode(5, TreeNode(3, TreeNode(2)), TreeNode(7)),
#                 TreeNode(20, TreeNode(15, None, TreeNode(18)), TreeNode(25)))

# # root1 and root2 have the same leaf nodes: [2, 7, 18, 25]
# print(are_similar_leaf_nodes(root1, root2))  # Output: 1

# root3 = TreeNode(10,
#                 TreeNode(5, TreeNode(3, TreeNode(2)), TreeNode(8)),
#                 TreeNode(20, TreeNode(15, None, TreeNode(18)), TreeNode(25)))

# # root1 and root3 do not have the same leaf nodes: root3 has leaf nodes [2, 8, 18, 25]
# print(are_similar_leaf_nodes(root1, root3))  # Output: 0

""" COMPLETE BINARY TREE"""


# A binary tree node has data, pointer to left child and a
# pointer to right child
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
# Given a binary tree, return true if the tree is complete
# else false
def isCompleteBT(root: Node) -> bool:
    # Base Case: An empty tree is complete Binary Tree
    if root is None:
        return True
 
    # Create an empty queue
    q = []
    q.append(root)
    # Create a flag variable which will be set true
    # when a non full node is seen
    flag = False
 
    # Do level order traversal using queue.
    while len(q) != 0:
        temp = q.pop(0)
 
        if temp is None:
            # If we have seen a NULL node, we set the flag
            # to true
            flag = True
        else:
            # If that NULL node is not the last node then
            # return false
            if flag:
                return False
            # Push both nodes even if there are null
            q.append(temp.left)
            q.append(temp.right)
 
    # If we reach here, then the tree is complete Binary
    # Tree
    return True
 
# Helper function that allocates a new node with the
# given data and NULL left and right pointers.
def newNode(data: int) -> Node:
    temp = Node(data)
    return temp
 
# Driver code
if __name__ == '__main__':
    # Let us construct the following Binary Tree which
    # is not a complete Binary Tree
    #        1
    #       / \
    #      2   3
    #     / \   \
    #    4   5   6
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
    root.right.right = newNode(6)

#     root = Node(1)
#     root.left = Node(2)
#     root.right = Node(3)
#     root.left.left = Node(4)
#     root.left.right = Node(5)
#     root.right.right = Node(6)
 
    if isCompleteBT(root) == True:
        print("Complete Binary Tree")
    else:
        print("NOT Complete Binary Tree")
 

