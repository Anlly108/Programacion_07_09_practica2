frase_ingresada= input("Ingresa la frase: ").lower().split()

if len({i[0] for i in frase_ingresada}) == 1:
    print('La frase es un tautograma')
else:
    print('La frase no es un tautograma')