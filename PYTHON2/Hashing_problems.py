"""
1.First Non-repeated charecter
2.check anagram
3.find duplicates
4.intersection(where two objects meet) of two arrays
5.Check if Two arrays are Equal
6.Frequency of Element in an array
7.Longest substring without Reapiting Charecters"""

"""# # 1 First Non-repeated charecter======================="""
# def first_non_rep_char(s):
#     freq_map={}
#     for char in s:
#         freq_map[char] = freq_map.get(char,0)+1
#     for i, char in enumerate(s):
#         if freq_map[char]==1:
#             return i
#         return -1
# x=("Hello world")
# result=first_non_rep_char(x)
# print(result)

"""# 2.check anagram================================"""
# def is_anagram(s,t):
#     if sorted(s) == sorted(t):
#         print("True")
#     else:
#         print("False")
# a="listen"
# b="silent"
# print(is_anagram(a,b))

"""# 3. find duplicates=============================="""
# def find_dup(nums):
#     nums_set=list(set(nums))
#     if nums == nums_set:
#         return "False"
#     return "True"
# num=[1,2,3,1]
# print(find_dup(num))  

# nums=[1,2,3,4,2]
# nums_set=list(set(nums))
# if nums == nums_set:
#     print("False")
# else:
#     print("True")

"""# 4. intersection(where two objects meet) of two arrays==============="""
# def intersection(num1,num2):
#     x=set(num1)
#     y=set(num2)
#     return list(x.intersection(y))
# a=[1,2,2,2,4,5,2,3,1,4,5]
# b=[2,5,3,4]
# print(intersection(a,b))

"""#5. Check if Two arrays are Equal==========================="""
# def equal(arr1,arr2):
#     if len(arr1) != len(arr2):
#         return False
#     return True
# a=[1,2,3]
# b=[3,2,1]
# print(equal(a,b))


"""#6. Frequency of Element in an array"""
# def count(nums):
#     hash_table={}
#     for i in nums:
#         hash_table[i] =hash_table.get(i,0)+1
#     return hash_table
# a="siva","siva","ramu" "siva",#  10,12,10,10,20,20,30,12,20,40,40,50
# print(count(a))

"""7.Longest substring without Reapiting Charecters"""



"""8. Find missing elements"""
# def missing(nums,start,end):
#     new_list=set(range(start,end+1))
#     old_list=set(nums)
#     missing_ele = list(new_list - old_list)
#     return missing_ele
# arr=[0,3,6,9,11]
# start=0
# end=11
# print(missing(arr,start,end))


"""# Find the single element in an array where every elment appears twice except once"""

# def single_element(nums):
#     result=0
#     for num  in nums:
#         result^=num
#     return result
# nums=[4,1,2,1,2]
# print(single_element(nums))

"""# Count the number of vowels in a list"""

# words="Hello word"
# vowels="aeiouAEIOU"
# count = 0
# for word in words:
#     if word in vowels:
#         count +=1
# print(count)

"""array integers retuern two indices such they up add up to a specific target"""

# def sub_array(arr):
#     n = len(arr)
#     data=[]
#     for i in range(n):
#         for j in range(i,n):
#             subarray=arr[i:j+1]
#             data.append(subarray)
#     print(data)
# arr=[1,2,3,4]
# sub_array(arr)

"""Non-repesaating charcters"""
# def fisrt_non_repeating_char(string):
#     char_count={}
#     for char in string:
#         char_count[char]=char_count.get(char,0)+1
#     print(char_count)
#     for index,char in enumerate(string):
#         if char_count[char] == 1:
#             print(index,char)
# word="Helo"
# fisrt_non_repeating_char(word)




"""Count the number of prime numbers in array"""

# num=int(input())
# count=0
# for i in range(1,num+1):
#     if num%i == 0:
#         count+=1
# if count==2:
#     print("Prime number")
# else:
#     print("Not a prime Number")


# def is_prime(n):
#     if n <=1:
#         return False
#     for i in range(2,n):
#         if n % i == 0:
#             return False
#     return True
# def count_prime_num_array(arr):
#     count=0
#     for num in arr:
#         if is_prime(num):
#             count+=1
#     return count
# array=[1,2,3,4,5,6,7,8,9]
# print(count_prime_num_array(array))



# def count(s):
#     hash_table={}
#     for i in s:
#         hash_table[s]= hash_table.get(i,0)+1
#         print(hash_table)
# string="tree"
# print(sorted(string))

"""Find single element"""
# def single(nums):
#     result = 0
#     for num in nums:
#         result^=num
#     return result
# arr=[2,2,1,1,2]
# print(single(arr))


"""Find missing elements on range"""

# def missing(start,end,arr):
#     data=[]
#     for i in range(start,end+1):
#         data.append(i)
#     # print(data)
#     old=set(data)
#     new=set(arr)
#     missing=list(old-new)
#     return missing
# start=1
# end=10
# array=[2,4,6,7]
# print(missing(start,end,array))



# """find  fist non-repeat character"""
# def fist_non_repeat(str1):
#     dic={}
#     for i in str1:
#         if i in dic:
#             dic[i]+=1
#         else:
#             dic[i]=1
#     # print(dic)
#     for j in str1:
#         if dic[j] == 1:
#             return j
#         return -1
# for key,value in dic.items():
#     if len(set(dic.values())) == 1:
#         print("-1")
#         break     
#     else:
#         if dic.get(key) == 1:
#             print(f"Fist non-repeating character -> {key}")
#             break

# str1=input()#eehlo
# dic={}
# res=True
# for i in str1:
#     if i in dic:
#         dic[i]+=1
#     else:
#         dic[i]=1
# # print(dic)  { e:2,h:1,l:1,o:1}
# for key,value in dic.items():#key:e value=3
#     if value == 1:
#         print(key)
#         res=False
#         break
# if res==True:
#    print(-1)

# #eee {e:3}
    
# """check if two array equal or not"""

# arr1=[1,2,3]
# arr2=[1,2,3]
# if hash(tuple(arr1)) == hash(tuple(arr2)):
#     print("Equal")
# else:
#     print("Not equal")

# """Number of vowels in string  (normal way)"""

# string="welcome to hyderabad"
# vowels="aeiouAEIOU"
# count=0
# for i in string:
#     if i in vowels:
#         count+=1
# print(count)

# """Number of vowels in string  (Using Hashing)"""
# string="welcome to hyderabad"
# vowels={"a":0,"e":0,"i":0,"o":0,"u":0}
# count=0
# for i in string:
#      if i.lower() in vowels:
#           count+=1
# print(count)
     

# # python3 implementation
# def FirstNonRepeat(s):
# 	for i in s:
# 		if (s.find(i, (s.find(i)+1))) == -1:
# 			print("First non-repeating character is", i)
# 			break
# 	return 

# # __main__
# s = 'forfor'
# FirstNonRepeat(s)

   
"""find  fist non-repeat character"""
# str1="Hello"
# dic={}
# for i in str1:
#     if i in dic:
#         dic[i]+=1
#     else:
#         dic[i]=1
# # print(dic)
# for key,value in dic.items():
#     if len(set(dic.values())) == 1:
#         print("-1")
#         break
#     else:
#         if dic.get(key) == 1:
#             print(f"Fist non-repeating character -> {key}")
#             # break
    
"""check if two array equal or not"""

# arr1=[1,2,3]
# arr2=[1,2,3]
# if hash(tuple(arr1)) == hash(tuple(arr2)):
#     print("Equal")
# else:
#     print("Not equal")


# print(hash(tuple(arr1)))
# print(hash(tuple(arr2)))

"""Count number of vowels in string  (normal way)"""

# string="welcome to hyderabad"
# vowels="aeiouAEIOU"
# count=0
# for i in string:
#     if i in vowels:
#         count+=1
# print(count)

# """Count number of vowels in string  (Using Hashing)"""
# string="welcome to hyderabad"
# vowels={"a":0,"e":0,"i":0,"o":0,"u":0}
# count=0
# for i in string:
#      if i.lower() in vowels:
#           count+=1
# print(count)
    

# vowels="aeiou"
# dic={}
# for i in vowels:
#     result=dic[i] = 0
# # print(dic)
# count=0
# string2="welcome to hyderabad"
# for j in string2:
#     if j in dic:
#         count+=1
# print(count)


# vowels={"a","e","i","o","u"} # keys
# values=0
# dic=dict.fromkeys(vowels,values)
# string3="welcome to hyderabad"
# count=0
# for i in string3:
#     if i.lower() in dic:
#         count+=1
# print(count)


# arr1=(1,2)
# print(hash(arr1))
# arr2=(1,2)
# print(hash(arr2))

# x={"a","b"}
# y=1
# dic=dict.fromkeys(x,y)
# print(dic)

# def binary_search(arr,target):
#     low = 0
#     high = len(arr)-1
#     while low <= high:
#         mid = (low+high)//2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1
# arr=[1,2,3,4,5,6,7,8]
# target=
# result=binary_search(arr,target)
# print(result)

# def hash_function(arr,size):
#     return arr % size
# hashTable={}
# size=7
# keys=[10,12,14,16]
# for key in keys:
#     hash_values=hash_function(key,size)
#     hashTable[key]=hash_values
# print(hashTable)
    
# str1=[1,2,3,4]
# str2=[1,2,3,4]
# count=0
# for i in str1:
#     if i in str2:
#         count+=1
# if count == len(str2):
#     print("Equal")
# else:
#     print("Not equal") 

"""two array are eual or Not"""
# str1=[1,2,3,4]
# str2=[1,2,3,4]
# dic1={}
# dic2={}
# for i in str1:
#     if i in dic1:
#         dic1[i]+=1
#     else:
#         dic1[i]=1
# for j in str2:
#     if j in dic2:
#         dic2[j]+=1
#     else:
#         dic2[j]=1
# if dic1 == dic2:
#     print("Equal")
# else:
#     print("Not Equal")

"""Given a non-empty array of integers,  return the k most frequant elements"""
# def most_frequent(arr):
#     dic = {}
#     for i in arr:
#         if i in dic:
#             dic[i] += 1
#         else:
#             dic[i] = 1
#     max_ele = max(dic.values())
#     print(dic)
#     key = None
#     for k,v in dic.items():
#         if v == max_ele:
#             key = k
#             break
#     return f"most frequent number is k={key}"
# arr=[int(x) for x in input("Enter values here :").split()]
# result=(most_frequent(arr))
# print(result)


# num1 = [1,4,3]
# num2 = [4,2,3,]
# def intersection(num1,num2):
#      num1.sort()
#      num2.sort()
#      l =0
#      j =0
#      ans = []
#      while l<len(num1) and j<len(num2):
#          if num1[l]<num2[j]:
#              l+=1
#          elif num1[l]>num2[j]:
#              j+=1
#          else:
#              ans.append(num1[l])
#              l+=1
#              j+=1
#      return ans
# res = intersection(num1,num2)
# print(res)

"""check if a string contains all unique charecters uising hasing"""
# def all_unique_char(str1):
#     dic={}
#     for i in str1:
#         if i in dic:
#             dic[i]+=1
#         else:
#             dic[i]=1
#     print( dic)
#     if len(set(dic.values())) == 1:
#         return "all Unique characters"
#     else:
#         return "Not a unique characters"
# string=input("Enter a word here :").lower()
# print(all_unique_char(string))

# def intersection(arr1,arr2):
#    return set(arr1).intersection(set(arr2))
# arr1=[int(x) for x in input().split()]
# arr2=[int(x) for x in input().split()]
# print(intersection(arr1,arr2))

# def intersection(arr1,arr2):
#     arr1.extend(arr2)
#     print(arr1)
#     dic={}
#     for i in arr1:
#         if i in dic:
#             dic[i]+=1
#         else:
#             dic[i]=1
#     # return dic 
#     for key,value in dic.items():
#         if value >=2:
#             return key 
#     return key  
# arr1=[int(x) for x in input().split()]
# arr2=[int(x) for x in input().split()]
# print(intersection(arr1,arr2))

# dic={1,2,3,1}
# dic2={1,1,2}
# dic3=dic.intersection(dic2)
# print(dic3)




# arr=[3,2,3]
# n=len(arr)
# n=3
# a=3//3
# a=1
# Sowmya N
# 9:29 AM
# 3
# arr=[1,1,1,3,3,2,2,2]
# n=len(arr)
# Sowmya N
# 9:30 AM
# n=8
# a=n//3
# a=8//3
# a=2
# [1,2]

'''Find all elements in an array that appear more than n/3 times using hashing.'''
# def solve(k,arr):
#     dic={}
#     for i in arr:
#         if i in dic:
#             dic[i]+=1
#         else:
#             dic[i]=1
#     # print(dic)
#     n=len(arr)
#     a=n//k
#     ans=[]
#     for key,value in dic.items():
#         if value > a:
#             ans.append(key)
#     return ans
# arr=[int(x) for x in input().split()]
# k=3
# print(solve(k,arr))
"""given a non-empty array of integers, return the k most frequant elements"""

# d={}
# num=[1,1,1,4,2,2,3]
# k=2
# for i in num:
#   if i in d:
#     d[i]+=1
#   else:
#     d[i]=1
#   #{1:3,4:1,2:2,3:1}
# sorted_dic=sorted(d.items(),key=lambda x:x[1],reverse=True) # d[0]-keys d[1]-value 
# #sorted dic={1:3,2:2,4:1,3:1}
# topk=[]
# for top in sorted_dic[:k]:
#    topk.append(top[0]) 
# print(topk)



"""1. Given a string, sort it in decreasing order based on the frequency of characters."""
# def decreasing(str1):
#     dic={}
#     for i in str1:
#         if i in dic:
#             dic[i]+=1
#         else:
#             dic[i]=1
#     sorteds = sorted(dic.items(), key =lambda x:x[1],reverse=True)
#     un_zip =zip(*sorteds)
#     list1,list2 = tuple(un_zip)
#     result = ''.join(list1)
#     return result
# str1="siva"
# result=decreasing(str1)
# print(result)

# def decreasing_order(num):
#     d = {}
#     for i in num:
#         if i in d:
#             d[i] += 1
#         else:
#             d[i] = 1
#     sorteds = sorted(d.items(), key = lambda x :x[1],reverse = True)  #x[1] = values
#     return sorteds
# num = "shaburdhin"
# res = decreasing_order(num)
# print(res)

""" 3. Find missing elements of a range"""
# def missing(arr):
#     start=arr[0]
#     end=arr[-1]
#     missing=[]
#     for i in range(start,end+1):
#         if i in arr:
#             pass
#         else:
#             missing.append(i)
#     return missing
# arr=[1,3,5,7]
# print(missing(arr))

# # 0r
# nums=[1,3,5,7]
# miss = [x for x in range(nums[0],nums[-1]+1) if x not in nums]
# print(miss)


''' 2. Count the number of prime numbers in tha array'''
# def is_prime(s):
#     if s <= 1:
#         return False
#     for i in range(2,s):
#         if s%i == 0:
#             return False
#     return True
# count=0
# arr=[1,2,3,4,5,6,7,8,9,10]
# for num in arr:
#     if is_prime(num):
#         count+=1
# print(count)
# #     #     print("prime Number")
# #     # else:
# #     #     print("Not a prime number")


""" Given a non-empty array of integers nums, every element appears twice except for one. Find that single one."""
# def single(arr):
#     dic={}
#     for i in arr:
#         if i in dic:
#             dic[i]+=1
#         else:
#             dic[i]=1
#     for k,v in dic.items():
#         if v == 1:
#             return f"{k} is the single element in array  "
# arr=[int(x) for x in input().split()]
# print(single(arr))
    
# def missing(arr):
#     result = 0
#     for i in arr:
#         result ^= i
#     return result
# arr=[1,1,2,2,3]
# print(missing(arr))


# def fact(n):
#     if n==1:  # n<=1
#         return 1 # n
#     else:
#         return n*fact(n-1)
# n=5
# print(fact(n))