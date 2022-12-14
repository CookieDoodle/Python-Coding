print("Hello")

if 5 > 2:
    print("5 is bigger than 2")

x, y, z = "Orange", "Banana", "Strawberry"
print(x, "is better than", y)

print("But isn't {} also good?".format(z))

a = "Chocolate"
print(f"Clearly {a} is the best!")

# I want to do some math
nums = [1, 21, 7, 13, 4]
maxNum = 0
for x in nums:
    if x > maxNum:
        maxNum = x
print(maxNum)

# User input
"""
name = input("Enter your name: ")
print("Your name is: " + name)

print("Okay, " + name + " let's go on an adventure!")
"""

numi = 0
if bool(numi):
    print("YES")
else:
    print("NO")

gay = True
if gay:
    print("You are gay")


class MathDo:
    x = 5


p1 = MathDo()
print(p1.x)

"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)

print(p1.name)
print(p1.age)
"""

"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"


p1 = Person("John", 36)

print(p1)
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person("John", 36)
p1.myfunc()


# Karl(34) Input from User for TextAdventure!
class UserInput:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello! Your name is " + self.name + ".")
        print("You are " + self.age + " years old.")

    def __str__(self):
        return f"{self.name}({self.age})"


print("Welcome to this Text Adventure!")
user1 = UserInput(input("But first! Who are you?\n"), input("And how old are you?\n"))
user1.myfunc()

print(user1)
