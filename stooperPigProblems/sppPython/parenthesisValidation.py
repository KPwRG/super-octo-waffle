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













