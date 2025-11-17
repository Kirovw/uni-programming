
#1,1-РЕДИЦА НА ФИБОНАЧИ
#n=(n-1)+(n-2)

def fib():
    n1=n2=1
    print(n1,n2,end=" ")
    for i in range(10-2):
        n1,n2= n1+n2,n1
        print(n1,end=" ") 
    print()
fib()
def fib1(count):
    n1=n2=1
    for i in range(count):
        print(n2,end=" ")
        n1,n2= n1+n2,n1
    print()
fib1(20)
fib1(25)
print(type(fib),fib,fib())

def fib2(limit):
    n1=n2=1
    while(n2<=limit):
        print(n2,end=" ")
        n1,n2= n1+n2,n1
    print()
fib1(20)
fib1(25)
print(type(fib),fib,fib())
fib2(100)
fib2(13)
def fib11(count):
    n1=n2=1
    fibList=[]
    for i in range(count):
        fibList.append(n2)
        n1,n2= n1+n2,n1
    return fibList
print()
fib1(20)
fib1(25)
print(type(fib),fib,fib())
def fib22(limit):
    n1=n2=1
    fibList=[]
    while(n2<=limit):
        fibList.append(n2)
        n1,n2= n1+n2,n1
    return fibList
print(type(fib),fib,fib())
fib2(100)
fib2(13)
print(fib11(10))
print(fib22(100))
print()
def fib222(limit=1000):
    n1=n2=1
    fibList=[]
    while(n2<=limit):
        fibList.append(n2)
        n1,n2= n1+n2,n1
    return fibList
print(type(fib),fib,fib())
fib2(100)
fib2(13)
print(fib11(10))
print(fib22(100))
print(fib222())
print(fib222(10))

import tkinter as tK


def BGNtoEUR(bgn=100):
    return round(bgn/1.95583,2)

def BGNtoEUR():
    value=float(inputText.get())
    outputText.config(state="normal")
    outputText.delete(0,tK.END)
    outputText.insert(0,str(round(value/1.95583,2)))
    outputText.config(state="readonly")
    inputText.select_range(0,tK.END)
if __name__=="__main__":
    inputValue=int(input("BGN= "))
    #print("%g"%BGNtoEur(inputValue))
    #print(f"{inputValue} BGN= {BGNtoEur(inputValue)} EUR")
    #print(f"{inputValue}= {BGNtoEur(inputValue)} \N{EURO SIGN}")
    #print(f"100 BGN= {BGNtoEUR()} \N{EURO SIGN}")
    #ключово предаване на параметри
    window=tK.Tk()
    window.title("BGN to EUR")
    window.minsize(width=100,height=100)
    window.resizable(width=False,height=False)
    inputLabel=tK.Label(text="BGN")
    inputLabel.grid(row=0,column=0,padx=10,pady=10)
    inputText=tK.Entry()
    inputText.grid(row=0,column=1,padx=10,pady=10)
    inputText.bind("<Return>", lambda event: convert.invoke())
    inputText.bind("<Key,>, clear")
    inputText.focus()
    convert=tK.Button(text="Convert",command="convert")
    convert.grid(row=0,column=2,padx=10,pady=10)
    outputLabel=tK.Label(text="EUR")
    outputLabel.grid(row=1,column=0,padx=10,pady=10)
    outputText=tK.Entry(state="readonly")
    outputText.grid(row=1,colmn=1,padx=1=,pady=10)
    window.mainloop()
    

import tkinter as tK

def BGNtoEUR(bgn=100):
    return round(bgn / 1.95583, 2)

def convert():
    try:
        value = float(inputText.get())
        outputText.config(state="normal")
        outputText.delete(0, tK.END)
        outputText.insert(0, str(BGNtoEUR(value)))
        outputText.config(state="readonly")
        inputText.select_range(0, tK.END)
    except ValueError:
        outputText.config(state="normal")
        outputText.delete(0, tK.END)
        outputText.insert(0, "Invalid input")
        outputText.config(state="readonly")

if __name__ == "__main__":
    window = tK.Tk()
    window.title("BGN to EUR Converter")
    window.minsize(width=300, height=120)
    window.resizable(width=False, height=False)
    inputLabel = tK.Label(window, text="BGN:")
    inputLabel.grid(row=0, column=0, padx=10, pady=10)
    inputText = tK.Entry(window)
    inputText.grid(row=0, column=1, padx=10, pady=10)
    inputText.focus()
    convertButton = tK.Button(window, text="Convert", command=convert)
    convertButton.grid(row=0, column=2, padx=10, pady=10)
    outputLabel = tK.Label(window, text="EUR:")
    outputLabel.grid(row=1, column=0, padx=10, pady=10)
    outputText = tK.Entry(window, state="readonly")
    outputText.grid(row=1, column=1, padx=10, pady=10)
    inputText.bind("<Return>", lambda event: convertButton.invoke())
    window.mainloop()
