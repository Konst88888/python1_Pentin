class Mailing:
    
    def __init__(self, from_address, to_address, cost, track):
            
        self.from_address = from_address
        self.to_address = to_address
        self.cost = cost
        self.track = track 

    def toString(self):
        return  'Отправление <' + self.track + '> из ' + self.from_address.toString() + ' в ' + self.to_address.toString() + '. Стоимость <' + str(self.cost) + '> рублей.'