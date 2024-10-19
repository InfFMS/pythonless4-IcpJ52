# Дано натуральное число N. Выведите слово YES,
# если число N является точной степенью двойки,
# или слово NO в противном случае.
# Операцией возведения в степень пользоваться нельзя!
# Задача на рекурсию!
def is_degree_2(n):
    if n == 1:
        return True
    if n % 2 == 0:
        return is_degree_2(n // 2)
    return False


n = int(input())
if is_degree_2(n):
    print('YES')
else:
    print('NO')
