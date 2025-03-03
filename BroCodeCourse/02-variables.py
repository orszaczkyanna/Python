# Variable = A container for a value (string, integer, float, boolean)
#            A variable behaves as if it was the value it contains

# String
first_name = "Jane"
last_name = "Doe"

# Integer
age = 25

# Float
price = 10.99

# Boolean
is_student = True # False

# f-string: formatted string literals
# f: format
print(f"Hello {first_name} {last_name}!")
print(f"You are {age} years old.")
print(f"The price is ${price}.")

if is_student:
    print("You are a student.")
else:
    print("You are NOT a student.")
    