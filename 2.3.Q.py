n = int(input())

output = ""

while n != 0:
    c = n % 10 # Очередная цифра с конца
    n = n // 10 # Всё число без последней цифры
    if c % 2 != 0:
        output = str(c) + output
print(output)