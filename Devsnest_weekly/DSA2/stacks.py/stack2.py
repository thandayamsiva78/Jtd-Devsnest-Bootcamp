"""Reverse a string using stack"""

def createstack(string):
    stack = []  # create a empty stack
    for char in string:
        stack.append(char)  # push the all elements in the stack
    # stack1 = []
    # while stack: # pop the all elements and push the popped elements in the new stack
    #     stack1.append(stack.pop())
    # return "".join(stack1)
    
    reversed = ""
    while stack:
        reversed+=stack.pop()
    return reversed
    
    # """without stack"""
    # revrese = stack[::-1]
    # return "".join(revrese)

string = 'aviS'
print(createstack(string))

"""Balanced Parantheses in an expression"""
def balencedPair(s):
    stack = []
    brackets = {")":"(" ,"]":"[" ,"}":"{"}
    for char in s:
        if char in brackets.values():
            stack.append(char)
        elif stack[-1] == brackets[char]:
            stack.pop()
        else:
            return False
    return len(stack) == 0
s= "[()()]"
print(balencedPair(s))

        # for char in s:
        #     if char in mapping.values():
        #         stack.append(char)
        #     elif char in mapping.keys():
        #         if not stack or mapping[char] != stack.pop():
        #             return False
        # return not stack
        
"""Next Greater Element"""
#------->Method 1 (Simple) Using two for loops  O(n^2)
def NGE(arr):
    n = len(arr)
    for i in range(0 ,n):
        next = -1
        for j in range(i+1 , n):
            if arr[j] > arr[i]:
                next = arr[j]
                break
        print(arr[i],"-->",next)
                
arr = [4,5,2,25,34,2]
NGE(arr)

# -------> Methode 2 using STack    
# def nextGreaterElement(arr):
#     stack = []
#     result = [-1] * len(arr)  # Initialize the result array with -1
#     # Push the first element to the stack
#     stack.append(0)
#     # Loop through the rest of the elements
#     for i in range(1, len(arr)):
#         next = arr[i]
#         # If stack is not empty, pop an element from the stack and compare it with next
#         while stack and arr[stack[-1]] < next:
#             index = stack.pop()
#             result[index] = next
#         # If next is smaller than the popped element, push the popped element back
#         stack.append(i)
#     # After the loop, pop all elements from stack and set their next greater element to -1
#     while stack:
#         index = stack.pop()
#         result[index] = -1

#     return result

# arr = [4, 5, 2, 25, 7, 8]
# print(nextGreaterElement(arr))  # Output should be [5, 25, 25, -1, 8, -1]


def NGE(arr):
    n = len(arr)
    stack = []
    result = [-1] * n
    stack.append(0)
    for i in range(1 , n):
        next = arr[i]
        while stack and arr[stack[-1]] < arr[i]:
            index = stack.pop()
            result[index] = arr[i]
        else:
            stack.append(i)
    return result
arr = [4,5,2,25,34,2]
print(NGE(arr))











