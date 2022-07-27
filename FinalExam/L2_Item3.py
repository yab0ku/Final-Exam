# Write a program that prompts the user to input a number between 0
# and 35. If the number is less than or equal to 9, the program should
# output the number; otherwise, it should output A for 10, B for 11, C for
# 12… and Z for 35.

lettersList = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
_input = int(input("Enter a number(0-35): "))

print("Result:")
if _input <= 9 and _input >= 0:
    print(_input)
elif _input > 9 and _input <= 35:
    print(lettersList[_input-10])
else:
    print("Invalid input!")