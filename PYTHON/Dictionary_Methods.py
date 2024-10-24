# Dictionary Syntax     dict ={ key : values }
 
# .keys() returns a list of all the keys in the dictionary.
my_dict={"name":"Siva","age":21,"location":"nagari"}
key=my_dict.keys()
print(key)

# values() Returns a list of all the values  in the dictionary
my_dict={"name":"Siva","age":21,"location":"nagari"}
values=my_dict.values()
print(values)

# .get() Reurn the value of the specified "key"
my_dict={"name":"Siva","age":21,"location":"nagari"}
name=my_dict.get("name")
print(name)
print(my_dict["age"])

# .items() Returns a list of key_values pairs as tuple
my_dict={"name":"Siva","age":21,"location":"nagari"}
items=my_dict.items()
print(items)

# Update()  (other_dict) Update the dicionary with key_values pairs from another dictionary or an iterable
my_dict={"name":"Siva","age":21,"location":"nagari"}
new_dict={"college":"GDC"}
my_dict.update(new_dict)
print(my_dict)

# Clear() Removes all (key_values) elements from the dictionary
my_dict={"name":"Siva","age":21,"location":"nagari"}
my_dict.clear()
print(my_dict)

# .pop(key,default) removes and returns the values associated with the given key. 
# If the key is not found, it return the  specified default value or raises a keyError.
my_dict={"name":"Siva","age":21,"location":"nagari","college":"GDC"}
my_dict.pop("age")
print(my_dict)

# popitem() Removes the last item from the dictionary
my_dict={"name":"Siva","age":21,"location":"nagari","college":"GDC"}
my_dict.popitem()
print(my_dict)

# .copy() Returns a shallow copy of the dictionary
my_dict={"name":"Siva","age":21,"location":"nagari","college":"GDC"}
my_dict.copy()
print(my_dict)

 
# Returns a dictionary with the specified kays and values
# Create a dictionary with 3 keys , all with the value 0:
x= ('key1','key2','key3')
y= 15
thisdict= dict.fromkeys(x,y)
print(thisdict)

# setdefault(key[,dafault])




# a={
#     "name":"Siva",
#     "age":21,
#     "location":{1:"nagari",2:"puttur",3:"tirupati"}
# }

# print(type(a))

# for i,j in a.items():
#     print(i,j)

# print(a["location"][2])

# value = nested_dict.get('outer_key', {}).get('inner_key')
# value=a.get("location",{}).get(2)
# print(value)

# a["colour"]="red"
# print(a)
# a.update({"num": 123})
# print(a)

# a.pop("colour")
# print(a)

# del a ["age"]
# print(a)

# print(a.keys())
# print(a.values())

# print(a.get("location"))
# a.items()
# print(a)
