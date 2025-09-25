def test(number):
    number += 1

def test_list(lst):
    lst.append(10)

x = 1
test(x)
print(x)

lst = [1,2,3]
test_list(lst)
print(lst)
