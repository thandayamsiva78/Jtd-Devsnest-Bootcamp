# """1. Find middle number from list

# if the length of the list odd ,the  middle number is at the index"""
# my_list=[2,4,6,8,10,12,14,16,18,20]
# print("Maximum of the list",max(my_list))
# print("minimum of the list",min(my_list))
# print("sum of the list",sum(my_list))
# print("reversed ordr my list",my_list[::-1])
# print("Length of the list",len(my_list))
# middle_no_odd=my_list[len(my_list)//2]
# print(middle_no_odd)

# """# if the length of the list is even ,there are two middle numbers ,at the indices"""
# middle_no_even=my_list[len(my_list)//2-1],my_list[len(my_list)//2]
# print(middle_no_even)
# h=[None]*10
# i=hash("book")
# # print(h[i]=="book")
# print(i)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
    dummy = ListNode()
    current = dummy
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    if l1:
        current.next = l1
    elif l2:
        current.next = l2
    return dummy.next

def display_linked_list(list1):
    current = list1
    while current:
        print(current.val, "-->", end=" ")
        current = current.next
    print("None")

# Create linked lists
list1 = ListNode(1, ListNode(2, ListNode(3)))
list2 = ListNode(0, ListNode(23, ListNode(32, ListNode(333, ListNode(999)))))

# # Display linked lists
# print("List 1:")
# display_linked_list(list1)
# print("List 2:")
# display_linked_list(list2)

# Merge the linked lists
res = mergeTwoLists(list1, list2)
# Display the result
print("Merged List:")
display_linked_list(res)

# # MERGE OF TWO SORTED LINKEDLIST#
# class ListNode:
#     def _init_(self, val=0, next=None):
#         self.val = val
#         self.next = next

# def mergeTwoLists(l1, l2):
#     dummy = ListNode()
#     current = dummy
#     while l1 and l2:#loop runs until elements 2 linkedlists hv equally completes:
#         if l1.val < l2.val:#l1==1 --> 2 l1 --> 3 --> None
#                            #l2==0 --> 3 l2 --> 2 --> 333 --> 999 --> None
#                            #l3----Dummy
#                            #       c->0-->1
#             current.next = l1
#             l1 = l1.next
#         else:
#             current.next = l2
#             l2 = l2.next
#         current = current.next
#     if l1:#extra node joined ..........
#         current.next = l1
#     elif l2:
#         current.next = l2
#     return dummy.next
# def display_linked_list(list1):
#     current = list1
#     while current:
#         print(current.val,"-->" ,end=" ")
#         current = current.next
#     print(None)

# list1 = ListNode(1, ListNode(2, ListNode(3)))
# list2 = ListNode(0, ListNode(23, ListNode(32,ListNode(333,ListNode(999)))))
# display_linked_list(list1)
# display_linked_list(list2)
# res= mergeTwoLists(list1, list2)#fun call
# display_linked_list(res)


#-===================================================================================================================
                                    # 1.REVERSE A LINKEDLIST


# class Node:
#     def _init_(self,data,next):
#         self.data=data
#         self.next=next
# def rev(head):
#     prev=None
#     current=head
#     while current:
#         nextptr=current.next
#         current.next=prev
#         prev=current
#         current=nextptr
#     return prev
        
# def disp(head):
#     while head:
#         print(head.data,"->",end="")
#         head=head.next
#     print(None)
        


# head=Node(10,Node(20,Node(30,Node(40,None))))
# disp(head)
# a=rev(head)
# disp(a)


#======================================================================================================================================
        # REMOVE LINKED LIST ELEMENTS
# class ListNode:
#     def _init_(self, val=0, next=None):
#         self.val = val
#         self.next = next

#     def remove_element(self, target):
#         dummy = ListNode()
#         dummy.next = self  # Dummy node to handle the case of removing the head node
#         prev, current = dummy, self

#         while current:
#             if current.val == target:
#                 prev.next = current.next
#             else:
#                 prev = current
#             current = current.next

#         return dummy.next

# def display_linked_list(head):
#     current = head
#     while current:
#         print(current.val, "-->", end=" ")
#         current = current.next
#     print(None)


# list1 = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(4)))))
# display_linked_list(list1)

# target_value = 2
# list1 = list1.remove_element(target_value)
# display_linked_list(list1)


# class Node:
#     def _init_(self,data=0,next=None):
#         self.data=data
#         self.next=next
# def printing(head):
#     current=head
#     while current:
#         print(current.data,"-->",end="")
#         current=current.next
#     print(None)

# def dlt_strt(head):
#     if head:
#         return head.next
#     else:
#         return None
# def dlt_end(head):
#     if not head:
#         return None
#     current=head
#     while current.next.next:
#         current=current.next
#     current.next=None
#     return head
# def dlt_mid(head,pos):
#     if pos==0 and head:
#         return head.next
#     i=0
#     current=head
#     while i<pos-1:#0<3-1=0<2        1 -->2 -->3 -->s -->b -->None
#         current=current.next
#         i+=1
#     if current and current.next:
#         current.next=current.next.next
#     return head
    
# head = Node(1, Node(2, Node(3, Node("s",Node("b")))))
# printing(head)
# # a=dlt_strt(head)
# # a=dlt_end(head)
# a=dlt_mid(head,3)#pos
# printing(a)

#====================================================================================================================================
                        #Add 2 linked lists individually nums after rev

# class ListNode:
#     def _init_(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class sol:
#     def addTwoNumbers(self, l1,l2):
#         dummy_node = ListNode()
#         current = dummy_node
#         carry_value = 0
#         while l1 or l2 or carry_value:
#             val1 = l1.val if l1 else 0#1
#             val2 = l2.val if l2 else 0#1
#             value = val1 + val2 + carry_value#1

#             carry_value = value // 10  # intdiv..if sum is 11 to 19 carry_val=11//10=1
#             value %= 10  # 15%10=5  remainderdiv..

#             current.next = ListNode(value)
#             current = current.next

#             l1 = l1.next if l1 else None
#             l2 = l2.next if l2 else None
        
#         return dummy_node.next

# # Helper function to print a linked list for testing
# def printLinkedList(head):
#     current = head
#     while current:
#         print(current.val, end=" -> ")
#         current = current.next
       
#     print("None")

# l1=ListNode(1,ListNode(1,ListNode(9)))#1-->1-->9======>911
#                                       #1-->1-->1======>111
#                                                     # ------------
#                                                       #D-->      # 0
#                                     #carried---
# l2=ListNode(1,ListNode(1,ListNode(1)))
# # l1 = ListNode(1)
# # l1.next = ListNode(1)
# # l1.next.next = ListNode(1)
# # l1.next.next.next = ListNode(1)
# # l2 = ListNode(1)
# # l2.next = ListNode(1)
# # l2.next.next = ListNode(1)
# s=sol()
# result = s.addTwoNumbers(l1, l2)
    
 
# printLinkedList(result)