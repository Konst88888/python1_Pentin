def bank(x,y):
    print(round((x*1.1**y), 2))   #без использования цикла


 
    for y in range(y):  # с использованием цикла
        x = x*1.1
    print(round(x, 2))

bank(250, 17)    