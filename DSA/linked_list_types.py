
## Single Linked list

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)
# node4 = Node(40)
# node5 = Node(50)

# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5

# currentNode = node1

# while currentNode:
#     print(currentNode.data,end="->")
#     currentNode = currentNode.next



# ## Doubler linked list

# class Node:
#     def __init__(self,data) -> None:
#         self.data = data
#         self.next = None
#         self.prev = None

# node1 = Node(11)
# node2 = Node(22)
# node3 = Node(33)
# node4 = Node(44)

# node1.next = node2
# node2.prev = node1
# node2.next = node3
# node3.prev = node2
# node3.next = node4
# node4.prev = node3

# currentNode = node1
# print("Traversing forward")
# while currentNode:
#     print(currentNode.data,end="->")
#     currentNode = currentNode.next

# currentNode = node4
# print("traversing Backword")
# while currentNode:
#     print(currentNode.data,end="->")
#     currentNode = currentNode.prev

# ## circular linked list

# class Node:
#     def __init__(self,data) -> None:
#         self.data = data
#         self.next = None
#         self.prev = None

# node1 = Node(45)
# node2 = Node(55)
# node3 = Node(67)
# node4 = Node(89)
# node5 = Node(98)


# node1.next = node2
# node2.prev = node1
# node2.next = node3
# node3.prev = node2
# node3.next = node4
# node4.prev = node3
# node4.next = node1

# currentNode = node1
# newNode = node1
# print(currentNode.data,end="->")
# currentNode = currentNode.next

# while currentNode != newNode:
#     print(currentNode.data,end="->")
#     currentNode = currentNode.next

# ## Circula double linked list
# class Node:
#     def __init__(self,data) -> None:
#         self.data = data
#         self.next = None
#         self.prev = None

# node1 = Node(45)
# node2 = Node(55)
# node3 = Node(67)
# node4 = Node(89)
# node5 = Node(98)


# node1.prev = node4
# node1.next = node2
# node2.prev = node1
# node2.next = node3
# node3.prev = node2
# node3.next = node4
# node4.prev = node3
# node4.next = node1

# currentNode = node1
# newNode = node1
# print("\nTrverse Forward")
# print(currentNode.data,end="->")
# currentNode = currentNode.next

# while currentNode != newNode:
#     print(currentNode.data,end="->")
#     currentNode = currentNode.next


# currentNode = node4
# newNode = node4
# print("\nTraverse Backword")
# print(currentNode.data,end="->")
# currentNode = currentNode.prev

# while currentNode != newNode:
#     print(currentNode.data,end="->")
#     currentNode = currentNode.prev

# Here is some sample code for the LeetCode questions I mentioned earlier:

# 1. Reverse Linked List:

# def reverseList(head):
# 	prev = None
# 	while head:
# 		next = head.next
# 		head.next = prev
# 		prev = head
# 		head = next
# 	return prev
# head = [int(x)for x in input().split()]
# print(head)


# # 1. Detect Linked List Cycle:

# def hasCycle(head):
# 	slow = head
# 	fast = head
# 	while fast and fast.next:
# 		slow = slow.next
# 		fast = fast.next.next
# 		if slow == fast:
# 			return True
# 	return False


# # 1. Merge Two Sorted Lists:

# def mergeTwoLists(l1, l2):
# 	dummy = cur = ListNode(0)
# 	while l1 and l2:
# 		if l1.val < l2.val:
# 			cur.next = l1
# 			l1 = l1.next
# 		else:
# 			cur.next = l2
# 			l2 = l2.next
# 		cur = cur.next
# 	cur.next = l1 or l2
# 	return dummy.next


# # 1. Remove Linked List Elements:

# def removeElements(head, val):
# 	dummy = cur = ListNode(0)
# 	cur.next = head
# 	while cur.next:
# 		if cur.next.val == val:
# 			cur.next = cur.next.next
# 		else:
# 			cur = cur.next
# 	return dummy.next


# # 1. Linked List Cycle II:

# def detectCycle(head):
# 	slow = head
# 	fast = head
# 	while fast and fast.next:
# 		slow = slow.next
# 		fast = fast.next.next
# 		if slow == fast:
# 			break
# 	slow = head
# 	while slow != fast:
# 		slow = slow.next
# 		fast = fast.next
# 	return slow


# 1. Sort Linked List:

# def sortList(head):
# 	if not head or not head.next:
# 		return head
# 	mid = getMid(head)
# 	midNext = mid.next
# 	mid.next = None
# 	left = sortList(head)
# 	right = sortList(midNext)
# 	return mergeTwoLists(left, right)

# def getMid(head):
# 	slow = head
# 	fast = head.next
# 	while fast and fast.next:
# 		slow = slow.next
# 		fast = fast.next.next
# 	return slow


# # 1. Insertion Sort List:

# def insertionSortList(head):
# 	dummy = cur = ListNode(0)
# 	while head:
# 		temp = head.next
# 		head.next = None
# 		pos = dummy
# 		while pos.next and pos.next.val < head.val:
# 			pos = pos.next
# 		head.next = pos.next
# 		pos.next = head
# 		head = temp
# 	return dummy.next


# # 1. Partition List:

# def partition(head, x):
# 	before = before_head = ListNode(0)
# 	after = after_head = ListNode(0)
# 	while head:
# 		if head.val < x:
# 			before.next = head
# 			before = before.next
# 		else:
# 			after.next = head
# 			after = after.next
# 		head = head.next
# 	after.next = None
# 	before.next = after_head.next
# 	return before_head.next


# # 1. Swap Nodes in Pairs:

# def swapPairs(head):
# 	dummy = ListNode(0)
# 	dummy.next = head
# 	cur = dummy
# 	while cur.next and cur.next.next:
# 		first = cur.next
# 		second = cur.next.next
# 		cur.next = second
# 		first.next = second.next
# 		second.next = first
# 		cur = first
# 	return dummy.next


# # 1. Find the Merge Point of Two Linked Lists:

# def getIntersectionNode(headA, headB):
# 	setA = set()
# 	while headA:
# 		setA.add(headA)
# 		headA = headA.next
# 	while headB:
# 		if headB in setA:
# 			return headB
# 		headB = headB.next
# 	return None

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# def reverseList(head):
#     prev = None
#     while head:
#         next_node = head.next
#         head.next = prev
#         prev = head
#         head = next_node
#     return prev

# # Helper function to convert a list to a linked list
# def list_to_linked_list(items):
#     if not items:
#         return None
#     head = ListNode(items[0])
#     current = head
#     for item in items[1:]:
#         current.next = ListNode(item)
#         current = current.next
#     return head

# # Helper function to convert a linked list to a list
# def linked_list_to_list(node):
#     items = []
#     while node:
#         items.append(node.val)
#         node = node.next
#     return items

# # Example Input
# input_list = [1, 2, 3, 4, 5]

# # Convert the input list to a linked list
# head = list_to_linked_list(input_list)

# # Reverse the linked list
# reversed_head = reverseList(head)

# # Convert the reversed linked list back to a list
# output_list = linked_list_to_list(reversed_head)

# # Output the result
# print(output_list)

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None
    
#     # Insertion at the beginning
#     def insert_at_beginning(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node

#     # Insertion at the end
#     def insert_at_end(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             return
#         last = self.head
#         while last.next:
#             last = last.next
#         last.next = new_node
    
#     # Deletion from the beginning
#     def delete_from_beginning(self):
#         if self.head:
#             self.head = self.head.next
    
#     # Deletion from the end
#     def delete_from_end(self):
#         if not self.head:
#             return
#         if not self.head.next:
#             self.head = None
#             return
#         second_last = self.head
#         while second_last.next.next:
#             second_last = second_last.next
#         second_last.next = None
    
#     # Traversal
#     def traverse(self):
#         current = self.head
#         while current:
#             print(current.data, end=" -> ")
#             current = current.next
#         print("None")

# # Testing the LinkedList implementation
# ll = LinkedList()

# # Inserting elements
# ll.insert_at_beginning(10)
# ll.insert_at_beginning(20)
# ll.insert_at_end(30)
# ll.insert_at_end(40)

# # Traversing the list
# print("Linked List after insertions:")
# ll.traverse()

# # Deleting elements
# ll.delete_from_beginning()
# ll.delete_from_end()

# # Traversing the list after deletions
# print("Linked List after deletions:")
# ll.traverse()

# arr = [3,6,1,7]
# min_val = arr[0]
# for i in arr:
#     if i < min_val:
#         min_val=i
# print(min_val)


# class Node:
#     def __init__(self, data=0, next=None):
#         self.data = data
#         self.next = next

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

# def list_to_linked_list(lst):
#     dummy = Node(0)
#     current = dummy
#     for val in lst:
#         current.next = Node(val)
#         current = current.next
#     return dummy.next

# def linked_list_to_list(node):
#     result = []
#     while node:
#         result.append(node.data)
#         node = node.next
#     return result

# def reverse_linked_list(head):
#     prev = None
#     current = head
#     while current:
#         next_node = current.next
#         current.next = prev
#         prev = current
#         current = next_node
#     return prev

# # Test case
# l1 = list_to_linked_list([2, 4, 3])  # represents the number 342
# l2 = list_to_linked_list([5, 6, 4])  # represents the number 465
# result = solve(l1, l2)

# # Reverse the result linked list to get the digits in the desired order
# result = reverse_linked_list(result)

# # Convert the result back to a list to display
# result_list = linked_list_to_list(result)
# print(result_list) 

# # Input :
# #     l1 = 9 9 9 9 9 9 9 
# #     l2 = 9 9 9 9 
# # Output :
# #     8 9 9 9 0 0 0 1
# class Node:
#     def __init__(self, data=0, next=None):
#         self.data = data
#         self.next = next

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

# def list_to_linked_list(lst):
#     dummy = Node(0)
#     current = dummy
#     for val in lst:
#         current.next = Node(val)
#         current = current.next
#     return dummy.next

# def linked_list_to_list(node):
#     result = []
#     while node:
#         result.append(node.data)
#         node = node.next
#     return result

# # Test case
# l1 = list_to_linked_list([9,9,9,9,9,9,9])  # represents the number 342
# l2 = list_to_linked_list([9,9,9,9])  # represents the number 465
# result = solve(l1, l2)

# # Convert the result back to a list to display
# result_list = linked_list_to_list(result)
# print(result_list)  # Output should be [7, 0, 8] which represents the number 807

# from collections import deque

# def maxSlidingWindow(nums, k):
#     # Base cases
#     if not nums or k == 0:
#         return []
#     if k == 1:
#         return nums
    
#     # Initialize a deque and the result list
#     deq = deque()
#     result = []

#     for i in range(len(nums)):
#         # Remove elements that are out of the current window
#         if deq and deq[0] < i - k + 1:
#             deq.popleft()
        
#         # Remove elements from the deque that are smaller than the current element
#         while deq and nums[deq[-1]] < nums[i]:
#             deq.pop()
        
#         # Add the current element's index to the deque
#         deq.append(i)
        
#         # Add the maximum for the current window to the result list
#         if i >= k - 1:
#             result.append(nums[deq[0]])
    
#     return result

# # Example usage
# nums = [1, 3, 6, 4, 8, 2]
# k = 3
# output = maxSlidingWindow(nums, k)
# print(output)  # Output: [6, 6, 8, 8]



"""Inserting Linked List"""
# # craeting a Node
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
        
# # creating a linked list
# class LinkedList:
#     def __init__(self):
#         self.head = None
    
#     def display(self):
#         temp = self.head
#         while temp:
#             print(temp.data,end="-->")
#             temp = temp.next
#         print("Null")
    
#     def insert_at_beg(self,data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node  # updating newNode to head
        
#     def inserting_at_end(self,data):
#         new_node = Node(data)
#         temp = self.head
#         while temp.next:
#             temp = temp.next
#         temp.next = new_node

#     def inserting_at_pos(self,pos,data):
#         new_node = Node(data)
#         temp = self.head
#         for i in range(pos-1): 
#             temp = temp.next  
#         new_node.next = temp.next
#         temp.next = new_node
         
# ll = LinkedList()             

# n1 = Node(20)
# n2 = Node(10)
# n3 = Node(30)
# n4 = Node(40)
# n5 = Node(50)
# ll.head = n1
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5

# ll.insert_at_beg(0) 
# # ll.insert_at_beg(1) 
# ll.inserting_at_end(100)
# ll.inserting_at_pos(3,25)
# ll.display()



# # craeting a Node
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
        
# # creating a linked list
# class LinkedList:
#     def __init__(self):
#         self.head = None
    
#     def display(self):
#         temp = self.head
#         while temp:
#             print(temp.data,end="-->")
#             temp = temp.next
#         print("Null")

# ll = LinkedList()              

# n1 = Node(10)
# n2 = Node(20)
# n3 = Node(30)
# n4 = Node(40)
# n5 = Node(50)


# ll.head = n1
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5

# ll.display()


"""Delition Linked List"""
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
        
# class LinkedList:
#     def __int__(self):
#         self.head = None
        
#     def display(self):
#         temp = self.head
#         while temp:
#             print(temp.data,end=" --> ")
#             temp = temp.next
#         print("None")
        
#     def delete_front(self):
#         if self.head is None:
#             print('Empty')
#         self.head = self.head.next
#         # self.head = n2
        
#     # def delete_last(self): 
#     #     if not self.head:    # if self.head is None:
#     #         # List is empty
#     #         print("List is empty. Nothing to delete.")
#     #         return
        
#     #     if not self.head.next:    # if self.head.next is None:
#     #         # List has only one node
#     #         self.head = None
#     #         return
        
#     #     # Find the second-last node
#     #     second_last = self.head
#     #     while second_last.next.next:
#     #         second_last = second_last.next
        
#     #     # Delete the last node
#     #     second_last.next = None
#     #         # or
       
#     def delete_last(self):
#         temp = self.head
#         while temp.next.next is not None:
#             temp = temp.next
#         temp.next = None

# ll =LinkedList()

# n1 = Node(10)
# n2 = Node(20)
# n3 = Node(30)
# n4 = Node(40)
# n5 = Node(50)
# n6 = Node(60)

# ll.head = n1
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
# n5.next = n6
# ll.delete_front()
# ll.delete_last()
# ll.display()



# def solve(s):
#     # CODE HERE
#     stack = []
#     for char in s:
#         if char not in stack :
#             stack.append(char)
#         elif char in stack and stack[-1] == char :
#             stack.pop()
#     result = sorted(stack)
#     return ''.join(result)
# # Input: devsnest
# # Output: devnst
# s='bcabc'
# print(solve(s))



# problems 
"""=========================================================================================================================="""
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class SingleLinkedList:
#     def __init__(self):
#         self.head = None
#     #  normal way
#     # def append(self, data):
#     #     new_node = Node(data)
#     #     new_node.next = self.head
#     #     self.head = new_node
    
#     # soeted way
#     def append(self, data):
#         new_node = Node(data)
#         if not self.head or self.head.data >= new_node.data:
#             new_node.next = self.head
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next and current.next.data < new_node.data:
#                 current = current.next
#             new_node.next = current.next
#             current.next = new_node
            
#     def display(self):
#         temp = self.head
#         while temp:
#             print(temp.data, end="-->")
#             temp = temp.next
#         print("None")  # To indicate the end of the list

# def merge_linkedList(l1, l2):
#     dummy = Node(0)
#     tail = dummy
    
#     while l1 and l2:
#         if l1.data < l2.data:
#             tail.next = l1
#             l1 = l1.next
#         else:
#             tail.next = l2
#             l2 = l2.next
#         tail = tail.next
        
#     if l1:
#         tail.next = l1
#     if l2:
#         tail.next = l2
        
#     return dummy.next

# # Create first linked list and append data
# l1 = SingleLinkedList()
# l1.append(10)
# l1.append(20)
# l1.append(30)

# # Create second linked list and append data
# l2 = SingleLinkedList()
# l2.append(40)
# l2.append(50)
# l2.append(60)

# # Merge the two linked lists
# merged_head = merge_linkedList(l1.head, l2.head)
# merged_list = SingleLinkedList()
# merged_list.head = merged_head

# # Display the merged linked list
# merged_list.display()



"""REVERSE LINKED LIST"""

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
        
# class LinkedList:
#     def __init__(self):
#         self.head = None
    
#     def insert(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node
        
#     def display(self):
#         temp = self.head
#         while temp:
#             print(temp.data, end="-->")
#             temp = temp.next
#         print("None")
     
#     def reverse(self):
#         prev = None
#         current = self.head
#         while current:
#             next_node = current.next  # Store the next node                      next_node = 20  --> 20
#             current.next = prev       # Reverse the current node's pointer       20 = None --> None
#             prev = current            # Move prev one step forward               none = 30 -->30
#             current = next_node       # Move current one step forward            30 = 20 -->20
#         self.head = prev               # Update the head to the new first node   self.head = 30

# ll = LinkedList()
# ll.insert(10)
# ll.insert(20)
# ll.insert(30)
# print("Original linked list")
# ll.display()

# ll.reverse()
# print("Reversed linked list")
# ll.display()

# """MIDDLE OF THE LINKED LIST"""
# class Node:
#     def __init__(self,val):
#         self.val = val
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def display(self):
#         temp = self.head
#         while temp:
#             print(temp.val,end='-->')
#             temp = temp.next  
#     def middle_of_the_LL(self):
#         slow = self.head
#         fast = self.head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#         return slow
#     def display_from_node(self,node):
#         temp = node
#         while temp:
#             print(temp.val ,end='-->' if temp.next else "\n")
#             temp = temp.next

    
# # def append_to_list(ll,values):
# #     if not values:
# #         return 
# #     ll.head = Node(values[0])
# #     temp = ll.head
# #     for value in values[1:]:
# #         temp.next = Node(value)
# #         temp  = temp.next

# ll = LinkedList()
# n1 = Node(1)
# n2 = Node(2)
# n3 = Node(3)
# n4 = Node(4)
# n5 = Node(5)

# ll.head = n1
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5


# # append_to_list(ll,[10,20,30,40,50,60,70])
# # ll.head = Node(10,Node(20,Node(30,Node(40,Node(50,None)))))
# middle_node = ll.middle_of_the_LL()
# print(middle_node.val)
# # ll.length()
# # ll.middle()
# ll.display_from_node(middle_node)
# ll.display()


# class Node:
#     def __init__(self,data ,next = None):
#         self.data  = data
#         self.next = next

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def display(self):
#         temp = self.head
#         while temp:
#             print(temp.data,end="-->")
#             temp = temp.next
#         print("Null")
#     def insert_beg(self,data):
#         new_node = Node(data)
#         temp = self.head
#         new_node.next = temp
#         self.head = new_node

#     def insert_pos(self,pos,data):
#         new_node = Node(data)
#         temp = self.head
#         for _ in range(pos-1):
#             temp = temp.next
#         new_node.next = temp.next
#         temp.next  = new_node
#     def insert_end(self,data):
#         new_node = Node(data)
#         temp = self.head
#         while temp.next:
#             temp = temp.next
#         temp.next = new_node

# ll = LinkedList()
# # n1 = Node(10)
# # n2 = Node(20)
# # n3 = Node(30)
# # n4 = Node(40)
# # n5 = Node(50)

# # ll.head = n1
# # n1.next = n2
# # n2.next = n3
# # n3.next = n4
# # n4.next = n5
# ll.head = Node(10,Node(20,Node(30,Node(40,Node(50)))))
# ll.insert_beg(0)
# ll.insert_pos(3,26)
# ll.insert_end(80)
# ll.display()


# def binarySearch(arr,target):
#     low = 0
#     high = len(arr)-1
#     while low <= high:
#         mid = (low+high)//2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             low = mid+1
#         else:
#             high = mid-1
#     return -1
# arr = [1,2,3,4,5]
# target = 3
# print(binarySearch(arr,target))

'''
"""PROBLEMS IN LINKED LIST"""

class listNode:
    def __init__(self,data , next = None):
        self.data = data
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,data):
        new_node = LinkedList(data)
        new_node.next = self.head
        self.head = new_node

    def printlinkedlist(self):
        temp = self.head
        while temp:
            print(temp.data, end="-->")
            temp = temp.next
        print('Null')

    # ## Reverse Linked List
    # def reverse(self):
    #     prev = None
    #     current = self.head
    #     while current:
    #         next = current.next
    #         current.next = prev
    #         prev = current
    #         current = next
    #     self.head =  prev

    ## Nth Node from end of linked list
    # def printNthFromLast(self,n):
    #     temp = self.head
    #     count = 0
    #     while temp:
    #         temp = temp.next
    #         count +=1

    #     if n > count:
    #         print("Out of LinkedList")
    #         return 
    #     temp = self.head
    #     for i in range(0,count - n):
    #         temp = temp.next
    #     print(temp.data)

    ## Find Middle Node
    # def find_middle_node(self):
    #     temp = self.head
    #     count = 0
    #     while temp:
    #         temp = temp.next
    #         count+=1

    #     temp = self.head
    #     mid = count // 2
    #     for _ in range(mid):
    #         temp = temp.next
    #     print(temp.data)

    ## delete Middle element
    # def delete_middle_node(self):
    #     temp = self.head
    #     count = 0
    #     while temp:
    #         temp = temp.next
    #         count+=1

    #     temp = self.head
    #     mid = count // 2
    #     for _ in range(mid-1):
    #         temp = temp.next
    #     temp.next = temp.next.next
    # def delete_last_occurance(self,key):
    #     ### deletening the last occurence of a specified value or key from linked list 
    #     ###means removing the node that contains this value and appears last when traversing the list from thebeginning to rhe end.
    #     ### ex     :  1-->2-->3-->4-->2-->5-->
    #     ### output : 1-->2-->3-->4-->5-->
    #     if not self.head:
    #         return 
    #     last_occurace = None
    #     last_occurace_prev = None
    #     prev = None
    #     temp = self.head
    #     while temp:
    #         if temp.data == key:
    #             last_occurace = temp
    #             last_occurace_prev = prev
    #         prev = temp
    #         temp = temp.next
    #     if not last_occurace:
    #         return
    #     if last_occurace == self.head:
    #         self.head = self.head.next
    #     else:
    #         last_occurace_prev.next = last_occurace.next

    ### Delete without head pointer
    # def delete_without_head_pointer(self,pos):
    #     if pos is None:
    #         return
    #     elif pos.next is None:
    #         return
    #     pos.data = pos.next.data
    #     pos.next = pos.next.next
    ### Pairwise Swap

    # def pairwiseswap(self):
    #     temp = self.head
    #     if temp is None:
    #         return
    #     while temp and temp.next:
    #         if (temp.data != temp.next.data):
    #             temp.data , temp.next.data = temp.next.data , temp.data
    #         temp = temp.next.next

ll = LinkedList()
ll.head = listNode(10,listNode(20,listNode(30,listNode(40,listNode(50,listNode(20,listNode(70)))))))
# ll.reverse()
# ll.printNthFromLast(1)
# ll.find_middle_node()
# ll.delete_middle_node()
# ll.delete_last_occurance(20)
# delete_node = ll.head.next
# ll.delete_without_head_pointer(ll.head.next.next)
ll.pairwiseswap()
ll.printlinkedlist()
'''

# class listNode:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def push(self,data):
#         new_node = listNode(data)
#         new_node.next = self.head
#         self.head = new_node
    
#     def print_linkedlist(self):
#         temp = self.head
#         while temp:
#             print(temp.data , end= '-->')
#             temp = temp.next

#     def merge_list(self,l1, l2):
#         dummy = listNode(0)
#         tail = dummy
#         while l1 and l2:
#             if l1.data < l2.data:
#                 tail.next = l1
#                 l1 = l1.next
#             else:
#                 tail.next = l2
#                 l2 = l2.next
        
#         if l1:
#             l1.next = l1
#         elif l2:
#             l2.next = l2

#         return dummy.next
       
# list1 = LinkedList()

# list1.push(5)
# list1.push(10)
# list1.push(15)
# list2 = LinkedList()

# list1.push(2)
# list1.push(3)
# list1.push(20)

# mergerd_list = LinkedList()
# mergerd_list.head = mergerd_list.merge_list(list1.head,list2.head)
# mergerd_list.print_linkedlist()


"""class listNode:
    def __init__(self, data ,next = None):
        self.data = data
        self.next = next
def printLinkdelist(head):
    temp = head
    while temp:
        print(temp.data ,end= "-->")
        temp = temp.next
    print("None")
def is_palindrome(head):
    l = []
    while head:
        l.append(head.data)
        head  = head.next
    return l == l[::-1]
head = listNode(10,listNode(20,listNode(20,listNode(10))))
printLinkdelist(head)
print(is_palindrome(head))"""

'''COUNT OCCURANCE'''
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class linkedlist:
    def __init__(self):
        self.head = None

    def count_occurances(self , key):
        temp = self.head
        count = 0
        while temp :
            if temp.data == key:
                count +=1
            temp = temp.next
        return count
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def printlinkedlist(self):
        temp = self.head
        while temp:
            print(temp.data , end= "-->")
            temp = temp.next

ll = linkedlist()
ll.head = Node(1,Node(2,Node(1,Node(3,Node(1,Node(4,Node(1)))))))
res = ll.count_occurances(1)
print(res)
ll.printlinkedlist()









