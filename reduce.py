from functools import reduce

lst = [0,5,-3,0,8,9]

print(reduce(lambda x, y: x * y if x!=0 and y!=0 else x, lst))