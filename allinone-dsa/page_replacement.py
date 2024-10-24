"""Page Replacement Algorithm"""
""" 1 . FIFO
    2 . least resently Used
    3 . Optimal page replacement """

# from collections import deque

# def pagefault(pages , capacity):
#     pf = 0
#     q = deque()
#     for page in pages:
#         if page not in q:
#             pf+=1
#             q.append(page)
#             if len(q) > capacity:
#                 q.popleft()
#     return pf
# # pages = [1,2,3,4,1,1,4,2,4]
# # capacity = 3
# print(pagefault(pages=[1,2,3,4,1,1,4,2,4] , capacity=3))


# def pagefault(pages , capacity):
#     q = []
#     pf = 0
#     for page in pages:
#         if page not in q:
#             pf +=1
#             q.append(page)
#             if len(q) > capacity:
#                 q.pop(0)
#     return pf , len(pages) - pf
# print(pagefault(pages=[5,3,1,2,4,6,4,2,5,4,1] , capacity=3))      

# # page fault = 8
# # page hit = 3
# # total pages = 11






                