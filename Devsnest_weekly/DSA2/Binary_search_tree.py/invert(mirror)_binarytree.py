# INVERT BINARY TREE     OR    M(T)
            
    #          4                             4 
    #        /   \                         /   \
    #       /     \                       /     \
    #      2       7                     7       2
    #     / \     / \                   / \     / \      
    #    /   \   /   \                 /   \   /   \
    #   1     3  6    9                9    6  3    1
    
    

class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
# def printtree(root):
#     if not root:
#         return None
#     print(root.val)
#     printtree(root.left)
#     printtree(root.right)

def inverttree(root):
    if not root:
        return None
    root.left,root.right=root.right,root.left
    inverttree(root.left)
    inverttree(root.right)
    return root

def levelorder(root):
    q = [root]
    while len(q) != 0:
        root = q.pop(0)
        print(root.data , end= " ")
        if root.left is not None:
            q.append(root.left)
        if root.right is not None:
            q.append(root.right)


root = TreeNode(1,
                TreeNode(2,
                         TreeNode(4),
                         TreeNode(5)),
                TreeNode(3,
                         TreeNode(6),
                         TreeNode(7,
                                  TreeNode(8),
                                  TreeNode(9))))
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
print("Before tree--->")
levelorder(root)
print()
print("Ofter Mirror Tree--->")
inverttree(root)
levelorder(root)
# printtree(root)

print()


class TreeNode:
    def __init__(self, data , left = None , right = None):
        self.data = data
        self.left = left
        self.right = right
        
        
class BinaryTree:
    def __init__(self) -> None:
        self.root = None
        
    def mirrorTree(self ,root):
        if root is None:
                return
        if root.left and root.right:
                root.left , root.right = root.right , root.left
        self.mirrorTree(root.left) and self.mirrorTree(root.right)
        return root
            
    def level_order(self ,root):
        queue = []
        queue.append(root)
        while len(queue) != 0:
            root = queue.pop(0)
            print(root.data , end=" ")
            if root.left is not None:
                queue.append(root.left)
            if root.right is not None:
                queue.append(root.right)
    
    
tree = BinaryTree()
root = TreeNode(1,
                TreeNode(2,
                         TreeNode(4),
                         TreeNode(5)),
                TreeNode(3,
                         TreeNode(6),
                         TreeNode(7,
                                  TreeNode(8),
                                  TreeNode(9))))

print("Before tree --->")
tree.level_order(root)

print()
print("Ofter Mirror Tree --->")
tree.mirrorTree(root)
tree.level_order(root)

