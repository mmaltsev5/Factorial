print('Факториал')
while True:
    x = int(input('Введите число>> '))
    count = 0
    y = 1

    while count < x:
        count += 1
        y *= count

    else:
        print(y)
        break