# Base case - simplest case output
# Recursive case
# “ String: In-Order Subsets
# Create strSubsets(str). Return an array with every possible in-order character subset of str. The resultant array itself need not be in any specific order – it is the subset of letters in each string that must be in the same order as they were in the original string. Given “abc”, return an array that includes [“”, “c”, “b”, “bc”, “a”, “ac”, “ab”, “abc”] (in any order).”
# Excerpt From: Martin Puryear. “Algorithm Challenges: E-book for Dojo Students.” iBooks.

def ios(str, sub="", i=0):
    if len(str) == i:
        return [sub]
    else:
        return ios(str, sub+str[i], i+1) + ios(str, sub, i+1)

print(ios("abc"))



