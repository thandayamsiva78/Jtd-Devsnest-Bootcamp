# hashing used to hash the passwords

# import hashlib
# print(hashlib.algorithms_available)#displays  all hashing algorithms
# print(hashlib.algorithms_guaranteed) #displays all hashing algo in this vscode
# ## most secure and commonly used are SHA256,SHA512

""" 1. digest(): This method returns the hash value of the data passed to the hash object.
the result is a byte string.
    2. hexdigest(): This method returns the hash value as a hexadecimal string, which is easier to read and work
with compared to the byete string returned by digest()."""

# import hashlib
# # step 1
# hash_object= hashlib.sha256()
# data=(b'Hello world') 
# # # step 2 Update the hash object with the data
# hash_object.update(data)
# # step 3 Get the hash value using digest() method
# hash_object_bytes=hash_object.digest()
# print("Hash value as bytes:",hash_object_bytes)  # returns  byte string
# # step 4 Get the hash value using hexadecimal sting using hexdigest() method
# hash_object_hex=hash_object.hexdigest() # returns hexadecimal string
# print("hash values as hexadecimal string:",hash_object_hex)    #0 t 9 and A to F
# print(type(data))



"""encode(): This method in python is used to convert a string into a byte representation using a specified encoding.
This methode is often used when working with text data and need to convert it into a formate that can be used  for Hashing or transmission over a network"""
# step 1 Define a string
# text="Hello word"
# #   step 2 Encode the string using a specific encoding
# encoded_text=text.encode() 
# #   step 3 Print the encoded text
# print("Encoded text:",encoded_text) # showing the byterepresentation of the original string.

# # simple way
# text=b"Hello word"
# print(text) 
# print(type(text)) 


# import hashlib
# h=hashlib.new("sha256")
# correct_password="mypassword@123456jhsdfjk"
# h.update(correct_password.encode()) #  Strings must be encoded So... we converting into bytes 'UPDATED'
# print(h.hexdigest())
# print(h.digest())

# ####
# userinput="mypassword@1234567"
# h=hashlib.new("sha256")
# h.update(userinput.encode())
# print(h.hexdigest())


# ## -----------------------------------------------------
# int=134234234 # we can't hash the integers (same out will be returns)
# str="hii" # string hasheble
# float=5.023   # float Hasheble
# print("hashing int",hash(int))  
# print("hashing str",hash(str))  #  Generating the Hash values
# print("hashing float",hash(float))   #  Generating the Hash values


## -----------------------------------------------------

# tuple=(1,2,3,4) # tuple is a not changing datatype  so it is  able to hash
# # list=[1,2,3,4]  # list is a changing datatype so it is not able to hash its throus Error
# #REASON::::::if we privide unique input oly we get the unique output at list in middle we can update so it is decline to hash()
# print(hash(tuple))
# print(hash(list))



# #------------------------------------Changing datatypes so we cant perform hash()
# list=[12,1,23,5]
# set={1,2,3}
# dictionary={12:1,23:5}
# print(hash(list)) 
# print(hash(set))
# print(hash(dictionary))
# unhashable type list/set/dictionary


# #-----------------------------------------Hash tables have to support 3 functions.

"""# 1. insert (key, value)"""

# my_hash_table={108:"ambulance",100:"policestation",101:"fireengine"}#declaration of HASHTABLE
# print(my_hash_table)#print before no operations
# x=my_hash_table[1073]="traffic help"#INSERTING THE VALUES into the hashtable 
# print(x)#printing after updation.
# print(my_hash_table)


'''# 2.get(key)    read an el in hashtable###       """keyword=get()"'''

# my_hash_table={108:"ambulance",100:"policestation",101:"fireengine"}#declaration of HASHTABLE
# print(my_hash_table)#print before no operations
# value=my_hash_table[100]#key is used as a reference for the accessing the value......
# value1=my_hash_table.get(100)  #"using get keyword  accessing the value"
# # print(value,"normal accessing using by key")#printing the accessed value..
# print(value)
# print(value1)



"""# 3.Deletion of an el in hashtable   keyword=del"""

# my_hash_table={108:"ambulance",100:"policestation",101:"fireengine"} # declaration of HASHTABLE
# print(my_hash_table)#print before no operations
# del my_hash_table[100]#performing the delete operation
# print(my_hash_table)#printing the accessed value..



## combination of INSERTION-DELETION-READING    an elements in an hashtable...

# my_hash_table={108:"ambulance",100:"policestation",101:"fireengine"}#declaration of HASHTABLE
# print(my_hash_table)#print before no operations
# my_hash_table[1073]="traffic help"  # INSERTING THE VALUES Into the hashtable 
# print(my_hash_table)#printing after updation
# print("above inserted")
# value=my_hash_table[108]#key is used as a reference for the accessing the value......
# value1=my_hash_table.get(101)
# print(value,"normal accessing using by key")#printing the accessed value..
# print(value1,"using get keyword")
# print("above accessed element")
# del my_hash_table[1073]#performing the delete operation
# print(my_hash_table)#printing the accessed value..
# print("element deleted...")


# ## Function to display hashtable 

# def display_hash(hashTable): #                                        55555555555
	
# 	for i in range(len(hashTable)): #A,m,d,p,n,m
# 		print(i, end = " ") #i=0,1,2,3,4,5,6,7,8,9
		
# 		for j in hashTable[i]: 
# 			print("-->", end = " ") 
# 			print(j, end = " ") 
			
# 		print() 


# # Creating Hashtable as 
# # a nested list. 

# HashTable = [[] for _ in range(10)] #creating hash table initially with 10 empty spaces....           1111
# print(HashTable,"#creating hash table initially with 10 empty spaces....")

# # display_hash (HashTable) 
# # Hashing Function to return 
# # key for every value. 
# def Hashing(key): #                                                      333333333
# 	return key % len(HashTable) ##hashing the key eg 10 is being hashed.. and returned to insert_fun()


# # Insert Function to add 
# # values to the hash table 
# def insert_fun(Hashtable, key, value): # paramiters
# 	# print("insert_fun")
# 	hash_key = Hashing(key) #hashing the key eg 10 is being hashed...and stored to hash_key
# 	Hashtable[hash_key].append(value) #resulted hash_key going to stored at hashtable[] with the index...
# 		# HashTable[0].append("Allahabad")

# #                     key    value
# insert_fun(HashTable, 10, 'Allahabad') #calling insert_fun(),   passing args     222222
# insert_fun(HashTable, 25, 'Mumbai') #calling insert_fun()       ,passing args
# insert_fun(HashTable, 20, 'Mathura') #calling insert_fun(),      passing args
# insert_fun(HashTable, 9, 'Delhi') #calling insert_fun(),        passing args
# insert_fun(HashTable, 21, 'Punjab') #calling insert_fun(),      passing args
# insert_fun(HashTable, 21, 'Noida') #calling insert_fun(),       passing args


# display_hash (HashTable)        #calling 55555


"""==========================================================================================================="""
# 1. Division method

# def hash_function(key,size):
#     return key % size
# # difining a hash table size
# size=10
# # difining a key to hash
# key=45
# # Caluculate the hash value using the hash_function
# print(hash_function(key,size))


# def hash_function(key,size):
#     return key % size
# hash_table_size=7
# keys=[10,20,30,15,25]
# hash_table={} # intialize an empty dictionary to store hash values
# for key in keys:
#     hash_value=hash_function(key,hash_table_size)
#     hash_table[key]=hash_value
# print(hash_table)


# def hash_function(key,size):
#     return key % size
# table_size=7
# keys=[10,20,30,15,25]
# for key in keys:
#     hash_value=hash_function(key,table_size)
#     print(f"keys  {key} : values  {hash_value}")
    

# def hash_table(key,size):
#     return key % size
# table_size=7
# keys=[10,12,14,45,60]
# HashTable={}
# for key in keys:
#     hash_values=hash_table(key,table_size)
#     HashTable[key]= hash_values
# print(HashTable)


# def hash(key,size):
#     return key % size
# table_size=7
# keys=[15,7,11,5,13]
# HashTbale={}
# # target=11
# for key in keys:
#     hash_value=hash(key,table_size)
#     HashTbale[key]=hash_value
# print(HashTbale)

# print(15%7)
# print(7%7)
# print(5%7)
# print(11%7)
# print(13%7)


# def count(arr):
#     hash_table={}
#     for i in arr:
#         hash_table[i] = hash_table.get(i,0)+1
#     return hash_table
# array=[10,10,10,20,20,21,40,30,45,50,50]
# print(count(array))

# s=input() # O(1)
# t=input()
# if sorted(s) == sorted(t):
#     print("Anagram")
# else:
#     print("not a valid anagram")

"""Find duplicate in array"""
# def duplicate(arr):
#     dic={}
#     for i in arr:
#         if i in dic:
#             dic[i]+=1
#         else:
#             dic[i]=1
#     for j in dic.values():
#         if j >=2:
#             return True
#     else:
#         return False
# arr=[int(x) for x in input().split()]
# result=duplicate(arr)
# print(result)