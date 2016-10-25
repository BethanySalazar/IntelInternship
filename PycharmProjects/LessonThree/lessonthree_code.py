"""
    Modules - libraries that someone has already created with some kind of functionality. Made code. Ex.Power created in Lesson

    import, from, as - takes info from different libraries to use

"""

import math #math library in python to do basic math
from math import pow
from math import pow as p #as lets you import variable in a different name
#import django-admin -- third party module

import power

# ** = math.pow(x,y)

print (math.pow(2,3)) # output 8.0, is a float
print (math.ceil(5.4)) # output 6, next biggest integer, (rounds)

print(power.power(3,4)) #output 81 ex. of imported module

print(pow(2,3)) # output 8.0
print(p(2,3)) # output 8.0

# itertools, collections, cmath, math

"""
    Functions - blocks of code that do stuff
    sectioned, scoped, takes input, may or may not return values

    ex. print, input, pow, int, str, format, center, ljust, rjust...

    def * **
"""
#Function Examples:
print()
def example(): #function definition
    print("Hello, World!") # a subroutine because it does not really return anything
example()

def test(x, y): # x and y are parameters
    print(x**y) # a subroutine
test(2,2) # the stuff here are the arguments

# in python you dont need to define the arguments like in java
#public string func(name, age)

def func(name, age):
    return (name, age) #function
print(func("John, 2"))

#default arguments
#good for making stuff optional
def default(name="", age=0):
    return name, age
print("\ncalling default")
default()

"""
    args - arguments, you can name it anything
    kwargs - keyword arguments, useful if you dont want to depend on possitional arguments when you call it
"""

# keyword arguments
# like any other
def basic_arguments(computer, shoes):
    print(computer, shoes)
print()
basic_arguments('laptop','sandals')

def basic_keywords(fruit, action): #cleaner if you know what people will put in
    print(fruit,action)

basic_keywords(action="run", fruit="pineapple")

def keywords(**kwargs): #unpredictable, can be called whatever **loop, denote it with anything
    for key, value, in kwargs.items():
        print(key, value)
print(keywords(a="apple", b="banana", c="cherry", action="run"))

#arguments- args, dont have to add a variable
def arguments(*args):
    for arg in args:
        print(args)
arguments('123', 'apple', 'banana', 3, True)

"""
    file input/output

    open, close, readline, read, write

    Open- open the file and ready to stream

"""

f = open('input.txt', 'r')
# input.txt -- location of file you want to open
# 'r' -- read
# 'w' -- write
# 'a' -- append
# 'r+' -- read/write
print('reading file')
print(f.read())
f.close()

write_file = open('input.txt', 'w')
write_file.write('\n Anuthuh line')
write_file.close()

append_file = open('input.txt', 'a')
append_file.write('\nhello world i\'m back')
append_file.close()

f = open('input.txt', 'r')
print("\n opening again")
print(f.read())
f.close()

#readline() instead of read