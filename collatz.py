
def collatz(number): # definiujemy funkcje collatz z parametrem number
        if number % 2 == 0: # loop while, ktory sprawdza czy podany parametr zostawia modulo 0
            print(int(number // 2))
            return number // 2 # zwracamy wartosc number, zeby wykonac na nim jeszcze raz operacje while
        elif number % 2 != 0: # jezeli parametr nie zostawia modulo 0, to wykonujemy loop if
            result = int(3 * number + 1)
            print(result)
            return result # zwracamy wartosc


try:
    a = int(input('podaj int'))
    while int(a) != 1:
        a = collatz(int(a))
except ValueError:
    print('musi byc integer')