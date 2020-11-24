#Escribir un programa que lea una frase, y pase ésta como parámetro a una
#función que debe contar el número de palabras que contiene. Debe imprimir el
#programa principal el resultado. Asumir que cada palabra está separada por
#un solo blanco:
#Asumir que cada palabra está separada por un solo blanco.
#a) No se sabe cómo están separadas las palabras. Pueden estar separadas por
#b) más de un blanco o por signos de puntuación.
def f(frase):
    contador = 1
    space = "  "
    signos = [".", ":", ",", ";", "-", ""," "]
    letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
              "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y",
              "z"]
    for i in frase:
        if i in signos:
            contador += 1
        if i is space:
            contador -= 1
    return contador

frase = input("Introduce una frase: ")
print(f'La frase tiene {f(frase)} palabras ')
