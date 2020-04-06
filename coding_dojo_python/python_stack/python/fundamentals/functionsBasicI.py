# Python Function Example

def values_greater_than_second(someList):
    if len(someList) < 2:
        return False
    else:
        newList = []
        secondVal = someList[1]
        for item in someList:
            if item > secondVal:
                newList.append(item)
        print(len(newList))
        return newList

print(values_greater_than_second([10,12,55,67,9]))