"""
    Functional Programming - bunch of inputs and make a bunch of outputs
        - you don't change the state of any variable outside of the method scope

    Recursion - a method that calls on itself
        - there is a method call within the body of the method itself
        - very inefficient
        - Can back track

    Iterators
    Comprehensions
    Functional Methods


"""
"""
    Recursion~~~~~
"""
# recursion sub for for-loops
# Inefficient
def recurse(x):
    """
    Call recurse

    :param x: number
    :return: None
    """
    # First if- statement
    # if (x == 10):
        # pass # stops the code
    # else:
        # recurse(x + 1) # don't just keep it as x or it will not change in the loop

    if (x == 0):
        return x
    elif (x == 1):
        return 1
    else:
        return recurse(x - 1) + recurse(x - 2)  # don't just keep it as x or it will not change in the loop
# recurse(1) for first if- statement
print(recurse(10))
# do not run you will get the computer to freeze if no parameters exist.

"""
    Fibonacci - the sequence of the sum of its two previous fibonacci values
fibo_values = {
    0:0, # 1 and 0 basically 1+0
    1:1, # 1+1 = 2 goes one to next line
    2:1, # start calc numbers
    3:2,
    4:3
}
"""

for i in range (1, 10):
    print(i)

x = 1
while x < 10:
    print (x)
    x += 1
# = whats happening to recursion

"""
    Comprehensions

    Another way of looping through/creating data structures
"""

nums = []
for i in range(10):
    nums.append(i)

print('nums:', nums)

nums_comp  = [i for i in range(10)]

print('nums_comp:', nums_comp)

tuples = (x for x in range(10))
print('tuples:', list(tuples))

evens = []
for i in range (1,11):
    if(i % 2 == 0):
        evens.append(i)
    else:
        pass

print('evens:', evens)

evens_comp = [ i for i in range(1, 11) if (1% 2 == 0)]
print('evens_comp:', evens_comp)

"""
    Lambdas - unnamed function
        - a function that is used once and not saved
    lambda [input]:[statement]
"""
# def func(x):
    # x + 1

# ==

lambda x: x + 1

"""
    map() = built-in python function
        - applies a method to all items in an iterable
"""

names = ['richard', 'bobby', 'jennifer']
# give me the lengths of all names in names

for name in names:
    print(name, ':', len(name))

def something(x):
    return len(x) + 3

print(list(map(len, names))) # created a list of names with list lists the length of the names
print(list(map(lambda x: len(x)+3, names)))

"""
    sum() = sums things
"""
import random
some_nums = [random.randint(1,10) for i in range(10)]
print(some_nums)
print(sum(some_nums))

answer = 0
for num in some_nums:
    answer += num
print(answer)

"""
    reduce() - brings down an interable to one value
        - flexible with any lambda
"""
import functools
print('nums:', nums)
print('reduce:', functools.reduce(lambda x, y: x + y, nums))
"""
0 1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9
3 3 4 5 6 7 8 9
6 4 5 6 7 8 9
10 6 7 8 9
... reduce
"""