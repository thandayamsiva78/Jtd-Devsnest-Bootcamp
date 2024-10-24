## 1. capitalize() Converts the "first charecter" to upper case
text="hello every one"  
x=text.capitalize()
print(x)

## 2. casefold()  Converts string into lower case
text="Hello ,And Welcome To my World!"
y=text.casefold()
print(y)

## 3. center(argument) Return a centerd string
text="Hello World! and Python is easy to learn "
text2="python"
z=text2.center(50)
print(z)

## 4. count(argument) Returns the number of item presents  in the list

num=1,2,3,4,3,4,3,4,5,6,7,3,9
string="today my mom preparing biryani and i love biryani"
x=num.count(3)
z=string.count("biryani")
print(x)
print(z)

## 5. endswith() Returns True if the string ends with the specified value
text="Hello world"
c=text.endswith("world")
print(c)

## 6. expandtabs() set the tab size
text ="H\te\tl\tl\to"
x=text.expandtabs(1)
print(x)

## 7. index() returns the index value from particular position
word="Good, morning"
index=word.index("m")
print(index)

## 8. join() Converts the elements of an iterable into a string
my_list1="siva","Naveen","selvam",'Madhan',"murthy","karuna"
z=" ".join(my_list1)
print(z)

## 9. replace() Replace the word
fruits="apple  banana cherry"
changed=fruits.replace("apple ","Mango")
print(changed)

## 10. rsplit() specified seperator
text="apple, banana, cherry"
x=text.rsplit(",")
print(x)

## 11. split() Split the string at the specified separator , and returns a list
word="Welcome to the amazon forest"
splitted=word.split()
print(splitted)

## 12. strip() it remove white spaces
text="     apple      "
x=text.strip()
print(x)

## 13. swapcase() Swap cases, lower case becomes upper case and vice versa
text="Hello My Name Is SIVA"
s=text.swapcase()
print(s)

## title()  Converts the first character of each word to upper case
##make the first letter in each word upper case
text= "Welcome to my world"
x=text.title()
print(x)

## upper() Converts a string into upper case
word="Hii Siva"
upper=word.upper()
print(upper)
## lower() Converts a string into lower case
word="Hii Siva"
print(upper)

