# caluculate the power of a number using recursion
# def power(n,p):
#     if p == 0:
#         return 1
#     elif p==1:
#         return n
#     else:
#         return n* power(n,p-1)
# a=5 # base number
# b=2 # power
# print(power(a,b))

# Factorial of a non-negative integers
# def solve(n):
#     if n==0:
#         return 1
#     else:
#         return n* solve(n-1)
# print(solve(5))

# nth fib0onacci number

# def solve(n):
#     if n <= 1:
#         return n
#     else:
#         return solve(n-1) + solve(n-2)
    
# x=6
# for i in range(x):
#     print(solve(i))
# print(solve(x))

#  Sum of digits of a positive integers
# def sum(n):
#     if n == 0:
#         return 0
#     else:
#         return n % 10 +sum(n//10)
# digits=465
# print(sum(digits))

# print(456%10)
# print(456//10)

# Revers a string
# def solve(n):
#     if len(n) == 0:
#         return n
#     else:
#         return solve(n[1:]) + n[0]
# string="Hello"
# print(solve(string))

# length of a string
# def string_length(s):
#     if s =='':
#         return 0
#     else:
#         return 1+ string_length(s[1:])
    
# string="Hello"
# print(string_length(string))

# Print numbers from 1 to n in increasing order

# def print_numbers(n):
#     if n > 0:
#         print_numbers(n-1)
#         print(n-1)
# array=5
# print(print_numbers(array))


# Factorial of nth element
# def solve(n):
#     if n <=1:
#         return n
#     else:
#         return n* solve(n-1)
# print(solve(5))

""" two Power"""
# def power(n,p):
#     if p ==0:
#         return 0
#     elif p ==1:
#         return n
#     else:
#         return n* power(n,p-1)
# base=5
# exponent=2
# print(power(base,exponent))

""" GCD using Recursion"""
# def gcd(a,b):
#     if b == 0:
#         return a
#     else:
#         return gcd(b,a%b)
# num1=48
# num2=18
# print(gcd(num1,num2))



# def factorial(s):
#     if s == 0:
#         return 1
#     else:
#         return s*factorial(s-1)
# s=4
# print(factorial(s))



# def is_palindrome(s):
#     s=s.lower()
#     if  len(s)<=1:
#       return True
#     elif s[0]!=s[-1]:
#        return False
#     else:
#       return is_palindrome(s[1:-1])
# s="madam"
# res=is_palindrome(s)
# if res==True:
#   print("palindrome")
# else:
#   print("not palindrome")


# def is_palidrome(s):
#     if s[0::] == s[::-1] :
#         return True
#     return False
# s= "level"
# res = is_palidrome(s)
# if res == True:
#     print("Palidrome")
# else:
#     print('Not a palidrome')   

# [11:42 am, 8/5/2024] Sowmya N JTD: .Write a recursive function to find the sum of digits of a positive integer.
# [11:43 am, 8/5/2024] Sowmya N JTD: .Write a recursive function to reverse a string.
# [11:43 am, 8/5/2024] Sowmya N JTD: Write a recursive function to find. the length of a string.
# [11:44 am, 8/5/2024] Sowmya N JTD: Write a recursive function to print numbers from 1 to n in increasing order.

# def sum_of_digits(n):
#     if n == 0: 
#         return 0
#     else:
#         return n % 10 + sum_of_digits(n//10)
# n=12
# res = sum_of_digits(n)
# print(res)

# # print(234%10)
# # print(234//10)
 



# def reverse(s):
#     if len(s) <= 1:
#         return s
#     else:
#         return reverse(s[1:]) + s[0]
# s="Siva"
# res = reverse(s)
# print(res)

# def length(s):
#     if s == '':
#         return 0
#     else:
#         return 1 + length(s[1:])
# s="keerthi"
# res = length(s)
# print(res)

# def number(num):
#     if num == 0:
#         return 
#     else:
#         number(num-1)
#         print(num) 
# num = 5
# res = number(num)
# print(res)

# def number(num):
#     if num == 1:
#         return 1
#     else:
#         return num+number(num-1)
# num = 5
# res = number(num)
# print(res)

"""2 power"""
# def solve(n):
#  if n == 1:
#   return 1
#  if n%2==1 or n==0:
#   return 0
#  return solve(n/2)

# n=64
# print(solve(n))

# def solve(n):
#     if n==1:
#         return 1
#     elif n%2==0 and n!=0:
#         return solve(n//2)
#     else:
#         return 0

s= 'c','a'
a=''.join(s)
print(a)
