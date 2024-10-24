# Calculate the nth Fibonacci number using recursion. ---Que no 5
# input : n = 6
# Output: 8
# def fibo(n):
#     if n == 1 or n == 0:  # n <= 1
#         return n
#     else:
#         return fibo(n-1) + fibo(n-2)
# x = 6
# print(fibo(x))


# Check if two strings are anagrams using hashing.----- Que no 3
# input : str1 = listen, str2 = silent
# Output: yes

# str_1 = "listen"
# str_2 = "silent"
# if hash(str_1) and hash(str_2):
#     print("Yes")
# else:
#     print('No')

# Write a function to count the number of vowels in a string-----Que no 4
# input : str = I love coding
# Output: 5
# count = 0
# string = "I love coding"
# vowels = "aeiouAEIOU"
# for j in vowels:
#     # print(j)
#     for i in string:
#         if j in i:
#             count = count + 1
#             # print(i, j)
# print(count)






##   1.
# array=[12,13,14,15,16,17,18,19]
# largest_ele=max(array)
# print(largest_ele)

##  2. 
# array=[12,13,14,15,16,17,18,19]
# smallest_ele=min(array)
# print(smallest_ele)

##  3.
# age=12
# if age >=18:
#     print("Your eligible to vote")
# else:
#     print("Your not eligible to vote")

##  4.
# age=65
# if age >=60:
#     print("Seniour citizen")
# else:
#     print("your age below 60 ")

##  5. lowest number
# a=int(input("Enter  a Number :"))
# b=int(input("Enter  a Number :"))
# if a > b:
#     print(b)
# else:
#     print(a)

## 6. Highest number
# a=int(input("Enter  a Number :"))
# b=int(input("Enter  a Number :"))
# if a > b:
#     print(a)
# else:
#     print(b)

##  7. Positive or not
# num=int(input("Enter  a Number :"))
# if num > 0:
#     print("Positive number")
# elif num == 0:
#     print("it is 0")
# else:
#     print("Negative number")


## 8. even or odd

# num=int(input("Enter  a Number :"))
# if num % 2 == 0:
#     print('Even number')
# else:
#     print("Odd number")

# print(6%2)
# print(5%2)

## 9.

# nums=[int(x) for x in input().split()]
# average=(sum(nums)/len(nums))
# print(average)

## 10. 0dd number
# array=[1,2,4,5,5,7,8,9,3]
# for i in range(len(array)): # 9
#     if array[i] % 2 == 1:
#         print(array[i])


## 11.
# rows=4
# for i in range(1,rows+1): # outer loop 4 (1,5)
#     for j in range(1,i+1): # inner loop 1  # inner loop will be excuted one time for each iterartion of the outer loop (1,5)  = 1,2,3,4 
#         print(j,end="")
#     print()

## 12.
# rows=5
# for i in range(rows,0,-1): # 1,2,3,4,5  
#     for j in range(1,i+1):  # (1,4)= 1,2,3
#         print("*",end="")
#     print()

## 13

# rows=4
# for i in range(rows): # 0,1,2,3
#     print(" "*(rows-i),end="")
#     for j in range(rows): # 0,1,2,3
#         print("*",end="")
#     print()


## 14.
# numbers_list=[3,5,7,2,8,5]
# numbers_list.append(20)
# print(numbers_list)

# def binary_search(arr,target):
#     low=0
#     high=len(arr)-1
#     while low <= high:
#         mid = (low+high)//2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1
# array=[1,2,3,4,5]
# key = 3
# result=binary_search(array,key)
# if result != -1:
#     print(result)
# else:
#     print("-1")


# arr=[1,2,3]
# k=5
# for i in range(len(arr)-1):
#     if arr[i] + arr[i+1] == k:
#         print(i,i+1)


# arr=[1,2,3]
# data=[]
# for i in range(len(arr)):
#     for j in range(i+1+1):
#         data.append(j)
# print(data)


# def sub_array(arr):
#     data=[]
#     n = len(arr)
#     for i in range(n):
#         for j in range(i,n):
#             subarray=arr[i:j+1]
#             data.append(subarray)
#     print(data)
#     for index,ele in enumerate(data):
#         if sum(ele) == 3:
#             print(index)
# arr=[1,2,3]
# sub_array(arr)

# 5.Given a sorted array of integers, write a function to perform binary search to find a specific target value. If the target is found, return its index; otherwise, return -1.
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
# my_list =[4,1,3,2]
# key = 3
# result = binary_search(my_list,key)
# print(result)

# 3.Write a recursive function to find the sum of digits of a positive integer.

# def digits(s):
#     if s == 0:
#         return 0
#     else:
#         return s%10 + digits(s//10)
# nums=456
# result=digits(nums)
# print(result)

# arr=[1,2,3,4,5,6,7,8,9,10]
# data=[]
# for i in arr:
#     if i % 2 != 0:
#         data.append(i)
# print(data)


# def reverse(s):
#     return s[::-1]
# s="aviS"
# print(reverse(s))



"""Positive & Negative Numbers"""
# nums=[1,2,4,5,-2,-1,-3,-6]
# pos_num=[]
# neg_num=[]
# for i in nums:
#     if i > 0:
#         pos_num.append(i)
#     else:
#         neg_num.append(i)
# print(pos_num)
# print(neg_num)


"""Find valid email or not"""
# email=input("Enter Email ID :")
# emailid="@gmail.com"
# if emailid in email:
#     print("Valid Email ID")
# else:
#     print("WRONG Email ID given  \nEnter a Valid Email ID")

"""Find prime number or not"""
# def is_prime(s):
#     if s<= 1:
#         return False
#     for i in range(2,s):
#         if s % i == 0:
#             return False
#     return True
# num=int(input("Eneter a number :"))
# if is_prime(num):
#     print("Prime Number")
# else:
#     print("Not a prime Number")

        

# def is_prime(s):
#     if s<= 1:
#         return False
#     for i in range(2,s):
#         if s % i == 0:
#             return False
#     return True
# num=int(input("Eneter a number :"))
# if is_prime(num):
#     print("Prime Number")
# else:
#     print("Not a prime Number")

"""two sum"""
# # time ncomplexity O(n^2)
# def solve(nums,tar):
#     for i in range(len(nums)):
#         for j in range(0,len(nums)):
#             if nums[i] + nums[j] == tar:
#                 return [i,j]
# numbers =[2,3,4,5]
# target = 6
# result = solve(numbers,target)
# print(result)

# time ncomplexity O(log n)
# def solve(num,target):
#     low = 0
#     high = len(num)-1
#     while low < high:
#         total = (num[low]+num[high])
#         if total == target:
#             return [low+1,high+1]
#         elif total < target:
#             low +=1
#         else:
#             high-=1
# numbers =[2,3,4,5]
# target = 6
# result = solve(numbers,target)
# print(result)






# # time complexity  O(n)
# def linearSearch(arr,target):
#     for i in range(len(arr)): 
#         if arr[i] == target:  
#             return i
#     else:
#         return -1
# numbers =[int(x) for x in input().split()]
# key = 3
# result=linearSearch(numbers,key)
# print(result)

# # time complexity  O(log n)
# def BinarySearch(arr,target):
#     low = 0
#     high = len(arr) -1  
#     while low <= high:
#         mid = (low+high)//2   # 5
#         if arr[mid] == target:
#             # 4 == 6 F
#             # 5 == 6 F
#             # 6 == 6 T
#             return mid # 5
#         elif arr[mid] < target:
#             # 4 < 6 T
#             # 5 < 6 T
#             low = mid + 1 # 4+1 = 5
#         else:
#             high = mid - 1
#     return -1

# numsbers = [5,7,3,1,2,6,4] 
# sort_num = sorted(numsbers)  # [1, 2, 3, 4, 5, 6, 7]
# print(sort_num)
# key = 6
# result = BinarySearch(sort_num,key)
# print(result)

# def most_frequent(arr):
#     dic = {}
#     for i in arr:
#         if i in dic:
#             dic[i] += 1
#         else:
#             dic[i] = 1
#     return dic

# arr = [1,1,2,2,3,4,4,4,4,6]
# print(most_frequent(arr))

# in python , the function is a block of code  difined with a name.
# -> A Function is a block of code that only runs when it is called
# -> you can pass the data , known as parameters, into a function
# -> Functions are used to perform specific a ctions nd rhey are also knowns as methods

"""why use function"""
# To reuse Code : Difine the code Once and use it many times

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# def solve(l1, l2):
#     curr = 0
#     dummy = Node(0)
#     ans = dummy

#     while l1 or l2 or curr:
#         l1data = l1.data if l1 else 0
#         l2data = l2.data if l2 else 0
#         total = curr + l1data + l2data
#         curr = total // 10
#         digit = total % 10
#         ans.next = Node(digit)
#         ans = ans.next
#         if l1:
#             l1 = l1.next
#         if l2:
#             l2 = l2.next

#     return dummy.next
# Node1 =Node()
# l1 = [2,4,3]
# l2 = [5,6,7]
# result = solve(l1,l2)
# print(result)

 #0+2+5=7  #4+6+0=10  #1+3+4=8
 #7//10=0  #10//10=1  #8//10=0
 #7%10=7   #10%10=0   #8%10=8

# def solve(nums, target):
#     for i in range(len(nums)):
#         if nums[i] == target:
#             return i
#     return -1

# nums=[2,7,8,5,0,1]
# target = 5
# print(solve(nums,target))

# even = []
# odd = []
# for i in range(1,100+1):
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(even , end= "")
# print(odd, end="")
        
# class Node:
#     def __init__(self , data) -> None:
#         self.data = data
#         self.left = None
#         self.right = None
# # def levelorder(root):
# #     q = []
# #     q.append(root)
# #     while len(q) > 0:
# #         root = q.pop(0)
# #         print(root.data , end= " ")
# #         if root.left:
# #             q.append(root.left)
# #         if root.right:
# #             q.append(root.right)
        
# def is_minheap(root):
#     if root is None:
#         return True
#     if root.left is None and root.right is None:
#         return True
#     if root.left is not None and root.data  <= root.left.data :
#         return True
#     if root.right is not None  and root.data  <= root.right.data :
#         return True
#     return  is_minheap(root.left)  and is_minheap(root.right)

# def is_complete_binarytree(root):
#     if not root:
#         return True
#     queue = []
#     queue.append(root)
#     flag = False
#     while queue:
#         current = queue.pop(0)
#         if current.left:
#             if flag:
#                 return False
#             queue.append(current.left)
#         else:
#             flag = True
#         if current.right:
#             if flag:
#                 return False
#             queue.append(current.right)
#         else:
#             flag = True
#     return True

# root = Node(1)
# root.left = Node(3)
# root.right = Node(6)
# root.left.left = Node(5)
# root.left.right = Node(9)
# root.right.left = Node(8)
# root.right.right = Node(10)
# print(is_complete_binarytree(root))
# if is_complete_binarytree(root) and is_minheap(root):
#     print("True")
# else:
#     print("False")
# # print(is_minheap(root))           
# # levelorder(root)
# arr =[11,81,94,43,3]

# n = len(arr)
# ans = []
# for i in range(n):
#     for j in range(i,n):
#         ans.append(arr[i:j+1])
# sub_min = []
# for subarray in ans:
#     sub_min.append(min(subarray))
# print(sum(sub_min))
        

# class Node :
#     def __init__(self , data = 0 , left = None , right = None) -> None:
#         self.data = data
#         self.left = left
#         self.right = right
        
# def is_complete_binary_tree(root):
#     if not root:
#         return True
#     queue = []
#     queue.append(root)
#     end = False
#     while queue:
#         root = queue.pop(0)
#         if root:
#             if end:
#                 return False
#             queue.append(root.left)
#             queue.append(root.right) 
#         else:
#             end = True     
#     return True

# root = Node(1)
# root.left = Node(2)
# # root.right = Node(3)
# # root.left.left = Node(4)
# # root.left.right = Node(5)
# # root.right.left = Node(6)
# # # root.right.right = Node(7)
# # # root.right.right.left = Node(8)

# # print(is_complete_binary_tree(root))

            
# """Next permutation"""
# # def next_permutation(arr):
# #     # step 1
# #     i = len(arr)-2
# #     while i >= 0 and arr[i] >= arr[i+1]:
# #         i = i-1
    
# #     if i == -1:
# #         arr.reverse()
# #         return arr
# #     # step 2
# #     j = len(arr)-1
# #     while arr[j] <= arr[i]:
# #         j = j-1
# #     # step 3
# #     arr[i],arr[j] = arr[j],arr[i]
# #     # step 4
# #     arr[i+1:] = reversed(arr[i+1:])
# #     return arr
# # arr = [1,2,4,3,2,1]
# # result = next_permutation(arr)
# # print(result)
            
            
# class TreeNode:
#     def __init__(self, data ) -> None:
#         self.data = data
#         self.left = None
#         self.right = None
#         self.level = None
        
# class BinaryTree:
#     def createNode(self,data):
#         return  TreeNode(data)
        
#     def insert(self, root_node , data):
#         if root_node is None:
#             return self.createNode(data)
#         if data < root_node.data:
#             root_node.left = self.insert(root_node.left , data)
#         if data > root_node.data:
#             root_node.right = self.insert(root_node.right , data)
#         return root_node
    
#     def traverse_inorder(self, root):
#         if root:
#             self.traverse_inorder(root.left)
#             print(root.data , end= " ")
#             self.traverse_inorder(root.right)
            
#     def levelOrder(self, root):
#         if root is None:
#             return
#         q = []
#         q.append(root)
#         while len(q) > 0:
#             current = q.pop(0)
#             print(current.data , end= " ")
#             if current.left is not None:
#                 q.append(current.left)
#             if current.right is not None:
#                 q.append(current.right)
                
#     def Topview(self,root):
#         q = []
#         dic = dict()
#         root.level = 0
#         q.append(root)
#         while len(q) != 0:
#             root = q.pop(0)
#             if root.level not in dic:
#                 dic[root.level] = root.data
#             # if root.left is not None:
#             #     q.append(root.left)
#             #     root.left.level = root.level -1
#             if root.right is not None:
#                 q.append(root.right)
#                 root.right.level = root.level +1
#         # print(*sorted(dic.values()))
#         res = list(sorted(dic.values()))
#         print(res)
#         # list = []
#         # for i in sorted(dic):
#         #     list.append(dic[i])
#         # print(list)
        
#     # def binaryTree_rightsideview(self, root):
#     #     if root is None:
#     #         return
#     #     print(root.data, end= " ")
#     #     self.binaryTree_rightsideview(root.right)
                
# tree = BinaryTree()
# root = tree.createNode(1)
# tree.insert(root , 2)
# # tree.insert(root , 15)
# # tree.insert(root , 25)
# # tree.insert(root , 13)
# # tree.insert(root , 45)
# # tree.insert(root , 8)
# tree.traverse_inorder(root)
# print()
# tree.levelOrder(root)
# print()
# tree.Topview(root)
# # tree.binaryTree_rightsideview(root)



"""============================================================================================================================================="""
# 4. Kth Largest Element in an Array
# Find the kth largest element in an unsorted array. This problem can be efficiently solved using a min heap of size k to keep track of the largest k elements encountered so far.
# Example: For the array [3, 2, 1, 5, 6, 4] and k = 2, the answer would be 5.


# def heapify_down(arr , i , N):
#     largest = i
#     l = 2*i +1
#     r = 2*i +2
    
#     if l < N and arr[l] > arr[largest]:
#         largest = i
#     if r < N and arr[r] > arr[largest]:
#         largest = r
        
#     if largest != i:
#         arr[i] , arr[largest] = arr[largest] , arr[i]
#         heapify_down(arr , largest , N)


# def createHeap(arr):
#     for i in range(N//2-1 , -1 ,-1):
#         heapify_down(arr , i , N)
        
# def printHeap(N):
#     for i in range(N):
#         print(arr[i] , end= " ")
        
# def kthLargest(arr):
#     arr.sort(reverse = True)
#     print(arr[k-1])
        
# arr = [3, 2, 1, 5, 6, 4]
# N = len(arr)
# k = 2

# createHeap(arr)
# # printHeap(N)
# kthLargest(arr)


# # 3 .Sort Characters By Frequency
# # Given a string, sort it in decreasing order based on the frequency of characters.
# # Example: For the string  Input"tree", the sorted characters would be  output"eert" or "eetr".

# def reversefrequancy_chr(string):
#     dic = dict()
#     for char in string:
#         if char in dic:
#             dic[char]+=1
#         else:
#             dic[char]=1
#     # print(dic)
#     data = []
#     for key in dic.keys():
#         data.append(key)
#     data.sort(reverse = False)
#     for i in data:
#         print(i , end= "")
    
#     # unique = []
#     # dup = []
#     # for char in string:
#     #     if char in unique:
#     #         dup.append(char)
            
#     #     else:
#     #         unique.append(char)
#     # print(unique)
#     # print(dup)
            
# string = "tree"
# reversefrequancy_chr(string)


# # 1. Merge K Sorted Lists
# # Given k sorted lists of integers, merge them into one sorted list and return it. This problem can be efficiently solved using a min heap to always pick the smallest element among the heads of all lists.
# # Example: If the input lists are  input [[1, 4, 5], [1, 3, 4], [2, 6]], the merged sorted list would be
# # Output  [1, 1, 2, 3, 4, 4, 5, 6]

# def heapify_up(arr , i , N):
#     largest = i
#     l = 2*i +1
#     r = 2*i +2
    
#     if l < N and arr[l] < arr[largest]:
#         largest = i
#     if r < N and arr[r] < arr[largest]:
#         largest = r
        
#     if largest != i:
#         arr[i] , arr[largest] = arr[largest] , arr[i]
#         heapify_up(arr , largest , N)


# def createHeap(arr):
#     for i in range(N//2-1 , -1 ,-1):
#         heapify_up(arr , i , N)
        
# def printHeap(N):
#     for i in range(N):
#         print(arr[i] , end= " ")
        
# def ascendingOrder(arr):
#     for i in range(N):
#         for j in range(i+1, N):
#             if arr[i] > arr[j]:
#                 arr[i] , arr[j] = arr[j] , arr[i]
#     print(arr)
        
# arr =[1, 4, 5 ,1, 3, 4 ,2, 6]
# N = len(arr)
# # createHeap(arr)
# # printHeap(N)
# ascendingOrder(arr)

"""Removing the Middle ELement"""
# class CreateStack:
#     def __init__(self):
#         self.stack = []
        
#     def is_Empty(self):
#         return len(self.stack) == 0
    
#     def push(self,data):
#         self.stack.append(data)
        
#     def pop(self):
#         if self.is_Empty() is None:
#             return "Stack is Empty"
#         else:
#             ele = self.stack.pop()
#             print("Removed element : " , ele)
#             # print(self.stack)
            
#     def middle_ele(self):
#         if self.is_Empty() is None:
#             return "Stack is Empty"
        
#         mid = len(self.stack)//2
#         temp_list = []
#         for _ in range(mid):
#             temp_list.append(self.stack.pop())
#         self.stack.pop()
        
#         while temp_list:
#             self.stack.append(temp_list.pop())
    
            
# stack = CreateStack()
# elements = [ 10,20,30,40,50]
# for ele in elements:
#     stack.push(ele)
# print("Before Stack :",stack.stack)
# stack.middle_ele()
# print("Ofter Stack :",stack.stack)

"""implent a queue using two stack"""
# class QueueUsingTwoStacks:
#     def __init__(self):
#         self.stack1 = []
#         self.stack2 = []

#     def enqueue(self, item):
#         self.stack1.append(item)

#     def dequeue(self):
#         if not self.stack2:
#             while self.stack1:
#                 self.stack2.append(self.stack1.pop())
#         if not self.stack2:
#             raise IndexError("Dequeue from an empty queue")
#         return self.stack2.pop()

#     def is_empty(self):
#         return not self.stack1 and not self.stack2

#     # def peek(self):
#     #     if not self.stack2:
#     #         while self.stack1:
#     #             self.stack2.append(self.stack1.pop())
#     #     if not self.stack2:
#     #         raise IndexError("Peek from an empty queue")
#     #     return self.stack2[-1]

#     def size(self):
#         return len(self.stack1) + len(self.stack2)

# # Example usage:
# queue = QueueUsingTwoStacks()
# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)
# print(queue.dequeue())  # Output: 1
# print(queue.dequeue())  # Output: 2
# queue.enqueue(4)
# # print(queue.peek())   # Output: 3
# print(queue.dequeue())  # Output: 3
# print(queue.dequeue())  # Output: 4

"""Delete a Consecutive same words in a sequance"""
# def Consecutive(string):
#     stack = []
#     for char in string:
#         if not stack or char != stack[-1]:
#             stack.append(char)
#         else:
#             stack.pop()
#         # if stack and char == stack[-1]:
#         #     stack.pop() 
#         # else:
#         #     stack.append(char)
#     return stack
# string = "abaaaabcdab"
# print(Consecutive(string))

"""Next greatest element """
# def next_greatest(arr):
#     n = len(arr)
#     next_greater = -1
#     for i in range(n):
#         for j in range(i+1 , n):
#             if arr[j] > arr[i]:
#                 next_greater = arr[j]
#                 break
#             else:
#                 next_greater = -1
#         print(arr[i] , "-->",next_greater)
                
# arr = [4,9,6,10,25,3] 
# next_greatest(arr)

"""Next greatest element Using stack """
# def next_greatest_element_left_to_right(arr):
#     result  = [-1] * len(arr) # [-1,-1,-1,-1]
#     stack = [] # [ ]
#     for i in range(len(arr)):  
#         while stack and arr[i] > arr[stack[-1]]:
#             index = stack.pop()
#             result[index] = arr[i]
#         # Push the current index onto the stack
#         stack.append(i)
        
#     return result

# arr = [4, 5, 2, 25]
# print(next_greatest_element_left_to_right(arr))  # Output: [5, 25, 25, -1]

'""Sort multiple list using bubble sort'
# arr = [[1,4,2], [8,3,6],[5,9,7], [15,12,34]]
# a=[]
# for i in arr:
#         for j in i:
#                 a.append(j)
# my_list = a
# # print(type(my_list))
# N = len(my_list)
# for k in range(N):
#         for s in range(k+1 , N):
#                 if my_list[k] > my_list[s]:
#                         my_list[k] , my_list[s] = my_list[s] , my_list[k]
# print(my_list)

"""Valid Parntheses"""
# def solve(s):
#     stack = [] # 
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

"""REVERSE  A ARRAY USING DEQUE """
# from collections import deque
# def reverse(stack):
#     q = deque()
#     while len(stack) != 0:
#         q.append(stack.pop())
#     while q:
#         stack.append(q.popleft())
#     print(stack)
#     # using for loop --->
#     # for i in stack:
#     #     print(i , end=" ")
    
# def print_stack(stack):
#     # using while loop
#     while stack:
#         print(stack[-1] , end= " ")
#         stack.pop()
    
# stack = []
# arr = [1,2,3,4,5]
# for ele in arr:
#     stack.append(ele)
# # reverse(stack)
# print_stack(stack)

"""#reverse a individual words"""

# def reverse_str(str):
#     st = [] #world
#     for i in range(len(string)):#0123456789 10 
#         if string[i] != " ":
#             st.append(string[i])
#         else:
#             while st:
#                 print(st[-1],end = "")
#                 st.pop()
#     while st:
#         print(st[-1],end = "")
#         st.pop()
# str = "Hello World"
# reverse_str(string)

"""Reverse a string using stack"""
# def reverse_str_stack(s):
#     stack = []
#     for char in s:
#         stack.append(char)
#     reversed_str = ""
#     while stack:
#         reversed_str+=stack.pop()
#     return reversed_str
# s = "Hello World"
# print(reverse_str_stack(s))

"""Reverse a array using stack"""
# def reverse_arr(arr):
#     stack = []
#     for el in arr:
#         stack.append(el)
#     reverse_arrrr = []
#     for i in range(len(stack)):
#         reverse_arrrr.append(stack.pop())
#     return reverse_arrrr
# arr = [1,2,3,4,5]
# print(reverse_arr(arr))

"""Next smaller element"""
# def next_smaller_element(arr):
#     stack = []
#     result = []
    
#     for num in arr:
#         while stack and stack[-1] >= num:
#             stack.pop()
#         if stack:
#             result.append(stack[-1])
#         else:
#             result.append(-1)  # or any other value to represent no next smaller element
#         stack.append(num)
#     return result
# arr =[1,2,3,4,5]
# print(next_smaller_element(arr))



# """valid paranthes"""
# def isValid(str1):
#     stack = []
#     brackets ={')':'(',']':'[','}':'{'}
#     for char in str1:
#         if char in brackets.values():
#             stack.append(char)
#         else:
#             if stack and stack[-1] == brackets[char]:
#                 stack.pop()
#             else:
#                 return 0
#     # return 1 if not stack else 0
#     if stack == []:
#         return 1
#     return 0
# s = "()(){}[]"
# result = isValid(s)
# print(result)



# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
# Example 1:
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

# nums = [1,2,3,4,5,6,7]
# k = 3

# def rotate_arr_right_by_k_steps(nums , k):
#     n = len(nums)
#     data = []
#     for i in range(k):
#         data.append(nums.pop())
#     for j in range(n-k):
#         data.append(nums[j])
#     return data
# nums = [1,2,3,4,5,6,7]
# k = 3
# result = rotate_arr_right_by_k_steps(nums , k)
# print(result)


# def revrese_kth(arr , k):
#     stack = []
#     for i in range(k):
#         stack.append(arr.pop(0))
#     dequeue = []
#     while stack:
#         dequeue.append(stack[-1])
#     for i in range(len(arr)-k):
#         dequeue.append(arr.pop())
#     print(dequeue)
# arr = [3,2,1,4,6,7]
# k = 3
# revrese_kth(arr , k)



# from collections import deque

# dq = deque()

# dq.append(10)
# dq.append(20)
# dq.append(30)

# dq.appendleft(0)

# front_element = dq.popleft()
# last_element = dq.pop()

# front_peek = dq[0]
# back_peek = dq[-1]

# length = len(dq)

# isempty = len(dq) == 0

# print(dq)
# print(length)
# print(isempty)

# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def find_middle(self):
#         slow = self.head
#         fast = self.head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#         return slow

#     def reverse(self, head):
#         prev = None
#         current = head
#         while current:
#             next_node = current.next
#             current.next = prev
#             prev = current
#             current = next_node
#         return prev

#     def reorder_list(self):
#         if not self.head or not self.head.next:
#             return

#         # Step 1: Find the middle of the linked list
#         middle = self.find_middle()
#         second_half = middle.next
#         middle.next = None  # Split the list into two halves

#         # Step 2: Reverse the second half of the linked list
#         second_half = self.reverse(second_half)

#         # Step 3: Merge the two halves
#         first_half = self.head

#         while first_half and second_half:
#             first_next = first_half.next
#             second_next = second_half.next

#             first_half.next = second_half
#             if first_next is None:
#                 break
#             second_half.next = first_next

#             first_half = first_next
#             second_half = second_next

#     def display(self):
#         temp = self.head
#         while temp:
#             print(temp.data, end=" --> ")
#             temp = temp.next
#         print("None")

# # Create the linked list and add nodes
# ll = LinkedList()
# ll.head = Node(10, Node(20, Node(30, Node(40, Node(50)))))

# # Reorder the linked list
# ll.reorder_list()

# # Display the reordered linked list
# ll.display()


# for i in range(4-2-1):
#     print(i)

# class Node:
#     def __init__(self , data , next = None):
#         self.data = data
#         self.next = next
    
# class Linkedlist:
#     def __init__(self):
#         self.head = None
        
#     def append(self , data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
#         temp = self.head
#         while temp.next:
#             temp = temp.next
#         temp.next = new_node
        
        
#     def display(self):
#         temp = self.head
#         while temp:
#             print(temp.data, end="-->")
#             temp = temp.next
    
# ll = Linkedlist()
# elements = [1,2,3,4,5,6]
# for ele in elements:
#     ll.append(ele)
# ll.display()
        

class Node:
    def __init__(self , data , next = None):
        self.data = data
        self.next = next
        
class Linkedlist:
    def __init__(self) -> None:
        self.head = None
        
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        
        
    # def append(self , data):
    #     new_node = Node(data)
    #     if not self.head:
    #         self.head = new_node
    #         return
    #     temp = self.head
    #     while temp.next:
    #         temp = temp.next
    #     temp.next = new_node
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="-->")
            temp = temp.next
    
ll = Linkedlist()
elements = [1,2,3,4,5,6]
for ele in elements:
    ll.push(ele)
ll.display()


# # rotate a linked list #
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LL:
#     def __init__(self):
#         self.head = None

#     def push(self, new_data):
#         new_node = Node(new_data)
#         new_node.next = self.head
#         self.head = new_node

#     def printLL(self):
#         temp = self.head
#         while temp:
#             print(temp.data, end = " ")
#             temp = temp.next

#     def rotate(self, k):
#         if k == 0: # 3==0
#             return
#         curr = self.head
#         count = 0

#         while count < k and curr: #2<3 and head
#             curr = curr.next
#             count += 1

#         if curr is None:
#             return 
#         kthNode = curr # 30
#         while curr.next is not None:
#             curr = curr.next
#         curr.next = self.head
#         self.head = kthNode.next
#         kthNode.next = None

# llist = LL()
# for i in range(60, 0, -10):
#     llist.push(i)

# print ("Given linked list")
# llist.printLL()
# llist.rotate(3)
# print()

# print("Rotated linked list")
# llist.printLL()



# ll = []
# for i in range(10, 70, 10):
#     ll.append(i)
# print(ll)