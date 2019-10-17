# pole powierzchni = dlugosc * szerokosc
# obwod okregu = 2pi r-radius
# ppp = dlugosc * szerokosc
# obwod prostokata = 2x dlugosc + 2x szerokosc
import math


# funkcja area() przyjmuje argument radius i zwraca wartosc pola powierzchni okregu
def area(radius):
    return math.pi * radius**2

# a tutaj tez argument radius i zwracamy obwod okregu
def circumference(radius):
    return 2 * math.pi * radius




