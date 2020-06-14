from num2words import num2words

class NumberToWord(object):
    def __init__(self, number):
        self.number = number

    def __int__(self):
        return "hi"

    def convert(self):
        return num2words(self.number, lang='en_IN')
