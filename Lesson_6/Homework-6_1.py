# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# Get input from the user
a1 = int(input("Enter the first element: "))
d = int(input("Enter the common difference: "))
n = int(input("Enter the number of elements: "))

# Calculate and fill the array
arithmetic_array = [a1 + (i-1) * d for i in range(1, n+1)]

# Print each element on a new line
for element in arithmetic_array:
    print(element)