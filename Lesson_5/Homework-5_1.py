# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

def recur(A,B,mult):
    if B == 0:
        return A
    return recur(A * mult, B-1, mult)
A = int(input('Введите первое число: '))
B = int(input('Введите второе число: '))
print(recur(1, B, A))