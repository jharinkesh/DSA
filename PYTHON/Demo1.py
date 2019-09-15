print("hello world")

a = 5
print("a = ",5)
a = "hi baba"
print("a = ",a)
print(type(a))

#Operators
#Operators are special symbols that carry out operations on operands (variables and values).
x = 35000
y = 17000
print(x+y)
print(x-y)
print(x/y)
print(x//y) #floor division
print(x*y)
print(x%y)
print(x**y)

#Assignment operators are used to assign values to variables
x = 5
x += 5
x /= 5
print(x)

#Get Input from User
inputString = input('Enter a sentence:')
print('The inputted string is:', inputString)

#This is a comment
# single line comment

"""This is a 
    multiline
    comment."""
    
'''This is also a
     multiline
     comment.'''
     
'''Type Conversion
The process of converting the value of one data type 
(integer, string, float, etc.) to another is called type conversion.
Python has two types of type conversion.'''

#Implicit conversion
#It doesn't need any user involvement.
#Python always converts smaller data type to larger data type to avoid the loss of data.

x = 34
y = 3.4
print(x+y)

#Explicit Conversion
#In case of explicit conversion, you convert the datatype of an object to the required data type.
#We use predefined functions like int(), float(), str() etc. to perform explicit type conversion
x  = 33
y = "34"
print(x+int(y))

'''Python Numeric Types
Python supports integers, floating point numbers and complex numbers. 
They are defined as int, float and complex class in Python.
In addition to that, booleans: True and False are a subtype of integers.'''

print(type(5))

#Output: <class>
print(type(5.0))

#<class>
c = 5 + 3j
print(type(c))

#Python Data Structures
#Python offers a range of compound datatypes often referred to as sequences

#Lists
#A list is created by placing all the items (elements) inside a square bracket [] separated by commas.
#It can have any number of items and they may be of different types (integer, float, string etc.)

#empty list
my_list = []
#list of integers
my_list = [1, 2, 3]
#list with mixed data types
my_list = [1, "Hello", 3.4]

language = ["French", "German", "English", "Polish"]
#Accessing first element
print(language[0])
#Accessing fourth element
print(language[3])

#You can also use list() function to create lists.
ls = list([12,33,33])
ls

#Python also allows negative indexing for its sequences. The index of -1 refers to the last item, -2 to the second last item and so on.
print(ls[-1])

#Tuples
#Tuple is similar to a list except you cannot change elements of a tuple once it is defined. Whereas in a list, items can be modifie
#tuple is immutable.
language = ("French", "German", "English", "Polish")
print(language[1]) #Output: German
print(language[3]) #Output: Polish
print(language[-1]) # Output: Polish

#You can also use tuple() function to create tuples.
t2 = tuple([1, 4, 6])
print('t2=', t2)

#You cannot delete elements of a tuple, however, you can entirely delete a tuple itself using del operator.
language = ("French", "German", "English", "Polish")
del language
# NameError: name 'language' is not defined
print(language)

#String
#A string is a sequence of characters. 
s = 'Hello'
print(s)
s = '''hi how are you'''
print(s)
s = """ Hi friends """
print(s)

ls = list(s)
print(ls)

#access individual characters of a string
print(s[-1])
print(s[1:5])
print(s[5:-2])

#Strings are immutable. You cannot change elements of a string once it is assigned.
s[0] = 'b'
del s

#Concatenation 
str1 = 'hi'
str2 = 'baba'
print(str1+str2)
print(str1*3)

#Sets
# A set is an unordered collection of items where every element is unique (no duplicates).
# set of integers
my_set = {1, 2, 3}
print(my_set)

# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

#Sets are mutable. You can add, remove and delete elements of a set. However, you cannot replace one item of a set with another as they are unordered and indexing have no meaning
# set of integers
my_set = {1, 2, 3}

my_set.add(4)
print(my_set) # Output: {1, 2, 3, 4}

my_set.add(2)
print(my_set) # Output: {1, 2, 3, 4}

my_set.update([3, 4, 5])
print(my_set) # Output: {1, 2, 3, 4, 5}

my_set.remove(4)
print(my_set) # Output: {1, 2, 3, 5}

#some commonly used set operations:
A = {1, 2, 3}
B = {2, 3, 4, 5}

# Equivalent to A.union(B) 
# Also equivalent to B.union(A)
print(A | B) # Output: {1, 2, 3, 4, 5}

# Equivalent to A.intersection(B)
# Also equivalent to B.intersection(A)
print (A & B) # Output: {2, 3}

# Set Difference
print (A - B) # Output: {1}

# Set Symmetric Difference
print(A ^ B)  # Output: {1, 4, 5}

#Dictionaries
#Dictionary is an unordered collection of items. While other compound data types have only value as an element, a dictionary has a key: value pair. For example:
# empty dictionary
my_dict = {}

#dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}

#dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}
my_dict

#access value from a dictionary,
person = {'name':'Jack', 'age': 26, 'salary': 4534.2}
print(person['age']) # Output: 26

#change, add or delete dictionary elements
person = {'name':'Jack', 'age': 26}

# Changing age to 36
person['age'] = 36 
print(person) # Output: {'name': 'Jack', 'age': 36}

# Adding salary key, value pair
person['salary'] = 4342.4
print(person) # Output: {'name': 'Jack', 'age': 36, 'salary': 4342.4}


# Deleting age
del person['age']
print(person) # Output: {'name': 'Jack', 'salary': 4342.4}

# Deleting entire dictionary
del person

#Python range()
#range() returns an immutable sequence of numbers between the given start integer to the stop integer.
print(range(1, 10)) # Output: range(1, 10)

numbers = range(1, 6)

print(list(numbers)) # Output: [1, 2, 3, 4, 5]
print(tuple(numbers)) # Output: (1, 2, 3, 4, 5)
print(set(numbers)) # Output: {1, 2, 3, 4, 5}

# Output: {1: 99, 2: 99, 3: 99, 4: 99, 5: 99} 
print(dict.fromkeys(numbers, 99))

# Equivalent to: numbers = range(1, 6)
numbers1 = range(1, 6 , 1)
print(list(numbers1)) # Output: [1, 2, 3, 4, 5]

numbers2 = range(1, 6, 2)
print(list(numbers2)) # Output: [1, 3, 5]

numbers3 = range(5, 0, -1)
print(list(numbers3)) # Output: [5, 4, 3, 2, 1]

#Python Control Flow

#if...else Statement
num = -1

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

if False:
  print("I am inside the body of if.")
  print("I am also inside the body of if.")
print("I am outside the body of if")

#while Loop
n = 100

# initialize sum and counter
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1    # update counter

print("The sum is", sum)

#for Loop
numbers = [6, 5, 3, 8, 4, 2]

sum = 0

# iterate over the list
for val in numbers:
  sum = sum+val

print("The sum is", sum) # Output: The sum is 28

#break Statement
#The break statement terminates the loop containing it. Control of the program flows to the statement immediately after the body of the loop. For example:
for val in "string":
    if val == "r":
        break
    print(val)

#continue Statement
#used to skip the rest of the code inside a loop for the current iteration only
for val in "string":
    if val == "r":
        continue
    print(val)

print("The end")

#Python Function
#A function is a group of related statements that perform a specific task.
def print_lines():
  print("I am line1.")
  print("I am line2.")

# function call
print_lines()

def add_numbers(a, b):
  sum = a + b
  return sum

result = add_numbers(4, 5)
print(result)

#Lambda Function - anonymous function
#define functions without a name
square = lambda x: x ** 2
print(square(5))


import math

result = math.log2(5) # return the base-2 logarithm
print(result) # Output: 2.321928094887362
abs(-67.98)
from math import pi
print("The value of pi is", pi)

#Python File I/O
#A file operation takes place in the following order.
#Open a file
#Read or write (perform operation)
#Close the file

# open a file
f = open("data.txt")
f = open("data.txt", mode='r')

#write to a file
#to write into a file in Python, we need to open it in write 'w', append 'a' or exclusive creation 'x' mode
f = open("data.txt", mode='w')
f.write('this is a school')
f.write('\nline1')
f.write('\nline2')
f.close()

#read files
f = open("data.txt",'r',encoding = 'utf-8')
f.read(4)

#Python Directory
#A directory or folder is a collection of files and sub directories. 
import os
os.getcwd()  # present working directory
os.chdir('D:\\Hello') # Changing current directory to D:\Hello
os.listdir()  # list all sub directories and files in that path
os.mkdir('test') # making a new directory test
os.rename('test','tasty') # renaming the directory test to tasty
os.remove('test')  # deleting old.txt file


#Python Exception Handling
#Errors that occur at runtime are called exceptions
import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!",sys.exc_info()[0],"occurred.")
        print("Next entry.")
        print()
print("The reciprocal of",entry,"is",r)


#Python OOP
#Everything in Python is an object including integers, floats, functions, classes, and None

#Class and Objects
#Object is simply a collection of data (variables) and methods (functions)
#class is a blueprint for the object

class MyClass:
  "This is my class"
  a = 10
  def func(self):
    print('Hello')

# Output: 10
print(MyClass.a)

# Output: <function 0x0000000003079bf8="" at="" myclass.func="">
print(MyClass.func)

# Output: 'This is my class'
print(MyClass.__doc__)

#Creating Objects
obj1 = MyClass()
print(obj1.a)  

obj2 = MyClass()
print(obj1.a + 5) 
obj1.func()

#Python Constructors
class Coordinate:
    def __init__(self,x = 0,y = 0):  # constructor
        self.x = x
        self.y = y

    def getData(self):
        print("{0}+{1}j".format(self.x,self.y))

c1 = Coordinate(2,3) # Create a new ComplexNumber object
c1.getData() # Output: 2+3j

c2 = Coordinate() # Create a new ComplexNumber object
c2.getData() # Output: 0+0j

#Python Inheritance
#Inheritance refers to defining a new class with little or no modification to an existing class
class Mammal:
  def __init__(self):
      print('Mammal cons')
  def displayMammalFeatures(self):
    print('Mammal is a warm-blooded animal.')

class Dog(Mammal):
  def __init__(self):
      print('Dog cons') 
  def displayDogFeatures(self):
    print('Dog has 4 legs.')

d = Dog()
d.displayDogFeatures()
d.displayMammalFeatures()
m = Mammal()

