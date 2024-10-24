"""Linear searches in Python happen when each item on a list is inspected individually, from one end to another, to find a match"""

# def linearsearch(arr,n):
#     if n in arr:
#         return arr[n]
#     return -1

# list=[1,2,3,4,5,6,7,8]
# x=1
# result=linearsearch(list,x)
# print(result)


# def search(arr,x):
#     for i in range(len(arr)):
#         if arr[i] == x:
#             return i
#         return -1
    
# list=[12,1,3,1,415,12,13]
# a=12
# result=search(list,a)
# print(result)


# arr=[1,2,3,4,5,6,7]
# x=5
# for i in range(len(arr)):
#     if arr[i] ==x:
#         print(i)
    
"""Binary search is a searching alogrithm for finding an element's position in a sorted array"""

def find(arr,search_value):
    low=0
    high=len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid]==search_value:
            return mid
        if arr[mid] < search_value:
            low=mid+1
        else:
            # arr[mid] < search_value
            high=mid-1
    return -1

my_arr=[10,12,20,32,50,55,65,80,99]
target=65

result=find(my_arr,target)

if result != -1:
    print(f"{target} found at index no",result)
else:
    print(f"{target} not found at index no",result)
