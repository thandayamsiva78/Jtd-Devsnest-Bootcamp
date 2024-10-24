# from collections import deque
# class TreeNode:
#     def __init__(self ,data ,left =None ,right=None) -> None:
#         self.data =data
#         self.left = left
#         self.right = right
        
# class BinaryTree:
#     def __init__(self) -> None:
#         self.head = None
    
#     def levelorder(self,root):
#         queue = deque()
#         queue.append(root)
#         while len(queue) !=0:
#             ele = queue.popleft()
#             print(ele.data,end=" ")
#             if ele.left is not None:
#                 queue.append(ele.left)
#             if ele.right is not None:
#                 queue.append(ele.right)
                
#     def sum_ofoddeven(self):
#         current = self.head
#         even = []
#         odd = []
#         while current:
#             if current.data % 2 == 0:
#                 even.append(current.data)
#             else:
#                 odd.append(current.data)
#         print(even)
#         print(odd)
        
# tree = BinaryTree()
# tree.head = TreeNode(10,
#                      TreeNode(20,
#                               TreeNode(40),
#                               TreeNode(60)),
#                      TreeNode(30))
# tree.levelorder(tree.head)
# tree.sum_ofoddeven()
            
        
        
        

        