# Stacks
# Last In First Out
# Push to add
# Pop to remove

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.back = None

class Stack:
    def __init__(self):
        self.top = None

    def display(self):
        print (self.top)
        runner = self.top
        outputstr = ""
        while runner !=None:
            outputstr += f"{runner.value}-->"
            runner = runner.next
        print(outputstr)
        return self

    def push(self, value):
        # newNode = Node(value)
        # newNode.next = self.top
        # if self.top == None:
        #     self.top = newNode
        # else:
        #     newNode.next = self.top
        #     self.top = newNode
        # return self
        newNode = Node(value)
        newNode.next = self.top
        self.top = newNode
        return self

    def pop(self):
        if self.top == None:
            return self
        else:
            self.top = self.top.next
        return self 

    def contains(self, valueToFind):
        if self.top == None:
            return False
        else:
            runner = self.top
            while runner != None:
                if runner.value == valueToFind:
                    print("true")
                    return True
                else:
                    runner = runner.next
            print("false")
            return False

    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False

    def size(self):
        count = 0
        if self.top == None:
            return count
        else:
            runner = self.top
            while runner != None:
                count += 1
                runner = runner.next
            print(count)
            return count

def compareStacks(stack1, stack2):
    if stack1.size() != stack2.size():
        return False
    else:
        runner1 = stack1.top
        runner2 = stack2.top
        while runner1 != None:
            if runner1.value != runner2.value:
                return False
            else:
                runner1 = runner1.next
                runner2 = runner2.next
        return True        

# def stackToQueue(stack):
#     newStack = Stack()
#     newQueue = Queue()
#     newNode = Node()
#     if stack.top == None:
#         return self
#     else:
#         runner = stack.top
#         while runner != None:
#             newNode.vaule = runner.value
#                 newStack.self.top.next = newNode
            

firstStack = Stack()
# secondStack = Stack()
firstStack.push(5).push(4).push(3)
# secondStack.push(5).push(4).push(-3)

print(compareStacks(firstStack, secondStack))