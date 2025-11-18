#Дефинирайте функция която връща като резултат второто по големина число предадено като аргумент на функцията
#Програма в коятое описана функция която проверява дали едно цяло число е просто, числото като аргумент на функцията, функцията връща True ако е просто и иизвън функцията да се принтират всички числа от интервала 2 до това просто чило

#1
def second_number(num):
    list_num = []
    for x in num:
        list_num.append(x)
    max_num = None
    for x in list_num:
        if max_num is None or x > max_num:
            max_num = x

    max_second = None
    for x in list_num:
        if x != max_num:
            if max_second is None or x > max_second:
                max_second = x
    return max_second

def second_number(num):
    list_num=[]
    for x in num:
        list_num.append(x)
    unique_numbers = set(list_num)
    unique_numbers.remove(max(unique_numbers))
    return max(unique_numbers)

print(second_number([5, 2, 9, 9, 7]))
#2
def primes_up_to(n):
    primes = []
    for x in range(2, n + 1):
        is_prime = True
        for i in range(2, x):
            if x % i == 0:     #delitel  razlichen ot samoto chislo
                is_prime = False #namira se delitel
                break
        if is_prime:
            primes.append(x)
    return primes

all_primes = primes_up_to(79)
print(all_primes)

# #4зад. Напишете програма, в която е описан клас. Обектите на класа трябва да имат поле, представляващо числов списък. Този списък се формира на основата на списък, предаден като аргумент на конструктора. 
# При това от списъка аргумент в списъка поле се включват само числовите елементи
# (елементите от други типове се игнорират). Също така трябва да се дефинират два метода:
# Първият метод показва съдържанието на полето списък, а вторият метод изчислява средната стойност на елементите на полето списък.
class NumberList:
    def __init__(self, input_list):
        self.numbers = []
        for x in input_list:
            if type(x) == int or type(x) == float:
                self.numbers.append(x)
    def show_list(self):
        print(self.numbers)

    def average(self):
        if len(self.numbers)==0:
            return 0
        sum_numbers = 0
        for x in self.numbers:
            sum_numbers+= x
        return sum_numbers / len(self.numbers)
    
#5
class Product:
    def __init__(self,id,name,price,quantity):
        self.id=id
        self.name=name
        self.price=price
        self.quantity=quantity
    
    def print_info(self):
        print(f"{self.id},{self.name},{self.price},{self.quantity}")
    
    def sale(self, quantity):
        if quantity <= self.quantity:
            self.quantity -= quantity #namalqva nalichnostta s posochenoto kolichetvo
        else:
            print("Няма достатъчно наличност")

    def purchase(self, quantity):
        self.quantity += quantity #uvelichava nalichnostta s posocheoto kolicehstvo

products = []
n = int(input("Брой продукти: "))
for i in range(n):
    id = input("ID: ")
    name = input("Име: ")
    price = float(input("Цена: "))
    quantity = int(input("Наличност: "))
products.append(Product(id, name, price, quantity))

while True:
    print("1.Показване 2.Търсене по ID 3.Търсене по име 4.Продажба 5.Зареждане 6.Изход")
    choice = input("Избор: ")

    if choice == "1":
        for product in products:
            product.print_info()

    elif choice == "2":
        id = input("ID: ")
        for product in products:
            if product.id == id:
                product.print_info()

    elif choice == "3":
        name = input("Име: ")
        for product in products:
            if product.name == name:
                product.print_info()

    elif choice == "4":
        id = input("ID: ")
        qty = int(input("Количество: "))
        for product in products:
            if product.id == id:
                product.sale(quantity)

    elif choice == "5":
        id = input("ID: ")
        quantity = int(input("Количество: "))
        for product in products:
            if product.id == id:
                product.purchase(quantity)

    elif choice == "6":
        break

    






