class Student:
  def __init__(self, str):
    self.message = str

  def printMessage(self):
    print(self.message)

  def __str__(self):
    return f"message body: {self.message}"

s1 = Student("test")
print(s1)



