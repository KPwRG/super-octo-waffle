# Singlely Linked List

class Node:
    def __init__(self, valueInput):
        self.value = valueInput
        self.next = None



class SLL:
    def __init__(self):
        self.head = None

    def addToBack(self, value):
        newnode = Node(value)
        if self.head == None:
            self.head = newnode 
        else:
            #runner is created to have a variable i can use to iterate to singly linked list
            runner = self.head
            #use a while loop to iterate
            # print(runner.next) #this would print a node object
            while runner.next != None:
                runner = runner.next
            runner.next = newnode
        return self

    def display(self):
        print (self.head)
        runner = self.head
        outputstr = ""
        while runner !=None:
            outputstr += f"{runner.value}-->"
            runner = runner.next

        print(outputstr)
        return self

    def addToFront(self, value):
        newnode = Node(value)
        newnode.next = self.head
        self.head = newnode
        return self

    def contains(self, valueToFind):
        if self.head == None:
            return False
        else:
            runner = self.head
            while runner != None:
                if runner.value == valueToFind:
                    print("true")
                    return True
                else:
                    runner = runner.next
            print("false")
            return False

    def removeFront(self):
        if self.head == None:
            return self
        else:
            self.head = self.head.next

        return self

    def removeBack(self):
        if self.head == None:
            return self
        if self.head.next == None:
            self.head = None
            return self
        else:
            runner = self.head
            while runner.next.next != None:
                runner = runner.next
            runner.next = None
        return self

    def moveMinToFront(self):
            minVal = self.head.value
            runner = self.head
            while runner.next:
                if runner.next.value < minVal:
                    minVal = runner.next.value
                    nodeBeforeMin = runner
                    minNode = runner.next
                runner = runner.next
            nodeBeforeMin.next = nodeBeforeMin.next.next
            minNode.next = self.head
            self.head = minNode
            return self

    def appendVal(self, value, valueToFind):
        newNode = Node(value)
        runner = self.head
        if self.head == None:
            self.head = newNode
        else:
            while runner.next != None:
                if runner.value == valueToFind:
                    newNode.next = runner.next
                    runner.next = newNode
                    return self
                else:
                    runner = runner.next
        runner.next = newNode
        return self






sll1 = SLL()
sll1.addToBack(5).addToBack(3).addToBack(7).addToBack(2)
sll1.appendVal(12,7).display()