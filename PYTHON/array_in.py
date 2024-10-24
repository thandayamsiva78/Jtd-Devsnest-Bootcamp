"""An array is a special variable , which can hold more than one value at a time"""
"""An array can hold many values under a single name, and you can access the values by referring to an index number"""

# Access the elements of an array

cars=["ford","volvo","BMW"]
x=cars[0]
print(x)

# modify the value of array (insert)
cars[0]="Toyota"
print(cars)

# The length of an array
y=len(cars)
print(y)

# looping array elements
for i in cars:
    print(i)

# adding array elements
cars.append("Honda")
print(cars)

## Removing array elements
# removes last element
cars.pop()
print(cars)

# removes specific elements
cars.pop(1)
print(cars)

# remove direct value
cars.remove("BMW")
print(cars)
