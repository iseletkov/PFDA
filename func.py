def multiply(number1, number2 = 1, number3 = 1):
    res = number1 * number2, number2 * number3
    
    return res

def division(number1, number2):
    if number2 == 0:
        return None
    
    return number1/number2


# x1 = float(input())
# x2 = float(input())
# x3 = float(input())
# (y1, y2) = multiply(x1, number2 = x2, number3 = x3)

# print(y1)
# print(y2)

x1 = float(input())
x2 = float(input())

y = division(x1, x2)
print(y)