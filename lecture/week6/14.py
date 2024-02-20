import re
f = open("row.txt", "r",encoding="utf8")
text = f.read()

KKM_codePattern = r"\n.+(РНМ).*(?P<KKM_code>[0-9]{12})"
BINPattern = r"\nБИН\s+(?P<BIN>[0-9]{12})"

BINValue = re.search(BINPattern, text)
KKM_codeValue = re.search(KKM_codePattern, text)

if BINValue:
    print(BINValue['BIN'])
else:
    print('bin not found!')

if KKM_codeValue:
    print(KKM_codeValue['KKM_code'])
else:
    print('KKM_code not found!')