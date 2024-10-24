"""REVERSE AN ARRAY"""


""" 1. Slicing Method"""
arr = [1,2,3,4,5]
reverse = arr[::-1]
print(reverse)

""" 2. Swapping Method"""
def revrsearr_using_swapmethode(arr):
    left = 0
    right = len(arr) -1
    while left < right:
        # swap elements at indices left and right
        arr[left] , arr[right] = arr[right] , arr[left]
        # move towards to middle
        left +=1 # increment left
        right -=1 # decrement right
    return arr
arr = [1,2,3,4,5]
print(revrsearr_using_swapmethode(arr))

def revrsearr_using_swapmethode(arr):
    n = len(arr)
    for i in range(n//2):
        arr[i] , arr[n-1-i] = arr[n-1-i] ,arr[i]
        
    return arr
arr = [1,2,3,4,5]
print(revrsearr_using_swapmethode(arr))




