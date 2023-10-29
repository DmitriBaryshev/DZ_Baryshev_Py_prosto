from math import prod

# 1 zd
N = int(input("Введите целое число N (> 0): "))

sum = 0

for i in range(1, N+1):
    sum += 1/i

print("Сумма =", sum)

# 2 zd
n = int(input("Введите целое число N: "))

sum = 0

for i in range(1, 2*n+1):
    term = (n + i)**2
    sum += term

print("Значение выражения =", sum)

# 3 zd
n = int(input("Введите целое число N: "))

product = 1.0

for i in range(1, n+1):
    product *= 1.0 + (i / 10.0)

print("Произведение =", product)

# 4 zd
n = int(input("Введите целое число N: "))

sum = 0

for i in range(1, n+1):
    term = (-1) ** (i+1) * (1 + i/10)
    sum += term

print("Значение выражения =", sum)

# 5 zd
n = int(input("Введите целое число N: "))

sum = 0

for i in range(1, 2*n, 2):
    sum += i
    print("Текущая сумма =", sum)

print("Квадрат числа", n, "=", sum)

# 6 zd
print(int(input())**int(input()))
