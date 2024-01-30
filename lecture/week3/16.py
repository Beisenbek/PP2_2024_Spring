class Student:
  def __init__(self, str):
    self.message = str

  def printMessage(self):
    print(self.message)

  def __str__(self):
    return f"message body: {self.message}"

class Master(Student):
    def __init__(self, str):
        self.message2 = str[0]
        Student.__init__(self, str)

s1 = Student("test")
print(s1)

m1 = Master("test2")
print(m1)
print(m1.message2)


