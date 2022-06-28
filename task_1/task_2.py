"""
Написать метод, который принимает 32-битное целое число и
возвращает строковое представление в виде IPv4-адреса
"""


def int32_to_ip(int32: int) -> str:
    num1 = int(int32 / 16777216) % 256
    num2 = int(int32 / 65536) % 256
    num3 = int(int32 / 256) % 256
    num4 = int(int32) % 256
    return f'{num1}.{num2}.{num3}.{num4}'


ints = [2149583361, 32, 0]

for i in ints:
    print('ip =', int32_to_ip(i))
