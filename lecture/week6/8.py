import re

txt = "The rain in Spain Seatle"
x = re.findall(r"\bS\w+", txt)
print(x)