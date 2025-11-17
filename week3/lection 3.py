#list comprehesion-leckiq
#list-mutable
import random

l=[]
for i in range(10):
    l.append(random.randint(-10,10))
print(l)

is_init=False
for x in l:
    if x%2==0:
        if not is_init:
            min=x
            is_init=True
        elif min>x:
            min=x
if is_init:
    print("min", min)
else:
    print("No such data...")

#list comprehension
import random
import builtins
l=[random.randint(-100,100) for i in range(10)]
print(l)

lll=[x for x in l if x % 2 == 0]
print(lll)

if len(lll) >0:
    print("min: ",builtins.min(lll))
else:
   print("No such data...")

#l = [random.randint(-100,100) for i in range(10)]
#print(l)

#ll = [x for x in l if x%2==0]
#print(ll)

#if len(ll) > 0:
    #print("min:",min(ll))
#else:
    #print("No such data...")

l1=[int(input(f"{i}="))for i in range(3)]
print(l1)

#queue
#стек и опашка-оснони структури данни в програмирането
#First In First Out FIFO
l.append(333)
print(l)
l.pop(0)
print(l)

#stack
#Last In First Out LIFO
l.append(444)
print(l)
print("last: ", l.pop())
print(l)

#deque
#dq=deque(l)
#print(dq)

#FIFO
#dq.append(-111)
#print(dq)
#dq.popleft()
#print(dq)

#LIFO
#dq.append(-222)
#print(dq)
#dq.pop()
#print(dq)

#tuple-тя е immutable, непроемянема структура
t=()
print(type(t),t)
t=(1,2,3,4,5)
print(t)
x1,x2,x3,x4,x5=t
print(x1,x2,x3,x4,x5)
t1=x1,x2,x3,x4
print(type(t1),t1)
t=(1,)
print(type(t),t)
t=1
print(type(t),t)

t=(1,2,3,4)
print(t[1]) #само за четене
#t[1]=11

t=tuple(l)
print(type(l),l)
print(type(t),t)

print("count:",t.count(20))
if -1 in t:
    print(t.index(-1))

l11=list(t)
print(l11)



#Работа с матрици
m=[[1,2,3],[4,5,6]]
print(type(m),m)

for row in m:
    for x in row:
        print(x, end=" ")
    print()

m=[[random.randint(0,100) for col in range(4)]
   for row in range(3)]
print(m)
m= [[]]
for row in range(3):
    l=[]
    for col in range(4):
        l.append(random.randint(0,10))
    m.append(l)
print(m)

#m=np.matrix([[1,2],[4,5]])
#print(type(m),m)

#l2=[x for x in np.arrange(0,10,2.5)]
#print(type(l2),l2)

num=complex(1,2)
print(type(num),num)

#Задача 1: Сумиране на положителните числа
import random
l=[random.randint(-50,50) for i in range(10)]
print(l)

lll=[x for x in l if x > 0]
print(lll)

if len(lll) >0:
    print("sum: ", sum(lll))
else:
   print("No such data...")


#🟢 Задача 2: Филтриране
#📘 Условие:
#Генерирай 15 случайни числа от -20 до 20.
#Създай нов списък, съдържащ само нечетните положителни числа.
#Изведи двата списъка.
#💡 Подсказка: използвай list comprehension и условие if x > 0 and x % 2 != 0.
import random
l=[random.randint(-20,20) for i in range(15)]
print(l)

lll=[x for x in l if x>0 and x%2 !=0]
print(lll)


#Задача 3: Брой срещания на елемент
#Условие:
#Въведи списък от 8 числа и провери колко пъти се среща най-малкото число в него.
#Подсказка: използвай .count() и min().+
l1=[int(input(f"{i}="))for i in range(8)]
print(l1)

min_l1=min(l1)
print("Count:", l1.count(min_l1))

#🟢 Задача 6: Минимален четен елемент

#📘 Условие:
#Генерирай 10 случайни числа от -100 до 100.
#Намери най-малкото четно число в списъка.
#Ако няма четни, изведи „Няма такива елементи“.
#💡 Подсказка: използвай филтър чрез list comprehension или флага is_init (както в примера ти от лекцията).
l=[random.randint(-100,100) for i in range(10)]
print(l)

lll=[x for x in l if x%2==0]
print(lll)

if len(lll)>0:
    print("Min nechetno: ", min(lll))
else:
    print("No such data")

   


