import math

'''
This function calculates the volume of a sphere given its radius
Formula for sphere volume: 4/3 * pi * r^3
'''
def volume_calculate(radius):
    if radius < 0: raise ValueError("radius must be positive")

    return (4 / 3) * math.pi * radius**3

if __name__ == '__main__':
    while True:
        try:
            radius = float(input("Enter the radius of the sphere: "))
            volume = volume_calculate(radius)
            print(f"The volume of the sphere with radius {radius} is {volume}")
        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nExiting...")
            break            