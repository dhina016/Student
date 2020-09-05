class A():
    def __init__(self, name='myname', age='22', username='user1', password='12345678'):
        self.name = name
        self.age = age
        self.__username = username
        self._password = password


obj1 = B()
print(obj1.name)
print(obj1.age)
print(obj1._password)
print(obj1.__username)