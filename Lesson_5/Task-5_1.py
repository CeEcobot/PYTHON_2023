# Последовательностью Фибоначчи называется
# последовательность чисел a0
# , a1
# , ..., an
# , ..., где
# a0
#  = 0, a1
#  = 1, ak
#  = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию

# НЕПРАВИЛЬНОЕ РЕШЕНИЕ - НЕВЕРНО СЧИТАЕТ ЧИСЛО!!!!
# def fibonacci (n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# n = int(input('Inter number n: '))

# fibonacci_array = [fibonacci(n) for _ in range(n)]
# print(f'Fibonacci namder = {fibonacci_array[n-1]}')

N = abs(int(input('Input number: ')))
def f(n):
    if n <= 1:
        return 1
    else:
        return f(n-1) + f(n-2)
print(f'Output: {f(N)}')