# input()
# number = int(input(""))
# round(variable, 2)

name = input("Enter your name: ")
print(f"Hello {name}")

age = int(input("Enter your age: "))
age += 1
print(f"You are {age} years old")

# EXERCISE 1 MAD LIBS
adjective1 = input("Enter an adjective: ")
noun = input("Enter a noun: ")
adjective2 = input("Enter an adjective: ")
verb = input("Enter a verb: ")
adjective3 = input("Enter an adjective: ")

print(f"Today I went to a(n) {adjective1} zoo.")
print(f"In an exhibit, I saw a(n) {noun}.")
print(f"The {noun} was {adjective2} and {verb}ing.")
print(f"I was {adjective3}!")

# EXERCISE 2 AREA CALC
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
height = float(input("Enter the height: "))

# area = width * length
# print(f"The area is: {area}cm^2")

volume = width * length * height
print(f"The volume is: {volume}cm^3")

# EXERCISE 3 SHOPPING CART
item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))

total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is ${round(total, 2)}")