
class Car:
    """A class that represents a car"""
    def __init__(self, name, model):
        self.name = name
        self.model = model


    def start(self):
        print(f"starting the {self.name} car")