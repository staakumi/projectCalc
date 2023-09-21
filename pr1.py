
import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "ошибка! деление на ноль невозможно."
    else:
        return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "ошибка! квадратный корень из отрицательного числа не существует."
    else:
        return math.sqrt(x)

def factorial(x):
    if x < 0:
        return "ошибка! факториал из отрицательного числа не существует."
    elif x == 0:
        return 1
    else:
        return x * factorial(x - 1)

def sine(x):
    return math.sin(x)

def cosine(x):
    return math.cos(x)

def tangent(x):
    return math.tan(x)

def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

while True:
    print("\nвыберите операцию:")
    print("1. сложение")
    print("2. вычитание")
    print("3. умножение")
    print("4. деление")
    print("5. возведение в степень")
    print("6. квадратный корень")
    print("7. факториал")
    print("8. синус")
    print("9. косинус")
    print("10. тангенс")
    print("11. выход")

    choice = input("введите номер операции (от 1 до 11): ")

    if choice == '11':
        print("до свидания!")
        break

    if not is_number(choice) or int(choice) < 1 or int(choice) > 11:
        print("ошибка! введите номер операции от 1 до 11.")
        continue

    if int(choice) <= 6:
        num1 = input("введите перове число: ")
        num2 = input("введите второе число: ")

        if not is_number(num1) or not is_number(num2):
            print("ошибка! введите корректные числа.")
            continue

        num1 = float(num1)
        num2 = float(num2)

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        elif choice == '5':
            print(num1, "^", num2, "=", power(num1, num2))
        elif choice == '6':
            print("sqrt(", num1, ") =", square_root(num1))
    else:
        num = input("введите число: ")

        if not is_number(num):
            print("ошибка! введите корректное число.")
            continue

        num = float(num)

        if choice == '7':
            print(num, "! =", factorial(num))
        elif choice == '8':
            print("sin(", num, ") =", sine(num))
        elif choice == '9':
            print("cos(", num, ") =", cosine(num))
        elif choice == '10':
            print("tan(", num, ") =", tangent(num))
