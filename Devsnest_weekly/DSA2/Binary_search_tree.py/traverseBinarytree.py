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
        
    def traverse_preorder(self , root):
        if not root:
            return
        print(root.data , end= " ")
        self.traverse_preorder(root.left)
        self.traverse_preorder(root.right)
        
    def traverse_postorder(self , root):
        if not root:
            return
        self.traverse_postorder(root.left)
        self.traverse_postorder(root.right)
        print(root.data , end= " ")
        
    
    
tree = TreeNode(5)
tree.insert_recursivly(tree , 2)
tree.insert_recursivly(tree , 10)
tree.insert_recursivly(tree , 15)
tree.insert_recursivly(tree , 7)
tree.insert_recursivly(tree , 6)
tree.insert_recursivly(tree , 12)
tree.insert_recursivly(tree , 8)
tree.insert_recursivly(tree , 20)

    
print("inorder Traversal    --->")
tree.traverse_inorder(tree)

# print()
# print("pre order Traversal  --->")
# tree.traverse_preorder(tree)

# print()
# print("post order Traversal --->")
# tree.traverse_postorder(tree)

print()