import sys, os

# try:
#     print(1 / int(input()))
# except ZeroDivisionError:
#     print("Ошибка деления на ноль.")
# except ValueError:
#     print("Невозможно преобразовать строку в число.")
# except Exception:
#     print("Неизвестная ошибка.")
# else:
#     print("Операция выполнена успешно.")


def square_rect(l1,l2):
    """
        None возникает в таких-то случаях.
    """
    if l1<0:
        raise ValueError("Длина стороны l1 прямоугольника не должна быть отрицателной!")
    if l2<0:
        raise ValueError("Длина стороны l2 прямоугольника не должна быть отрицателной!")

    return l1*l2


try:
    ret = square_rect(3, -2)
except ValueError as e:
    print(e.args[0])

except Exception as e:
    print("Неизвестная ошибка.")
else:
    print("Операция выполнена успешно.")


