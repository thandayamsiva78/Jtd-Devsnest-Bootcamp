# stack=[]
# # push
# stack.append('A')
# stack.append('B')
# stack.append('C')
# print("Stack :",stack)

# # pop
# element=stack.pop()
# print("Pop :",element)

# # peek
# topelement= stack[-1]
# print("Peek :",topelement)

# # isEmpty
 
# isEmpty= not bool(stack)
# print("isEmpty :",isEmpty)

# # size
# print("Size :",len(stack))

# """================================================================================"""
# stack=[]
# stack.append("a")
# stack.append("b")
# stack.append("c")
# print("stack :",stack)

# # pop
# element=stack.pop()
# print("pop :",element)

# # peep
# topelement=stack[-1]
# print("peep :",topelement)

# # isEmpty
# isEmpty=not bool(stack)
# print("isEmpty :",isEmpty)

# # size
# print("Size :",len(stack))

    
"""=================================STACK PROBLEMS============================================================="""
"""VALID PARENTHES"""
# def valid_paranthes(string):
#     stack =  []
#     brackets = {')': '(', '}': '{', ']': '['}
#     for char in string:
#         if char in brackets:
#             if stack and stack[-1] == brackets[char]:
#                 stack.pop()
#             else:
#                 stack.append(char)
#         if stack == []:
#             return "valid"
#         else:
#             return "invalid"
# # s =  "({[]})"
# s = "[(])"
# print(valid_paranthes(s))

# #########
# def solve(s):
#     stack = [] # {
#     open_brackets = ("(" , "[" , "{")
#     for char in s:
#         if char in open_brackets:
#             stack.append(char)
#         else:
#             if stack and stack[-1] == "(" and char == ")" or stack[-1] == "[" and char == "]" or stack[-1] == "{" and char == "}" :
#                 stack.pop()
        
#     if len(stack)  == 0:
#         return "Balenced"
#     else:
#         return "UnBalenced"
# s = "[(])"
# # s =  "({[]})"
# print(solve(s))


# def solve(string):
#     stack = [] # [ ( 
#     open = ["(" , "[" , "{"]
#     for char in string:
#         if char in open:
#             stack.append(char)
#         else:
#             if stack[-1] != char :
#                 stack.pop()     
#     if len(stack) == 0:
#         print("Balenced")
#     else:
#         print("Not Balenced")
        
# string = "[(])"
# solve(string)


"""Valid Parenthesis without Using stacks"""
# def validparanthes(s):
#     open_paren = 0
#     open_square = 0
#     open_curly = 0

#     for char in s:
#         if char == '(':
#             open_paren += 1
#         elif char == ')':
#             open_paren -= 1
#             if open_paren < 0:
#                 return False
        
#         elif char == '[':
#             open_square += 1
#         elif char == ']':
#             open_square -= 1
#             if open_square < 0:
#                 return False
        
#         elif char == '{':
#             open_curly += 1
#         elif char == '}':
#             open_curly -= 1
#             if open_curly < 0:
#                 return False

#     return open_paren == 0 and open_square == 0 and open_curly == 0

# s = "({[]})"
# print(validparanthes(s))  # Output: True

# s = "({[})"
# print(validparanthes(s))  # Output: False

# """REVRESE A STRING"""
# def reverse(s):
#     stack = []
#     for char in s:
#         stack.append(char)
    
#     reverse_char = ""
#     while stack:
#         reverse_char += stack.pop()
#     return reverse_char
# a = "aviS"
# print(reverse(a))






# """SORT STACK"""
# def sort_stack(stack):
#     temp_stack = []
#     while stack:
#         temp = stack.pop()
#         while temp_stack and temp_stack[-1] > temp:
#             stack.append(temp_stack.pop())
#         else:
#             temp_stack.append(temp)
#     return temp_stack
# s = [4,2,6,1,3,5]
# print(sort_stack(s))

# """Remove Consecutive Duplicates"""
# def solve(s):
#     stack = []
#     for char in s:
#         if stack and stack[-1] == char:
#             continue  
#         else:
#             stack.append(char)
#     return ''.join(stack)

# s = "aaaaabbbbbbc"
# print(solve(s))  # Output: "ab"

# #reverse a individual words

# def reverse_str(string):
#     st = [] #world
#     for i in range(len(string)):#0123456789 10 
#         if string[i] != " ":
#             st.append(string[i])
#         else: #==" "
#             # while len(st) > 0:#olleh
#             while st:
#                 print(st[-1], end = "")
#                 st.pop()
#             print(" ")

#     while st:
#         print(st[-1], end = "")
#         st.pop()

# string = "Hello World"
# reverse_str(string)

"""==========================================================================================================="""
# stack = []
# def push():   
#     if len(stack) == n :
#         print("stack is Empty")
#     else:
#         element = int(input("Enter any Element : "))
#         stack.append(element)
#         print(stack)
    
# def pop_element():
#     ele = stack.pop()
#     print("removed Element" , ele)
#     print(stack)
# n = int(input("stack length ?  "))   
# while True:
#     print("Select operations --> 1.Push 2.Pop 3.Quit")
#     choice = int(input())
#     if choice == 1:
#         push()
#     if choice == 2:
#         pop_element()
#     if choice == 3:
#         print("Quitted")
#         break
        
    
# Input: exp = “[()]{}{[()()]()}” 
# Output: Balanced
# Explanation: all the brackets are well-formed

# Input: exp = “[(])” 
# Output: Not Balanced 
# Explanation: 1 and 4 brackets are not balanced because 
# there is a closing ‘]’ before the closing ‘(‘


# def reverse(arr):
#     data = []
#     while arr:
#         reversed=arr.pop()
#         data.append(reversed)
#     return data
# arr = [1,2,3,4,5]
# print(reverse(arr))

# class Solution(object):
#     def isValid(self, s):
#         # Create a pair of opening and closing parrenthesis...
#         opcl = dict(('()', '[]', '{}'))
#         # Create stack data structure...
#         stack = []
#         # Traverse each charater in input string...
#         for idx in s:
#             # If open parentheses are present, append it to stack...
#             if idx in '([{':
#                 stack.append(idx)
#             # If the character is closing parentheses, check that the same type opening parentheses is being pushed to the stack or not...
#             # If not, we need to return false...
#             elif len(stack) == 0 or idx != opcl[stack.pop()]:
#                 return False
#         # At last, we check if the stack is empty or not...
#         # If the stack is empty it means every opened parenthesis is being closed and we can return true, otherwise we return false...
#         return len(stack) == 0

# hii = Solution()
# print(hii.isValid("{()}"))
    
    
    
"""NEXT GREATER ELEMENT"""
def next_greater_elements(nums):
    stack = []
    result = [-1] * len(nums)
    for i in range(len(nums)):
        while stack and nums[stack[-1]] < nums[i]:
            result[stack.pop()] = nums[i]
        stack.append(i)
    return result
s = [2,4,6,1,3,5]
print(next_greater_elements(s))
    
"""revrse string and arr"""
def reverse_arr_queue(arr):
    q = []
    for el in arr:
        q.append(el)
    rev = []
    while q:
        r = q.pop()
        print(r , end="")
arr = [x for x in input().split()]
reverse_arr_queue(arr)

"""Remove Consecutive Duplicates"""
def solve(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            continue  
        else:
            stack.append(char)
    return ''.join(stack)

s = "aaaaabbbbbbc"
print(solve(s))  # Output: "ab"


"""revrse string and arr"""
# def revrse(string1 , list1):
#     stack1 = []
#     for word in string1:
#         stack1.append(word)
        
#     stack2 = []
#     reversed2 = []
#     reversed = ""
#     while stack1:
#         reversed+=stack1.pop()
#     print(reversed)
    
#     for el in list1:
#         stack2.append(el)
        
#     while stack2:
#         reversed2.append(stack2.pop())
#     print(reversed2)
    
# a = "Hii"
# s = [1,2,3,4,5]
# revrse(a , s)

"""Remove Consucuteve duplicates ////"""

# def remove_consecutive_duplicates_string(s):
#     if not s:
#         return ""
#     stack = []
#     for char in s:
#         if not stack or stack[-1] != char:
#             stack.append(char)

#     return ''.join(stack)
# s = "aaabbccdaa"
# print(remove_consecutive_duplicates_string(s))



"""# #reverse a individual words"""

# def reverse_str(string):
#     st = [] #world
#     for i in range(len(string)):#0123456789 10 
#         if string[i] != " ":
#             st.append(string[i])
#         else: #==" "
#             # while len(st) > 0:#olleh
#             while st:
#                 print(st[-1], end = "")
#                 st.pop()
#             print(" ")

#     while st:
#         print(st[-1], end = "")
#         st.pop()

# string = "Hii bro"
# reverse_str(string)



"""valid paranthes"""
def isValid(str1):
    stack = []
    brackets ={')':'(',']':'[','}':'{'}
    for char in str1:
        if char in brackets.values():
            stack.append(char)
        else:
            if stack and stack[-1] == brackets[char]:
                stack.pop()
            else:
                return 0
    # return 1 if not stack else 0
    if stack == []:
        return 1
    return 0
s = "()(){}[]"
result = isValid(s)
print(result)

"""Reverse a string using stack"""
def reverse_str_stack(s):
    stack = []
    for char in s:
        stack.append(char)
    reversed_str = ""
    while stack:
        reversed_str+=stack.pop()
    return reversed_str
s = "Hello World"
print(reverse_str_stack(s))

"""Reverse a array using stack"""
def reverse_arr(arr):
    stack = []
    for el in arr:
        stack.append(el)
    reverse_arrrr = []
    for i in range(len(stack)):
        reverse_arrrr.append(stack.pop())
    return reverse_arrrr
arr = [1,2,3,4,5]
print(reverse_arr(arr))
