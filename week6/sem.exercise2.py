#1Отпечатва утроен списък
#Сортира списъка"
n=int(input("От колко елементи да е списъкът"))
l=[]
for i in range(n):
    x=int(input(f"[{i+1}]"))
    l.append(x)
print(l)

tripled_list = l * 3
print(tripled_list)

for x in l:
    print(x)
check_number= int(input("Въведи число за проверка: "))
if check_number in l:
    print("Да")
else:
    print("Не")

l.sort()
print(l)

max_num=None
for x in l:
    if max_num is None or x>max_num:
        max_num=x
print(max_num)

idx = int(input("Въведете индекс за изтриване: "))
if 0 <= idx < len(l):
    del l[idx]
    print("Списък след изтриване:", l)
else:
    print("Грешен индекс!")


idx = int(input("Въведете индекс за промяна: "))
if 0 <= idx < len(l):
    new_value = int(input("Нова стойност: "))
    l[idx] = new_value
    print("Списък след нова стойност:", l)
else:
    print("Грешен индекс!")


#2
p = int(input("Колко низа ще въведеш: "))

strings = []
for i in range(p):
    x = input(f"[{i}]: ")
    strings.append(x)
print(strings)
#2.1
longest = strings[0]
for x in strings:
    if len(x) > len(longest):
        longest = x
print(longest)
#2.2
x = input("Въведи низ за замяна: ")
r = input("Въведи новия низ: ")
if x in strings:
    i = strings.index(x)
    strings[i] = r
    print("След замяната:", strings)
else:
    print("Не съществува!")
#2.3
d= input("Въведи низ за изтриване: ")
if d in strings:
    strings.remove(d)
    print(strings)
else:
    print("Няма го")
#2.4
new = input("Въведи нов низ за вмъкване: ")
inde = int(input("Къде да се вмъкне: "))
if 0 <= inde <= len(strings):
    strings.insert(inde, new)
    print("Списък след вмъкване:", strings)
else:
    print("Невалиден индекс!")

#4
m=int(input("Колко елемента ще има всяко множество"))
a=set()
b=set()

for i in range(m):
    x = int(input(f"[{i+1}]: "))
    a.add(x)
print(a)

for i in range(m):
    x = int(input(f"[{i+1}]: "))
    b.add(x)
print(b)

l1=len(a)
l2=len(b)
print(l1)
print(l2)

a1_b1=a.union(b)
a2_b2=a.difference(b)
a3_b3=a.intersection(b)
print(a1_b1)
print(a2_b2)
print(a3_b3)

remove_a = int(input("Премахване от първото множество: "))
if remove_a in a:
    a.remove(remove_a)
    print("Първо множество след премахване:", a)
else:
    print("Елементът не съществува в първото множество!")

a.clear()
b.clear()


#3
m = int(input("Колко елемента ще има речникът? "))
d = {}

for i in range(m):
    key = input(f"Въведи ключ [{i+1}]: ")
    value = int(input(f"{key}: "))
    d[key] = value
print(d)
#3.1
search = input("Въведи ключ за търсене: ")
if search in d:
    print(f"{search}", d[search])
else:
    print("Такъв ключ няма!")

#3.2
change = input("Въведи ключ за промяна на стойност: ")
if change in d:
    new_val = int(input("Нова стойност: "))
    d[change] = new_val
    print("Речник след промяната:", d)
else:
    print("Такъв ключ няма!")

#3.3
delete = input("Въведи ключ за изтриване: ")
if delete in d:
    del d[delete]
    print("Речник след изтриване:", d)
else:
    print("Такъв ключ няма!")

#3.4
print(list(d.keys()))
print(list(d.values()))
#3.5
sorted_it = dict(sorted(d.items()))
print(sorted_it)
#3.6
for key in sorted_it:
    print(key, sorted_it[key])

#6
cities = []
n = int(input("Колко града ще въведеш? "))
for i in range(n):
    city = input(f"Град {i+1}: ")
    cities.append(city)
print(cities)

new_city = input("Въведи град за добавяне: ")
cities.append(new_city)
print("След добавяне:", cities)

remove_city = input("Въведи град за изтриване: ")
if remove_city in cities:
    cities.remove(remove_city)
print("След изтриване:", cities)

cities.sort()
print("След сортиране:", cities)

search_ci = input("Въведи град за търсене: ")
if search_ci in cities:
    print("Градът е намерен!")
else:
    print("Градът не съществува.")

k = int(input("Колко нови града ще добавиш към списъка? "))
new_c=[]
for i in range(k):
    town = input(f"Нов град {i+1}: ")
    new_c.append(town)
cities = cities + new_c
print("Краен списък:", cities)
#8
s = "ab be ab bd ab be"
count = s.count("ab")
print("Брой'ab':", count)
new_s = s.replace("ab", "ba")
print("Разместване:", new_s)





