#!/usr/bin/env python3

from itertools import zip_longest
from types import NoneType


class Polynomial:
    polynom = []

    def __load_from_kwargs(self, kwargs):
        """Prevedeni hodnot polynomu pri pouziti kwargs"""
        if not kwargs:
            self.polynom = []
            return

        # Naparsovani indexu
        indexes = []
        for key in kwargs.keys():
            index = int(key.split("x")[1])
            indexes.append(index)
        
        # Vytvoreni prazdneho pole se spravnym poctem prvku
        self.polynom = []
        for i in range(max(indexes) + 1):
            self.polynom.append(0)

        # Nastaveni hodnot indexu
        for key,value in kwargs.items():
            index = int(key.split("x")[1])
            self.polynom[index] = value
            
        

    def __init__(self, *args, **kwargs):
        """ Inicializace polynomu"""
        # Zadano jako key values
        if len(args) < 1:
            self.__load_from_kwargs(kwargs)
            return

        # Zadano jako list
        if type(args[0]) == list:
            self.polynom = args[0]
            return 

        # Zadano jako individualni argumenty
        self.polynom = list(args)        


    def __str__(self):
        """ Prevedeni polynomu do pozadovaneho string fromatu """
        string = ""

        for key, value in reversed(list(enumerate(self.polynom[:]))):
            if value == 0:
                continue
            
            str_sign = ""
            str_index = ""
            str_value = ""
            
            # nastaveni znamenka
            if value > 0 and string != "":
                str_sign = '+ '
            elif value < 0:
                str_sign = '- '

            # nastaveni hodnoty
            if abs(value) != 1 or key == 0:
                str_value = str(abs(value))

            # nastaveni mocniny x
            if key != 0:
                if key == 1:
                    str_index = 'x'
                else:
                    str_index = 'x^' + str(key)

            # odsadit jednotlive hodnoty jen pokud jsou nejake pritomny 
            if string != "":
                string += ' '

            # sestaveni vysledneho formatu
            string +=  str_sign + str_value + str_index

        if string == "":
            string = "0"

        return string


    def __eq__(self, other):
        """ Porovnavaci funkce dvou polynomu """
        if not isinstance(other, Polynomial):
            return False

        return str(self) == str(other)


    def __add__(self, other):
        """ Scitaci funkce dvou polynomu """
        if not isinstance(other, Polynomial):
            raise TypeError
        
        new_list = []
        for x, y in zip_longest(self.polynom, other.polynom):
            # jeden polynom muze byt kratsi nez druhy
            if type(x) == NoneType:
                new_list.append(y)
            elif type(y) == NoneType:
                new_list.append(x)
            else:
                new_list.append(x + y)

        return Polynomial(new_list)


    def derivative(self):
        """ Funkce zderivuje polynom """
        if len(self.polynom) <= 1:
            return Polynomial([])

        new_polynom = self.polynom[:]
        new_polynom.pop(0)

        for i in range(len(new_polynom)):
            new_polynom[i] = new_polynom[i]*(i+1)

        return Polynomial(new_polynom)


    def at_value(self, x1, x2 = None):
        """ Vypocet hodnotu polynomu pri zadanem x """
        value1 = 0
        for n in range(len(self.polynom)):
            value1 += (x1**n) * self.polynom[n]

        # pri pouziti obou parametru 
        if x2:
            value2 = 0
            for n in range(len(self.polynom)):
                value2 += (x2**n) * self.polynom[n]

            return  value2 - value1

        return  value1


def test():
    assert str(Polynomial(0,1,0,-1,4,-2,0,1,3,0)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x"
    assert str(Polynomial([-5,1,0,-1,4,-2,0,1,3,0])) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x - 5"
    assert str(Polynomial(x7=1, x4=4, x8=3, x9=0, x0=0, x5=-2, x3= -1, x1=1)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x"
    assert str(Polynomial(x2=0)) == "0"
    assert str(Polynomial(x0=0)) == "0"
    assert Polynomial(x0=2, x1=0, x3=0, x2=3) == Polynomial(2,0,3)
    assert Polynomial(x2=0) == Polynomial(x0=0)
    assert str(Polynomial(x0=1)+Polynomial(x1=1)) == "x + 1"
    assert str(Polynomial([-1,1,1,0])+Polynomial(1,-1,1)) == "2x^2"
    pol1 = Polynomial(x2=3, x0=1)
    pol2 = Polynomial(x1=1, x3=0)
    assert str(pol1+pol2) == "3x^2 + x + 1"
    assert str(pol1+pol2) == "3x^2 + x + 1"
    # assert str(Polynomial(x0=-1,x1=1)**1) == "x - 1"
    # assert str(Polynomial(x0=-1,x1=1)**2) == "x^2 - 2x + 1"
    # pol3 = Polynomial(x0=-1,x1=1)
    # assert str(pol3**4) == "x^4 - 4x^3 + 6x^2 - 4x + 1"
    # assert str(pol3**4) == "x^4 - 4x^3 + 6x^2 - 4x + 1"
    assert str(Polynomial(x0=2).derivative()) == "0"
    assert str(Polynomial(x3=2,x1=3,x0=2).derivative()) == "6x^2 + 3"
    assert str(Polynomial(x3=2,x1=3,x0=2).derivative().derivative()) == "12x"
    pol4 = Polynomial(x3=2,x1=3,x0=2)
    assert str(pol4.derivative()) == "6x^2 + 3"
    assert str(pol4.derivative()) == "6x^2 + 3"
    assert Polynomial(-2,3,4,-5).at_value(0) == -2
    assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3) == 20
    assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3,5) == 44
    pol5 = Polynomial([1,0,-2])
    assert pol5.at_value(-2.4) == -10.52
    assert pol5.at_value(-2.4) == -10.52
    assert pol5.at_value(-1,3.6) == -23.92
    assert pol5.at_value(-1,3.6) == -23.92

if __name__ == '__main__':
    test()
        