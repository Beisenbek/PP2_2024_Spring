class Student:
  def __init__(self, str):
    self.message = str

  def printMessage(self):
    print(self.message)

s1 = Student(input())
s2 = Student(input())

s2.printMessage()
s1.printMessage()


