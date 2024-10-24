"""An array is a special variable , which can hold more than one value at a time"""
"""An array can hold many values under a single name, and you can access the values by referring to an index number"""

# # Access the elements of an array

# cars=["ford","volvo","BMW"]
# x=cars[0]
# print(x)

# # modify the value of array (insert)
# cars[0]="Toyota"
# print(cars)

# # The length of an array
# y=len(cars)
# print(y)

# # looping array elements
# for i in cars:
#     print(i)

# # adding array elements
# cars.append("Honda")
# print(cars)

# ## Removing array elements
# # removes last element
# cars.pop()
# print(cars)

# # removes specific elements
# cars.pop(1)
# print(cars)

# # remove direct value
# cars.remove("BMW")
# print(cars)

"""first missing element in array"""
# def first_missing(n,arr):
#     for ele in range(n+1):
#         if ele not in arr:
#             return ele   
# arr=[0,1,2,4,5,6]
# n=max(arr)
# print(first_missing(n,arr))


"""kadan's Algorithm"""

# def kadans(arr):
#     globalSum = arr[0]
#     currsum = 0
#     for i in arr:
#         currsum=currsum+i
#         if currsum < 0:
#             currsum = 0
#         else:
#             globalSum=max(globalSum,currsum)
#     return globalSum
# arr =[2,1,3,4,6]
# print(kadans(arr))

"""two sum"""
# # time ncomplexity O(n^2)
# def solve(nums,tar):
#     for i in range(len(nums)):
#         for j in range(0,len(nums)):
#             if nums[i] + nums[j] == tar:
#                 return [i,j]
# numbers =[2,3,4,5]
# target = 6
# result = solve(numbers,target)
# print(result)


# time ncomplexity O(log n)
# def solve(num,target):
#     low = 0
#     high = len(num)-1
#     while low < high:
#         total = (num[low]+num[high])
#         if total == target:
#             return [low+1,high+1]
#         elif total < target:
#             low +=1
#         else:
#             high-=1
# numbers =[2,3,4,5]
# target = 6
# result = solve(numbers,target)
# print(result)

# def linearSearch(arr,target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             result = i
#             return result
#     else:
#         return -1
    
# nums=[1,2,3,4,6]
# target = 9
# result = linearSearch(nums,target)
# # print(result)
# if result != -1:
#     print(f"target found at index {result}")
# else:
#     print(f"target  not found in array")



# def solve(arr):
#     low = 0
#     high = len(arr) - 1
#     max_water = 0
#     while low < high:
#         current = min(arr[low], arr[high]) * (high - low)
#         max_water = max(max_water, current)
#         if arr[low] < arr[high]:
#             low += 1
#         else:
#             high -= 1
#     return max_water

# arr = [2, 5, 4, 1, 6]
# print(solve(arr))

# # container with most water
# #           -
# #     -     -
# #     - -   -
# #     - -   -
# #   - - -   -
# #   - - - - -
# # ------------------------------
# #  [2,5,4,1,6]
# # container with most water
# arr=[2,5,4,1,6]   #a=0  b=4   diff=b-a=3
# # #    0 1 2 3 4
# def solve(arr):
#     l=0   # 0+1=1+1=2+1=3
#     r=len(arr)-1   #5-1=4
#     max_water=0   #area= 15
#     while l<=r:
#         curr_water = min(arr[l],arr[r])    *  (r-l)
#         # curr = min(4,6)*(4-2)
#         #           4*2=8
#         # curr = min(5,6)*(4-1)


# def solve(arr, target):
#     l=0
#     r=len(arr)-1
#     while l<=r:
#         currsum=arr[l]+arr[r]
#         if currsum==target:
#             return [l+1,r+1]
#         if currsum<target:
#             l+=1
#         else:
#             r-=1

# container with most water
#           -
#     -     -
#     - -   -
#     - -   -
#   - - -   -
#   - - - - -
# ------------------------------

#    0 1 2 3 4 
# arr=[2,5,4,1,6]
# def solve (arr):
#     l=0  # 2
#     r=len(arr)-1 # 0
#     max_water = 0  # 15 
#     while l <= r:
#         curr_water = min(arr[l],arr[r]) * (r-l)
#         # curr = min(2,6) * (4-0) = 8
#         # curr = min(5,6) * (4-1) = 15
#         # curr = min(4,6) * (4-2) = 8
#         # curr = min(4,1) * (3-2) = 1
#         # curr = min(4,4) * (2-2) = 0
#         if curr_water > max_water:
#             # 8 > 0
#             # 15 > 8
#             # 8 > 15
#             # 1 > 15
#             # 0 > 15
#             max_water = curr_water 
#         if arr[l]<arr[r]:
#             l += 1  
#         else:
#             r -= 1 
#     return max_water 
# print(solve(arr))

# def next_permutation(arr):
#     # Step 1: Find the largest index k such that arr[k] < arr[k + 1]
#     k = len(arr) - 2
#     print(k)
#     while k >= 0 and arr[k] >= arr[k + 1]:
#         k -= 1

#     if k == -1:
#         # The array is in the highest permutation, return the lowest permutation
#         arr.reverse()
#         print(arr)
#         return arr

#     # Step 2: Find the largest index l greater than k such that arr[k] < arr[l]
#     l = len(arr) - 1
#     print(l)
#     while arr[l] <= arr[k]:
#         l -= 1

#     # Step 3: Swap the value of arr[k] with that of arr[l]
#     arr[k], arr[l] = arr[l], arr[k]

#     # Step 4: Reverse the sequence from arr[k + 1] up to the last element
#     arr[k + 1:] = reversed(arr[k + 1:])
#     print(arr[k+1:])
#     print(arr)
#     return arr

# # Example usage:
# arr = [1,2,3,6,4,3,2,1]
# print("Current permutation:", arr)
# next_permutation(arr)
# print("Next permutation:", arr)


"""Next permutation"""
# def next_permutation(arr):
#     # step 1
#     i = len(arr)-2
#     while i >= 0 and arr[i] >= arr[i+1]:
#         i = i-1
    
#     if i == -1:
#         arr.reverse()
#         return arr
#     # step 2
#     j = len(arr)-1
#     while arr[j] <= arr[i]:
#         j = j-1
#     # step 3
#     arr[i],arr[j] = arr[j],arr[i]
#     # step 4
#     arr[i+1:] = reversed(arr[i+1:])
#     return arr
# arr = [2,4,6,8,4,3]
# result = next_permutation(arr)
# print(result)


# def kadans_algo(arr):
#     global_sum = arr[0]
#     curr_sum = 0
#     for i in arr:
#         curr_sum = curr_sum+i
#         if curr_sum < 0:
#             curr_sum = 0
#         else:
#             global_sum = max(global_sum,curr_sum)
#     return global_sum
# arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# result= kadans_algo(arr)
# print(result)

"""Kadans Algorithms"""
# def kadans(arr):
#     global_sum =arr[0]
#     currsum = 0
#     for i in arr:
#         currsum = currsum+i
#         if currsum < 0:
#             currsum = 0
#         else:
#             global_sum = max(global_sum,currsum)
#     return global_sum
# arr = [-2,-3,4,-1,-2,1,5,-3]
# result= kadans(arr)
# print(result)

"""# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative."""
# Example 1:
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

# def rotate_arr_right_by_k_steps(nums , k):
#     n = len(nums)
#     data = []
#     for i in range(k):
#         data.append(nums.pop())
#     for j in range(n-k):
#         data.append(nums[j])
#     return data
# nums = [1,2,3,4,5,6,7]
# k = 3
# result = rotate_arr_right_by_k_steps(nums , k)
# print(result)


