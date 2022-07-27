# Write a program that will display all numbers divisible by 3, 4 and 5 from 1-50.

div3 = []
div4 = []
div5 = []
for i in range(1,51):
    if i % 3 == 0 :
        div3.append(i)
    if i % 4 == 0 :
        div4.append(i)
    if i % 5 == 0:
        div5.append(i)
print(f"Divisible by 3:\n{div3}")
print(f"Divisible by 4:\n{div4}")
print(f"Divisible by 5:\n{div5}")


