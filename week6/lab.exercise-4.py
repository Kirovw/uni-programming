#1
def faceofrighttriagnle(a,b=5):
    S=a*b/2
    return S
print("Лицето на правоъгълния тригълник: ", faceofrighttriagnle(3))

def faceofrighttriagnle(a,b):
    S=a*b/2
    return S
print("Лицето на правоъгълния тригълник: ", faceofrighttriagnle(3,5))

def faceofrectangle(a,b):
    B=a*b
    return B
print("Лицето на правоъгълника: ", faceofrectangle(4,5))

def faceofsquare(a):
    A=a*a
    return A
print("Лицето на квадрата: ", faceofsquare(5))

#figure = input("Въведете фигура (триъгълник / правоъгълник / квадрат): ")
#if figure == "триъгълник":
  #  print("Лицето на правоъгълния триъгълник е:", faceofrighttriagnle(4,5))
#elif figure == "правоъгълник":
   # print("Лицето на правоъгълника :", faceofrectangle(3,4))
#elif figure == "квадрат":
  #  print("Лицето на квадарата е: ", faceofsquare(2))
#else:
  #  print("Невалидна фигура!")

#2
def changenumber(nlist, wholenumber):
    for i in range(len(nlist)):
        if nlist[i] > wholenumber:
            nlist[i] = 0
changenumber([1,1,1,1,7,8,9], 5)
#3 Функция получава като аргумент число и връща като резултат дали е палиндром(труе,фолсе)
def is_palindrome(num):
    num_str=str(num)
    num_str[::-1]
    return num_str
if is_palindrome(1234):
    print("True")
else:
    print("False")
    

