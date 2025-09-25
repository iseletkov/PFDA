def func1(param1):
    x_global = param1
    return param1

def func2(param2):
    x2 = param2 + 5
    return func1(x2)

x_global = 10
func2(x_global)