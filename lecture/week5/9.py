x = 300

def myfunc():
  global x
  x = 200
  print(x)

myfunc()

print(x)