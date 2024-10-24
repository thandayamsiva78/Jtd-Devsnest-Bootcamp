# A Function calling itself ---Recursion

#  factorial of n!----------------------------

# def factorial(n):
#     if n <=1:  # or n==0
#         return n
#     else:
#         return n* factorial(n-1)

# x=5
# result=factorial(x)
# print(result)

# fibonacci series-----------------------------

def fibo(n):
    if n==1 or n==0:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
    
x=int(input())
for i in range(x):
    print(fibo(i))
print(fibo(x))
# fibo(x)


# fibonacci series without using Recursion------------------------------

# num=10
# a=0
# b=1
# print(a)
# print(b)
# for i in range(2,num+1):
#     c = a + b
#     a = b  # swaping
#     b = c  # swaping
#     print(c)

# Head Recursion---------------------

# def fun(n):
#     if n > 0:
#         fun(n-1)
#         print(n)
# fun(10)

# # Tail Recursion-------------------
# def fun(n):
#     if n > 0:
#         print(n)
#         fun(n-1)
# fun(10)

# using Head & Tail Recursion--------------------
# def fun(n):
#     if n > 0:
#         print(n,end="")
#         fun(n-1)
#         print(n-1,end="")
# fun(5)


 # Some Problems

# def reverse_string(s):
#     if len(s)==0:
#         return s
#     else:
#         return reverse_string(s[1:]) +s[0]

# x="Hello world"
# print(reverse_string(x))


# Sum_list
# def sum_list(l):
#     if len(l) == 0:
#         return 0
#     else:
#         return l[0] + sum_list(l[1:])
# x=[1,2,3,3,4,4]
# print(sum_list(x))

# gcd
# def gcd(a,b):
#     if b==0:
#         return a
#     else:
#         return gcd(b,a % b)
    
# x=40
# y=80
# print(gcd(x,y))

