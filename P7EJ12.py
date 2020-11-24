#Escribir un programa que lea una frase, y pase ésta como parámetro a una
#función que debe contar el número de palabras que contiene. Debe imprimir el
#programa principal el resultado. Asumir que cada palabra está separada por
#un solo blanco:
#Asumir que cada palabra está separada por un solo blanco.
#a) No se sabe cómo están separadas las palabras. Pueden estar separadas por
#b) más de un blanco o por signos de puntuación.
def f(a):
    text = a.split()
    b = len(text)
    return b

frase = input("Introduce una frase: ")
print(f(frase))

frase = input("Introduce una frase: ")
#print(f(frase))