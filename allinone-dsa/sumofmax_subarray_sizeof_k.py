def max_of_subarrays_brute_force(arr, k):
    n = len(arr) # 9
    if n * k == 0:  # Edge case if array or k is zero
        return []
    max_values = []
    for i in range(n - k + 1): # 9 - 3 = 6 + 1 = = 7              
        current_max = arr[i] # 1
        for j in range(1, k):
            if arr[i + j] > current_max:
                current_max = arr[i + j]
        max_values.append(current_max)
    return max_values
arr1 = [1, 2, 3, 1, 4, 5, 2, 3, 6]
k1 = 3
print(max_of_subarrays_brute_force(arr1, k1))  # Should return [3, 3, 4, 5, 5, 5, 6]
arr2 = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
k2 = 4
print(max_of_subarrays_brute_force(arr2, k2))  # Should return [10, 10, 10, 15, 15, 90, 90]


def find_max_for_subarrays(arr, K):
  result = []
  for i in range(len(arr)):
    # Check if there are enough elements remaining to form a subarray of size K
    if i + K > len(arr):
      break
  # Find the maximum element in the current subarray
    current_max = arr[i]
    for j in range(i + 1, i + K):
        current_max = max(current_max, arr[j])
    # Append the maximum to the result list
    result.append(current_max)
  return result
arr = [1, 4, 2, 3, 1, 5, 2, 3, 6]
K = 3
result = find_max_for_subarrays(arr, K)
print(result)  # Output: [4, 4, 3, 5, 5, 5, 6]

