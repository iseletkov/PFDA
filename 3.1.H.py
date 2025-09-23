n = int(input())

count = 0
for i in range(n):
    str1 = input()
    
    

    index = str1.find("зайка")
    if index<0:
        print("Заек нет =(")
    else:
        print(index+1)
        


