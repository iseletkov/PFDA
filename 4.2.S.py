

def treat_char(char, **kwargs):
    if char in kwargs:
        replace_info = kwargs[char]
        replace_str = replace_info[0][replace_info[1]]
        replace_info[1] += 1
        if replace_info[1] >= len(replace_info[0]):
            replace_info[1] = 0    
        return replace_str
    return char

def secret_replace(text, **kwargs):

    for key, value in kwargs.items():
        # key - символ, который надо заменять.
        # value - картеж, по которому осуществляется замена.
        kwargs[key] = [value, 0]

    ret = [treat_char(char, **kwargs) for char in text]
    return "".join(ret)

result = secret_replace("ABRA-KADABRA",
    A=("Z", "1", "!"),
    B=("3",),
    R=("X", "7"),
    K=("G", "H"),
    D=("0", "2"),
)
print(result)