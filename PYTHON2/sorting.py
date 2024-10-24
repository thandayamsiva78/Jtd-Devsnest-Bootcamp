# Here are the Python solutions for the sorting algorithm questions:

# 1. Bubble Sort:

def bubble_sort(arr):
	for i in range(len(arr)):
		for j in range(len(arr)-1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
	return arr
arr=[3,4,1,2,6]
print(bubble_sort(arr))


# 1. Insertion Sort:

def insertion_sort(arr):
	for i in range(1, len(arr)):
		key = arr[i]
		j = i-1
		while j >= 0 and arr[j] > key:
			arr[j+1] = arr[j]
			j -= 1
		arr[j+1] = key
	return arr
arr=[3,4,1,2,6]
print(insertion_sort(arr))

# 1. Selection Sort:

def selection_sort(arr):
	for i in range(len(arr)):
		min_idx = i
		for j in range(i+1, len(arr)):
			if arr[j] < arr[min_idx]:
				min_idx = j
		arr[i], arr[min_idx] = arr[min_idx], arr[i]
	return arr
arr=[3,4,1,2,6]
print(selection_sort(arr))

# 1. Merge Sort:

def merge_sort(arr):
	if len(arr) <= 1:
		return arr
	mid = len(arr)//2
	left = merge_sort(arr[:mid])
	right = merge_sort(arr[mid:])
	return merge(left, right)

def merge(left, right):
	result = []
	while len(left) > 0 and len(right) > 0:
		if left[0] <= right[0]:
			result.append(left.pop(0))
		else:
			result.append(right.pop(0))
	result.extend(left)
	result.extend(right)
	return result

arr=[5,3,1,2,4]
sorted_arr=merge_sort(arr)
print(sorted_arr )


# 1. Quick Sort:

def quick_sort(arr):
	if len(arr) <= 1:
		return arr
	pivot = arr[len(arr)//2]
	left = [x for x in arr if x < pivot]
	middle = [x for x in arr if x == pivot]
	right = [x for x in arr if x > pivot]
	return quick_sort(left) + middle + quick_sort(right)
arr = [64, 34, 25, 12, 22, 11, 90, 5]
print(quick_sort(arr))


"""Bubble Sort==================================================="""

# def bubble_sort(arr):
#     n = len(arr)
#     # For lop to traverse through all
#     # Element in array
#     for i in range(n):
#         for j in range(0,n-i-1):
#             # Range of the array is from 0 to n-i-1
#             # Swap the element if the element found
#             # is greater than the adjacent element
#             if arr[j] > arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1],arr[j]
#     return arr
# nums=[4,1,3,2] # 1 4 2 3,,, 1 2 4 3 ,,  1 2 3 4
# print(bubble_sort(nums))

# print(0,4-0-1)



# def bubblesort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0,n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j],arr[j+1] =arr[j+1],arr[j]
#     return arr
# my_list=[4,1,3,2]
# print(bubblesort(my_list))



"""Sorting without built in functions"""
# arr=[4,9,5,3,2,1]
# while True:
#     swapped =False
#     for j in range(len(arr)-1):
#         if arr[j] > arr[j+1]:
#             arr[j],arr[j+1] = arr[j+1],arr[j]
#             swapped=True
#     if not swapped:
#         break
# print(arr)
        
"""Selection_sorting"""

# my_array = [64, 34, 25, 12, 22, 11, 90, 5]
# n = len(my_array)
# for i in range(n):
#     min_index = i
#     for j in range(i+1, n):
#         if my_array[j] < my_array[min_index]:
#             min_index = j   
#     my_array[i], my_array[min_index] = my_array[min_index], my_array[i]

# print("Sorted array:", my_array)


# arr=[3,4,2,1,5,8,9,6,7]
# n=len(arr)
# for i in range(n):
#     min_index=i
#     for j in range(i+1,n):
#         if arr[j] < arr[min_index]:
#             min_index = j
#     arr[i],arr[min_index] = arr[min_index],arr[i]
# print("Sorted array using Selection Sort:",arr)



# arr=[2,5,7,4,8,9]
# n=len(arr)
# for i in range(n): # 1,2,3,4,5,6,7
#     min_index=i # 1 -->(2)
#     for j in range(i+1,n): #(2+1= 3 ),8 ---> 3,4,5,6,7
#         if arr[j] < arr[min_index]:  # 2 < 5
#             min_index = j # 2
#     arr[i],arr[min_index] = arr[min_index],arr[i]   
# print(arr)

# arr=[10,11,2,4,6,8,3,1]
# # n=len(arr)
# for i in range(len(arr)):
#     min_index=i
#     for j in range(i+1,len(arr)):
#         if arr[j] < arr[min_index]:
#             min_index=j
#     arr[i],arr[min_index] = arr[min_index],arr[i]
# print(arr)

"""Insertion Sort"""
# my_array = [64, 34, 25, 12, 22, 11, 90, 5]

# n = len(my_array)
# for i in range(1,n):
#     insert_index = i
#     current_value = my_array[i]
#     for j in range(i-1, -1, -1): 
#         if my_array[j] > current_value:
#             my_array[j+1] = my_array[j]
#             insert_index = j
#         else:
#             break
#     my_array[insert_index] = current_value

# print("Sorted array:", my_array)

# for k in range(1-1, -1, -1):
#     print(k)

"""Merge Sort"""

# def merge(left, right):
#     result = []
#     i = j = 0
    
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
            
#     result.extend(left[i:])
#     result.extend(right[j:])
    
#     return result

# def mergeSort(arr):
#     step = 1  # Starting with sub-arrays of length 1
#     length = len(arr)
    
#     while step < length:
#         for i in range(0, length, 2 * step):
#             left = arr[i:i + step]
#             right = arr[i + step:i + 2 * step]
            
#             merged = merge(left, right)
            
#             # Place the merged array back into the original array
#             for j, val in enumerate(merged):
#                 arr[i + j] = val
                
#         step *= 2  # Double the sub-array length for the next iteration
        
#     return arr

# unsortedArr = [3, 7, 6, -10, 15, 23.5, 55, -13]
# sortedArr = mergeSort(unsortedArr)
# print("Sorted array:", sortedArr)

# def insertion_sort(arr):
#     for i in range(len(arr)):
#         # print(i,"i val")
#         current_index = arr[i]#current_index=64
#         # print(current_index,"current_index")
#         for j in range(i - 1, -1, -1):#0 to 0
            
#             # print(j,"j val")
#             if current_index < arr[j]:#34<64
#                 arr[j + 1] = arr[j]
#                 arr[j] = current_index
#             else:
#                 break
#             # print(arr,j)

# arr = [64, 34, 25, 12, 22, 11, 90, 5]
# print(arr,"unsorted array","\n")
# insertion_sort(arr)
# print("Sorted array:", arr)


# def quickSort(arr):
#     if len(arr) <=1:
#         return arr
#     pivot =arr[ len(arr)//2]
#     left=[x for x in  arr if x < pivot]
#     middle=[x for x in arr if x == pivot]
#     right=[x for x in arr if x > pivot]
#     return quickSort(left) + middle + quickSort(right)
# arr=[3,4,1,2,6]
# print(quickSort(arr))
    

# def bubble_sort(arr):
# 	for i in range(len(arr)): # 0,1,2,3,4,5
# 		for j in range(len(arr)-1): # 0,1,2,3,4
# 			if arr[j] > arr[j+1]:
# 				arr[j],arr[j+1]=arr[j+1],arr[j]
# 	return arr
# arr=[3,4,1,2,6]
# print(bubble_sort(arr))



