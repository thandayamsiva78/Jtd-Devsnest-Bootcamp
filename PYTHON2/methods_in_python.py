# 1. enumarate()
# 2. zip()
# 3. map()
# 4. sorted()
# 5. filter()
""" 1. enumarate()========================================================================"""
# enumarate() is a built in python function that allows you to iterate over a sequence (such as a list,tuple or String)
# while also keeping track of the index of each item
#  syntax(iterable,start=0)
# for index,item in enumarate(iterable): you get pairs of index and item
fruits=["apple","banana","orange"]
for index,fruits in enumerate(fruits):
    # print(f"index{index}:{fruits}")
    print(index,fruits)

my_list=[1,2,3,4,5]
for index,my_list in enumerate(my_list):
    print(index,my_list)

""" 2. zip()==============================================================================="""
# syntax : zip(iterable1,iterable2,...) the iterable that you want zip together
list1=[12,13,14,15]
list2=[16,17,18,19]
for l,m in zip(list1,list2):
    print(l,m)
    
names=["alice","bob","charlie"]
age=[21,25,35]
merged=list(zip(names,age))
print(merged)

for x,y in zip(names,age):
    print(x,y)

# combining list into dictionary
keys=["a,","b","c"]
values=[1,2,3]
dictionary=dict(zip(keys,values))
print(dictionary)

# transposed a Matrix
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
trasposed=list(zip(*matrix))
print(trasposed)

# processsing Multiple lists in a loops
names=["alice","bob","charlie"]
age=[21,25,35]
grade=["A","C","B"]
for x,y,z in zip(names,age,grade):
    print(f"{x} age is {y} and his grade:{z}")

# unzipping a list of tuple
pairs=[(1,'a'),(2,'b'),(3,'c')]
nums,letters=zip(*pairs)
print(nums)
print(letters)


""" 3. map()==========================================================================="""
# map() is a built in python function used to apply functions to all items in an iterable (like list) and returns a new iterable with the results.
def square(n):
    return n*n
numbers=[1,2,3,4,5,6]
squared_nums=map(square,numbers)
squared_nums_list=list(squared_nums)
print(squared_nums_list)

# Converting temperaturs into Celsius
def celsius_to_temp(celsius):
    return (celsius * 9/5)+32
temperatures=[0,10,20,30,40,50]
temp_cel=map(celsius_to_temp,temperatures)
temp_cel_list=list(temp_cel)
print(temp_cel_list)

# Capitalizing for each word in a list of strings
  
words=["hello","world","python"]
capitalized=map(str.capitalize,words)
capitalized_list=list(capitalized)
print(capitalized_list)

word=["radha","krishna","rama","seeths"]
upper_word=map(str.upper,word)
upper_word_list=list(upper_word)
print(upper_word_list)
    
# Squaring each element of a matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
squared_matrix = map(lambda row: list(map(lambda x: x ** 2, row)), matrix)

# Convert the map object to a list of lists
squared_matrix_list = [list(row) for row in squared_matrix]

print(squared_matrix_list)  # Output: [[1, 4, 9], [16, 25, 36], [49, 64, 81]]
       
"""4. sorted()======================================================================="""
# # is a built in python function used to sort functions, such as lists,tuples and strings.
# # It returns a new sorted list while leaving the original sequence unchanged
# # Sorting a list
# my_list=[3,1,4,1,5,9,2,6,5]
# sorted_list=sorted(my_list)
# print(sorted_list)

# # Sorting a tuple
# my_tuple=(1,2,3,4,5)
# sorted_tuple=sorted(my_tuple)
# print(sorted_tuple)

# # Sorting a srting
# my_string="hello"
# sorted_string=sorted(my_string)
# print(sorted_string)

# # sort in descending order
# my_list=[3,1,4,1,5,9,2,6,5]
# sorted_list_desc=sorted(my_list,reverse=True)
# print(sorted_list_desc)

## sorting based on absolute values
# my_list=[3,-1,4,-1,5,-9,2,-6,5]
# sorted_list_abs=sorted(my_list,key=abs)
# print(sorted_list_abs)
### normal 
# my_list=[3,-1,4,-1,5,-9,2,-6,5]
# sorted_list_abs=sorted(my_list)
# print(sorted_list_abs)

# my_list=[3,-1,4,-1,5,-9,2,-6,5]
# my_list.sort()
# print(my_list)

"""5. filter()========================================================================"""
# filter() id python built in function that is used to construct an iterator from elements of an iterable for
# which a function return true.

# def is_even(n):
#     if n % 2 == 0:
#         return n
# numbers=[1,2,3,4,5,6,7,8,9,10]
# even_list=filter(is_even,numbers)
# result=list(even_list)
# print(result)