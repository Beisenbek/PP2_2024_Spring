class MyNumbers:
  def __init__(self, start, stop):
    self.current = int(start)
    self.stop = int(stop)

  def __iter__(self):
    return self

  def __next__(self):
    if self.current < self.stop:
        x = self.current
        self.current += 1
        return x
    else:
        raise StopIteration

myclass = MyNumbers(0, 20)
myiter = iter(myclass)

for x in myiter:
    print(x)