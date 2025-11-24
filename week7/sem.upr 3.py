def uppernumber(numbers):
    total=0
    for x in numbers:
        if x<=total:
            return False
        total+=x
    return True
print(uppernumber([1,2,3,4,5,6,7,8]))
#2-Напишете функция, която взема сортиран списък от числа и връща медианата. Ако числото е дроб, то трябва да се закръгли до най-близката десета.
def median(sorted_list):
    n = len(sorted_list)
    if n == 0:
        return None 
    mid = n // 2
    if n % 2 == 1:
        #медианата е средният елемент-нечетност
        med = sorted_list[mid]
    else:
        #медианата е средното на двата средни елемента=>четност
        med = (sorted_list[mid - 1] + sorted_list[mid]) / 2
    return round(med, 1)
#3
def most_valuable_item(items_dict):
    if not items_dict:
        return None
    max_item=None
    max_value=0
    for item in items_dict:
        value = items_dict[item]#->inicializiram promenliva kato vzimame stojnostta za klucha
        if value > max_value:
            max_value = value 
            max_item = item    
    return max_item
items = {
    "часовник": 5000,
    "пръстен": 12000,
    "картина": 8000
}
print(most_valuable_item(items))
#4Напишете функция, която приема списък от числа и връща две числа, чиято абсолютна разлика е минимална. Двойката числа трябва да се върне като списък, сортиран във възходящ ред.
def min_difference_pair(numbers):
    if len(numbers) < 2:
        return None#->trqbva za dvoika
    numbers_sorted = numbers.sort()#->ili sorted
    min_diff =200
    pair = []
    for i in range(len(numbers_sorted) - 1):
        a = numbers_sorted[i]
        b = numbers_sorted[i + 1]
        difference = abs(a - b)#_>modul za polojitelno chislo(razlika)
        if difference < min_diff:
            min_diff = difference
            pair = [a, b] 
    return pair
#5-Напишете функция, която взема три числа: ширината и височината на правоъгълника и радиуса на кръга, и връща True, ако правоъгълникът може да се побере в кръга.
def face_of_a_rectangle(a,h,r):
    return a**2 + h**2 <= (2 * r)**2#->diagonalyt na praw.<=diametyryt, vmesto koren kvadraten vidgam na kvadrat

#6-Напишете функция, която взема списък с имена на плодове, разделя тези думи наполовина и ги сортира по азбучен ред.
def split_and_sort_fruits(fruits):
    halves = []
    for fruit in fruits:
        mid = len(fruit) // 2#->centura na dumata(ploda)tursim index
        half = fruit[:mid]#->vzimam bukvite ot nachaloto do sredata(bez mid) za samiq plod(element)
        halves.append(half)
    halves.sort()
    return halves
#7-Напишете функция, която получава списък на всички естествени делители на цяло число
def divisors(n):
    if n <= 0:
        return None#->deliteli polojitelni chisla 
    result = []
    for i in range(1, n + 1):#->vsichki vuzmojni deliteli
        if n % i == 0:#->proverka dali e delitel
            result.append(i)#->dobavqme delitel
    return result
#8-Напишете функция, която връща всички неуникални елементи от редицата
def ununique(lst):
    result = []
    for x in lst:
        if lst.count(x) > 1 and x not in result:#->ako se sudurja poveche ot edin put i ne e predvaritelno v spisuka
            result.append(x)
    return result
#10-Ученикът е изправен пред задача: входът на функцията sieve() е списък от цели числа. Тази функция води до кортеж от уникални елементи от списък в обратен ред.
def sieve(numbers):
    result = []
    for x in numbers[::-1]:#->obhojdam v obraten red
        if x not in result:#->uslovieto za unikalnost,ako e dobaveno v argument ne go dobavqme v rezultatniq kortej za da e unikalen 
            result.append(x)
    return tuple(result)










