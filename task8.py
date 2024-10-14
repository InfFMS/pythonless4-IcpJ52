# Напишите рекурсивную функцию, которая
# раскладывает натуральное число на простые сомножители.
#
# Пример:
# Ввод:
# 378
# Вывод:
# 2*3*3*3*7
def fact(n):
    if n == 1:
        return 'No prime factors'
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return str(i) + '*' + fact(n // i)
    return str(n)


print(fact(int(input())))
