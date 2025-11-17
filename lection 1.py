print("Hello Python!")
print(2 + 3)   # събиране
print(2 - 3)   # изваждане
print(2 * 3)   # умножение
print(2 / 3)   # деление
print(2 // 3)  # целочислено деление
print(2 % 3)   # остатък
print(2 ** 3)  # степенуване
print()

# Цикъл for
for x in range(1, 10):
    print(x)

# този цикъл принтира всички числа от 1 до 99 на нов ред:
for x in range(1,100):
    print(x)

#този цикъл принтира всички числа от 1 до 100 на нов ред
for x in range(1,101):
    print(x)

# 4. Сумиране на 3 числа
sum=0
for i in range(3):
    x=int(input(f"[{i+1}]= "))
    sum += x
    print("sum", sum)

#5. Сумиране на произволен брой числа
numbers = int(input("Колко числа искаш да събереш: "))
sum = 0
for i in range(numbers):
    x = int(input(f"[{i+1}] = "))
    sum += x
print("sum =", sum)

# този цикъл генерира numbers случайни числа от -10 до 9, показва ги на екрана и накрая извежда тяхната сума.

numbers = int(input("Колко числа искаш да събереш: "))
sum = 0
for i in range(numbers):
    x = random.randrange(-10,10)
    print(x,end= "")
    sum += x
print("\nsum=",sum)

# 6. Умножение на произволен брой числа
numbers=int(input("Колко числа искаш да умножиш: "))
mult=1
for i in range(numbers):
    x=int(input(f"[{i+1}]= "))
    mult *=x
print("mult= ", mult)

# 6. Умножение на произволен брой числа, генерира n случайни числа между -10 и 9, отпечатва ги и извежда тяхното произведение.
numbers=int(input("Колко числа искаш да умножиш"))
mult=1
for i in range(numbers):
    x=random.randrange(-10,10)
    print(x,end= "")
    mult*=x
print("mult= ", mult)


# 8. Въвеждане числа до 0 и сумиране
sum=0
while True:
    x=int(input("Въведи число (0 за край): "))
    if x==0:
        break
    sum+=x
    print("Сумата е: ",sum)

# този цикъл събира въведени числа, докато не въведеш 0, и после показва сумата и намира най-малкото от тях.
sum=0
min=0
while True:
    x=int(input(x= ""))
    if x==0:
        break
    sum+=x
    if min==0:
        min=x
    elif min>x:
        min=x
print("sum",sum,"min", min)

# втори вариант
sum=0
isn_init=False
while True:
    x=int(input(x=""))
    if x==0:
        break
    sum+=x
    if not is_init:
        min=x
        is_init:True
    elif min>x:
        min=x
print("sum",sum,"min", min)


# този цикъл въвежда числа, докато не въведеш 0, и намира най-голямото четно число сред тях.

is_init=False
while True:
    x=int(input(x= ""))
    if x==0:
        break
    if x%2==0:
        if not is_init:
            max_even=x
            is_init=True
        elif max_even<x:
            max_even=x
if is_init:
    print("max_even= ", max_even)
else:
    print("Няма въведени четни числа")




    

