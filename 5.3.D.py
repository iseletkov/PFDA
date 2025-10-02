def only_positive_even_sum(param1, param2):
    if (type(param1) is not int) or (type(param2) is not int):
        raise TypeError(" adand and ln")
    
    # try:
    #     x = int(param1)
    #     y = int(param2)
    # except ValueError:
    #     raise TypeError(" adand and ln")

    if param1 <= 0 or param1 % 2 != 0 or param2 <= 0 or param2 % 2 != 0:
        raise ValueError(" adand and ln")    

    return param1 + param2

if __name__ == "__main__":
    # print(only_positive_even_sum("3", 2.5))
    print(only_positive_even_sum(2, 4))
