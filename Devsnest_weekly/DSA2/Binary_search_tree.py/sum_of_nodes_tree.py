class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def sumofnodes(node):
    if not node:
        return 0
    return node.data+sumofnodes(node.left)+sumofnodes(node.right)
root=TreeNode(23)
nodeA=TreeNode(45)
nodeB=TreeNode(78)
nodeC=TreeNode(45)
nodeD=TreeNode(78)
nodeE=TreeNode(45)
nodeF=TreeNode(78)
root.left=nodeA
root.right=nodeB
nodeA.left=nodeC
nodeA.right=nodeD
nodeB.left=nodeE
nodeB.right=nodeF 
print(sumofnodes(root))