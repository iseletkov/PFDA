# str1 = input()

# # числа строками
# snumbers = str1.split()

# # numbers = []
# for snumber in snumbers:    
#     number = float(snumber)
#     numbers.append(number)

# filtered = []
# for number in numbers:
#     if number % 2 ==0 and number >= 50 and number <= 100:
#         filtered.append(number)  

# filtered.sort()

# for number in filtered:
#     print(number)

str1 = input()
# числа строками
numbers = str1.split()
for i, snumber in enumerate(numbers):
    numbers[i] = float(snumber)

for i, number in enumerate(numbers):
    if not (number % 2 ==0 and number >= 50 and number <= 100):
        del numbers[i]

numbers.sort()

for number in numbers:
    print(number)
       



 
