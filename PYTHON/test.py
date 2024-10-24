# 1.Reversing string using stack
# 2.Implement stack using two queues
# 3.find next greatest element in an array using stack
# 4.valid paretnhesis of a given string
# 5.page replacement
# 6.generate binary


# 1.Reversing string using stack

def revrese(string):
    stack = []
    for char in string:
        stack.append(char)
        
    reversed = ""
    while stack:
        reversed+=stack.pop()
    return reversed

string = "Hello Hyderabad"
res = revrese(string)
print(res)


def revrese(string):
    stack = []
    for char in string:
        stack.append(char)
        
    data = []
    while stack:
        el = stack.pop()
        data.append(el)
    return "".join(data)

string = "Hello Hyderabad"
res = revrese(string)
print(res)

# 4.valid paretnhesis of a given string


def validparanthesis(string):
    stack = []
    brackets = {")":"(","]":"[","}":"{"}
    for char in string:
        if char in brackets.values():
            stack.append(char)
        else:
            if stack[-1] == brackets[char]:
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False

string = "{()}"
print(validparanthesis(string))


# 5.page replacement

from collections import deque

def pagefalut(pages , capacity):
    pf = 0
    queue = deque()
    for page in pages:
        if page not in queue:
            queue.append(page)
            pf+=1
            if len(queue) > capacity:
                queue.popleft()
    return pf

pages = [1,2,3,4,5,6,1]

capacity = 3
print(pagefalut(pages , capacity))


# 3.find next greatest element in an array using stack

# def nextgeatest_element(arr):
#     stack = []
#     result = [-1] * len(arr)
#     for i in range(len(arr)):
        # while st
    
                
        
            

    
            
        







""""""
# class Node:
#     def __init__(self ,data , next = None):
#         self.data = data
#         self.next = next
        
# class linkedlist:
#     def __init__(self):
#         self.head = None
        
#     def reverse(self):
#         prev = None
#         current = self.head
#         while current:
#             next_node = current.next
#             current.next = prev
#             prev = current
#             current = next_node
#         self.head = prev
#         return self.head
        
#     def display(self):
#         temp = self.head
#         while temp :
#             print(temp.data , end="--->")
#             temp = temp.next 
#         print("Null")
        
        
# ll = linkedlist()
# ll.head = Node(10 , Node(20 , Node(30 , Node(40 , Node(50)))))
# print("Reveresed Linked List :")
# ll.reverse()
# ll.display()


        
    