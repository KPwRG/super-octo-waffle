# Bracket Validation

def bracketsValid(stringInput):
    openParensCount = 0
    closeParenCount = 0
    openCurlyCount = 0
    closeCurlyCount = 0
    openSquareCount = 0
    closeSquareCount = 0
    for i in range(0, len(stringInput), 1):
        if stringInput[i] == "(":
            openParensCount += 1
        elif stringInput[i] == ")":
            closeParenCount += 1
            if stingInput[i] == "{"
                openCurlyCount += 1

        if closeParenCount > openParensCount:
            return False

    if openParensCount != closeParenCount:
        return False
    else:
        return True