from math import *
import sys

x = float(input("Введите значение x -> "))
y = float(input("Введите значение y!=0 -> "))
msg = "Выберите вид функции f(x): tanh(y) -> 1, x**5 -> 2, sqrt(x**y)) -> 3 "

f = float(input(msg + "\n -> "))
fx = None
b = None

if y == 0:
    print("Вы ввели недопустимое значение y")
    sys.exit()
else:
    match f:
        case 1:
            fx = tanh(y)

        case 2:
            fx = x ** 5
        case 3:
            fx = sqrt(x ** y)
        case _:
            print("Неверный выбор")
            sys.exit()

    if x / y > 0:
        b = log(fx) - cbrt(fx)
    elif x / y < 0:
        b = log(abs(fx) / y) * pow((x + y), 3)
    elif (x / y) == 0:
        b = pow(((fx ** 2) + y), 3)

print("Результат: ", b)


