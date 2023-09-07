#user_name = input()
#print("Привет, " +  user_name) # Насколько понял задание, нужно было сделать так?

from address import Address
from mailing import Mailing

mail = Mailing(Address('123321', 'Kirov', 'Vorovskogo', '1', '1'), Address('123321', 'Kirov', 'Vorovskogo', '2', '2'), 123, 'track')

print(mail)








