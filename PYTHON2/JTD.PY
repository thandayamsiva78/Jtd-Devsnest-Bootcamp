"""## 1. Prime number or Not"""
# num=int(input())
# count=0
# for i in range(1,num+1):
#     if num >1:
#         if num%i == 0:
#             count +=1
# if count == 2:
#     print("Prime Number")
# else:
#     print("Not a prime number")


"""## number positive or Not"""
# num=int(input())
# if num >0:
#     print("Positive Number")
# elif num ==0:
#     print("given number is 0")
# else:
#     print("Negative number")

"""## number Even or Odd:"""
# num=int(input())
# if num % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")
"""
## Prime number or not"""
# num=int(input())
# count=0
# for i in range(1,num+1):
#     if (num%i) == 0:
#         count+=1
# if count ==2:
#     print("Prime number")
# else:
#     print("Not a prime number")

"""## number is an armstrong number or not"""

# nums=input()
# len_nums=len(nums)
# data=[]
# for i in nums:
#     each_digit_power=int(i)**len_nums
#     data.append(each_digit_power)
#     # print(data)
#     sum_data=sum(data)
#     # print(sum_data)
# if sum_data == int(nums):
#     print("Armstrong Number")
# else:
#     print("Not a Armstrong number")    

"""## print all elements in array"""
# array=[int(x) for x in input().split()]
# print(array)

"""## product of all elements"""
# def product_of_array(arry):
#     product=1 
#     for i in arry:
#         product *=i
#     return product
# nums=[int(x) for x in input().split()]
# result=product_of_array(nums)
# print(result)

"""## convert integer to string"""

# nums=int(input())
# print(nums)
# print(type(nums))
# int_to_string=str(nums)
# print(int_to_string)
# print(type(int_to_string))

"""## reverse string"""
# string="Hello python"
# print(string[::-1])

# string="Hello python"
# while True:
#     print(string[::-1])
#     break

# string="Hello python"
# len_string=len(string)
# while len_string > 0:
#     reverse=string[len_string-1]
#     print(reverse,end="")
#     len_string -=1

"""
## find a string whether contains alphanumeric or not"""
# def alphanumeric(string):
#     return string.isalnum()
# test_string="heloo"
# result=alphanumeric(test_string)
# print(result)


"""## rearanging the array"""
# arr=[2,3,4,6,5,1,8]
# filtered_list=[x for x in arr if x %2 ==0]
# # print(filtered_list)
# remaining_list=[x for x in arr if x not in filtered_list]
# # print(remaining_list)
# new_list=filtered_list+remaining_list
# print(new_list)

# def rearange(array):
#     even_arr=[x for x in array if x %2==0]
#     odd_arr=[x for x in array if x %2 != 0]
#     return even_arr + odd_arr
# arr=[2,3,4,6,5,1,8]
# print(rearange(arr))

"""# sum of digts"""
# def sum_of_digit(nums):
#     if nums ==0:
#         return 0
#     else:
#         return nums % 10 + sum_of_digit(nums//10)
# array=124
# print(sum_of_digit(array))

# nums="12345"
# count=0
# for i in nums:
#     count+=int(i)
# print(count)

"""## Convert integer into a Binary"""

# integer=12345
# binary_representation=bin(integer)
# print(binary_representation)

# num=123
# x=bin(num)
# print(x)

"""## product of all even numbers present in an array"""

# arr=[1,2,3,4,5,6,7,8,9]
# data=[]
# product=1
# for i in arr:
#     if i %2 ==0:
#         even_num=i
#         data.append(even_num)
# for j in data:
#     product*=j
# print(product)

"""## whether a string is palindrome or not"""
# def is_palidromic(s):
#     s=s.replace("","").lower()
#     return s == s[::-1]
#     #     return "Palidromic"
#     # else:
#     #     return "Not a Palidromic"
# string="A man a plan a canal panama"
# if is_palidromic(string):
#     print("Palidromic")
# else:
#     print("Not a Palidromic")

# string="ammaa"
# s=string.replace("","").lower()
# print(s)

"""# A man a plan a canal panama"""
# rows=5
# for i in range(1,rows+1):
#     print(" "*(rows-i),end="")
#     for k in range(1,i+1):
#         print(k,end="")
#     for j in range(i-1,0,-1):
#         print(j,end="")
#     print()

"""## reverse all words present in a string"""

# def reverse_string(string):
#     splitted_words="".join(string[::-1])
#     return splitted_words
# words= "Welcome to the JTBB bootcamp"
# print(reverse_string(words))

"""## print two indices of two numbers present in an array ,whose sum is equal to target"""
# array=[2,3,4,6,8,1]
# target=14
# for i in range(len(array)):
#     if array[i] + array[i+1] == target:
#         print(i,i+1)
#         break

"""
## factorial of number"""
# num=10
# product=1
# for i in range(num,0,-1):
#     product*=i
# print(product)

# def fact(n):
#     if n <=1:
#         return n
#     else:
#         return n* fact(n-1)
# num=10
# print(fact(num))

"""## Find anagram or not"""
# def anagram(str1,str2):
#     if sorted(str1) == sorted(str2):
#         return "The given string is a anagaram"
#     return " Not a anagram"
# word1="angel"
# word2="glean"
# print(anagram(word1,word2))

"""## find 3rd largest element and 2nd smallest element"""

# array=[3,8,19,3,2,7,6]
# new_array=list(set(array))
# third_max=new_array[-3]
# second_smal=new_array[1]
# print(third_max,second_smal)
"""
## count all vowel and Consonents"""

"""leap year or not"""
# year=2017
# if year % 4==0 or year% 400 ==0:
#     print("Leap year")
# else:
#     print("Not a Leap year")

"""Simple interset and Compound interest"""
# principle = 1000
# rateOf_interest= 15/100
# time= 3

# simple_interset=(principle*(rateOf_interest))*3
# print(simple_interset)

# ## Compound interest =principle * [(1+rate)^time-1]
# compound_interest=principle *(1+rateOf_interest)**3
# print(compound_interest)

"""print indices of three numbers present in array whose sum equal to target value"""
# def sum_equal(arr,target):
#     for i in range(len(arr)):
#         if arr[i] + arr[i+1] + arr[i+2] == target:
#             return i,i+1,i+2
# nums=[2,3,4,6,8,1]
# key=13
# print(sum_equal(nums,key))

"""Write a program to print all border element present in a 2d array"""
# mat=[
#     [1,3,4],
#     [6,3,2],
#     [9,2,10]
# ]

# print(mat[0][0],mat[1][0],mat[2][0],mat[2][1],mat[2][2],mat[1][2],mat[0][2],mat[0][1])

""" caluculate a sum of left diagonal and right diagonal elements presents in 2d array"""
mat=[
    [1,3,4],
    [6,3,2],
    [9,2,10]
]

            
""" print Z traverasal elements present in an array"""
# mat=[
#     [1,3,4],
#     [6,3,2],
#     [9,2,10]
# ]

# print(mat[0][0],mat[0][1],mat[0][2],mat[1][1],mat[2][0],mat[2][1],mat[2][2]) 
    
""" print N traverasal elements present in an array"""
# mat=[
#     [1,3,4],
#     [6,3,2],
#     [9,2,10]
# ]

# print(mat[2][0],mat[1][0],mat[0][0],mat[1][1],mat[2][2],mat[1][2],mat[0][2])

"""sum of max and min elements present in an array is even or odd"""
# def even_odd(arr):
#     maxi=max(arr)
#     mini=min(arr)
#     maxi_mini=maxi+mini
#     if maxi_mini % 2 == 0:
#         return "Even number"
#     return "Odd Number"
# nums=[3,8,19,3,2,7,6]
# print(even_odd(nums))

"""sort an array in the descending order without an inbuilt sort method"""
# def bubble_sort(arr):
#     n= len(arr)
#     for i in range(n):
#         for j in range(0,n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1],arr[j]
#     return arr[::-1]
        
# nums=[2,8,6,5,9,4,7]
# print(bubble_sort(nums))

"""print the occurence of every element present in an array"""
# def ocurence(arr):
#     hash_table={}
#     for i in arr:
#         hash_table[i]= hash_table.get(i,0)+1
#     return hash_table
# nums=[2,5,6,5,6,9,9,7,2,9]
# print(ocurence(nums))

# add two 2d arrays
# mat1=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# mat2=[
#     [9,8,7],
#     [6,5,4],
#     [3,2,1]
# ]

# result=[[0,0,0,]for _ in range(len(mat1))]

# for i in range(len(mat1)):
#     for j in range(len(mat1[0])):
#         result[i][j]=mat1[i][j] + mat2[i][j]
# # print(result)
# for row in result:
#     print(row)
    

""" print all even length words present in the sentence"""
# string="JTD is running JTBB Bootcamp"
# str_splitted=string.split()
# # print(str_splitted)

# for index,word in enumerate(str_splitted):
#     # print(index,word)
#     len_word=len(word)
#     if len_word % 2 == 0:
#         print(str_splitted[index])

"""removing the leading zero prsent in a string"""
# integer="00000123569"
# for i in integer:
#     if int(i) > 0:
#         print(i,end="")

"""Compare two strings based on ASCII values od a charecters"""

# string1="jtd"
# string2="jtd"
# data1=[]
# data2=[]
# for i in string1:
#     x=ord(i)
#     data1.append(x)
# # print(data1)
# for j in string2:
#     y=ord(j)
#     data2.append(y)
# # print(data2)
# if sum(data1)==sum(data2):
#     print("0")
# elif sum(data1)>sum(data2):
#     print("Positive number")
# else:
#     print("Negative number")


""" transpose a given 2D Array"""
# mat=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# x=mat[0]
# y=mat[1]
# z=mat[2]
# output=list(zip(x,y,z))
# print(output)


"""pattern """
# rows=6
# space=rows
# for i in range(1):
#     print("* "*rows)
# for j in range(rows-2):
#     print("* "," "*space,"*")
# for i in range(1):
#     print("* "*rows)
    
# rows=4
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print("*",end="")
#         print("_",end="")
#     # for k in range(2,i+1):
#     #     print("_",end="")
#     print()


# arr=[1,2,3,4,5,6,7,8,9,10]

# count1=0
# count2=0
# count3=0
# for i in range(len(arr)):
#     if arr[i] % 2 ==0:
#         count1+=1
#     elif arr[i] % 2 !=0:
#         count2+=1
# for j in range(arr):
#     if j % i == 0:
#         count3+=1
# # if count3 == 2:
              
# print("Even numbers,",count1)
# print("Odd Numbers ,",count2)
# print("Prime Numbers",count3)

# if i >0:
#         if arr[i] % 2 == 0:
#             count1+=1
#         if count1 == 2:
#             print("Prime number ",count1)

"""reverse all words present in a string"""
# words="Welcome to the JTBB bootcamp"
# new_list=words.split()
# for index,word in enumerate(new_list):
#     print(word[::-1],end=" ")

        
"""Palidrome pattern"""
# rows=5
# for i in range(rows+1):
#     print(" "*(rows-i),end="")
#     for j in range(1,i):
#         print(j,end="")
#     for k in range(i,0,-1):
#         print(k,end="")
#     print()

""" find prime number in array"""
# num=[int(x) for x in input().split()]
# for j in num:
#     count=0
#     for i in range(1,j+1):
#         if j>1:
#             if (j%i) == 0:
#                 count+=1
#     if count == 2:
#         print(i,"Prime Number")
#     # else:
#     #     print("Not a prime Number")
   
"""sort an array"""
# def bubble(arr):
#     n=len(arr)-1
#     for i in range(n):
#         for j in range(0,n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1],arr[j]
#     return arr
# array=[0,1,2,0,1,2]
# print(bubble(array))

# arr=[0,1,2,0,1,2]
# sorted_arr=sorted(arr)
# print(sorted_arr)

"""negative num left side Positive Number right side"""
# arr=[0,-10,8,-20,-1,3,-9]
# print(sorted(arr))


# arr=[0,-10,8,-20,-1,3,-9]
# list1=[]
# list2=[]
# for i in arr:
#     if i < 0:
#         list1.append(i)
#     if i >= 0:
#         list2.append(i)

# print(list1+list2)

"""count x=2 the number acuureces of x in arr"""
# arr=[1,1,2,2,2,2,3]
# x=2
# count=0
# for i in arr:
#     if x == i:
#         count+=1
# print(count)

# def count_arr(arr):
#     my_dict={}
#     for i in arr:
#         my_dict[i] = my_dict.get(i,0)+1
#     return my_dict
# array=[1,1,2,2,2,2,3]
# print(count_arr(array))

"""union of two sorted arrays"""
# arr1=[1,3,4,5,7]
# arr2=[2,3,5,6]
# arr1.extend(arr2)
# print(list(set(arr1)))

"""find intersection of two sorted arrays"""
# num1=[1,3,4,7,5]
# num2=[2,3,5,6]
# intersection=[value for value in num1 if value in num2]
# print(intersection)

"""peak element which not smaller than its neibours"""

# array=[5,10,20,15]
# peak_ele=max(array)


"""misssing Number"""
# arr=[11,14,13,19]
# start=min(arr)
# end=max(arr)
# data1=[]
# for i in range(start,end+1):
#     data1.append(i)
# missing=set(data1)-set(arr)
# print(list(missing))
    
"""find common element present in a list"""
# arr1=[1,5,10,20,40,80]
# arr2=[6,7,20,80,100]
# arr3=[3,4,15,20,30,70,80,120]
# data=[]
# for i in arr1:
#     for j in arr2:
#         for k in arr3:
#             if i==j==k:
#                 data.append(i)
# print(data)


"""Find missing Number"""
# array=[1,3,4,6]
# min_ele=min(array)
# max_ele=max(array)
# data=[]
# for i in range(min_ele,max_ele+1):
#     data.append(i)

# missing=set(data) - set(array)
# print(missing)

"""if String palidrome or  not"""
# def is_palidrome(str1):
#     return str1 == str1[::-1]
# string="madam"
# if is_palidrome(string):
#     print(f"{string} is palidrome")
# else:
#     print(f"{string} Not a palidrome")

"""palidrome words present in a sentence"""
# sentence="madam speak malayalam fluency"
# substrings=sentence.split(" ")
# for i in substrings:
#     if i == i[::-1]:
#         print(i,end=" ")

"""kth missing number in array"""
# arr=[2,3,5,9,10,11,12]
# k=4
# min_ele=min(arr)
# max_ele=max(arr)
# data=[]
# for i in range(min_ele,max_ele):
#     data.append(i)
# print(data)
# for j in range(len(data)):
#     if j == k:
#         print(data[k])

"""missing largest number"""
# arr=[2,3,7,6,8,-1,-10,15]
# start=min(arr)
# end=max(arr)
# data=[]
# for i in range(start,end+1):
#     data.append(i)
# missing_ele=set(data) - set(arr)
# largest_ele=max(missing_ele)
# print(largest_ele)

"""matrix"""
# mat=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# def print_full_name(first, last):
#     sentence=(f"Hello {first} {last} You just delved into python.")
#     return sentence

# first = input()
# last = input()
# result=print_full_name(first, last)
# print(result)

"""interchange first ele swap to last ele"""
# num1=[12,35,9,56,24]
# num2=[1,2,3]

# num1[0],num1[-1] = num1[-1],num1[0]
# print(num1)

# # num2[0],num2[-1] = num2[-1],num2[0]
# # print(num2)

# # num=[12,35,9,56,24]
# # temp=num[0]
# # num[0] = num[-1]
# # num[-1] = temp
# # print(num)


"""find sum & average"""
# # normal way
# arr=[2,7,5,64,14]
# count=0
# for i in arr:
#     count+=i
# print("sum of arr :",count)

# # use in built in function
# sum_of=sum(arr)
# print("sum of arr :",sum_of)

# #  find average
# average=sum(arr)/len(arr)
# print("Average of arr :",average)

"""second largest number"""

# array=[2,7,5,64,14]
# array.sort()
# second_largest=array[-2]
# print(second_largest)

# # all test cases
# array=[2,7,5,64,64,14,14]
# my_list=list(set(array))
# my_list.sort()
# second_largest=my_list[-2]
# print(second_largest)

"""count Even & Odd"""
# list1=[2,7,5,64,14]
# even_count=0
# odd_count=0
# for i in list1:
#     if i % 2 == 0:
#         even_count+=1
#     else:
#         odd_count+=1        
# print("Even =",even_count)
# print("Odd =",odd_count)

# """count unique values inside a list"""
# my_list=[1,3,2,4,5,4,3]
# unique_values=len(set(my_list))
# print("unique values :",unique_values)


# set1={1,2,3}
# # set1.update({8})
# # print(set1)
# set2={4,5,6}
# print(set1 | set2)

# my_set1={1,2,3,4}
# my_set2={2,3}
# print(my_set1 & my_set2) # common element
# print(my_set1.intersection(my_set2)) # common element
# print(my_set1.union(my_set2))
# print(my_set1.difference(my_set2)) # difference

# set1={1,2,3,4}
# max_ele=max(set1)
# set1.remove(max_ele)
# second_ele=max(set1)
# print(second_ele)


"""count frequancy of numbers"""
# arr ="Siva"
# my_dict={}
# for i in arr:
#     if i in my_dict: # incremenet
#         my_dict[i]+=1
#     else:
#         my_dict[i]=1 # intilization
# print(my_dict)


arr=["a","e","i",]
dic={}
for i in arr:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
print(dic)