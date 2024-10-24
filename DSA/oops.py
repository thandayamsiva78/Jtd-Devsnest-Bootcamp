"""Class and Object"""
## Class {ClassName}:


## without constructor taking more space and much time
# class AdmissinForm:  # class
#     name = None
#     age = None
#     gender = None
#     location = None

# xerox1=AdmissinForm() # object

# xerox1.name="Siva"
# xerox1.age = 20
# xerox1.gender="Male"
# xerox1.location="Nagari"

# xerox2=AdmissinForm()

# xerox2.name="kenal"
# xerox2.age = 24
# xerox2.gender="male"
# xerox2.location="chennai"

# print(xerox1.name)
# print(xerox2.name)

## we use constructor for efficiancy for time saving and less space required

# class AdmissionForm:
#     name = None
#     age = None
#     gender = None
#     location = None
#     def __init__(self,name,age) -> None:
#         self.name = name
#         self.age = age

# xerox1=AdmissionForm("Siva",21)
# print(xerox1.age)


"""creating a single  NODE"""
# class Node:
#     data = None
#     pointer = None
#     def __init__(self,data) -> None:
#         self.data = data
# node1=Node(10)

# node2=Node(20)
# print(node1.data)
# print(node1.pointer)

# print(node2.data)
# print(node2.pointer)

"""Multiple linked lists create"""
## creating nodes
# class myclass:
#     data = None
#     pointer = None
#     def __init__(self,data) -> None:
#         self.data = data

# head = myclass(100)
# node2 = myclass(1001)
# node3 = myclass(1005)
# node4 = myclass(2002)
# node5 = myclass(3004)

# head.pointer = node2
# node2.pointer = node3
# node3.pointer = node4
# node4.pointer = node5

# curr = head # temporary storage 

# while (curr is not None):
#     print(curr.data)
#     curr = curr.pointer

