import re
import csv

f = open("row.txt", "r",encoding="utf8")
text = f.read()

pattern = r"\n(?P<order>[0-9]+)\.\n(?P<name>.+)\n(?P<count>.+)x(?P<price>.+)\n"
#compiledPattern = re.compile(pattern)
#x = re.search(pattern, text)

results = re.finditer(pattern, text)

with open('data.csv', 'w', newline='',encoding="utf8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['order', 'name', 'count', 'price'])
    for x in results:
        writer.writerow([
            x.group('order'), 
            x.group('name'),
            float(x.group('count').strip().replace(',','.')),
            float(x.group('price').strip().replace(',','.').replace(' ',''))
        ])
        