#!python3
"""
Create a function that determines the largest number in a list of values and returns it.
1 input parameter:
list: the numbers to be checked for the largest value

return: float value of the largest number

Sample assertions:
assert largest([3,10,3]) == 10
"""

def largest(x):
    x.sort(reverse=True)
    biggest = x[0]
    pass
    return biggest

assert largest([3,10,3]) == 10
