def reverseArray(x):
    for i in range(0, len(x)//2, 1):
        temp = x[i]
        x[i] = x[len(x)-1-i]
        x[len(x)-1-i] = temp
    return x
print(reverseArray([5,6,7,8,9,95]))

# def reverseArray(x):
#     for i in range(0, intlen(x)/2, 1):
#         temp = x[i]
#         x[i] = x[len(x)-1-i]
#         x[len(x)-1-i] = temp
#     return x
# print(reverseArray([5,6,7,8,9,95]))