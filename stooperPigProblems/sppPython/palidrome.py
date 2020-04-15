#  Palidrome


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