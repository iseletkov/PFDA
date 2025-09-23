a = float(input())
b = float(input())
c = float(input())

d = b * b - 4 * a * c

if d < 0 :
    print("No solution")
    exit()
elif a == 0 and b == 0 and c != 0:
    print("No solution")
    exit()
elif a ==0 and b == 0 and c == 0:
    print("Infinite solutions")
    exit()
elif d == 0:
    print(f"{round(-b / (2 * a), 2)}")
    exit()
else:
    x1 = (-b + d ** 0.5 ) / (2 * a)
    x2 = (-b - d ** 0.5 ) / (2 * a)

    if x1 < x2:
        print(f"{round(x1, 2)} {round(x2, 2)}")    
    else:
        print(f"{round(x2, 2)} {round(x1, 2)}")    


    