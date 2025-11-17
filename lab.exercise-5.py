class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
animal1=Animal("Rex", 2)
print(animal1.age)
animal1.name="Tom"

class Animal:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    def get_age(self):
        return self.__age
    def set_age(self,age):
        self.__age=age
animal1=Animal("Rex",2)
print(Animal.get_age())
animal1.set_age(3)

class Dog(Animal):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        Animal.__init__(set,name,age)
        self.color=color
    def __str__(self):
        return f"{self.name} {self.__age} {self.color}"
#1.Дефинирайте клас пърсън с атрибути име фамилия възраст и националност, ще предефинираме конструктора,който да инициализира полетата на класа, 
# добаяте метод принт инфо който отпечата имената и националността. Създайте три обекта на класа и зад тях извикайте мето принт инфо
class Person:
    def __init__(self,name,family_name,age,nationality):
        self.name=name
        self.family_name=family_name
        self.age=age
        self.nationality=nationality
    def print_info(self):
        print (f"{self.name},{self.family_name},{self.nationality}")
person1=Person("Стефан","Георгиев",20,"БГ")
person2=Person("Антон","Киров",20,"БГ")
person1.print_info(person1)



