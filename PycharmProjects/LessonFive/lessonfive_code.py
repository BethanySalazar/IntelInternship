"""
    Object Oriented Programming (OOP)

    Making objects from a piece of code
    Objects - something that you make
    Class - bunch of similar characteristics

    Why do we use OOP?
    - easier to organize
    - logical
    - easy to understand
    ---
    - Modularise code: break up code into reusable snippets
        - Plug-in & plug-out code
    - Easier to maintain and modify code
    - Encourages abstraction to hide complicated code
    - Give users a clearly defined interface

    Why would we not use OOP?
    - Because it's fit for the job
    - There may be other programing paradigms right for the job
        - Data-driven
        - Functional Programming

    Programming Paradigm
    - A way of programming
    - Similar to TAXONOMY (biology, maybe)

    Objects and Classes
    Class - bunch of similar characteristics shared across different objects
        - A blueprint/template
        - Defines everything that is needed for the object during instantiation
        - Defines all of the characteristics that an object needs
    Objects - something that you make
        - Defined from a class
        - Overarching data type from which everything inherits from
        - Has a bunch of characteristics
        - Almost everything is an object
        Python
        - Int, Boolean, String, Float, List, Dictionary, Set, Tuple...

    Encapsulation (basis of OOP)
     - Grouping all items into a single unit
     ex. all of the characteristics of a class
     ex. putting everything into a single class

    Inheritance
    - Acquires properties of another class
    Polymorphism
    Abstraction
"""
class Animal(object):
    def init (self):  #init is like an initializer
        #self it self is the thing we are working on. referense of object at runtime.
        #run whenever the objejct instance is created
        #characteristics
        self.numLegs = 4 #even if we "defined" numLegs and color by itself it acts as if it didn't have anything
        self.color = "brown" #self is required on everything.

    def eat(self):
        print("Om nom. Just ate.")

    #encapsulated all this

anAnimal = Animal()
print(anAnimal) #you've created an animal object and created a memory of it. "Dadmehr birth the baby"
print(Animal) #shows you the location
# print(anAnimal.eat()) no need to do this
anAnimal.eat() #acess or run eat object -> 1. anAnimal variable which holds/referenses animal object
# 2. eat 3. () -want to run the function of the print statement (prints out whats in eat)

"""
    Inheritance

    Animal
    - Birds
    - Dogs
    - Cats
    - Fish
    - Reptiles

 Animal = parent class
 cat = child class
"""


class Cat(Animal): #here you do the inheritance. You pass Animal class through it.
    pass #not gonna do anything else, dont want to add anything else

aCat = Cat() #cat object in memory
print(aCat)
aCat.eat() #prints "Om nom. I just ate"
# print(aCat.color()) error
print(anAnimal.color) #needed that self that referenses object at run time

blueCat = Cat() #referense and change whats in the main class
blueCat.color = "blue"
print(blueCat.color)

"""
    Polymorphism
    - takes many forms
    - changing an existing function to suit a subclass requirement
        Subclass/child class requirements

    Override (not present in Python)
    - taking a function and making it do something completely different
    Overloading
    - defining a function with the same name with different functionality
    - allowed by different function definitions
        - different parameters(arguments)

"""

class Dog(Animal):
    def eat(self): #definition
        print("On nom. I just ate dog food.")

#    def eat(self, food):
#       print("Om nom, I just ate, but I ate {0} instead.")
#            .format(food))

aDog = Dog()
aDog.eat()

"""
    Abstraction
    - being able to hide all of the details of how something works

    print()- we know how to use it, what it does, but not how it works
"""

class Calc(object):
    def __init__(self):
        pass

    def generateNum(self, num):
        num =+ 2
        num -= num * num
        num == 5
        num = num + 3 * 4
        return num

aCalc = Calc()
print(aCalc.generateNum(5)) #know that it does something

import math
print(math.pow(2,2)) #we never know what math does. We knows it does something to get result.

"""
    Getter and setter methods
    -
"""
class Person(object):
    def __init__(self):
        self.numLegs = None
        self.eyeColor = None
        self.abs = None

    #setter methods
    def setNumLegs(self, numLegs): #getting user input and setting to the attribute
        self.numLegs = numLegs
    #getter method
    def getNumLegs(self):
        return self.numLegs

a = Person()
a.setNumLegs(4)
print(a.getNumLegs(), "legs")

a.numLegs = 3 #setting
print(a.numLegs) #getting

#you can run more functionality, easier for user to use