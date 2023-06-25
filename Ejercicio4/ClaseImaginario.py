import cmath
class Imaginario:
    def __init__(self, real, imaginario):
        self.real = real
        self.imaginario = imaginario
    
    def getImaginario(self):
        return self.imaginario
    def getReal(self):
        return self.real

    def __add__(self, other):
        real = self.real + other.real
        imaginario = self.imaginario + other.imaginario
        return Imaginario(real, imaginario)

    def __sub__(self, other):
        real = self.real - other.real
        imaginario = self.imaginario - other.imaginario
        return Imaginario(real, imaginario)

    def __mul__(self, other):
        real = (self.real * other.real) - (self.imaginario * other.imaginario)
        imaginario = (self.real * other.imaginario) + (self.imaginario * other.real)
        return Imaginario(real, imaginario)
    """2 + 1i    /  3 + 2i"""
    def __truediv__(self, other):
        divisor = (other.real ** 2) + (other.imaginario ** 2)
        real = ((self.real * other.real) + (self.imaginario * other.imaginario)) / divisor
        imaginario = ((self.imaginario * other.real) - (self.real * other.imaginario)) / divisor
        return Imaginario(real, imaginario)
                        

    def __str__(self):
            return f"{str(self.real)} + {str(self.imaginario)}i"