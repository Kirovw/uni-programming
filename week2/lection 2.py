l=[1,2,3,4,5]
print(l)

l=[]
for i in range(5):
    x=int(input(f"[{i+1}]:"))
    l.append(x)
print(l)

import random
l=[]
for i in range(5):
    l.append(random.randint(-10,10))
print(l)

sum=0
for i in range(len(l)):
    sum+=l[i]
print("sum= ", sum)

sum=0
for x in l:
    sum+=x
print("sum=",sum)
print("min= ", min(l))
print("max= ", max(l))

#ll=input().split(",")
#print(ll)
#ll.append([1,2,3])
#print(ll)

ll=[[1,2,3],
    [11,12,13],
    [-1,-2,-3]]
print(ll)

for x in l:
    print(x)

#for x in l:
    #for y in x:
        #print(y,end="")
    #print()

print(l)
print(l[1])
print(l[-1])
#print(l[10])
print(l[-5])

#slice-представлява част от списъка
print(l[1:3])#принтира два елемента(отворен интервал)
print(l[1:])#принтира всички елементи на списъка освен първия елемент
print(l[:4])#Принтира всички елементи до четвъртия
print(l[-2:])#Принтира предпоследния и последния елемент
print(l[:-3])#Принтира всички елементи до пред предпоследния елемент
print(l[-2:-4])#Принтира от предпоследния до пред пред предпоследния елемент,празен списък
print(l[-4:-2])# Принтира от пред пред предпоследния до предпоследния елемент
print(l[:])#Принтира целия списък

l[1]=[11,12,13] # <- Променя първия елемент
print(l)
l+=[-1,-2,-3] # <- Добавя елемент
print(l)

del l[0] # <- Изтрива елемент 1
print(l)
del l[2:3] # <- Изтрива елемент в област, но горната граница не се трие
print(l)
del l[:]# Изтрива всички елементи от списъка и е еквивалентно на l.clear()
print(l)
#!del l е грешка, трябва да е del l[:]

l=[]
for i in range(5):
    l.append(random.randint(-10,10))
l+=[1,1] #Добавя се подсписък
print(l)

print(l.count(1))# Показва и брои в списъка колко единици има
print(l.index(1))# Показва в списъка на кое място е 1

#Разлика между += и l.insert- Първото добавя елемнт в края на списъка, а второто добавя при конкретно място на елемент подсписък
l.insert(0,[1,1])
print(l)

l[0]+=[2,2]# Добавя в края на елемент 0 2,2
print(l)

l.remove(1)# premahva se element rawen na edinica
print(l)

#l.remove(111)#-error
#print(l)

if 1 in list:
    l.remove(1)
print(l)

print(8>>1)# 8 се дели на 2 на първа степен 8/2
print(8>>2)# 8 се дели на 2 на втора степен 8/4
print(8<<1)# 8 се умножава на 2 на първа степен 8*2
print(8<<2)# 8 се умножава на 2 на втора степен 8/4

    

