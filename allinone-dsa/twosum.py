# 1. Two Sum 
 
def twosum(arr , target):
    arr.sort()
    print(arr)
    left = 0
    right = len(arr)-1
    while left < right:
        sumof = arr[left] + arr[right]
        if sumof == target:
            return [left+1 , right+1]
        if sumof > target:
            left+=1
        else:
            right-=1
            
arr = [2,7,4,6]
target = 9
print(twosum(arr , target))
            
        
def twosum(arr , target):
    n = len(arr)
    for i in range(n): # 0 1 2 3 
        for j in range(i+1,n): # 0 1 2 3 
                                  # 2 7 4 6
            if arr[i] + arr[j] == target:
                return i+1,j+1 
    return "No pairs Found"       
arr = [2,4,7,6]
target = 10
print(twosum(arr , target)) 