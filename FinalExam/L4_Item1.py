# Write a program that will generate 100 3-digit random numbers and
# store it in a list. The program should display the following:
# a. All elements in the list
# b. All numbers grouped by odd and even numbers
# c. All numbers divisible by 9.
# d. All prime numbers
# e. All numbers that contains the digit 9 (e.g 29, 91, 393, 961)

import random

listNum = []
for i in range(0,100):
    listNum.append(random.randint(100,999))

def print_all(list):
    print("All elements in the list:", end="")
    for i in range(len(list)):
        if i%20==0:
            print("")
        print(list[i],end="   ")


def group_oddEven(list):
    odd = []
    even = []

    for i in range(len(list)):
        if list[i]%2 == 0:
            even.append(list[i])
        else:
            odd.append(list[i])
    print("\n\nOdd Numbers:",end="")
    for i in range(len(odd)):
        if i%20==0:
            print("")
        print(odd[i],end="   ")

    print("\n\nEven Numbers:",end="")
    for i in range(len(even)):
        if i%20==0:
            print("")
        print(even[i],end="   ")

def divBy9(list):
    div9 = []
    for i in range(len(list)):
        if list[i]%9 == 0:
            div9.append(list[i])
    print(f"\n\nNumbers divisible by 9: \n{div9}")

def primeNumbers(list):
    primeList = []
    for i in list:
        prime = True
        for j in range(2, i):
            if i % j == 0:
                prime = False
                break
        if prime is True:
            primeList.append(i)

    print(f"\n\nPrime Numbers: \n{primeList}")

def list_has9(list):
    listHas9 = []
    for i in range(len(list)):
        if str(list[i]).__contains__(str(9)):
            listHas9.append(int(list[i]))
    print(f"\n\nContains 9: \n{listHas9}")

print_all(listNum)
group_oddEven(listNum)
divBy9(listNum)
primeNumbers(listNum)
list_has9(listNum)
