names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names[2])
print(names[-1])
print(names[2:])
# prints from third to end
print(names[2:4])
# prints third to fourth, does not include last one

names[0] = 'Jon'

# Find largest number in list
numbers = [1, 34, 34, 12312, 123, 23, 903, 341093, 34]
max_number = numbers[0]
for item in numbers:
    if item > max_number:
        max_number = item
print(f"The largest number is {max_number}.")

# 2D Lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# matrix[0][1] = 20
# print(matrix[0][1])
# for row in matrix:
#     for item in row:
#         print(item)

# List Methods
numbers = [5, 2, 1, 7, 4, 5, 5, 5]
numbers.append(20)
numbers.insert(0, 10)

# removes first mention of 5
numbers.remove(5)
# clears entire list
# numbers.clear()
# removes last item
numbers.pop()
print(numbers)
# finds index of first occurence of item
print(numbers.index(5))
# safer version, if not found returns false
print(50 in numbers)
print(numbers.count(5))
numbers.sort()
numbers.reverse()
print(numbers)
numbers2 = numbers.copy()
numbers2.append(10)
print(numbers2)

# Write a program to remove the duplicates in a list
list1 = [1, 3, 5, 5, 7, 9, 9, 9, 1]
checked_number = 0
check_count = 0
for item in list1:
    checked_number = item
    check_count = 0
    for number in list1:
        if checked_number == number:
            check_count += 1
            if check_count > 1:
                list1.remove(checked_number)

print(list1)

#Solution
numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)