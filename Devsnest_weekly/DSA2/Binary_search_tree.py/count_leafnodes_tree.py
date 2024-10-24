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
                
    """Iterative Way using DFS"""
    
    def count_leaf_nodes(self, root):
        if root is None:
            return 0
        count = 0
        stack = [root]
        while stack:
            node = stack.pop(0)
            # Check if the node is a leaf node
            if node.left is None and node.right is None:
                count += 1
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        return count
    
    # def count_leafnodes(self, root):
    #     if root is None:
    #         return 0
    #     count = 0
    #     stack = []
    #     stack.append(root)
    #     while stack:
    #         root = stack.pop(0)
    #         count +=1
    #         if root.left is not None:
    #             stack.append(root.left)
    #         if root.right is not None:
    #             stack.append(root.right)
    #     leaf = count // 2
    #     return count - leaf
    
    """Recursive way"""
    def leaf_nodes(self , root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        return self.leaf_nodes(root.left) + self.leaf_nodes(root.right)


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
print("Iterative way")
print(tree.leaf_nodes(root))
print("Recursive way")
print(tree.leaf_nodes(root))

# print(tree.count_leafnodes(root))




        