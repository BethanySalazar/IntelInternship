"""
    Control Structures
    06.22.16

    Ranges & Lists

    Ranges
    range(x, y, step)
    - x: starting
    - y: number to stop at (-1)
    - step: the number to increment by

    List
    [a, b, c, d]
    ints, string, floats, booleans, classes, functions, lambola
    [[]]
"""

print(list(range(0,10,1))) #from o-9 in increments of one

aList = [1,2,3]
print(aList)

"""
    In operator
    boolean operator or pull from list
"""

#boolean operator
print (1 in aList) #true
print('A' in aList) #false

"""
    for
    loop through a range of numbers, items of a list other date structures
    for i in range(0,10,1) = for i in range (0,10)
"""
print()
for i in range(0,10):
    print(i)
    """ extra code """
else:
    #if you reach the end of the list
    print("you have reached the end of the list")

for item in aList:
    print(item)

"""
    while('expression') == True):
    while loops while expression is true
"""

x = 3
print()
while (x>0):
    print(x)
    x-= 1
else:
    #runs when the expression in the while loop is false
    print("x is equal to 0\n")

for x in range(3,0,-1):
    print(x)

"""
    if statements
    if('expression' == True):
        'code'
    elif('expression' == True):
        'elif code'
    else:
        'else code'
"""
x = 2
if (2==2):
    print(x)
elif (x==3):
    print(x)
else:
    print(x, "isn't a number maybe")

"""
    break continue
    break - if the interpreter ever reaches break, break out of the preceding loop

    continue - stops the iteration and goes to the next iteration
"""

for i in range(0,10):
        if(i==5):
            print("I'm breaking")
            #break
        elif (i==6):
            print("gonna just continue")
            continue
        else:
            print(i)

        print("finished checking if conditions")
else:
    print("some else code")

"""
    pass- do nothing
"""

for i in range(0,10):
    if(i < 5):
        print(i)
    elif(i == 7):
        pass
    else:
        print(i, "some things")

"""
    nested loops
"""

a = ["apple", "banana", "kiwi"]
for fruit in a:
#"apple" = ["a", "p", "p", "l", "e"]
    for letter in fruit:
        print(fruit)


