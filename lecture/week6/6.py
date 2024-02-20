import re

def f(t):
    pattern = r"^\S+@\S+\.\S+$"
    x = re.search(pattern, t)
    print(x.string)
    print(x.group())
    

str = input()
f(str)


