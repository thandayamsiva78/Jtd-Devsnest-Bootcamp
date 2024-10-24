# Heaps
# What is Heap data dtructure ?
# A Complete binary tree in which the value node is either greaterthan , lesserthan or equal to values in child node is called a Heap
# -- Ther are two kind of heaps
# 1. MinHeap : 
# In a minheap , the value of each parent node is lessthan or equal to the values of its children .
# The smallest element (eich the lowest values) is always positionaid at the root (index 0)

# 2. MaxHeap :
# Conversely , in maxheap , the values of each parent node is greater than or equal to the values of its children . 

"""  MAX HEAP"""
# def heapifydown(arr , i):
#     n = len(arr)
#     while i < n:
#         l , r = (2*i) + 1 , (2*i) + 2
#         max_idx = l if l < n and arr[l] > arr[i] else i
#         max_idx =  r if r < n and  arr[r] > arr[max_idx] else max_idx
#         if max_idx == i:
#             break
#         arr[max_idx] , arr[i] = arr[i] , arr[max_idx]       

# def createheap(arr):
#     for  i in range(len(arr)//2-1 , -1 ,-1): # 4 ,3 ,2 ,1 ,0
#         heapifydown(arr , i)
#     print("Heap :" , arr)
    
# arr = [ 1,3,5,4,6,13,10,9,8,15,17]
# createheap(arr)

# def maxheapify(arr , i ,n):
#     while i <= n:
#         l = 2*i +1
#         r = 2*i +2
#         largest = l if l < n and arr[l] > arr[i] else i
#         largest = r if r < n and arr[r] > arr[largest] else largest
#         if largest == i:
#             return None
#         arr[largest] , arr[i] = arr[i] , arr[largest]
#         maxheapify(arr , largest , n)
#         # print(arr)
# def create_heap(arr , n):
#     for i in range(0, n-1):
#         maxheapify(arr , i , n)
#     print(arr)
    
# arr = [ 1,3,5,4,6,13,10,9,8,15,17]
# n = len(arr)
# create_heap(arr , n)

"""MAX HEAP --------------------------------------------------------------------------------------------------------"""
# def heapify_down(heap , i , N):
#     # heap : The list representing the min-heap
#     # i : The index of the root nodeof the subtree
#     largest = i  # Initialize largest as root
#     left = 2*i + 1
#     right = 2*i + 2
#     # check if left child is smaller
#     if left < N and heap[left] > heap[largest]:
#         largest = left  
#     # check is right side is smaller
#     if right < N and heap[right] > heap[largest]:
#         largest = right
#     # Swap element with the smaller child if necessary
#     if largest != i:
#         heap[i] , heap[largest] = heap[largest] , heap[i]
#         heapify_down(heap , largest , N)

# def create_heap(heap):
#     """ Convert a list into a min heap using bottom-up heap construction"""
#     """heap : The list to be converted into a min-heap"""
#     # len(heap)//2-1 ---> Get INDEX OF non-leaf nodes 
#     for i in range(len(heap)//2-1 , -1, -1): # 4 , 3 , 2 ,1 , 0
#         heapify_down(heap , i ,N)

# def printHeap(N):
#     for i in range(N):
#         print(arr[i] , end= ' ')
        
# arr = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
# N = len(arr)
# create_heap(arr)
# # print(arr)
# printHeap(N)


def heapify_down(arr , i ,N):
    largest = i  # 29
    l = (2*i)+1 # 7 ,     5
    r = (2*i)+2 # None    6 
    
    if l < N and arr[l] > arr[largest]: # 7 < 8 and  30 > 15  --> 5 < 8 and 6 > 9 false :
        largest = l # 7
    if r < N and arr[r] > arr[largest]: # 6 < 8 and 29 > 9 True:
        largest = r # 29
        
    if largest != i: # 29 != 9 
        arr[i] , arr[largest] = arr[largest] , arr[i] 
        heapify_down(arr , largest , N)

def createHeap(arr):
    for i in range(N//2-1 , -1 ,-1):
        heapify_down(arr , i , N)
        
def printHeap(N):
    for i in range(N):
        print(arr[i], end= " ")

def bubbleSort(arr):
    for i in range(N):
        for j in range(i+1 , N):
            if arr[i] < arr[j]:
                arr[i] , arr[j] = arr[j] , arr[i]
    return arr
        
def kth_largest(arr):
    k = 2
    # for i in range(k):
    #   print(arr[i] , end= " ")
    print(arr[k-1])
            
arr = [100, 50, 80, 10, 25, 20, 75]

N = len(arr)
createHeap(arr)
print("MAX -heap --->")
printHeap(N)
print()
print("Sorted array--->")
print(bubbleSort(arr))
kth_largest(arr)

# def bubbleSort(arr):
#     for i in range(N):
#         for j in range(i+1 , N):
#             if arr[i] < arr[j]:
#                 arr[i] , arr[j] = arr[j] , arr[i]
#     arr.sort(reverse = True)
#     return arr
# arr = [-8414,1064, 0,-6601, -2320 ,-9766, 4211 ,3129 ,-3541, 8120, -7270 ,-7015 ,5518, -2775 ,6426 ,-494 ,-27]
# N = len(arr)
# print(bubbleSort(arr))

    
"""-----------------------------------------------------------------------------------------------------------------------------"""


# class TreeNode:
#     def  __init__(self , data = 0 , left =None , right = None):
#         self.data = data
#         self.left = left
#         self.right = right
        
# def is_minHeap(root):
#     if not root:
#         return
#     q = [root]
#     # q.append(root)
#     is_complete = True
#     while q:
#         node = q.pop(0)
#         if node.left:
#             if  root.left.data > root.data :
#                 return False
#             if not is_complete:
#                 return False
#             q.append(root.left)
#         if node.right:
#             if  root.right.data > root.data :
#                 return False
#             if not is_complete:
#                 return False
#             q.append(root.right)
#     return True
    
# root = TreeNode(50,
#                 TreeNode(30,
#                          TreeNode(20,
#                                   TreeNode(15),
#                                   TreeNode(12)),
#                          TreeNode(10)),
#                 TreeNode(40,
#                          TreeNode(25),
#                          TreeNode(35)))

# print(is_minHeap(root))

# def heapify_down(arr , i ,N):
#     largest = i
#     l = (2*i)+1
#     r = (2*i)+2
    
#     if l < N and arr[l] > arr[largest]:
#         largest = l
#     if l < N and arr[r] > arr[largest]:
#         largest = r
        
#     if largest != i:
#         arr[i] , arr[largest] = arr[largest] , arr[i]
#         heapify_down(arr , largest , N)

# def createHeap(arr):
#     for i in range(N//2-1 , -1 ,-1):
#         heapify_down(arr , i , N)
        
# def printHeap(N):
#     for i in range(N):
#         print(arr[i], end= " ")
        
# arr = [12 , 3 , 9 , 15 , 24, 6, 29 , 30]
# N = len(arr)
# createHeap(arr)
# printHeap(arr)

"""BT is MIn heap or Not ? """
# class Node:
#     def __init__(self , data , left = None , right = None):
#         self.data = data
#         self.left = left
#         self.right = right
        
# def is_minHeap(root):
#     if root is None:
#         return  True
#     if root.left is None and root.right is None:
#         return True
#     if root.left and root.data > root.left.data:
#         return False
#     if root.right and root.data > root.right.data:
#         return False
#     return is_minHeap(root.left) and is_minHeap(root.right)

# root = Node(10,
#             Node(20,
#                  Node(40),
#                  Node(50)),
#             Node(30,
#                  Node(60),
#                  Node(60)))

# if is_minHeap(root):
#     print("The tree is a min-heap")
# else:
#     print("The tree is not a min-heap")