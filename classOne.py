class ClassOne:
    def __init__(self, message):
        self.message = message

    def show_message(self):
        print(self.message)


    @staticmethod
    def say_goodbye():
        print('goodbye!')