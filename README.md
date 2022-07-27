# FinalExam
Lainez, Grand Vince J.
BSCS 3B

LEVEL 2: (5 points each)

2. In a right triangle, the square of the length of one side is equal to the sum of the squares of the lengths of the other two sides. Write a program that prompts the user to enter the length of the three sides of a triangle and then outputs a message indicating whether the triangle is a right triangle.

CODE:

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

OUTPUT:
 
![image](https://user-images.githubusercontent.com/82772962/181285619-135a5fa7-b7ed-4880-a4a4-8275aa3825ab.png)

3. Write a program that prompts the user to input a number between 0 and 35. If the number is less than or equal to 9, the program should output the number; otherwise, it should output A for 10, B for 11, C for 12… and Z for 35.

CODE:

lettersList = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
_input = int(input("Enter a number(0-35): "))

print("Result:")
if _input <= 9 and _input >= 0:
    print(_input)
elif _input > 9 and _input <= 35:
    print(lettersList[_input-10])
else:
    print("Invalid input!")
    
OUTPUT:
![image](https://user-images.githubusercontent.com/82772962/181289836-4e6a70f8-b2a8-4024-85fb-292de193e3d1.png)


