def bank(x, y):
    print(round((x * 1.1 ** y), 2))   #без использования цикла


 
    for y in range(y):  # с использованием цикла
        x *= 1.1
    print(round(x, 2))
x, y = int(input('Введите сумму вклада: ')), int(input('Введите срок вклада в годах: '))
bank(x, y)    