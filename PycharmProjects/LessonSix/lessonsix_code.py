"""
    Data Structures (structs) - implimentations of code people use to organize different
        types of data

    Stacks, Queues, and LinkedLists

    list, sets, tuples, dicts, maps, hashmaps, trees, doubly linkedlists, etc.

    Stacks
    - Stack of items
        - ints, strings, coords, language syntax
        - every operation has the constraint of having O(1)
            - constant time: no matter how many items you have it still takes the same amount
                of time to perform this action
    - LIFO: last in, first out
        - whatever item is added last is the first to come out

    4 operations
        1. Push
        2. Pop
        3. Peek
        4. Size
    - every operation has the constraint of having O(1)
            - constant time: no matter how many items you have it still takes the same amount
                of time to perform this action

    Why would we use this?
        - order might matter
        - user only needs the last element
        - more user-friendly
        - more organized data: look at most recent item
        - git fetching: only grabbing most recent data
        - there are actual practical applications
            - algorithms: BST (Binary-Search Tree)
                          DFS (Depth-First Search)

    Why would not we want to stack?
        - access to only top element
        - better ways to organize data
        - can't do much: only 4 functions
        - loss of data when popping
            - popping into another stack
                - reversing a stack
        - time efficiency: not scalable
            - list of 10000 items and I wanted to look at the value of the first item
            - O(n) operations to look at the first item

"""

class Stack:
    # initializer
    def __init__(self): #init is instantiate when you make an instance of this class, runs code
        #global variables, charictaristics/ atribues go here
        self.stack = [] #holding an empty list

    #to print out testing purposes
    def __str__(self):
        return str(self.stack)

    # adds/puts an element at the top of the stack
    def push(self, add): #function definition is whole the self itself is an argument anythign in parenthesis
        self.stack.append(add)

    # take the last element from the top of the stack and return it
    def pop(self):
        return self.stack.pop() #pop is a function
        # return self.stack(self.stack[-1])
        # return self.stack[-1] #you just called it
        # return self.stack.remove(self.stack[-1]) #returns none because you removed it,
        # when you remove something it does not return a value back

    #looks at the last item in the stack
    #looks at the item at the top of the stack
    def peek(self):
        return self.stack[-1]

    #returns how many items are in the stack
    def size(self):
        return len(self.stack) #len is a function

aStack = Stack()
print(aStack)
aStack.push(1)
print(aStack)
aStack.push(2)
print(aStack)
print (aStack.pop())
print(aStack)
print("peeking", aStack.peek())
print(aStack)
aStack.push(3)
print("size of the stack:", aStack.size())


"""
    Queue
    - A line that you wait in
    - FIFO: First in First out

"""

class Queue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return str(self.queue)

    # add item to the end or left of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # removes an item from the front the queue and returns the item
    def dequeue(self):
        self.queue.pop(0) # 0 for the index of the first element

    # returns how many items are in the queue
    def size(self):
        return len(self.queue)

    # returns if it's empty or not
    def isEmpty(self):
        if(self.size() == 0):
            return True
        else:
            return False

        """
            return self.size() == 0 (more efficient)
                turns into 0 == 0
                then into True

                turns into 1 == 0
                then into False

            return not bool(self.size())
            return not bool(len(self.queue))
            return not bool(self.queue)
            ****return not self.queue**** --- most simple ~~~~~

            truthy or falsy
            0 = false 1 = true
            "" = false "a" = true
            [] false [1 or anything else] = true

            self.queue = [] = false
            self.queue = [1,2] = true
        """


aQueue = Queue()
print("le queue:", aQueue)
aQueue.enqueue(1)
print("le queue:", aQueue)
aQueue.enqueue(2)
print("le queue:", aQueue)
print("popped", aQueue.dequeue())
print("le queue:", aQueue)
aQueue.enqueue(3)
print("le queue:", aQueue)
print("size of le queue:", aQueue.size())
print("isEmpty", aQueue.isEmpty())
bQueue = Queue()
print("bQueue isEmpty?:", bQueue.isEmpty())

