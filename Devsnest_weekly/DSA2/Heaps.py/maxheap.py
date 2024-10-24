# Max Heap Creation Process
# Identify Non-Leaf Nodes: In a complete binary tree represented as an array, non-leaf nodes are those indices that have children. These indices range from len(heap)//2 - 1 to 0.

# Heapify-Down: For each non-leaf node, starting from the last non-leaf node to the root, we apply the heapify-down process. This ensures that each subtree satisfies the max heap property:

# If the node's value is smaller than any of its children, swap the node with the largest of its children.
# Repeat the process for the swapped child node until the subtree rooted at the node satisfies the max heap property.

#              1
#         /        \
#       3           5
#     /   \       /   \
#    4     6    13    10
#  /  \   /  \ 
# 9   8 15  17

# Step-by-step Heapify-Down:

# Start with the last non-leaf node (index 4):

# Current node: 6
# Left child: 15
# Right child: 17
# Largest child: 17
# Swap 6 with 17
# Heapify node at index 4:

# Tree after swap:
#              1
#         /        \
#       3           5
#     /   \       /   \
#    4     17    13    10
#  /  \   /  \ 
# 9   8 15    6

# - Repeat for the next non-leaf node (index 3), and so on.      
        
            

def heapifydown(arr , i , n):
    largest = i  # step 2 . initialize largest as root 
    left = 2*i + 1  # indicate the left child node
    right = 2*i + 2 # indicate the right chile node
    
    if left < n and arr[left] > arr[largest]:          # step 3. if left child is graterthan root 
        largest = left                                 #  initialize that greater left child as largest
    if right < n and arr[right] > arr[largest]:        #         if right child is graterthan root
        largest = right                                #  initialize that greater right child as largest
    if largest != i:                                   # step 4. if finalized largest != i
        arr[i] , arr[largest] = arr[largest] , arr[i]  #  then swap root to chiled node
        heapifydown(arr , largest , n)                 # repeat  for the next non-leaf node (index 3) and so an
    return arr

def creatheap(heap):
    for i in range(n//2 -1 , -1 ,-1):  # step 1. find non-leaf nodes
        heapifydown(heap , i , n)
        
def printHeap(n):
    for i in range(n):
        print(arr[i] , end=" ")
        
arr = [1,4,3,6,5,8,10,24,13,19,30]
n = len(arr)

creatheap(arr)
printHeap(n)





# Explanation
# heapify_down:

# Takes the heap, an index i, and the size N.
# Compares the node at index i with its left and right children.
# Swaps the node with the largest child if necessary and recursively applies the same to the swapped child.
# create_heap:

# Iterates from the last non-leaf node to the root.
# Applies heapify_down to each node to ensure the entire array satisfies the max heap property.
# printHeap:

# Simply prints the elements of the heap.
