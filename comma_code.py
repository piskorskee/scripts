spam = ['apples', 'bananas', 'tofu', 'cats', 'demons', 'hounds']


def list_thing(lista):
    # creating a string then splitting it as list with two items, second being last word

    new_string = ', '.join(lista).rsplit(',', 1)  # .join dodaje , przed ostatnia wartoscia (hound) dzieki rsplit
    print(new_string)  # i wciaz jest lista

    # Using the same method used above to recreate string by replacing the separator.

    new_string = ' and'.join(new_string)  # .join laczy dwie wartosci w liscie wyrazem and
    return new_string


print(list_thing(spam))

lista = ['jeden', 'dwa', 'trzy', 'cztery']
lista2 = ['trzy', 'trzy', 'trzy', 'trzy']
new_lista = ' trzy i pol '.join(lista) # wartosc trzy i pol dolacza do kazdej kolejnej wartosci
                                       # a new lista jest stringiem!
print(new_lista)

new_lista2 = 'OOOO '.join(lista).rsplit('jeden',
                                        1)  # pierwszy apostrof - co dodajemy, .rsplit('zamiast czego', 'ile wart'
print(new_lista2)
new_lista3 = 'hmm '.join(lista2).rsplit(', ', 2)  # 'hmm' co dodajemy, rsplit('gdzie', 'ile ma byc wartosci'
print(new_lista3)
