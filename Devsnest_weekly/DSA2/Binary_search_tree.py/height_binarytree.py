class TreeNode:
    def __init__(self, data , left = None , right = None):
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
        
    def height_of_tree(self, root):
        if root is None: # Base Condition
            return -1
        left = self.height_of_tree(root.left)
        right = self.height_of_tree(root.right)
        return 1 + max(left , right)
    
tree = BinaryTree()
root = TreeNode(1,
                TreeNode(2,
                         TreeNode(4),
                         TreeNode(5)),
                TreeNode(3,
                         TreeNode(6),
                         TreeNode(7,
                                  TreeNode(80),
                                  TreeNode(90))))
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)

height = tree.height_of_tree(root)
print("Height of Tree is:" , height)
tree.traverse_inorder(root)

print()