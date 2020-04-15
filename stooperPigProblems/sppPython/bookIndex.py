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