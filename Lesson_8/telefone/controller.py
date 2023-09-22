# В этом файле пишется функция

from database import *
from view import *

def main():
    while True:
        num = input_num()
        if num == 1:
            res = input_name()
            write_name(res)
            print("Успешно записано\n")
        if num == 2:
            char = input_char()
            search_data(char)
            print("Успешно найдено\n")


main()
