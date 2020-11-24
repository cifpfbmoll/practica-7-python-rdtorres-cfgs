# Escribe un programa que te pida una palabra o número, pase por parámetro
# estos datos a una función, y ésta te diga si es o no palíndroma o capicúa.
# El programa principal imprimirá el resultado de la función:
def f(a):
    if a == (a[::-1]):
        b = str("La palabra es palindroma o capicua")
        return b
    else:
        b = str("La palabra no es palindroma o capicua")
        return (f'{a} no es palindroma o capicua')

character = input("Introduce una palabra o número: ")
print(f(character))