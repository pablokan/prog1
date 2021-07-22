class Person:
    def __init__(self, name):
        self.name = name
    def sayHi(self):
        print('Hello, my name is', self.name)

person1 = Person('Swaroop')
person1.sayHi()
