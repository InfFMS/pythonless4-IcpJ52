# Напишите процедуру, которая выводит на экран
# запись переданного ей числа в римской системе счисления.
# Числа находятся в диапазоне [1, 3999]
# I - 1, V - 5, X - 10, L - 50, C - 100, D - 500, M - 1000
# Пример:
# 2013
# MMXIII
def to_roman(n):
    if n <= 3:
        return 'I' * n
    if n == 4:
        return 'IV'
    if n <= 8:
        return 'V' + 'I' * (n - 5)
    if n == 9:
        return 'IX'
    if n == 10 or n == 20 or n == 30:
        return 'X' * (n // 10)
    if n == 40:
        return 'XL'
    if n in [50, 60, 70, 80]:
        return 'L' + 'X' * (n // 10 - 5)
    if n == 90:
        return 'XC'
    if n in [100, 200, 300]:
        return 'C' * (n // 100)
    if n == 400:
        return 'CD'
    if n in [500, 600, 700, 800]:
        return 'D' + 'C' * (n // 100 - 5)
    if n == 900:
        return 'CM'
    if n in [1000, 2000, 3000]:
        return 'M' * (n // 1000)
    return to_roman(n // 1000 * 1000) + to_roman(n % 1000 // 100 * 100) + to_roman(n % 100 // 10 * 10) + to_roman(
        n % 10)


print(to_roman(int(input())), end='')
