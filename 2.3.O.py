n = int(input())

count = 0
for i in range(n):
    str1 = input()
    if "зайка" in str1:
        count = count + 1

print(count)