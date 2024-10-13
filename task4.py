# Напишите функцию, которая находит
# наибольший общий делитель двух натуральных чисел
# На входе два числа, на выходе их НОД.
def gcd(a, b):
     a, b = max(a, b), min(a, b)
     if b == 0:
         return a
     if a % b == 0:
         return b
     return gcd(a % b, b)

a = int(input())
b = int(input())
print(f'НОД: {gcd(a, b)}')
