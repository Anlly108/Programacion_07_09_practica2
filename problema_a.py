def anagrama(palabra_1, palabra_2):
    palabra_1 = palabra_1.lower()
    palabra_2 = palabra_2.lower()
    palabra_1_arreglo = list(palabra_1)
    palabra_2_arreglo = list(palabra_2)
    palabra_1_arreglo.sort()
    palabra_2_arreglo.sort()
    palabra_1_ordenada = "".join(palabra_1_arreglo)
    palabra_2_ordenada = "".join(palabra_2_arreglo)
    return palabra_1_ordenada == palabra_2_ordenada

palabra_ingresada_1 = input("Ingresa la primera palabra: ")
palabra_ingresada_2 = input("Ingresa la segunda palabra: ")
es_anagrama = anagrama(palabra_ingresada_1, palabra_ingresada_2)

if es_anagrama:
    print(f"{palabra_ingresada_1} es anagrama de {palabra_ingresada_2}")
else:
    print(f"{palabra_ingresada_1} NO es anagrama de {palabra_ingresada_2}")