"""TOP VIEW BINARY TREE"""
class TreeNode:
    def __init__(self, data ) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.level = None
        
class BinaryTree:
    def createNode(self,data):
        return  TreeNode(data)
        
    def insert(self, root_node , data):
        if root_node is None:
            return self.createNode(data)
        if data < root_node.data:
            root_node.left = self.insert(root_node.left , data)
        if data > root_node.data:
            root_node.right = self.insert(root_node.right , data)
        return root_node
    
    def traverse_inorder(self, root):
        if root:
            self.traverse_inorder(root.left)
            print(root.data , end= " ")
            self.traverse_inorder(root.right)
            
    def levelOrder(self, root):
        if root is None:
            return
        q = []
        q.append(root)
        while len(q) > 0:
            current = q.pop(0)
            print(current.data , end= " ")
            if current.left is not None:
                q.append(current.left)
            if current.right is not None:
                q.append(current.right)
                
    def Topview(self,root):
        q = []
        dic = dict()
        root.level = 0
        q.append(root)
        while len(q) != 0:
            root = q.pop(0)
            if root.level not in dic:
                dic[root.level] = root.data
            if root.left is not None:
                q.append(root.left)
                root.left.level = root.level -1
            if root.right is not None:
                q.append(root.right)
                root.right.level = root.level +1
        print(dic)
        print(*sorted(dic.values()))
                
tree = BinaryTree()
root = tree.createNode(5)
tree.insert(root , 20)
tree.insert(root , 15)
tree.insert(root , 25)
tree.insert(root , 13)
tree.insert(root , 45)
tree.insert(root , 8)
tree.traverse_inorder(root)
print()
tree.levelOrder(root)
print()
tree.Topview(root)