"""
    Python's build in data structures

    lists
        - array that holds stuff
            - holds anything
            ex. lists, strings, functions, lambdas, classes, etc.
        - mutable
        ex. [1,2,3] -> [2,2,3]
        - non homogeneous
        ex. ['a string', 5, [1,2,3]]
        - length-independent
        [1,2,3] (length = 3) -> [1,2,3,4] (length = 4)

    Index - its place in the array
    ex.['a', 'string', 'asdf']
       [0,       1,      2   ]

    mutable & immutable-
    mutable - changeable or can be edited or overwritten
    immutable - not changeable or edited or overwritten

    homogeneous - same; only allows the same data types
    ex. [only integers], [only strings]

"""

aList = [1,2,3]
print('alist', aList)

# adding a list: append
aList.append(4)
print('alist append', aList)
aList.append('5')
print('append "5"', aList)

# removing from a list: remove
aList.remove(1)
print('alist remove', aList) #if element is in the list it removes it
aList.remove(1)
print('alist remove', aList)
# aList.remove(1)
# print('remove 1', aList)

# indexing a list uses - []
firstElement = aList[0]
print('firstElement of aList', firstElement)

# pop from list: pop - you remove it and hold it, it returns the element
poppedElement = aList.pop()
print('poppedElement:', poppedElement)
print('aList:', aList)
poppedElement = aList.pop(1) #can pop any element by its index

"""
    Indexing and Slicing
    Index - its place in the array
    ex.['a', 'string', 'asdf']
       [0,       1,      2   ]
    Indexing/Accessing/Retrieving - accessing the element at the desired
    Slicing - advanced indexing; indexes multiple elements at the same time
    [:] square brakets with collen
"""
bList = ['my', 'name', 'is', 'John', 'doe']
print(bList[1])
print(bList[2], bList[4])
# slicing, returns a list back, with just indicated things
print(bList[0:4])
print(bList[:3])
# output = ['doe', 'john', 'is']
print(bList[4])


# indexing backwards
print(bList[-1]) #to move backwards use neg numbers
print(bList[-1:1])
# output = []
print(bList[-1:1:-1])

print(bList[1:5])
# want all just add one output = ['name', 'is', 'john', 'doe']

print(bList[1:])
# output ['name, is, john, doe

print(bList[::2]) #changing step
# output [ my, is, doe]

# back to strings
aString = 'abcedfg'
print(aString[2])
#c
print(aString)
#abcedfg
print(aString[6])
#g
print(aString[-1])
#g

#modifying a list element, replaces an element
print()
print('bList', bList)
bList[-2] = 'richard'
print('bList with Richard', bList)

bList[0:4] = 'asdf' #'asdf' = ['a', 's', 'd', 'f'] replaces and adds extras
print('blist with asdf', bList)

"""
    Tuples()
    - just like a list
        - non-homogeneous
        - iterable
    -UNLIKE A LIST
        - immutable
        - length-independent
"""
print()
aTuple= (1,2,3,4,5)
print('aTuple', aTuple)
# aTuple.add(6) - you can't add to a Tuple
# print('added 6', aTuple)
print(aTuple[0])

bTuple = (6,7,8)
cTuple = aTuple+bTuple
print(cTuple) #can concatinate

"""
    Sets {}
    - like a list
        - holds things
        - iterable
        - length-independent
    -UNLIKE A LIST
        - homogeneous
        - immutable
        - only contain unique values
"""

print()
duplicates = [1,1,2,2,3,3]
aSet = set(duplicates) #set()
print(aSet)
aSet.add(4)
print(aSet)
aSet.remove(1) #you delete the actual value
print(aSet)

#unions, interesetions, differences, symmetric_differences

"""
    Dictionaries/Hashes/Maps/HashMap {}
    - containers with key: value pairs
        - don't use indices
        - instead, they use keys
    - keys
        - can be strings, integers..
        - immutable
    - values
        -literally can be anything
    - unordered
"""
aDict = {# empty dictionary{}
    'a': 'apple',
    'b':'banana',
    'c':'cherry'
}
print(aDict['a'])
print(aDict['b'])
# adding
aDict['d'] = 'drangonfruit'
print(aDict['d'])

# see all keys
print(aDict.keys())

# values
print(aDict.values())

# see all keys & values
print(aDict.items())
# prints as tuples

"""
    Performance, Time complexity, Expense

    Performance
    - if something runs fast

    Time complexity
    - how long something will take to run or perform an operation
    - Big(O) notation
        O(1) - no matter how much data you have, time performance is constant;
                most optimal
            ex. [1,2,3,4,5] .001 u-seconds to pop 5
                [1,2,3] .001 u-secs to pop 3
        O(n) - your time scales linearly with your data size
                Dont really want to use anything more than this
            ex. [1,2,3,4,5] 1 second to print each value in the list
                [1,2,3,4,5,6,7,8,9,10] 2 seconds to print each
            ex2.O(2n+2) = O(n) scales linearly
        O(n^2) - time scales exponentially with your data
            ex. [1,4,3,2,5] 3 seconds to bubble sort
        O(log(n)) - choice delineation
            ex. bunch of branches of an if statement
                n would be number of branches
        n is the number of items or elements in the dataset

    Expense
    - "is it expensive to do x?"
        - Well, is it fast? What time complexity does it run under?
        - How much memory does it take?

"""

"""
    Error Handling
    Exception Handling
    Error Catching

    Error - when code does not compile - does not happen in python
        - can't run
        - any problem with code
        - anything that cuses your program to break

    Three types of error
    - Compile-time
    - Runtime
    - Logic errors - hardest to fix

    Try Except
    Raise Finally

        Try -- try to do something that might result in a runtime error
        Except -- run this code if the try results in an error
        Finally -- code that runs no matter what
        Raise -- create an error and send to user
"""
#myVar = int('a') contains an error with no integer there
#print(aVariable) Name error because it does not exists
try:
    # myVar = int('a')
    myVar = 5/0 #this is not a valueerror, its a zero division error
except (ValueError, ZeroDivisionError): # except: by its self can catch any error. Can be a ValueError, ZeroDivisionError
    print('you ran into a Value Error')
#with parenthesis it can be a tuple containing specific errors
except NameError as a: #referencing a variable before instantiation
   # print("You ran into a Name Error")
    print("Error:", a)
finally:
    print("you're done catching errors")

try:
    raise Exception('you didn\'t crack the eggs')
except Exception as exc:
    print(exc)

raise(Exception('you didn\'t crack the eggs))

num = int(input("Please enter a number under 100: "))
if(num>=100):
    raise(Exception("u didn\'t listen 2 me"))
#your own error message if its over 100