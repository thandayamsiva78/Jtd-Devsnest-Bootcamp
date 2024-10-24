""" A lambda function is a small anonymous function"""
""" A lambda fonction can take any number of arguments but can only have one expression"""
# syntax: lambda arguments : expression

x=lambda a:a+10
print(x(5))

# lambda function take any number of arguments

x = lambda a,b : a*b
print(x(4,5))

y = lambda x,y,z : (x+y)*z
print(y(2,4,6))

# summarize argument a,b and c and return the result
i = lambda a,b,c:a+b+c
print(i(5,10,5))

def solve(n):
    return lambda a:a*n
result=solve(5)
print(result(11))

# use same function definition to make both functions in the same programe
def my_fun(n):
    return lambda a:a*n
doubler=my_fun(2)
tripler=my_fun(3)
print(doubler(5))
print(tripler(10))