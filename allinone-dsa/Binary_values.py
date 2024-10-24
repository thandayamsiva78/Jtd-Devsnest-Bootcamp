## 0 and 1 combination values are called binary values 

from collections import deque

def binary_values(n):
    ans = ["0"] # intilizing ans variable at 0
    queue = deque(["1"])  #  creating deueue and intilizing 1
    for i in range(n): # run the loop untill n times
        el = queue.pop() # remove the last element at the end of queue
        ans.append(el)  # then popped element append the ans variable
        queue.appendleft(el + "0") # concatenate the el + 0 and insert the frount of queue
        queue.appendleft(el + "1")  # concatenate the el + 1 and insert the frount of queue
    return ans # ofter loop completing return the ans 

print(binary_values(10))
   
     