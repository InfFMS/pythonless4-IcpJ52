# Напишите функцию convert_base(num, from_base, to_base),
# которая переводит натуральное число num из системы
# счисления с основанием from_base в систему счисления
# с основанием to_base
# 2 ≤ to_base ≤ 36 ; 2 ≤ from_base ≤ 36
# На входе три числа num, from_base, to_base
# На выходе одно число - результат работы функции
# Подсказка (если не получается решить):
# Попробуйте разбить задачу на две подзадачи:
# перевод из десятичной системы счисления в любую
# перевод из любой системы счисления в десятичную
# Объедините эти две подзадачи, получите ответ.
def convert_from_base_10(num, to_base):
    num = int(num)
    res = ''
    while True:
        r = num % to_base
        if r >= 10:
            res += chr(r + 55)
        else:
            res += str(r)
        num //= to_base
        if num < to_base:
            r = num
            if r >= 10:
                res += chr(r + 55)
            else:
                res += str(r)
            break
    return res[::-1]


def convert_to_base_10(num, from_base):
    res = 0
    num = str(num)[::-1]
    for i in range(len(num)):
        el = num[i]
        if el in '1234567890':
            res += from_base ** i * int(el)
        else:
            res += from_base ** i * (ord(el) - 55)
    return res


def convert_base(num, from_base, to_base):
    return convert_from_base_10(convert_to_base_10(num, from_base), to_base)


num = input()
from_base = int(input())
to_base = int(input())
print(convert_base(num, from_base, to_base))
