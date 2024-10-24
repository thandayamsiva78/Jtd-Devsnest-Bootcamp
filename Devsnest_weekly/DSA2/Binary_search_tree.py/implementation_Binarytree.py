"""Create Binary  Tree"""
class TreeNode:
    def __init__(self , data ,left = None , right = None):
        self.data = data
        self.left = left
        self.right = right
        
class BinaryTree:
    def __init__(self):
        self.root = None
            
    def traverse_inorder(self ,root):
        if root is None:
            return
        self.traverse_inorder(root.left)
        print(root.data , end=" ")
        self.traverse_inorder(root.right)

tree = BinaryTree()

root = TreeNode(1,
                TreeNode(2,
                         TreeNode(4),
                         TreeNode(5)),
                TreeNode(3,
                         TreeNode(6),
                         TreeNode(7)))
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(7)

tree.traverse_inorder(root)

print()

"""Create Binary Seaarch Tree"""
"""Iterative way"""
class TreeNode:
    def __init__(self , data ,left = None , right = None):
        self.data = data
        self.left = left
        self.right = right
        
class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert_nodes(self , value):
        new_node = TreeNode(value)
        if self.root is None:
            self.root = new_node
            return

        current = self.root
        while True:
            if value < current.data:
                if current.left is None:
                    current.left = new_node
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    break
                current = current.right
            
    def traverse_inorder(self ,root):
        if root is None:
            return
        self.traverse_inorder(root.left)
        print(root.data , end=" ")
        self.traverse_inorder(root.right)

tree = BinaryTree()
tree.insert_nodes(5)
tree.insert_nodes(10)
tree.insert_nodes(3)
tree.insert_nodes(9)
tree.insert_nodes(16)
tree.insert_nodes(25)
tree.insert_nodes(30)

tree.traverse_inorder(tree.root)

print()
"""Recursion Way"""

class TreeNode:
    def __init__(self , data ,left = None , right = None):
        self.data = data
        self.left = left
        self.right = right
        
    def insert_recursivly(self , root , value):
        if root is None:
            return TreeNode(value)
        if value < root.data:
            root.left = self.insert_recursivly(root.left , value)
        else:
            root.right = self.insert_recursivly(root.right , value)
        return root
    
    def traverse_inorder(self ,root):
        if root is None:
            return
        self.traverse_inorder(root.left)
        print(root.data , end=" ")
        self.traverse_inorder(root.right)
    
tree = TreeNode(5)
tree.insert_recursivly(tree , 10)
tree.insert_recursivly(tree , 3)
tree.insert_recursivly(tree , 9)
tree.insert_recursivly(tree , 16)
tree.insert_recursivly(tree , 25)
tree.insert_recursivly(tree , 30)
    
tree.traverse_inorder(tree)