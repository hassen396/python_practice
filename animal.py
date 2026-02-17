class Animal:
    def __init__(self):
        self.age = 0


    def walk(self):
        print(f'The {self.age} year{"s " if self.age >=2 else " "}old animal is walking! 😁')


    @staticmethod
    def pee():
        print('the animal is ***')


    def set_age(self, age):
        self.age = age