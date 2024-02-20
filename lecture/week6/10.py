f = open("row.txt", "r",encoding="utf8")
for x in f:
    if 'БИН' in x:
        print(x.split()[1].strip())