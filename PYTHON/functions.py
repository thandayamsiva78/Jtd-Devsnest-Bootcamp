# in python , the function is a block of code  difined with a name.
# -> A Function is a block of code that only runs when it is called
# -> you can pass the data , known as parameters, into a function
# -> Functions are used to perform specific a ctions nd rhey are also knowns as methods

"""why use function"""
# To reuse Code : Difine the code Once and use it many times


# # calling a function

# def disply(str1):
#     """this displays a passed string into the function"""
#     print(str1)
   
# disply("Hello world")

# def name(n):
#     print( 'Hii' ,n)
# name("Siva")

# passing by referene by value
def changelist(alist):
    """this changes a passed list into this function"""
    print("list element inside the function before change:",alist)
    alist[2]=25
    print("list element inside the function after change:",alist)
    return
alist=[10,20,30,40,50,60]
print('Before calling function , list elemenet are:',list)
changelist(alist)
print("after calling function , list element are:",list)

def add_ele(nums):
    nums[3]=100
    return nums
x=[2,3,4,5,6,7,8,9]
print(add_ele(x))

# pass by value
def changevalue(a):
    """this changes a passed value into this function"""
    print("value of a inside the function before change:",a)
    a+=1
    print("value of a inside the function after change:",a)
    return
changevalue(2)


def solve(a):
    a+=1
    print(a)
x=3
solve(x)

# scope of variable 
