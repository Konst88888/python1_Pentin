from smartphone import Smartphone


phone1 = Smartphone('Samsung', 'Galaxy M12', '+79091234567')
phone2 = Smartphone('Nokia', 'G11', '+79113216549')
phone3 = Smartphone('Philips', 'Xenium S566', '+79036985214')
phone4 = Smartphone('Oukitel', 'WP5', '+79085236987')
phone5 = Smartphone('Xiaomi', 'Poco C40', '+79159874562')

catalog = [phone1, phone2, phone3, phone4, phone5]

def say():
    for n in catalog:
        print(n.sayPhone())

say()        
        


