"""construct a program that checks if all the numbers are unique in a sentence."""
# def uniqueue_distinict(l1):
#     if len(l1) == len(set(l1)):
#         return True
#     return False
# l1 = [6,8,9,11] # true
# l1 = [6,6,8,8,9,11] # False
# print(uniqueue_distinict(l1))
"""what can the 'is' operator do ? """
# # the is operator can compare the id of the two objects.
# list1 = [1,2,3]
# list2 = [1,2,3]

# list3 = list1
# list1 = list2 # True
# list1 is list2 # False
# list1 == list3 # True

""" why do you use break statement ?"""
# you can use the break statement to terminate the current loop's excution.

""" what is the pass statement ?"""
# when there's syntactic, the pass statement is used. it is not used there's an operational requirment.
""" How can random numbers be generated in python ?"""
# ## generate a rondom float between 0 and 1.
# import random
# random_num = random.random()
# print(random_num)
# ## generate a rondom integer within a specified range.
# import random
# random_num = random.randint(1,10)
# print(random_num)
# ## generate a rondom  float values
# import random
# random_num = random.uniform(1.5,2.10)
# print(random_num)
# ## generate a rondom random element in a list
# import random
# list1 = [12,2,3,33,23]
# rand_ele = random.choice(list1)
# print(rand_ele)
# ## Gernerate a multiple random elements from a list without replace
# import random
# list1 = [12,122,3,33,23]
# without_replace = random.sample(list1,2)
# print(without_replace)
# list1 = [12,122,3,33,23]
# with_replace = [random.choice(list1) for _ in range(3)]
# print(with_replace)

# def solve(n, prices):
#     if not prices or n <= 1:
#         return 0
    
#     min_price = prices[0]
#     max_profit = 0
    
#     for i in range(1, n):
#         # Update the minimum price seen so far
#         min_price = min(min_price, prices[i])
#         # Calculate the potential profit at current day and update max_profit if greater
#         max_profit = max(max_profit, prices[i] - min_price)
    
#     return max_profit

# arr = [1,2,3,4,5]
# n = len(arr)
# data = [[]]
# for i in range(n):
#     for j in range(i,n):
#         subarray = arr[i:j+1]
#         data.append(subarray)
# print(data)
# subarry_products =[]
# for subarray in data:
#     subarry_product =1
#     for num in subarray:
#         subarry_product*=num
#     subarry_products.append(subarry_product)
# print(subarry_product)
# arr = [6,1,2,12,3,4,5]
# max_num = arr[0]
# for i in arr:
#     if i > max_num:
#         max_num = i
# print(max_num)

# arr = [6,1,2,12,3,4,5,0]
# min_val = arr[0]
# for i in arr:
#     if i < min_val:
#         min_val = i
# print(min_val)


# arr = "aviS"
# data = []
# for i in range(len(arr)-1,-1,-1):
#     data.append(arr[i])
# print(''.join(data))


# class Node:
#     def __init__(self,data) -> None:
#         self.data = data
#         self.next = None
# class Linkedlist:
#     def __init__(self) -> None:
#         self.head = None

#     def display(self):
#         temp = self.head
#         while temp:
#             print(temp.data,end=" --> ")
#             temp = temp.next
#         print("null")
#     # inserng at begening
#     def insert_at_beg(self,data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node
#     # inserting at ending
#     def inserting_at_end(self,data):
#         new_node = Node(data)
#         temp = self.head
#         while temp.next:
#             temp =temp.next
#         temp.next = new_node
#     # inserting at specified position
#     def insert_at_pos(self,pos,data):
#         new_node = Node(data)
#         temp = self.head
#         for i in range(pos-1):
#             temp = temp.next
#         new_node.next = temp.next
#         temp.next = new_node
#     # delete at front
#     def delete_at_front(self):
#         # self.head = self.head.next
#         # or
#         temp = self.head
#         self.head = self.head.next
#         temp.next = None
#     def delete_at_end(self):
#         temp = self.head
#         while temp.next.next != None:
#             temp = temp.next
#         temp.next = None

# ll = Linkedlist()

# n1 = Node(10)
# n2 = Node(20)
# n3 = Node(30)
# n4 = Node(40)

# ll.head = n1
# n1.next = n2
# n2.next = n3
# n3.next = n4

# ll.insert_at_beg(0)
# ll.inserting_at_end(100)
# ll.insert_at_pos(3,25)
# ll.delete_at_front()
# ll.delete_at_end()

# ll.display()


# class Node:
#     def __init__(self,data,next = None) -> None:
#         self.data = data
#         self.next = next

# class LinkedList:
#     def __init__(self) -> None:
#         self.head = None
    
#     def display(self):
#         temp = self.head
#         while temp:
#             print(temp.data,end="-->")
#             temp = temp.next
#     def insert_at_beg(self,data):
#         new_node = Node(data)  # creating NEW_NODE
#         new_node.next = self.head
#         self.head = new_node

#     def insert_at_end(self,data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return 
#         temp = self.head
#         while temp.next: # find the last node
#              temp = temp.next
#         # ofter finding last node then update current(new_node)
#         temp.next = new_node 
#     def insert_at_pos(self,pos,data):
#         new_node = Node(data)
#         temp = self.head
#         for i in range(pos-1):
#             temp = temp.next
#             new_node.next = temp.next
#         temp.next = new_node

#     def delete_front(self):
#         if self.head is None:
#             return "Empty"
#         self.head = self.head.next
#     def delete_end(self):
#         temp = self.head
#         while temp.next.next is not None:
#             temp = temp.next
#         temp.next = None
#     # def reverse(self):
#     #     prev = None
#     #     curr = self.head
#     #     while curr:
            
# ll = LinkedList()

# ll.head = Node(10,Node(20,Node(30,Node(40))))
# ll.insert_at_beg(5)
# ll.insert_at_end(50)
# ll.insert_at_pos(2,25)
# ll.delete_front()
# ll.delete_end()
# ll.reverse()
# ll.display()

# arr = [1,2,3,4,5,6,7]
# min_val = arr[0]
# for i in arr:
#     if i < min_val:
#         min_val = i
# print(min_val)


# arr = [8,4,3,1,6,5]
# max_val = arr[0]
# i = 0
# while i < len(arr):
#     if arr[i] > max_val:
#         max_val = arr[i]
#     i+=1
# print(max_val)

# arr = [12,11,5]
# print(arr[len(arr)//2])

"""kth largest element"""
        # num_sort = sorted(nums)
        # second_large = num_sort[-k]
        # return second_large
        # nums.sort()
        # nums = nums[::-1]
        # return nums[k-1]


# def merge(arr1,arr2):
#     merge_sorted = []
#     i,j = 0,0
#     while i < len(arr1) and j < len(arr2):
#         if arr1[i] < arr2[j]:
#             merge_sorted.append(arr1[i])
#             i+=1
#         else:
#             merge_sorted.append(arr2[j])
#             j+=1
#     while i < len(arr1):
#         merge_sorted.append(arr1[i])
#         i+=1
#     while j < len(arr2):
#         merge_sorted.append(arr1[i])
#         j+=1
#     return merge_sorted
# list1 = [1,3,5,7,9,11]
# list2 = [2,4,6,8]
# print(merge(list1,list2))

# class Node:
#     def _init_(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class SingleLinkedList:
#     def _init_(self):
#         self.head = None

#     def insert(self, val):
#         new_node = Node(val)
#         if not self.head:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = new_node

#     def display(self):
#         current = self.head
#         while current:
#             print(current.val, end=" -> " if current.next else "\n")
#             current = current.next

#     def remove_nth_from_end(self, n):
#         dummy = Node(0)
#         dummy.next = self.head
#         first = dummy
#         second = dummy
        
#         # Advance the first pointer n + 1 times
#         for _ in range(n + 1):
#             if first is None:
#                 raise ValueError("n is larger than the number of nodes in the list")
#             first = first.next

#         # Move both pointers until first reaches the end
#         while first:
#             first = first.next
#             second = second.next

#         # Remove the n-th node from the end
#         second.next = second.next.next

#         # Update the head of the list
#         self.head = dummy.next

# # Example usage
# sll = SingleLinkedList()
# sll.insert(1)
# sll.insert(2)
# sll.insert(3)
# sll.insert(4)
# sll.insert(5)
# sll.insert(6)
# sll.display()  # Linked List: 1 -> 2 -> 3 -> 4 -> 5 -> 6
# sll.remove_nth_from_end(2)
# sll.display()  # Linked List: 1 -> 2 -> 3 -> 4 -> 6


"""====================================================================================================="""

# class Node:
#     def __init__(self,data,next = None) -> None:
#         self.data = data
#         self.next = next
# class LinkedList:
#     def __init__(self) -> None:
#         self.head = None

#     def display(self):
#         temp = self.head
#         while temp:
#             print(temp.data,end="-->")
#             temp = temp.next
#     def inseting_at_beg(self,data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node
#     def insert_at_end(self,data):
#         new_node = Node(data)
#         temp = self.head
#         while temp.next:
#             temp = temp.next
#         temp.next = new_node
#     def insert_at_pos(self,pos,data):
#         new_node = Node(data)
#         temp = self.head
#         for _ in range(pos-1):
#             temp = temp.next
#         new_node.next = temp.next
#         temp.next = new_node

#     def delete_front(self):
#         if self.head is None:
#             print("Empty")
#             return 
#         self.head = self.head.next
#     def delete_end(self):
#         if self.head is None:
#             print("Empty")
#             return 
#         temp = self.head
#         while temp.next.next is not None: 
#             temp = temp.next
#         temp.next = None
#     def delete_pos(self,data):
#         # if self.head is None:
#         #     print("Empty")
#         #     return 
#         # temp = self.head
#         # for _ in range(pos-1):
#         #     temp = temp.next
#         # temp.next = temp.next.next
#         if self.head is None:
#             print("Empty")
#             return
#         if self.head.data == data:
#             self.head = self.head.next
#             return
#         temp = self.head
#         while temp.next and temp.next.data != data:
#             temp = temp.next
#         if temp.next:
#             temp.next = temp.next.next
#     def length(self):
#         count = 0
#         temp = self.head
#         while temp:
#             count += 1
#             temp = temp.next
#         print("length of LinkedList",count)
#     def check(self,data):
#         temp = self.head
#         while temp:
#             if temp.data == data:
#                 print("Data found")
#                 return
#             temp = temp.next
#         print("Data not found")
#     def sum_ll(self):
#         count = 0
#         sum = 0
#         temp = self.head
#         if temp is None:
#             print("Empty")
#         while temp:
#             sum+=temp.data
#             count += 1
#             temp = temp.next
#         print(sum)
#         print(count)
#     def product(self):
#         prod = 1
#         temp = self.head
#         while temp:
#             prod*=temp.data
#             temp = temp.next
#         print(prod)
#     def divisbel3(self):
#         temp = self.head
#         my_list = []
#         while temp:
#             if temp.data % 3 == 0:
#                 my_list.append(temp.data)
#             temp = temp.next
#         print(my_list)
#     # def even_odd(self):
#     #     temp = self.head
#     #     even_count = 0
#     #     odd_count = 0
#     #     even = []
#     #     odd = []
#     #     while temp:
#     #         if temp.data % 2 == 0:
#     #             even.append(temp.data)
#     #             even_count+=1
#     #         else:
#     #             odd.append(temp.data)
#     #             odd_count+=1
#     #     print(even, even_count)
#     #     print(odd, odd)
#     def reverse(self):
#         prev = None
#         current = self.head
#         while current:
#             next_node = current.next
#             current.next = prev
#             prev = current
#             current = next_node
#         self.head = prev

# ll = LinkedList()
# ll.head = Node(10,Node(20,Node(30,Node(40,Node(50,Node(60,Node(70)))))))
# ll.inseting_at_beg(5)
# ll.insert_at_end(80)
# ll.insert_at_pos(5,45)
# ll.delete_front()
# ll.delete_end()
# ll.delete_pos(45)
# ll.length()
# ll.check(60)
# ll.sum_ll()
# ll.product()
# ll.divisbel3()
# # ll.even_odd()
# # ll.reverse()
# ll.display()
"""============================================================================================================"""
# class Node:
#     def __init__(self,data,next = None) -> None:
#         self.data = data
#         self.next = next
# class LinkedList:
#     def __init__(self) -> None:
#         self.head = None

#     def display(self):
#         temp = self.head
#         while temp:
#             print(temp.data,end="-->")
#             temp = temp.next

    
#     def remove_nth_from_end(self, n):
#         # step 3 : Use a dummy node to handle edge cases
#         dummy = Node(0)
#         dummy.next = self.head
#         first = dummy
#         second = dummy
        
#         # step 4: Move the fist pointer n+1 steps ahead
#         for _ in range(n + 1):
#             if first is None:
#                 raise ValueError("n is larger than the number of nodes in the list")
#             first = first.next

#         #step 5 : Move both pointers until the first pointer reaches the end
#         while first:
#             first = first.next
#             second = second.next

#         # step 6: Remove the n-th node from the end
#         second.next = second.next.next

#         # Update the head of the list
#         # self.head = dummy
#         return dummy.next

# ll = LinkedList()
# ll.head = Node(10,Node(20,Node(30,Node(40,Node(50)))))
# ll.remove_nth_from_end(2)
# ll.display()
        
# from collections import deque
# def max_subarray(arr,k):
#     n=len(arr)
#     if n*k==0:
#         return []
#     if k==1:
#         return arr
#     def clean_deque(i):
#         if deq and deq[0]==i-k:
#             deq.popleft()
#         while deq and arr[i]>arr[deq[-1]]:
#             deq.pop()
#     deq=deque()
#     max_idx=0
#     for i in range(k):
#         clean_deque(i)
#         deq.append(i)
#         if arr[i]>arr[max_idx]:
#             max_idx=i
#     output=[arr[max_idx]]
#     for i in range(k,n):
#         clean_deque(i)
#         deq.append(i)
#         output.append(arr[deq[0]])
#     return output
# arr=[8,5,10,7,9,4,15,12,90,13]
# k=3
# print(max_subarray(arr,k))

# def armstrong(nums,k):
#     data = []
#     for i in nums:
#         square = int(i)**k
#         data.append(square)
#         sum_data = sum(data)
#     if nums == str(sum_data):
#         return True
#     else:
#         return False
# nums = "371"
# k = len(nums)
# print(armstrong(nums,k))

# def palidrome(nums):
#     if nums  == nums[::-1]:
#         return True
#     return False
# nums = "madam"
# print(palidrome(nums))


# rows = 5
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     for j in range(i-1,0,-1):
#         print(j,end="")
#     print()

# def solve(n):
#     # CODE HERE
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print(j,end="")
#         for j in range(i-1,0,-1):
#             print(j,end="")
#         print(end=" ")
#     return()
"""========================================================================================================================"""

# class Node:
#     def __init__(self,data):
#         self.left = None
#         self.right = None
#         self.data = data

# class createTree:
#     def createNode(self,data):
#         return Node(data)
#     # inserting recursion methode
#     def insert(self,node,data):
#         if node is None:
#             return self.createNode(data)
#         if data < node.data:
#             node.left = self.insert(node.left,data)
#         else:
#             node.right = self.insert(node.right,data)
#         return node

#     def traverse_inorder(self,root):
#         if root is not None:
#             self.traverse_inorder(root.left)
#             print(root.data , end= " ")
#             self.traverse_inorder(root.right)

#     def traverse_preorder(self,root):
#         if root is not None:
#             print(root.data ,end= " ")
#             self.traverse_preorder(root.left)
#             self.traverse_preorder(root.right)

#     def traverse_postorder(self,root):
#         if root is not None:
#             self.traverse_postorder(root.left)
#             self.traverse_postorder(root.right)
#             print(root.data, end=" ")

#     def height(self,root):
#         if root is None:
#             return -1
#         return max(self.height(root.left) ,self.height(root.right))+1
    
# tree = createTree()
# root = tree.createNode(5)
# # print(root.data)
# tree.insert(root,2)
# tree.insert(root,10)
# tree.insert(root,7)
# tree.insert(root,15)
# tree.insert(root,21)
# tree.insert(root,20)
# print("Inorder--->")
# tree.traverse_inorder(root)
# print()
# print("preorder--->")
# tree.traverse_preorder(root)
# print()
# print("Postorder-->")
# tree.traverse_postorder(root)
# print()
# print("Tree Height--->")
# print(tree.height(root))

"""=========================================================================================================================="""

"""Inserting Binary Tree"""

# class Node:
#     def __init__(self,data):
#         self.left = None
#         self.right = None
#         self.data = data
# def traverse_preorder(root):
#     if root is not None:
#         print(root.data ,end= " ")
#         traverse_preorder(root.left)
#         traverse_preorder(root.right)
# def height(root):
#         if root is None:
#             return -1
#         return max(height(root.left),height(root.right))+1
# class createTree:
#     # inserting iterative methode
#     def __init__(self):
#         self.root = None
#     def insert(self,data):
#         if self.root is None:
#             self.root = Node(data)
#             return
#         root = self.root
#         while True:
#             if data < root.data:
#                 if root.left is not None:
#                     root = root.left
#                 else:
#                     root.left = Node(data)
#                     break
#             elif data > root.data:
#                 if root.right is not None:
#                     root = root.right
#                 else:
#                     root.right = Node(data)
#                     break
        
# tree = createTree()
# tree.insert(2)
# tree.insert(5)
# tree.insert(10)
# tree.insert(4)
# tree.insert(3)
# tree.insert(15)
# traverse_preorder(tree.root)
# print()
# print("Height --->")
# print(height(tree.root))

# class TreeNode:
#     def __init__(self,data):
#         self.data = data
#         self.left = None
#         self.right = None
# class Tree:
#     def createNode(self,data):
#         return TreeNode(data)
    
#     def insert(self,node,data):
#         if node is None:
#             return self.createNode(data)
#         if data < node.data:
#             node.left = self.insert(node.left , data)
#         else:
#             node.right = self.insert(node.right ,data)
#         return node

#     def height(self,root):
#         if root is None:
#                 return  0
#         return max(self.height(root.left), self.height(root.right)) +1
    
#     def postorder(self,root):
#         if root is not None:
#             self.postorder(root.left)
#             self.postorder(root.right)
#             print(root.data , end= " ")

#     def preorder(self,root):
#         if root is not None:
#             print(root.data , end= " ")
#             self.preorder(root.left)
#             self.preorder(root.right)

#     def inorder(self,root):
#             if root is not None:
#                 self.inorder(root.left)
#                 print(root.data ,end= ' ')
#                 self.inorder(root.right)


#     def levelOrder(self,root):
#         if root is None:
#             return
#         q = []
#         q.append(root)
#         while len(q) != 0:
#             root = q.pop(0)
#             print(root.data , end=" ")
#             if root.left is not None:
#                 q.append(root.left)
#             if root.right is not None:
#                 q.append(root.right)
                
# tree = Tree()
# root = tree.createNode(5)
# tree.insert(root,3)
# tree.insert(root,2)
# tree.insert(root,9)
# tree.insert(root,10)
# tree.insert(root,7)
# tree.insert(root,4)
# print("Inorder")
# tree.inorder(root)
# print("preorder")
# tree.preorder(root)
# print("postorder")
# tree.postorder(root)
# print("hight")
# print(tree.height(root))
# tree.levelOrder(root)

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def find_leaf_nodes(root):
#     if not root:
#         return []
#     if not root.left and not root.right:
#         return [root.val]  # Only return the value
#     leaves = []
    
#     if root.left:
#         leaves.extend(find_leaf_nodes(root.left))
#     if root.right:
#         leaves.extend(find_leaf_nodes(root.right))
#     return leaves
    

# def are_similar_leaf_nodes(root1, root2):
#     # Find leaf nodes of both trees
#     leaves1 = find_leaf_nodes(root1)
#     leaves2 = find_leaf_nodes(root2)

#     # Sort the leaf nodes to ensure they can be compared
#     leaves1.sort()
#     leaves2.sort()

#     # Compare the leaf nodes
#     return 1 if leaves1 == leaves2 else 0

# # Example usage:
# root1 = TreeNode(10,
#                 TreeNode(5, TreeNode(3, TreeNode(2)), TreeNode(7)),
#                 TreeNode(20, TreeNode(15, None, TreeNode(18)), TreeNode(25)))

# root2 = TreeNode(10,
#                 TreeNode(5, TreeNode(3, TreeNode(2)), TreeNode(7)),
#                 TreeNode(20, TreeNode(15, None, TreeNode(18)), TreeNode(25)))

# # root1 and root2 have the same leaf nodes: [2, 7, 18, 25]
# print(are_similar_leaf_nodes(root1, root2))  # Output: 1

# # root3 = TreeNode(10,
# #                 TreeNode(5, TreeNode(3, TreeNode(2)), TreeNode(8)),
# #                 TreeNode(20, TreeNode(15, None, TreeNode(18)), TreeNode(25)))

# # # root1 and root3 do not have the same leaf nodes: root3 has leaf nodes [2, 8, 18, 25]
# # print(are_similar_leaf_nodes(root1, root3))  # Output: 0


# arr = [[1,4,2], [8,3,6],[5,9,7], [15,12,34]]
# a=[]
# for i in arr:
#         for j in i:
#                 a.append(j)
# my_list = a
# # print(type(my_list))
# N = len(my_list)
# for k in range(N):
#         for s in range(k+1 , N):
#                 if my_list[k] > my_list[s]:
#                         my_list[k] , my_list[s] = my_list[s] , my_list[k]
# print(my_list)

# from collections import deque

# d = deque()
# def enqueue(item):
#     d.append(item)
# def dequeue():
#     if not d:
#         return
#     else:
#         a = d.popleft()
#         print(a)
# enqueue(10)
# enqueue(20)
# enqueue(30)
# enqueue(40)
# d.append(10)
# d.appendleft(2000)
# d.appendleft(5005)
# d.append(400)
# dequeue()
# print(d)

# def validorNot(s):
#         stack = [] # {
#         brackets = {")":"(" , "]":"[" , "}":"{"}
#         for char in s: # }
#                 if char in brackets: # }
#                         if stack and stack[-1] != brackets[char]:#  { }
#                                 stack.pop()
#                         else:
#                                 stack.append(char)
#         if stack == []:
#                 return True
#         else:
#                 return False
# s = "{}()()"
# print(validorNot(s))

# def isvalid(s):
#         stack = []
#         brackets ={')':'(',']':'[','}':'{'}
#         for char in s:
#                 if char in brackets.values():
#                         stack.append(char)
#                 else:
#                         if stack and stack[-1] == brackets[char]:
#                                 stack.pop()
#                         else:
#                                 return False
#         return len(stack) == 0
# s = "{[())]}"
# result = isvalid(s)
# print(result)


class TreeNode:
    def __init__(self, data , left = None , right = None):
        self.data = data
        self.left = left
        self.right = right
        
        
class BinaryTree:
    def __init__(self) -> None:
        self.root = None
        
        def mirrorTree(root):
                if root is None:
                        return 0
                if root.left and root.right:
                        root.left , root.right = root.right , root.left
                mirrorTree(root.left) and mirrorTree(root.right)
                
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


