class Smartphone:
    brend = 'None'
    model = 'None'
    number = 0

    def __init__(self, brend, model, number):
        self.brend = brend
        self.model = model
        self.number = number

    def sayPhone(self):
        print(self.brend, self.model, self.number)
            
#phone0 = Smartphone('brend', 'model', 'number')
#phone0.sayPhone()