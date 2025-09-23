size = int(input())
width = int(input())

for i in range(1, size + 1):  # Перебор строк
    for j in range(1, size + 1):  # Перебор ячеек внутри строки
        print(f"{i * j: ^{width}}", end = "")
        if j < size:
            print("|", end="")
    print(f"")
    if i < size:
        print("-" * (size * width + size - 1))
    