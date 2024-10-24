# def binary_search(arr, target):
#     low, high = 0, len(arr) - 1

#     while low <= high:
#         mid = (low + high) // 2

#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1
# arr = [1,2,3,4,5,6,7,8,9,10]
# target = 6
# print(binary_search(arr , target))


def binary_search(arr , target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right )// 2
        if arr[mid] == target:
            return arr[mid]
        elif arr[mid] > target:
            left = mid -1
        else:
            right = mid+1
    return -1

arr = [1,2,3,4,5,6,7,8,9,10]
target = 8
print(binary_search(arr , target))


def binary_search(arr,target):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            low = mid+1
        else:
            high = mid-1
    return -1
my_list = [1,2,3,4,5,6,7,8,9,10]
searched_ele=5
result = binary_search(my_list,searched_ele)
print(result)

if result != -1:
    print(f"{searched_ele} is founded at index no {result}")
else:
    print(f"{searched_ele}  not founded ")