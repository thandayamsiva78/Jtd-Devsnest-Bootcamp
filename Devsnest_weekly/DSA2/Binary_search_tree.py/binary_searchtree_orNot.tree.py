"""Simple approach    BST [ left < root < right]"""  
# Inorder traversal so our condition is the tree is sorted order it is True otherwise False

class TreeNode:
    def __init__(self, data , left = None , right = None):
        self.data = data
        self.left = left
        self.right = right
        
def isBibarySearch_untill(root , values):
    if root is None:
        return
    isBibarySearch_untill(root.left , values)
    values.append(root.data)
    isBibarySearch_untill(root.right , values)
    
def isBibarySearch(root):
    values = []
    isBibarySearch_untill(root , values)
    
    for i in range(len(values)- 1):
        if values[i] >= values[i+1]:
            return False
    return True

    
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(2)
root.left.right = TreeNode(6)
root.right.left = TreeNode(12)
root.right.right = TreeNode(20)

print(isBibarySearch(root))

