str1 = input()

numbers = str1.split()

power = int(input())

for snumber in numbers:
    number = int(snumber)
    ret = number ** power
    
    print(ret, end=" ")

