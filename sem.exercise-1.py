while True:
    n = int(input("Колко числа искате да въведете? "))  
    if n <= 0:
        print("Броят на числата трябва да е положителен. Опитайте пак.")
        continue
    even_sum = 0
    odd_sum = 0

    for i in range(n):
        x = int(input("Въведете число: "))
        if x % 2 == 0:
            even_sum += x
        else:
            odd_sum += x

    print(even_sum)
    print(odd_sum)

