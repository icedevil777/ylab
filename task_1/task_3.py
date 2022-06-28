"""
Написать метод, который принимает на вход int и возвращает
количество конечных нулей на конце факториала заданного числа
"""
from math import log


def zeros(num):
    if num < 1:
        return 0
    k_max = int(log(num, 5))
    zer = 0
    for k in range(1, k_max + 1):
        zer += int(num / 5 ** k)
    return zer


print(zeros(11))

