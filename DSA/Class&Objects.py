# Classes:
"""
A class is a blueprint defines the properties and behaviour of an object.

A class Defines:-

1. Atribute (data) :- Also known as data members , these are variable that are defined inside the class.
2. Methods (functions) :- These are functions that belong to the class and operate on the attributes.
"""

# Objects:

"""
An object is an instance of a class. it represents a real-world entity or concepts that has its own set of attributs (data) and methods (functions).
Each objects has its own set of values for its attributes.
"""

# Key differences:
#                CLASS                            OBJECT
# Defintion  :   Blueprint or template            Instance of a class
# Attributes :   Defines attributes               Has its own attributs values
# Methods    :   Defines methods                  Can call methods


# Define a class:

class Car:
    color = ""
    model = ""
    year = ""
    
    def honk(self):
        print("Honk konk")
        
    def display_details(self):
        print(f"color : {self.color} , model : {self.model} , year : {self.year}")
        
my_car = Car()

my_car.color = "red"
my_car.model = "Toyata"
my_car.year = 2022

my_car.honk()
my_car.display_details()

# Car is the class (object).
# my_car is object (instance of object)
# color , model, year are attributes.
# honk and display_details are methods.

# Constructor (__init__ method):
""" 
The __init__ method is a special method that's called when an object is created.
it intializes the objects attributes.
"""

# 1.Simple Intialization:-
class Person:
    def __init__(self , name ,age) -> None:
        self.name = name
        self.age = age
        
person = Person("Siva" , 21)
print(person.name)
print(person.age)

# 2. Default values:-

class Car:
    def __init__(self , color="red" , model= "Toyata" , year= 2022) -> None:
        self.color = color
        self.model = model
        self.year = year
        
car1 = Car()
print(car1.color)
print(car1.model)
print(car1.year)

car2 = Car("green" , "BMW" , 2222)
print(car2.color)
print(car2.model)
print(car2.year)

# 3. Validation :-

class Student:
    def __init__(self ,name , age) -> None:
        if age < 0:
            raise ValueError("Age cannot be negative")
        self.name = name
        self.age = age
    
student = Student("Sivudu" , 5)
print(student.name)
print(student.age)

# 4. Object Composition

class Address:
    def __init__(self , street , city , state , zip) -> None:
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip
        
class Employee:
    def __init__(self, name , address) -> None:
        self.name = name
        self.address = address
        
address = Address("New Thalari Street" , "Chittor" , "Ap" , 517590 )
employee = Employee("Rama" , address)
print(employee.name)
print(employee.address.street)

# 5. Inheritance:-
class Animal:
    def __init__(self , name , age) -> None:
        self.name = name
        self.age = age
        
class Dog(Animal):
    def __init__(self ,name, age , breed) -> None:
        super().__init__(name , age)
        self.breed = breed

dog = Dog("Buddy" , 4 , "Golden Retriever")
print(dog.name)
print(dog.age)
print(dog.breed)





