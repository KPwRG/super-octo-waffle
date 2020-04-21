# Stacks
# Last In First Out
# Push to add
# Pop to remove

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

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






newStack = Stack()
newStack.push(5).push(4).push(-3)
newStack.push(19).push(2)
newStack.pop().display()
