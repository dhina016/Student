class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def checkColor(self):
        if(self.color == 'BROWN'):
            return 'DARK'
        else:
            return 'LIGHT'

dog1 = Dog('LABRADOR', 'BROWN')
dog2 = Dog('SHEPHERD', 'WHITE')
print(dog1.checkColor())
print(dog2.checkColor())
