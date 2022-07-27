# In a right triangle, the square of the length of one side is equal to the
# sum of the squares of the lengths of the other two sides. Write a
# program that prompts the user to enter the length of the three sides of
# a triangle and then outputs a message indicating whether the triangle
# is a right triangle.

firstSide = float(input("First side: "))
secondSide = float(input("Second side: "))
thirdSide = float(input("Third side: "))

if secondSide ** 2 + thirdSide ** 2 == firstSide ** 2:
    print("It is a right triangle")
elif firstSide ** 2 + thirdSide ** 2 == secondSide ** 2:
    print("It is a right triangle")
elif firstSide ** 2 + secondSide**2 == thirdSide ** 2:
    print("It is a right triangle")
else:
    print("It is not a right triangle")