N = int(input())

i = 1  # номер числа
length = 1
lastRow = False
number = 0
lastRowCount = 0
while i <= N:
    j = 0

    if N-i < length:  # Признак перехода к заполнению последней строчки
        lastRow = True

    while (j < length) and (i <= N):
        # if i > N:
        #    break

        # print(f"{i} ", end="")

        # Выполняем подсчёт количества символов в последней строчке.
        if lastRow:

            number = i
            while number>0:
                number = number // 10
                lastRowCount = lastRowCount + 1

            lastRowCount = lastRowCount + 1  # Учёт пробелов между числами

        i = i + 1
        j = j + 1
    
    # print("")
    length = length + 1

lastRowCount = lastRowCount - 1
print (f"Длина строки: {lastRowCount}")


i = 1  # номер числа
length = 1
while i <= N:
    j = 0

    str1 = ""
    while (j < length) and (i <= N):
        # if i > N:
        #    break
        str1 = str1 + str(i)
        if j<length-1 and i <= N-1:
            str1 = str1 + " "   
        # print(f"{i} ", end="")

        i = i + 1
        j = j + 1
    
    print(f"{str1  :^{lastRowCount}}")
    length = length + 1
