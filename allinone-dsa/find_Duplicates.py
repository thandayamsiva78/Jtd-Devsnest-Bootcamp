"""Sorted list"""

# def find_duplicate(arr):
#     for i in range(len(arr) - 1):
#         if arr[i] == arr[i + 1]:
#             return arr[i]
#     return None

# # Example usage:
# arr = [1, 2, 3, 4, 5, 5, 5, 6,6, 7, 8, 9, 10]
# print(find_duplicate(arr))  # Output: 5


"""find duplicates using Binary Seach"""
# def find_dup_binarySearch(arr):
#     duplicates = []
#     left = 0
#     right = len(arr) -1
    
#     while left <= right:
#         mid = (left+right) // 2
#         if mid > 0 and arr[mid] == arr[mid-1]:
#             duplicates.append(arr[mid])
#             right = mid -1
#         elif mid < right and arr[mid] == arr[mid+1]:
#             duplicates.append(arr[mid])
#             left = mid + 1
            
#     return duplicates
# arr = [1,2,3,4,5,5,6,7,8,9]
# dup = find_dup_binarySearch(arr)
# print(dup)
            
            
def find_dup_binarySearch(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left + right) // 2
        if mid > 0 and arr[mid] == arr[mid - 1]:
            return arr[mid]
        elif mid < right and arr[mid] == arr[mid + 1]:
            return arr[mid]
        elif arr[mid] < arr[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return None

arr = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]
dup = find_dup_binarySearch(arr)
print(dup)  # Output: 5