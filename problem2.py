#!python3
"""
Create a function that finds the missing side in a right triangle.
3 input parameters:
float: one side
float: another side
boolean: indicates whether one of the sides is the hypotenuse

return: float length of the missing side

Sample assertions:
assert hypotenuse(12,5,False) == 13
assert hypotenuse(5,3,True) == 4
(2 points)
"""
def hypotenuse(x,y,z):
    if z == True:
        if x > y:
            hyp = x
            side = y
            miss = ((hyp**2)-(side**2))**(1/2)
        elif y > x:
            hyp = y
            side = x
            miss = ((hyp**2)-(side**2))**(1/2)
    elif z == False:
        miss = ((x**2)+(y**2))**(1/2)
    if miss%1 == 0:
        miss = int(miss)
    return miss


print(hypotenuse(12,5,False))
