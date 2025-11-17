num1 = float(input("Въведи първото число: "))
num2 = float(input("Въведи второто число: "))
num3 = float(input("Въведи третото число: "))


if num1 <= num2 and num1 <= num3:
    print(num1)
elif num2 <= num1 and num2 <= num3:
    print(num2)
else:
    print(num3)

#2
while True:
    numb = int(input("Въведи число между 5 и 20: "))
    if 5 <= numb <= 20:
        print(numb)
        break
    else:
        print("Грешка! Опитай пак.")

min= 10000
for n in range(numb):
     value=int(input("Въведи число между 5 и 20: "))
     if value<min:
         min=value
print(min)

#3
while True:
    numb = int(input("Въведи число между 5 и 20: "))
    if 5 <= num <= 20:
        print(numb)
        break
    else:
        print("Грешка! Опитай пак.")
sum=0
for n in range(numb):
 num=int(input("Въведи число между 5 и 20: "))
 if value<10:
    continue
 if value //10 %2:
    sum+=value
print(sum)
#4
n = int(input("Enter number of rows: "))
for i in range(n):
    print("*" * (i + 1))


#1
#🧩 Упражнение 1 — Проверка на число

#🔹 Напиши програма, която:

#иска от потребителя едно цяло число;

#казва дали то е:

#положително

#отрицателно

#или нула.

#💡 Подсказка: използвай if, elif, else.

num=int(input("Въведете едно цяло число: "))
if num>0:
    print("Положително число")
elif num<0:
    print("Отрицателно число")
else:
    print("Нула")
