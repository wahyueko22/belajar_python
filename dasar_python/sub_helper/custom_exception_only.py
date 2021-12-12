class BusinessException(Exception):
    """ it is custom exception """
    def __init__(self, message=""):
        self.message = message
        super().__init__(self.message)


class Employee:
    #constructor
    def __init__(self, name, age):
        # instance variable
        self.name = name
        self.age = age
