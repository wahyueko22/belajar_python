class Person:
    #constructor
    class_var = "init class var"
    def __init__(self, name, age):
        # instance variable
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

#inheritance class, class Student inherit from class Person
class Student(Person):
    def myfunc(self):
        print("Hello child my name is " + self.name)

class B:
    def x(self):
        print('x: B')


class C:
    def x(self):
        print('x: C')


class D(C, B):
    pass

class Tokenizer:
    """Tokenize text"""
    def __init__(self, text):
        print('Start Tokenizer.__init__()')
        self.tokens = text.split()
        print('End Tokenizer.__init__()')


class WordCounter(Tokenizer):
    """Count words in text"""
    def __init__(self, text):
        print('Start WordCounter.__init__()')
        super().__init__(text)
        self.word_count = len(self.tokens)
        print('End WordCounter.__init__()')


class Vocabulary(Tokenizer):
    """Find unique words in text"""
    def __init__(self, text):
        print('Start init Vocabulary.__init__()')
        super().__init__(text)
        self.vocab = set(self.tokens)
        print('End init Vocabulary.__init__()')


class TextDescriber(WordCounter, Vocabulary):
    """Describe text with multiple metrics"""
    def __init__(self, text):
        print('Start init TextDescriber.__init__()')
        super().__init__(text)
        print('End init TextDescriber.__init__()')

class Geeks:
     def __init__(self):
          self._age = 0
       
     # using property decorator
     # a getter function
     @property
     def age(self):
         print("getter method called")
         return self._age
       
     # a setter function
     @age.setter
     def age(self, a):
         if(a < 18):
            raise ValueError("Sorry you age is below eligibility criteria")
         print("setter method called")
         self._age = a