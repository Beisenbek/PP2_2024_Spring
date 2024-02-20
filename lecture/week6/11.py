f = open("row.txt", "r",encoding="utf8")
flag = False
for x in f:
    if flag:
        print(x)
        flag = False
    if 'Стоимость' in x:
        flag = True