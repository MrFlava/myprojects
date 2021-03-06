"""

Лаборатонрая работа #11
Вариант 9

Нахождение значения интеграла по
методу трапеции

"""

import math

n = 1
a = 0.4
b = 1.2
epsi = 0.0001
f = lambda x: math.cos(0.63 + 0.5 * x) / (0.4 + math.pow((math.pow(x, 2) + 9), 0.5))

def trapezium_rule(f, a, b, n):
    sum = 0.0
    h = (b - a) / n
    func = (f(a) + f(b)) / 2
    for i in range(n):
        x = a + i * h
        fx = f(x)
        sum += fx
    return (sum * h)

a_1 = trapezium_rule(f, a, b, n)

while True:
    l = a_1
    n = 2 * n
    a_1 = trapezium_rule(f, a, b, n)
    if math.fabs(a_1 - l) > epsi:
        break
print("Метод трапеции = ", a_1)
