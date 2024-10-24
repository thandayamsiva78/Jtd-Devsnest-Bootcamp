
""""full binary tree or not"""
class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.value = data
# def inorder(root):
#     if root:
#         inorder(root.left)
#         print(root.value,end=" ")
#         inorder(root.right)
def is_full_binarytree(node):
    if node is None:
        return True
    if node.left is None and node.right is None:
        return True
    if node.left is not None and node.right is not None:
        return is_full_binarytree(node.left) and is_full_binarytree(node.right)
    return False

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
# inorder(root)
print(is_full_binarytree(root))