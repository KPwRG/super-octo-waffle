# If number of opening does not equal to number of closing parenthesis
# If closing parenthesis does not have corresponding opening parenthesis before it

def parensValid(stringInput):
    openParensCount = 0
    closeParenCount = 0
    for i in range(0, len(stringInput), 1):
        if stringInput[i] == "(":
            openParensCount += 1
        elif stringInput[i] == ")":
            closeParenCount += 1

        if closeParenCount > openParensCount:
            return False

    if openParensCount != closeParenCount:
        return False
    else:
        return True


# def parensValid(stringInput):
#     openParensCount = 0
#     closeParensCount = 0
#     for i in range(0, len(stringInput), 1):
#         if stringInput[i] == "(":
#             openParensCount +=1
#         elif stringInput[i] == ")":
#             closeParensCount += 1
#         if closeParensCount > openParensCount:
#             return False
        

#     if openParensCount != closeParensCount:
#         return False
#     else:
#         return True



print(parensValid("((()))"))


def palidrome(stringInput):
    for i in range(0, len(stringInput)//2, 1):
        if stringInput[i] != stringInput[len(stringInput)-1-i]:
            return False
    return True

print(palidrome("tacocat"))
print(palidrome("fred"))

def isPalidrome(stringInput):
    newStr = ""
    for i in range(len(stringInput)-1, -1,-1):
        newStr += stringInput[i]
    if stringInput != newStr:
        return False
    else:
        return True

print(isPalidrome("racecar"))
print(isPalidrome("potato"))


# def bracketsValid(stringInput):
#     openParensCount = 0
#     closeParenCount = 0
#     openCurlyCount = 0
#     closeCurlyCount = 0
#     openSquareCount = 0
#     closeSquareCount = 0
#     for i in range(0, len(stringInput), 1):
#         if stringInput[i] == "(":
#             openParensCount += 1
#         elif stringInput[i] == ")":
#             closeParenCount += 1
#             if stingInput[i] == "{"
#                 openCurlyCount += 1

#         if closeParenCount > openParensCount:
#             return False

#     if openParensCount != closeParenCount:
#         return False
#     else:
#         return True




# Book Index

y = [4,5,6,12,14,18,19,20,21,22,56]

# desired result = "4-6,12,14,18-22,56"


def bookIndex(listInput):
    newString = ""
    seqCounter = 0
    for i in range(0, len(listInput)-1, 1):
        if listInput[i+1]  == listInput[i] + 1:
            if seqCounter == 0:
                newString += f"{listInput[i]} - "
            seqCounter += 1
        
        else:
            newString += f"{listInput[i]}, "
            seqCounter = 0
    newString += f"{listInput[i+1]}"
    return newString

print(bookIndex(y))         