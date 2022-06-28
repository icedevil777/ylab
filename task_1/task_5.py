"""
Написать метод count_find_num, который принимает на вход список простых
множителей (primesL) и целое число, предел (limit), после чего попробуйте
сгенерировать по порядку все числа. Меньшие значения предела,
которые имеют все и только простые множители простых чисел primesL.
"""

from itertools import combinations_with_replacement
import math


def count_find_num(primesL, limit):
    min_num = max_num = math.prod(primesL)
    if min_num > limit:
        return []

    count_num = 1
    per_len = 1
    while True:
        combs = tuple(combinations_with_replacement(primesL, per_len))
        if math.prod((min_num,) + combs[0]) > limit:
            break
        for comb in combs:
            comb_prod = math.prod((min_num,) + comb)
            if comb_prod > limit:
                continue
            count_num += 1
            max_num = max(max_num, comb_prod)
        per_len += 1

    return [count_num, max_num]


primesL = [2, 5, 7]
limit = 500
print(count_find_num(primesL, limit))
