# if = Do some code IF condition is True
# elif
# else = Do something else if above condition/s are False

# Ternary Operator = "True" if CONDITION else "False"

# String Methods
# variable.lower() = lowercase
# variable.upper() = uppercase
# variable.strip() = remove leading and ending whitespace characters

# EXAMPLE 1
age = int(input("Enter your age: "))

if age >= 100:
    print("You are too old to sign up")
elif age >= 18:
    print("You are now signed up")
elif age < 0:
    print("You haven't been born yet")
else:
    print("You must be 18+ to sign up")

# EXAMPLE 2
online = True

if online:
    print("You are online")
else:
    print("You are offline")

# EXAMPLE 3
response = input("Do you want some food? (Y/N): ")

#if response == "Y" or response == "y":
if response.strip().lower() == "y":
    print("Have some food")
else:
    print("No food for you")

# Ternary Operator
n = 5
res = "Even" if n % 2 == 0 else "Odd"
print(res)

# Short Hand If
a = 10
b = 5
if a > b: print(f"{a} is greater than {b}")