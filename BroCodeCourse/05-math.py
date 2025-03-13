# Arithmetic Operators
number = 5
number += 7 # Addition +
number -= 2 # Subtraction -
number *=3 # Multiplication *
number /= 2 # Division /
number //= 2 # Floor Division //
             # Floor division means the // will always take the floor or the lower number.
             # 5/3 = 1,666
             # 5//3 = 1
remainder = number % 4 # Modulus %
number **= 2 # Power/Exponentiation **

print(number)
print(remainder)

# Built-in Math Functions
x = 4.74
y = -4
z = 6

rounded = round(x) # 5
absolute = abs(y) # 4
power = pow(2, 3) # 8
highest = max(x, y, z) # 6
lowest = min(x, y, z) # -4

# Math Module
import math

print(math.pi) # 3.141592653589793 (π)
print(math.e) # 2.718281828459045 (Euler's number)
square_root = math.sqrt(25) # 5
round_up = math.ceil(1.2) # 2
round_down = math.floor(5.9) # 5

# Exercises
# 1. Circumference of a Circle
radius = float(input("Enter the radius of a circle: "))
circumference = 2 * radius * math.pi
print(f"The circumference is: {round(circumference, 2)}cm")

# 2. Area of a Circle
area = math.pi * pow(radius, 2)
# area_v2 = math.pi * radius ** 2
print(f"The area of the circle is: {round(area, 2)}cm^2")

# 3. Hypotenuse of a Right Triangle
a = float(input("Enter side 'a': "))
b = float(input("Enter side 'b': "))
c = math.sqrt(pow(a,2) + pow(b,2))
print(f"The hypotenuse (side 'c') of the right triangle is {c}")
