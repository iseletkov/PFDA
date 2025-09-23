
# Пользователь вводит числа по отдельности.
# Надо посчитать среднее, максимальное, минимальное, количество введённых чисел.
# Конец ввода - специфический символ.

str1 = input()

sum1 = 0
min1 = 0
max2 = 0
count = 0

while str1 != "": 
    number = float(str1) 

    count += 1 
    sum1 += number

    if count == 1:
        min1 = number
    else:   
        if number<min1:
            min1 = number

    if count == 1:
        max1 = number
    else:   
        if number>max1:
            max1 = number

    str1 = input()        

if count == 0:
    print("No data")
else:
    average = sum1/count
    print(f"count={count}")
    print(f"min={min1}")
    print(f"max={max1}")
    print(f"sum={sum1}")
    print(f"average={average}")