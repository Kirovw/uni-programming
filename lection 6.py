import math
from operator import mul
from functools import reduce
def func(pos1:int,pos2:int, /,mix1:str,mix2:str,*,key1:float,key2:float=2.4)->None:
    """Documentation
    """
    print(pos1,pos2,mix1,mix2,key1,key2)
    print(func.__annotations__)
def func1(mix1,mix2): #podrazbirano mseno predavane na parametri
    print(mix1,mix2)

def func2(*,key1,key2):
    print(key1,key2)

def func3(pos1,pos2):
    print(pos1,pos2)

def mult(list):
    #3.8+ python
    return math.prod(list)

def mult1(list):
    #vsichki versii
    return reduce(mul, list)

def mult2(list):
    prod=1
    for x in list:
        prod*=x
    return prod

def printList(*args):
    print(args)#printira kortezha
    print(*args)#printira razopakovan kortezha
    for x in args:
        print(x)#printira otdelnite elementi

def addtoList(L:list=[], data:int=1)->None:
    L.append(data)

def addtoList1(L:list=[], data:int=1)->list:
    L.append(data)
    return L

def addtoList2(L:list=None, data:int=1)->list:
    if list==None:
        L=[]
    return L

def dictionary(**d)->None:
    print(**d)
    print(*d)
    print(d)

def dictionary(key:int,value:str)->None:
    print(key)
    print(value)

   
#lambda functions


if __name__=="__main__":
    print("Hello","World",sep="#|",end=" |")
    func(5,10,"hi","22",key1="abc",key2=False)
    func(5,10,mix1="hi",mix2="22",key1="abc",key2=False)
    func(5,10,"hi",mix2="22",key1="abc",key2=False)
    #func(5,pos2=10,mix1="hi",mix2="22",key1="abc",key2=False)-error
    #func(5,10,"hi","22","abc",key2=False)
    func1(1,mix2=22)
    #func2(33,key2=11)
    func2(key1=33,key2=11)
    #func3(44,pos2=101)
    func3=(44,101)
    printList(1,2,3,4,5)
    printList(1,2,3)
    print(mult([1,2,3]))
    print(mult1([1,2,3]))
    print(mult2([1,2,3]))
    
    list=[1,22,33,11,5]
    list.sort()
    print(list)
    list.sort(reverse=True)
    print(list)
    print(sorted(list))
    
    pairs=[(1,"One"),(2,"Two"),(3,"Three"),(10,"Ten"),(5,"Five")]
    pairs.sort()
    print(pairs)
#lambda functions   
    pairs.sort(key=lambda pair: pair[1])#promqna na sortiraneto
    print(pairs)
    
    list=[]
    addtoList(list)
    addtoList(list)
    print(list)
    
    #list=None
    #addtoList(list)
    #addtoList(list)
    
    list= addtoList1()
    print(list)
    list= addtoList1(data=22)
    print(list)

    list= addtoList2()
    print(list)
    list= addtoList2(data=33)
    print(list)
    d={"key":"1","value":"one"}
    dictionary(**d)
