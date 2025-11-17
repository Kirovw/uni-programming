#Класове и обекти
class MyFirstClass:
    x = 3
    def printX():
        print(MyFirstClass.x)

class MyFirstObjectClass:
    #def __init__(self):
       # self.a=0
    def __init__(self,a=0):
        self.a=0
    def __str__(self):#vajen metod1-kogato eddin obekt trqbva da se prevurne v string
        return str(self.a)
    def __repr__(self):#vajen metod2
        return str(self.a)
    def print(self):
        print(self.a)
if __name__=="__main__":
    MyFirstClass.printX
obj=MyFirstObjectClass()
print(obj.a)
print(obj)
obj.print()

obj=MyFirstObjectClass(10)
print(obj.a)
print(obj)
obj.print()



