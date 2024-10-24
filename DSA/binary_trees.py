
"""====================================BINARY TREES================================="""
# tree is a non linear data structure in which the elements are arranged in the form of hierarchical order
# and in which the elements are represented as nodes...

# Basic Tree Terminology : 

# node, root node, edge, parent, child, sibling, leaf, internal node, degree, level, height, depth, path, subtree

#                                    top
#                     A              -->      0-level
#                 /      \
#              B            C        -->      1-level
#           /     \
#        D           E               -->      2-level
#      /   \       /   \
#     F     G     H                  -->      3-level
#                                   bottom

# node = the elements of a tree is called nodes  Ex : A,B,C,D,E,F,G,H

# root node = the starting node is called as root node. or the node which not have a parent node 
            #   a tree have only one root node

# edge = the connection b/w the two nodes is called edges
        # no.of edges = ( no.of nodes - 1 )

# parent node = the node which is having branches or childrens from top to bottom is known as parent node
            # Ex : from the above ex. A is a parent of B,C 
                                    # B is a parent of D,E
                                    # D is a parent of F,G
                                    # E is a parent of H

# child node = the barnches of a parent is known as child node (or) the node which have a parent
            # Ex : B,C,D,E,F,G,H are the child nodes

# siblings = child nodes of a same parent is known as a siblings 
            # Ex : B-C , D-E , F-G are siblings

# leaf node = node which do not have a child node is called a leaf node
            # Ex : C,F,G,H are leaf nodes

# internal nodes = all the nodes except leaf nodes(or) node with child is know as internal nodes 
                # Ex : A,B,D,E are the internal nodes [it's similar to the parent nodes]

# degree = no.of child nodes represent the degree of node
        # Ex : degree of (A) = 2
            #  degree of (B) = 2
            #  degree of (D) = 2
            #  degree of (E) = 1
        # the highest degree among all nodes is called as the degree of tree
        # so, the degree of the tree is 2

# level = the no.of steps or no.of hierarchy is called as a level of tree
        #  level starts from  0
        #  for every step/hierarchy level will be increased by +1
            # the level of the given tree is 3

# height = the longest path from leaf node to the particular node is known as height of the node
            # Ex : the height of A : 3
                            #    B : 2
                            #    D,E : 1
            # the highest path is considered as the height of tree == 3

# depth = the longest path from the root node to the particular node is known as depth
            # Ex : the depth of (B) : 1
                #  the depth of (C) : 1
                #  the depth of (D) : 2
                #  the depth of (G) : 3
            # The highest depth is considered as the depth of tree == 3

# path = the sequences of nodes from source to the destination or a root to the leaf
        # Ex : path ( A - G ) = A -> B -> D -> G

# Sub-tree = the node with children is always forms a sub tree
#  Ex :
#  it is a sub tree
# (1)

#                    B     
#                /       \
#               D          E    
#            /    \      /   \
#           F      G    H 

# (2)

#       D
#     /   \
#   F       G

# --------------------------------------------------------------------------

# Intro to binary tree and the types of binary tree
# binary means ----> 2

# its defined as every node in a tree should have atmost 2 childrens/child nodes

# a tree can have 0 node, 1 node, 2 nodes is called a binary tree
# Ex. of binary tree
#                                    top
#                     A              -->      0-level
#                 /       \
#              B            C        -->      1-level
#           /     \
#        D           E               -->      2-level
#      /   \       /    \
#     F     G     H       I          -->      3-level
#                                   bottom

# Types of Binary tree : 
                    # 1.Full Binary tree / Strictly Binary tree
                    # 2.Almost Binary tree / Incomplete Binary tree
                    # 3.Complete Binary tree / Perfect Binary tree
                    # 4.Left skewed Binary tree
                    # 5.Right skewed Binary tree


# 1.Full Binary tree / Strictly Binary tree : 
# ------------------------------------------
#  Every node must have two childrens except the leaf nodes

# Ex 1 :  Not a full binary tree--->

#                           A               lev-0
#                       /       \
#                    B             C        lev-1
#                  /   \         /   \
#                D      E       F           lev-2

# in this c is having only one child ... so it is not considered as a full binary tree

# Ex 2 :  full binary tree--->

#                          A               lev-0
#                       /     \
#                    B           C         lev-1
#                 /     \
#               D        E                 lev-2
#            /    \
#          F        G                      lev-3 

# in this all the parents having the 2 child nodes .. so it is a full binary tree


# 2.Almost Binary tree / Incomplete Binary tree : 
# ------------------------------------------------

#  every node must have two childrens in all levels except in last level but filled from left to right

# Ex 1 :  Not a Incomplete binary tree--->

#                          A               lev-0
#                       /     \
#                    B           C         lev-1
#                 /     \
#               D        E                 lev-2
#            /    \
#          F        G                      lev-3 

# in this Ex... level-2 have an incomplete child nodes.. so it is not considered as a Incomplete binary tree

# Ex 2 :  Incomplete binary tree--->

#                           A                       lev-0
#                       /       \
#                    B             C                lev-1
#                 /    \         /   \
#               D       E       F      G            lev-2
#             /   \
#            H      I                               lev-3

# in this Ex... all levels have filled with 2 child nodes except last level.. so it is considered as a Incomplete binary tree


# 3.Complete Binary tree / Perfect Binary tree :
# ----------------------------------------------

#  every node must have two childrens in all the levels.
#  each level there must e 2^l nodes where l- level 

# Ex 1 :  Not a Perfect binary tree--->

#                           A                       lev-0  ----> 2^0 = 1 node --> satisfied
#                       /       \
#                    B             C                lev-1  ----> 2^1 = 2 node --> satisfied
#                 /    \         /    \
#               D        E      F       G           lev-2  ----> 2^2 = 4 node --> satisfied
#             /   \
#            H      I                               lev-3  ----> 2^3 = 8 node --> not satisfied


# in this Ex... all levels have filled with nodes except last level.. so it is not considered as a Perfect binary tree

# Ex 2 :  Perfect binary tree--->

#                                                A                                      lev-0  ----> 2^0 = 1 node --> satisfied
#                                       /                \
#                                B                               C                      lev-1  ----> 2^1 = 2 node --> satisfied
#                            /      \                        /       \
#                       D                E                F              G              lev-2  ----> 2^2 = 4 node --> satisfied
#                    /    \           /     \          /    \          /    \
#                 H          I      J         K      L        M       N       O         lev-3  ----> 2^3 = 8 node --> satisfied

# in this Ex... all levels have filled with all nodes.. so it is considered as a Perfect binary tree


# 4.Left skewed Binary tree :
# ---------------------------

# every node should have only left childs

#                         A
#                       /   \
#                     B
#                   /   \
#                 C
#               /   \
#             D


# 5.Right skewed Binary tree :
# ---------------------------

# every node should have only Right childs

#           A
#         /   \
#               B
#             /   \
#                   C
#                 /   \
#                       D

# --------------------------------------------------------------------------------------

# Binary Tree representation ----->

# Binary Tree can be represented in 2 ways :

            # ---> using in linear or sequencial way ( arrays )
            # ---> using list concept [ double linked list ]

# using arrays --->
# ---------------

# consider the root node at index 0
# left child is placed at 2#      
      
#                         A              lev-0

#                    B          C        lev-1

#                D      E                lev-2

#            G       H                   lev-3i+1 ; " i " is position of parent
# right child is placed at 2i+2 ; " i " is position of parent

# Ex : 
#              A
#            /   \
#           B     C

#   node       position
# -------     -----------
#     A             0
#                   ----> B is left child of A
#     B        2(0)+1=1     ----> the parent of B is A [ position is 0 ]
#                   ----> C is Right child of A
#     C        2(0)+2=2     ----> the parent of C is A [ position is 0 ]

# Array representation is --->
#           node  --->         [  A   B   C  ]
#           index --->            0   1   2

# Ex : 
#                         A
#                     /       \
#                  B             C
#               /    \         /  \
#            D               E
#          /   \           /   \
#        F               G

#   node       position
# -------     -----------
#     A             0
#                   ----> B is left child of A
#     B        2(0)+1=1     ----> the parent of B is A [ position is 0 ]
#                   ----> C is Right child of A
#     C        2(0)+2=2     ----> the parent of C is A [ position is 0 ]
#                   ----> D is left child of B
#     D        2(1)+1=3     ----> the parent of D is B [ position is 1 ]
#                   ----> E is Right child of B
#     E        2(1)+2=4     ----> the parent of E is B [ position is 1 ]
#                   ----> F is left child of D
#     F        2(3)+1=7     ----> the parent of F is A [ position is 3 ]
#                   ----> G is left child of E
#     G        2(4)+1=9     ----> the parent of C is A [ position is 4 ]


# Array representation is --->
#           node  --->         [  A   B   C   D   E   -   -   F   -   G  ]
#           index --->            0   1   2   3   4   5   6   7   8   9


# using list --->
# ---------------

# Double Linked-list for representing each node
#       we know that Double Linked-list have 3 parts 

#    _______________________________________________________
#    |                   |           |                     |
#    |  address of left  |    data   |   address of right  |
#    |       child       |           |      child          |
#    |___________________|___________|_____________________|   

# Ex : 
#                          A                       lev-0
#                      /        \
#                    B           C                 lev-1
#                 /    \        /   \
#               D       E     F       G            lev-2


#                           _____________
#                           |             |       |             |
#                           | (adrs of B) |   A   | (adrs of C) |                                  lev-0
#                           |____|__|_____|
#                                  /                      \
#                                 /                        \
#        ________/___      ____\_________
#        |             |     |             |      |             |       |             |
#        | (adrs of D) |  B  | (adrs of E) |      | (adrs of F) |   C   | (adrs of G) |            lev-1
#        |____|_|____|      |____|__|_____|
#                  /            \                        /                   \
#          __/__     _\__        __/__           __\__
#          |   |   |   |     |   |   |   |       |   |   |   |           |   |   |   |
#          | N | D | N |     | N | E | N |       | N | F | N |           | N | G | N |             lev-2
#          |_|_|_|     |_|_|_|       |_|_|_|           |_|_|_|

#       N = None ----> all the leaf nodes have the address of left and right nodes is None

# ------------------------------------------------------------------------------------------

# there are three types of tree traversals.....
                    # ---> in order                    EX :         A
                    # ---> pre order                              /   \
                    # ---> post order                            B     C

# in order   ---->    LEFT CHILD -- ROOT NODE -- RIGHT CHILD
                    # EX :  B A C

# pre order  ---->    ROOT NODE -- LEFT CHILD -- RIGHT CHILD
                    # EX :  A B C

# POST ORDER ---->    LEFT CHILD -- RIGHT CHILD -- ROOT NODE
                    # EX :  B C A


"""================================================================================================================================"""




""""full binary tree or not"""
# class Node:
#     def __init__(self,data):
#         self.left = None
#         self.right = None
#         self.value = data
# # def inorder(root):
# #     if root:
# #         inorder(root.left)
# #         print(root.value,end=" ")
# #         inorder(root.right)
# def is_full_binarytree(node):
#     if node is None:
#         return True
#     if node.left is None and node.right is None:
#         return False
#     if node.left is not None and node.right is not None:
#         return True
#     return False

# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right.left = Node(6)
# root.right.right = Node(7)
# # inorder(root)
# print(is_full_binarytree(root))

"""binary tree implementation"""
# creating Node

# class Node:
#     def __init__(self,value):
#         self.left = None
#         self.data = value
#         self.right = None

# class Tree:
#     def CreateNode(self,data):
#         return Node(data)
    
#     def Insert(self,node,data):
#         if node is None:
#             return self.CreateNode(data)
#         if data < node.data:
#             node.left = self.Insert(node.left,data)
#         else:
#             node.right = self.Insert(node.right,data)
#         return node

#     def traverse_inorder(self,root):
#         if root is not None:
#             self.traverse_inorder(root.left)
#             print(root.data)
#             self.traverse_inorder(root.right)
# tree = Tree()
# root = tree.CreateNode(5)
# # print(root.data)
# tree.Insert(root,2)
# tree.Insert(root,10)
# tree.Insert(root,7)
# tree.Insert(root,15)
# tree.Insert(root,12)
# tree.Insert(root,20)
# tree.Insert(root,30)
# tree.Insert(root,6)
# tree.Insert(root,8)
# tree.traverse_inorder(root)

"""BINARY TREE INSERTION"""
# class Node:
#     def __init__(self,data):
#         self.left = None
#         self.right = None
#         self.data = data
# def insert(root,data):
#     if root is None:
#         return Node(data)
#     else:
#         if data < root.data:
#             root.left = insert(root.left,data)
#         elif data > root.data:
#             root.right = insert(root.right,data)
#         # Handle duplicates (optional)
#         # else:
#         #     option 1 : Ignore Duplicates
#         #        PASS   
#         #     option 2 : Raise an Error
#         #        raise ValueError("DUPLICATE DATA FOUND")
#         return root
    
# def inorder(root):
#     if root is not None:
#         inorder(root.left)
#         print(root.data)
#         inorder(root.right)

# root = None
# root = insert(root,50)
# insert(root,30)
# insert(root,20)
# insert(root,40)
# insert(root,70)
# insert(root,60)
# insert(root,80)
# inorder(root)

# # class Node:
# #     def __init__(self,data):
# #         self.left = None
# #         self.right = None
# #         self.data = data

# # class createTree:
# #     def createNode(self,data):
# #         return Node(data)
# #     # inserting recursion methode

# #     def insert(self,node,data):
# #         if node is None:
# #             return self.createNode(data)
# #         if data < node.data:
# #             node.left = self.insert(node.left,data)
# #         else:
# #             node.right = self.insert(node.right,data)
# #         return node

# #     def traverse_inorder(self,root):
# #         if root is not None:
# #             self.traverse_inorder(root.left)
# #             print(root.data , end= " ")
# #             self.traverse_inorder(root.right)

# #     def traverse_preorder(self,root):
# #         if root is not None:
# #             print(root.data ,end= " ")
# #             self.traverse_preorder(root.left)
# #             self.traverse_preorder(root.right)

# #     def traverse_postorder(self,root):
# #         if root is not None:
# #             self.traverse_postorder(root.left)
# #             self.traverse_postorder(root.right)
# #             print(root.data, end=" ")

# #     def height(self,root):
# #         if root is None:
# #             return -1
# #         return max(self.height(root.left) ,self.height(root.right))+1
    
# # tree = createTree()
# # root = tree.createNode(5)
# # # print(root.data)
# # tree.insert(root,2)
# # tree.insert(root,10)
# # tree.insert(root,7)
# # tree.insert(root,15)
# # tree.insert(root,21)
# # tree.insert(root,20)
# # print("Inorder--->")
# # tree.traverse_inorder(root)
# # print()
# # print("preorder--->")
# # tree.traverse_preorder(root)
# # print()
# # print("Postorder-->")
# # tree.traverse_postorder(root)
# # print()
# # print("Tree Height--->")
# # print(tree.height(root))

# # """Level order"""
# class TreeNode:
#     def __init__(self,data):
#         self.data = data
#         self.left = None
#         self.right = None
# class Tree:
#     def createNode(self,data):
#         return TreeNode(data)
    
#     def insert(self,node,data):
#         if node is None:
#             return self.createNode(data)
#         if data < node.data:
#             node.left = self.insert(node.left , data)
#         else:
#             node.right = self.insert(node.right ,data)
#         return node
    
#     def levelOrder(self,root):
#         if root is None:
#             return
#         q = [root]
#         # q.append(root)
#         while len(q) != 0:
#             root = q.pop(0)
#             print(root.data , end=" ")
#             if root.left is not None:
#                 q.append(root.left)
#             if root.right is not None:
#                 q.append(root.right)
# tree = Tree()
# root = tree.createNode(5)
# tree.insert(root,3)
# tree.insert(root,2)
# tree.insert(root,9)
# tree.insert(root,10)
# tree.insert(root,7)
# tree.insert(root,4)
# tree.levelOrder(root)

"""========================================================================================================================"""
# INVERT BINARY TREE     OR    M(T)
            
    #          4                             4 
    #        /   \                         /   \
    #       /     \                       /     \
    #      2       7                     7       2
    #     / \     / \                   / \     / \      
    #    /   \   /   \                 /   \   /   \
    #   1     3  6    9                9    6  3    1




# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def invert_tree(root):
#     if root is None:
#         return None 
#     # Swap left and right children
#     root.left, root.right = root.right, root.left
#     invert_tree(root.left)
#     invert_tree(root.right)
#     return root

# root = TreeNode(4)
# root.left = TreeNode(2)
# root.right = TreeNode(7)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(3)
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(9)
# inverted_root = invert_tree(root)

# # Function to print tree level order traversal
# def level_order_traversal(root):
#     if not root:
#         return []
#     result = []
#     queue = [root]
#     while queue:
#         node = queue.pop()
#         result.append(node.val)
#         if node.left:
#             queue.append(node.left)
#         if node.right:
#             queue.append(node.right)
#     return result
# print("Level order traversal of the inverted tree:")

# print(level_order_traversal(inverted_root))




# SUM OF ROOT TO LEAF BINARY NUMBERS
        #          1           2|_4_                                2|6__
        #        /   \         2|_2_ REMINDER =0,0,1 B.N=1,0,0      2|_3__REMINDER=0,1,1 B.N=1,1,0
        #       /     \            1                                        1
        #      0       1
        #     / \     / \       2|_5_                               2|7__
        #    /   \   /   \      2|_2_ REMINDER=1,0,1                2|3__REMINDER=1,1,1
        #   0     1 0     1         1                                      1
                                # (1,0,0)+(1,0,1)+(0,1,1)+(1,1,1)=4+5+6+7=22



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumRootToLeaf(root):
    def dfs(node, current_sum):
        nonlocal total_sum
        if not node:
            return
        current_sum = (current_sum << 1) | node.val
        if not node.left and not node.right:
            total_sum += current_sum
            return
        dfs(node.left, current_sum)
        dfs(node.right, current_sum)
    
    total_sum = 0
    dfs(root, 0)
    return total_sum

root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(1)
root.left.left = TreeNode(0)
root.left.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(1)

# Calculate the sum of all root-to-leaf binary numbers
result = sumRootToLeaf(root)
print(result)




# Maximum Depth Of Binary Tree
# class TreeNode:
#     def _init_(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def maxDepth(root):
#     if not root:
#         return 0
#     left_depth = maxDepth(root.left)
#     right_depth = maxDepth(root.right)
#     return max(left_depth, right_depth) + 1

# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)

# result = maxDepth(root)
# print(result)  


## SYMMETRIC TREE
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def isSymmetric(root):
#     if not root:
#         return True
    
#     def isMirror(left, right):
#         if not left and not right:
#             return True
#         if not left or not right:
#             return False
#         return (left.val == right.val) and isMirror(left.left, right.right) and isMirror(left.right, right.left)
    
#     return isMirror(root.left, root.right)

# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(2)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(4)
# root.right.left = TreeNode(4)
# root.right.right = TreeNode(3)

# result = isSymmetric(root)
# print(result)
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# def printtree(root):
#     if not root:
#         return None
#     print(root.val)
#     printtree(root.left)
#     printtree(root.right)
# def inverttree(root):
#     if not root:
#         return None
#     root.left,root.right=root.right,root.left
#     inverttree(root.left)
#     inverttree(root.right)
#     return root
# root=TreeNode(4)
# nodeA=TreeNode(2)  
# nodeB=TreeNode(7)
# nodeC=TreeNode(1)
# nodeD=TreeNode(3)
# nodeE=TreeNode(6)
# nodeF=TreeNode(9)
# root.left=nodeA
# root.right=nodeB
# nodeA.left=nodeC
# nodeA.right=nodeD
# nodeB.left=nodeE
# nodeB.right=nodeF
# inverttree(root)
# printtree(root)


# [3:42 pm, 7/6/2024] Bhuvana_jtd: #--------------------sum of nodes---------------------------------#
# class TreeNode:
#     def _init_(self,data):
#         self.data=data
#         self.left=None
#         self.right=None
# def sumofnodes(node):
#     if not node:
#         return 0
#     return node.data+sumofnodes(node.left)+sumofnodes(node.right)
# root=TreeNode(23)
# nodeA=TreeNode(45)
# nodeB=TreeNode(78)
# nodeC=TreeNode(45)
# nodeD=TreeNode(78)
# nodeE=TreeNode(45)
# nodeF=TreeNode(78)
# root.left=nodeA
# root.right=nodeB
# nodeA.left=nodeC
# nodeA.right=nodeD
# nodeB.left=nodeE
# nodeB.right=nodeF 
# print(sumofnodes(root))


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def find_mode(root):
#     if not root:
#         return []

#     def in_order_traversal(node):
#         if not node:
#             return
#         in_order_traversal(node.left)
#         count[node.val] = count.get(node.val, 0) + 1
#         in_order_traversal(node.right)

#     count = {}
#     in_order_traversal(root)
    
#     max_freq = max(count.values())
#     return [key for key, val in count.items() if val == max_freq]

# # Helper function to insert a new node in the BST
# def insert_node(root, val):
#     if not root:
#         return TreeNode(val)
#     if val < root.val:
#         root.left = insert_node(root.left, val)
#     else:
#         root.right = insert_node(root.right, val)
#     return root

# # Example usage
# root = None
# values = [5, 3, 8, 3, 7, 8, 8, 2, 1]
# for value in values:
#     root = insert_node(root, value)

# modes = find_mode(root)
# print("Mode(s):", modes)

class Node:
    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end="-->")
            self.inorder(root.right)

    def preorder(self,root):
        if root:
            print(root.data , end="-->")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self,root):
        if root:
            self.preorder(root.left)
            self.preorder(root.right)
            print(root.data , end="-->")
# Constructing the tree
root = Node("A",
            Node("B",
                 Node("C"),
                 Node("D")),
            Node("F",
                 Node("G"),
                 Node("H")))

# Performing inorder traversal
print("Inorder --->")
root.inorder(root)
print()
print("preorder --->")
root.preorder(root)
print()
print("Postorder --->")
root.postorder(root)



