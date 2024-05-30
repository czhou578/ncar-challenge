import math

'''
This function calculates the volume of a sphere given its radius
Formula for sphere volume: 4/3 * pi * r^3
'''
def volume_calculate(radius):
    if radius < 0: raise ValueError("radius must be positive")

    return (4 / 3) * math.pi * radius**3