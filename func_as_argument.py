
# def sort(lst, compare):
#     n = len(lst)  
#     for i in range(n):  
#         for j in range(0, n - i - 1):  
#             if compare(lst[j], lst[j + 1]):  
#                 lst[j], lst[j + 1] = lst[j + 1], lst[j]  
#     return lst

# def isGreater(a,b):
    
#     return a>b

# def isLess(a,b):
#     return a<b 

# def alfaSort(a,b):
#     return str(a)>str(b)     

# print(sort([10,40, -4, 5, 100], lambda a, b : str(a)>str(b) ))  




# print(sort([10,40, -4, 5, 100], lambda a, b : str(a)>str(b) ))  


# print(sort([10,40, -4, 5, 100], isGreater ))  




# print(sort([10,40, -4, 5, 100], isGreater ))  


# lf = lambda a, b : str(a)>str(b)
# res = lf(10,20)
# print(res)
# print(sort([10,40, -4, 5, 100], lf ))  
# print(sort([-8,44, -4, 54, 123], lf ))  




# def only_pos(x):
#     return x > 0

# result = filter(only_pos, [-1, 5, 6, -10, 0])
# print(", ".join(str(x) for x in result))

# def inc(x):
#     return x + 10

# result = map(inc, range(5))
# print(", ".join(str(x) for x in result))
