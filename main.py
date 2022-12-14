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
