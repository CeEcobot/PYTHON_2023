# В этом файле работаем с данными из Базы данных
# Сама БД ф файле telephone.txt

def write_name(name):
    with open ("input.txt", "w", encoding = "UTF-8") as file:
        file.write(name)

def search_data(char):
    with open ("input.txt", "r", encoding = "UTF-8") as file:
        lst = file.readlines()
        for row in lst:
            if char in row:
                print(row)