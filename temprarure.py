class Temprature(object):
    def __init__(self, value):
        self.value = value

    def fahrenheit(self):
        far = ( self.value * (9/5)) + 32
        return far

    def celcious(self):
        cel = ((self.value - 32) * 5 /9)
        return cel



Far = Temprature(37.5).fahrenheit()
Cel = Temprature(Far).celcious()
print("Fahrenheit is: {} F, Celcious is: {} C".format(Far, Cel))
