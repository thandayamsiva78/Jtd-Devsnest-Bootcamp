s= "aviS"
print(s[::-1])


a = "aviS"
for i in range(len(a)-1,-1,-1):
    print(a[i] , end="")

print()

x = "Hello World"
i = 1
reversed = ''
while i <= len(x):
    reversed+=x[-i]
    i+=1
print(reversed)
    
x = "Hello World"
i = len(x) -1
reversed = ''
while i >= 0:
    reversed+=x[i]
    i-=1
print(reversed)
    
    
def revrese_string(string):
    stack = []
    for el in string:
        stack.append(el)
    revrese_string = ""
    while stack:
        revrese_string+=stack.pop()
    return revrese_string

    # stack1 = []
    # while stack: # pop the all elements and push the popped elements in the new stack
    #     stack1.append(stack.pop())
    # return "".join(stack1)
    
string = "Hello World"
print(revrese_string(string))



