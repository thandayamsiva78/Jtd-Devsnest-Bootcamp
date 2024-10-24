"""1. if statement
The if statement is used for conditional excution. it allows you execute a block of code only if a certaion condition True"""
# x=10
# if x < 5:
#     print("x is greater than 5")

"""2. elif statement
The elif statement is short for 'else if' it allows you to check multiple conditions in a sequence"""

x=15
if  x < 10:
    print("x is grater than 10")
elif x == 10:
    print("x is equal to 10")
else:
    print("x is less than 10")

"""3. else statement
The else statement is used in conjuction with an if statement .
it specifies the block of code to be excuted if the Condition in the if statement is False"""

# x = 3
# if x > 5:
#     print("x is greater than 5")
# else:
#     print("x is less than or equal to 5")

"""4. Nested if statements
A nested if statement is an if statement that is inside another if statement .
it allows for more complex conditional logic."""

x=10
if x > 5:
    if x < 15:
        print("x is between 5 and 15")
    else:
        print("x is greater than 15")
else:
    print("x is less than 5")

# grade=50
# if grade >= 90:
#     print("A grade")
# else:
#     if grade >=80:
#         print("B grade")
#     else:
#         if grade >=70:
#             print("C grade")
#         else:
#             if grade <=69:
#                 print("fail") 



"""Here are the 3 logical operarions in python"""
# and - Returns True if both conditions are True.Otherwise , it return False.
# or - Return True if either of the conditions is True.Otherwise, it returns Fasle
# not - Inverts the results, ex:- True is changed to False and False is changed to True.

# and operator
# x = 5
# y = 10
# if  x > 0 and y > 0:
#     print("Both x and y are positive")
# else:
#     print("At least one of x and y is not positive")

# or operator
# x = 5
# y = 10
# if x > 0 or y > 0:
#     print("At least one of x and y is positive")
# else:
#     print("Neither x nor y is positive")

# Not operator
# x = 5
# if not x < 0:
#     print("x is not positive")
# else:
#     print("x is positive")

"""There are six comparison operators in python"""
#  == (equal to)
#  != (not equal to)
#  > (greater than)
#  >= (greater than or equal to)
#  < (less than)
#  <= (less than or equal to)


# a=True # 5
# b=False # 10
# if a == b:
#     print("a is equal to b")
# else:
#     print("a is not equal to  b")