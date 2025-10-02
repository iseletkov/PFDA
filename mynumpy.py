import numpy as np

# ПРимер проблемы
# a = np.array([[9, 8], [7, 8]])
# b = np.array([1, 2, 3, 5])
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)

a = np.arange(1, 13).reshape(3, 4)
print(a)
print()
print(a[:2, :2])     # Срез: 2 строки, последние 2 столбца
print()
print(a[:, ::2])     # Срез всех строк, каждый второй столбец

