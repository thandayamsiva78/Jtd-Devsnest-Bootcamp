
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def preorder(root):
    if not root:
        return
    print(root.val,end=" ")
    preorder(root.left)
    preorder(root.right) 
    
            
def mergeTrees(root1,root2):
    if root1 and root2:
        root = TreeNode(root1.val + root2.val)
        root.left = mergeTrees(root1.left , root2.left)
        root.right = mergeTrees(root1.right , root2.right)
        return root
    else:
        return root1 or root2  
    

root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.right = TreeNode(2)
root1.left.left = TreeNode(5)

root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(3)
root2.left.right = TreeNode(4)
root2.right.right = TreeNode(7) 
root=mergeTrees(root1,root2)
# print("level order:")
# levelorder(root) 
# print()
print("preorder:") 
preorder(root)