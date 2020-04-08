# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]


def positiveBig(listInput):
    for i in range(0, len(listInput), 1):
        if listInput[i] > 0:
            listInput[i] = "big"
    return (listInput)

z = positiveBig([-1, 5, -9, 10])
print(z)

# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it


def countPositive(listInput):
    positiveCounter = 0
    for i in range(0, len(listInput), 1):
        if listInput[i] > 0:
            positiveCounter += 1
    listInput[len(listInput)-1] = positiveCounter
    return listInput

print(countPositive([-1,1,1,1]))
print(countPositive([1,6,-4,-2,-7,-2]))

# Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

def sumTotal(listInput):
    sum = 0
    for i in range(0, len(listInput), 1):
        sum += listInput[i]
    return sum

z = sumTotal([1,2,3,4])
print(z)

# Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5

def returnAverage(listInput):
    average = 0
    sum = 0
    for i in range(0,len(listInput),1):
        sum += listInput[i]
    average = sum/len(listInput)
    return average

z = returnAverage([1,2,3,4])
print (z)

# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

def returnLength(listInput):
    return len(listInput)

z = returnLength([1,2,3,4,5,6])
print(z)
x = returnLength([])
print(x)

# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

def returnMin(listInput):
    if len(listInput) == 0:
        return False
    minVal = listInput[0]
    for i in range(0, len(listInput), 1):
        if listInput[i] < minVal:
            minVal = listInput[i]
    return minVal


z = returnMin([37,2,1,-9])
print(z)
x = returnMin([])
print(x)

# Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False

def returnMax(listInput):
    if len(listInput) == 0:
        return False
    maxVal = listInput[0]
    for i in range(0, len(listInput), 1):
        if listInput[i] > maxVal:
            maxVal = listInput[i]
    return maxVal


z = returnMax([37,2,1,-9])
print(z)
x = returnMax([])
print(x)

# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

def ultimate_analysis(listInput):
    newDictionary = {}
    newDictionary["sumTotal"] = sumTotal(listInput)
    newDictionary["average"] = returnAverage(listInput)
    newDictionary["minimum"] = returnMin(listInput)
    newDictionary["maximun"] = returnMax(listInput)
    newDictionary["length of the list"] = returnLength(listInput)
    return newDictionary

print(ultimate_analysis([37,2,1,-9]))

# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

def reverse_list(listInput):
    temp = 0
    for i in range(0, len(listInput)//2, 1):
        temp = listInput[i]
        listInput[i] = listInput[len(listInput)-1-i]
        listInput[len(listInput)-1-i] = temp
    return listInput
print(reverse_list([37,2,1,-9]))
