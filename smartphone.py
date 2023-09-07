class Smartphone:
    brend = 'None'
    model = 'None'
    number = 0

    def __init__(self, brend, model, number):
        self.brend = brend
        self.model = model
        self.number = number

    def sayPhone(self):
        stringValue = '<' + self.brend + '> - <' + self.model + '>. <' + self.number + '>'
        return(stringValue)

    def toString(self):
        return '<' + self.brend + '> - <' + self.model + '>. <' + self.number + '>'