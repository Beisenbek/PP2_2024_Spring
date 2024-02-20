import re
f = open("row.txt", "r",encoding="utf8")
text = f.read()

BINPattern = r"\nБИН\s+(?P<BIN>[0-9]{12})"

print(re.search(BINPattern, text).group('BIN'))