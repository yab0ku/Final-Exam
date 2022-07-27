# Create a function in Python that accepts two parameters. The first will
# be a list of numbers. The second parameter will be a string that can
# be one of the following values: asc, desc, and none. If the second
# parameter is "asc," then the function should return a list with the
# numbers in ascending order. If it's "desc," then the list should be in
# descending order, and if it's "none," it should return the original list
# unaltered.

def sortList(listVal, mode):
    if mode == 'asc':
        return sorted(listVal)
    elif mode == 'desc':
        return sorted(listVal, reverse=True)
    elif mode == 'none':
        return listVal

listNum = [5,9,7,3,12,43]

print("asc:\n",sortList(listNum, 'asc'))
print("desc:\n",sortList(listNum, 'desc'))
print("none:\n",sortList(listNum, 'none'))