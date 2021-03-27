def say_yosoro(greeting):
  print(greeting)

hello = say_yosoro
hello("Good Morning")

def add(num01,num02):
  return(num01 + num02)

add_result=add(6,2)
print(add_result)

def div(a,b,c):
  return(a + b + c)/3

div_result = div(9,4,2)
print(div_result)

class Student:
  def __init__(self,name):
     self.name = name

  def avg(self,math,english):
      print((math + english)/2)

a001 = Student("sato")
print(a001.name)

a002 = Student("tanaka")
print(a002.name)