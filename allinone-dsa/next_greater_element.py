"""Using two loops"""
def next_greater_ele(arr):
    n  = len(arr)
    for i in range(n):
        next = -1
        for j in range(i+1 , n):
            if arr[i] <  arr[j]:
                next = arr[j]
                break
        print(arr[i], "-->",next)   
arr = [4,5,25,2]
next_greater_ele(arr)

"""Using stacks"""