import circle
import rectangle

# menu options

AREA_CIRCLE_CHOICE = 1
CIRCUMREFERENCE_CHOICE = 2
AREA_RECTANGLE_CHOICE = 3
PERIMETER_RECTANGLE_CHOICE = 4
QUIT_CHOICE = 5

def main():
    choice = 0

    while choice != QUIT_CHOICE:
        display_menu()

        choice = int(input('Wybierz opcje: '))

        if choice == AREA_CIRCLE_CHOICE:
            promien = float(input('Podaj promien okregu: '))
            print('Pole powierzchni wynosci ', circle.area(promien))
        elif choice == CIRCUMREFERENCE_CHOICE:
            promien = float(input('Podaj promien okregu:'))
            print('Pole powierzchni wynosi ', circle.circumference(promien))
        elif choice == AREA_RECTANGLE_CHOICE:
            dlugosc = float(input('Podaj dlugosc podstawy: '))
            szerokosc = float(input('Podaj szerokosc podstawy '))
            print('Pole powierzchni prostokata wynosi: ', rectangle.area(dlugosc, szerokosc))
        elif choice == PERIMETER_RECTANGLE_CHOICE:
            dlugosc = float(input('Podaj dlugosc podstawy: '))
            szerokosc = float(input('Podaj szerokosc podstawy '))
            print('Obwod wynosi: ', rectangle.perimeter(dlugosc, szerokosc))
        elif choice == QUIT_CHOICE:
            break
        else:
            print('Bledna opcja')


def display_menu():
    print('MENU', '1) Pole powierzchni okregu', '2) Obwod okregu', '3) Ppp',
          '4) Obwod prostokata', '5) Koniec', sep='\n')

main()


