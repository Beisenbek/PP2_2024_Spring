import re

str = input()
pattern = r"^\S+@\S+\.\S+$"

x = re.search(pattern, str)
print(x)
