def month_to_season(n):    
        if n == 1 or n == 2 or n == 12:
            print('Зима')
        elif 3 <= n <= 5:
            print('Весна')
        elif 6 <= n <= 8:
            print('Лето') 
        elif 9 <= n <= 11:
            print('Осень')
        else:
            print('ошибка, введите число от 1 до 12')           
n = int(input('Введите порядковый номер месяца: '))        
month_to_season(n)               