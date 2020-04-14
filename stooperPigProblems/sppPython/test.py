# # If number of opening does not equal to number of closing parenthesis
# # If closing parenthesis does not have corresponding opening parenthesis before it

# def parensValid(stringInput):
#     openParensCount = 0
#     closeParenCount = 0
#     for i in range(0, len(stringInput), 1):
#         if stringInput[i] == "(":
#             openParensCount += 1
#         elif stringInput[i] == ")":
#             closeParenCount += 1

#         if closeParenCount > openParensCount:
#             return False

#     if openParensCount != closeParenCount:
#         return False
#     else:
#         return True


# # def parensValid(stringInput):
# #     openParensCount = 0
# #     closeParensCount = 0
# #     for i in range(0, len(stringInput), 1):
# #         if stringInput[i] == "(":
# #             openParensCount +=1
# #         elif stringInput[i] == ")":
# #             closeParensCount += 1
# #         if closeParensCount > openParensCount:
# #             return False
        

# #     if openParensCount != closeParensCount:
# #         return False
# #     else:
# #         return True



# print(parensValid("((()))"))


# def palidrome(stringInput):
#     for i in range(0, len(stringInput)//2, 1):
#         if stringInput[i] != stringInput[len(stringInput)-1-i]:
#             return False
#     return True

# print(palidrome("tacocat"))
# print(palidrome("fred"))

# def isPalidrome(stringInput):
#     newStr = ""
#     for i in range(len(stringInput)-1, -1,-1):
#         newStr += stringInput[i]
#     if stringInput != newStr:
#         return False
#     else:
#         return True

# print(isPalidrome("racecar"))
# print(isPalidrome("potato"))


# # def bracketsValid(stringInput):
# #     openParensCount = 0
# #     closeParenCount = 0
# #     openCurlyCount = 0
# #     closeCurlyCount = 0
# #     openSquareCount = 0
# #     closeSquareCount = 0
# #     for i in range(0, len(stringInput), 1):
# #         if stringInput[i] == "(":
# #             openParensCount += 1
# #         elif stringInput[i] == ")":
# #             closeParenCount += 1
# #             if stingInput[i] == "{"
# #                 openCurlyCount += 1

# #         if closeParenCount > openParensCount:
# #             return False

# #     if openParensCount != closeParenCount:
# #         return False
# #     else:
# #         return True




# # Book Index

# y = [4,5,6,12,14,18,19,20,21,22,56]

# # desired result = "4-6,12,14,18-22,56"


# def bookIndex(listInput):
#     newString = ""
#     seqCounter = 0
#     for i in range(0, len(listInput)-1, 1):
#         if listInput[i+1]  == listInput[i] + 1:
#             if seqCounter == 0:
#                 newString += f"{listInput[i]} - "
#             seqCounter += 1
        
#         else:
#             newString += f"{listInput[i]}, "
#             seqCounter = 0
#     newString += f"{listInput[i+1]}"
#     return newString

# print(bookIndex(y))         





# Let's revisit Generate Coin Change!

# Change is inevitable (especially when breaking a twenty). Make generateCoinChange(cents). Accept a number of American cents, compute and represent that amount with smallest number of coins. Common American coins are pennies (1 cent), nickels (5 cents),dimes (10 cents), and quarters (25 cents).

# Instead of a string, we will return an object/dictionary.
# If the amount of cents was 33, you would return:

# generateCoinChange(33):

# return output
# {"Q" : 1, "D" : 0, "N" : 1, "P" : 3}


# There are MANY ways to do this algo! Try more than one!

# def generateCoinChange(cents):
#     change= {
#         "Q" : 0,
#         "D" : 0,
#         "N" : 0,
#         "P" : 0
#     }
#     change["Q"]=cents//25
#     change["D"]=(cents%25)//10
#     change["N"]=((cents%25)%10)//5
#     change["P"]=((cents%25)%10)%5

#     return change

# print(generateCoinChange(33))
    




# Singlely Linked List

class Node:
    def __init__(self, valueInput):
        self.value = valueInput
        self.next = None



class SLL:
    def __init__(self):
        self.head = None

    def append(self, value):
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

    def addtoFront(self, value):
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


sll1 = SLL()
sll2 = SLL()
sll1.append(5).append(8).append(3).addtoFront(4).addtoFront(1).display().contains(18)