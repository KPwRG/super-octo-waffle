# Base case - simplest case output
# Recursive case

def rSigma(input):
    if input <= 0:
        return 0
    elif input == 1:
        return 1
    else:
        return input + rSigma(input-1)

# “ Recursive Factorial
# Given num, return the product of ints from 1 up to num. If less than zero, treat as zero. If not integer, truncate. Experts tell us 0! is 1. rFact(3) = 6 (123). Also, rFact(6.5) = 720 (12345*6).”

