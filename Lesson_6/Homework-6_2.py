# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

arr = [52, 33, 70, 39, 57, 59, 7, 2, 46, 69, 11, 74, 58, 60, 63, 43, 75, 92, 65, 19, 1, 79, 22, 38, 26, 3, 66, 88, 9, 15, 28, 44, 67, 87, 21, 49, 85, 32, 89, 77, 47, 93, 35, 12, 73, 76, 50, 45, 5, 29, 97, 94, 95, 56, 48, 71, 54, 55, 51, 23, 84, 80, 62, 30, 13, 34]

# Specify the range
min_value = 20
max_value = 40

# Find indices of elements in the specified range
indices = [index for index, value in enumerate(arr) if min_value <= value <= max_value]

# Print the indices
for index in indices:
    print(index)
