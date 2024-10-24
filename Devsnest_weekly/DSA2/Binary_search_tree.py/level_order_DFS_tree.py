"""Level order Traversal"""
# using queues without import
class TreeNode:
    def __init__(self, data , left = None , right = None):
        self.data = data
        self.left = left
        self.right = right
        
class BinaryTree:
    def __init__(self) -> None:
        self.root = None
        
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

tree.level_order(root)


print()
# using queues with import  deque()
from collections import deque
class TreeNode:
    def __init__(self, data , left = None , right = None):
        self.data = data
        self.left = left
        self.right = right
        
class BinaryTree:
    def __init__(self) -> None:
        self.root = None
        
    def level_order(self ,root):
        queue = deque()
        queue.append(root)
        while len(queue) != 0:
            root = queue.popleft()
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

tree.level_order(root)





