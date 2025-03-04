# Type Casting = The process of converting a value of one data type to another
#                (string, integer, float, boolean)
#                 Explicit vs Implicit

name = "JohnDoe"
age = 25
gpa = 3.2
student = True

print(type(name)) # str
print(type(age)) # int
print(type(gpa)) # float
print(type(student)) # bool

print("\nExplicit Type Casting")

age = float(age)
print(age) # 25.0

gpa = int(gpa)
print(gpa) # 3

student = str(student)
print(student) # True
print(type(student)) # str

name = bool(name)
print(name) # True

print("\nImplicit Type Casting")

x = 2
y = 2.0

z = x / y

print(z) # 1.0
print(type(z)) # float