
def is_year_leap(x):
  
    if int(x) % 4 == 0 :
        print('год', x, ':',True)
    elif int(x) % 4 != 0:
        print('год', x, ':',False)    
x = int(input('Введите год: '))
is_year_leap(x)



