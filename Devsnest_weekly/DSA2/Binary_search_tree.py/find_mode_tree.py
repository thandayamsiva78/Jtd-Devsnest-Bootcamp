class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_mode(root):
    if not root:
        return []

    def in_order_traversal(node):
        if not node:
            return
        in_order_traversal(node.left)
        count[node.val] = count.get(node.val, 0) + 1
        in_order_traversal(node.right)

    count = {}
    in_order_traversal(root)
    
    max_freq = max(count.values())
    return [key for key, val in count.items() if val == max_freq]

# Helper function to insert a new node in the BST
def insert_node(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_node(root.left, val)
    else:
        root.right = insert_node(root.right, val)
    return root

# Example usage
root = None
values = [5, 3, 8, 3, 7, 8, 8, 2, 1]
for value in values:
    root = insert_node(root, value)

modes = find_mode(root)
print("Mode(s):", modes)