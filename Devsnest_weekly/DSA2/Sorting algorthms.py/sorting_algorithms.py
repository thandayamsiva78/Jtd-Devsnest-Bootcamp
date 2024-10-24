
""""Sorting algorithms """
"""Bubble Sort"""

def Bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1 , n):
            if arr[i] > arr[j]:
                arr[i] , arr[j] = arr[j] , arr[i]
    return arr
arr = [3,1,5,2,6,4]
result = Bubblesort(arr)
print("BubbleSort :",result)

"""quick sort"""

def Quicksort(arr):
    if len(arr) <= 1:
       return arr
    pivot = arr[len(arr)//2] # 3 -> val = 2
    left = [ x for x in arr if x < pivot] # l = [1]
    middle = [x for x in arr if x == pivot] # m =[2]
    right = [x for x in arr if x > pivot] # r = [3,5,6,4]
    return Quicksort(left) + middle + Quicksort(right)  # 
arr = [3,1,5,2,6,4]
result = Quicksort(arr)
print("Quick Sort :",result)


# Let's perform a dry run of the Quicksort function with the array [3, 1, 5, 2, 6, 4].

# First call:

# arr = [3, 1, 5, 2, 6, 4]
# pivot = arr[len(arr) // 2] = arr[6 // 2] = arr[3] = 2
# left = [x for x in arr if x < pivot] = [1]
# middle = [x for x in arr if x == pivot] = [2]
# right = [x for x in arr if x > pivot] = [3, 5, 6, 4]
# Recursive calls: Quicksort([1]), Quicksort([3, 5, 6, 4])
# Second call (Quicksort([1])):

# arr = [1]
# Since len(arr) <= 1, return [1]
# Third call (Quicksort([3, 5, 6, 4])):

# arr = [3, 5, 6, 4]
# pivot = arr[len(arr) // 2] = arr[4 // 2] = arr[2] = 6
# left = [x for x in arr if x < pivot] = [3, 5, 4]
# middle = [x for x in arr if x == pivot] = [6]
# right = [x for x in arr if x > pivot] = []
# Recursive calls: Quicksort([3, 5, 4]), Quicksort([])
# Fourth call (Quicksort([3, 5, 4])):

# arr = [3, 5, 4]
# pivot = arr[len(arr) // 2] = arr[3 // 2] = arr[1] = 5
# left = [x for x in arr if x < pivot] = [3, 4]
# middle = [x for x in arr if x == pivot] = [5]
# right = [x for x in arr if x > pivot] = []
# Recursive calls: Quicksort([3, 4]), Quicksort([])
# Fifth call (Quicksort([3, 4])):

# arr = [3, 4]
# pivot = arr[len(arr) // 2] = arr[2 // 2] = arr[1] = 4
# left = [x for x in arr if x < pivot] = [3]
# middle = [x for x in arr if x == pivot] = [4]
# right = [x for x in arr if x > pivot] = []
# Recursive calls: Quicksort([3]), Quicksort([])
# Sixth call (Quicksort([3])):

# arr = [3]
# Since len(arr) <= 1, return [3]
# Seventh call (Quicksort([])):

# arr = []
# Since len(arr) <= 1, return []
# Now, let's combine the results:

# From the fifth call: Quicksort([3, 4]) returns [3] + [4] + [] = [3, 4]
# From the fourth call: Quicksort([3, 5, 4]) returns [3, 4] + [5] + [] = [3, 4, 5]
# From the third call: Quicksort([3, 5, 6, 4]) returns [3, 4, 5] + [6] + [] = [3, 4, 5, 6]
# From the second call: Quicksort([1]) returns [1]
# From the first call: Quicksort([3, 1, 5, 2, 6, 4]) returns [1] + [2] + [3, 4, 5, 6] = [1, 2, 3, 4, 5, 6]
# Thus, the sorted array is [1, 2, 3, 4, 5, 6].

"""Merge Sort"""
#---------------> [2,4,6,1,3,5]

def  mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2  # mid = 1
    left = mergeSort(arr[:mid]) # l = [6]
    right = mergeSort(arr[mid:]) # r = []
    return merge( left , right) 

def merge(left , right):
    result = []  # [1,2,3,4,5,6]
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:           # 6 <= 0 f
            result.append(left.pop(0))
        else:                             # T         
            result.append(right.pop(0))  
    result.extend(left)
    result.extend(right)
    return result
arr = [2,4,6,1,3,5]
sorted_arr = mergeSort(arr)
print("Merge Sort :",sorted_arr)        
    
    
    
"""Selection Sort"""
def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1 , n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i] , arr[min_idx] = arr[min_idx] , arr[i]
    return arr
arr = [3,1,5,2,6,4]
print("selection sort :",selectionSort(arr))

"""Insertion Sort"""
def insertoinSort(arr):
    n = len(arr)
    for i in range(n):
        current = arr[i]
        for j in range(i-1 ,-1 ,-1):
            if  current <  arr[j]:
                arr[j+1] = arr[j]
                arr[j] = current
            else:
                break
    return arr
arr = [3,1,5,2,6,4]
print("Insertion Sort",insertoinSort(arr))