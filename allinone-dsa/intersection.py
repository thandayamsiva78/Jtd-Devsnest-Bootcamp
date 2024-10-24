"""  1 .Using python set()"""
def intersection(s1 , s2):
    return list(set(s1) & set(s2))
    
s1 = [1,2,3,4,5]
s2 = [1,2,6,7,8,]
print(intersection(s1 ,s2))

"""Using List comprehension"""

def intersection(s1 , s2):
    return [val for val in s1 if val in s2]

s1 = [1,2,3,4,5]
s2 = [1,2,6,7,8,]
print(intersection(s1 , s2))


"""Sorting and Two pointers"""
def intersection(arr1 , arr2):
    arr1.sort()
    arr2.sort()
    i , j = 0 , 0
    result = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i+=1
        elif arr1[i] > arr2[j]:
            j+=1
        else:
            result.append(arr1[i])
            j+=1
            i+=1
    return result
arr1 =[1,2,3,4,5] 
arr2 = [1,2,6,7,8,]
print(intersection(arr1 , arr2))




def common_num(arr1 , arr2):
    stack = []
    for el in arr1:
        if el in arr2:
            stack.append(el)
        else:
            pass
    return stack
arr1 =[1,2,3,4,5] 
arr2 = [1,2,6,7,8,]
print(common_num(arr1 ,arr2))