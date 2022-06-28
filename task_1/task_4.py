"""
Написать метод bananas, который принимает на вход строку и
возвращает количество слов «banana» в строке.
"""
import itertools


def bananas(w: str) -> set:
    out = set()
    for word in itertools.combinations(range(len(w)), len(w) - len('banana')):
        arr = list(w)
        for i in word:
            arr[i] = '-'
        intermediate_result = ''.join(arr)
        if intermediate_result.replace('-', '') == 'banana':
            out.add(intermediate_result)
    return out


print(bananas('banana'))
