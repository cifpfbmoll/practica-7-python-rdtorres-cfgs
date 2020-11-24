#Escribe un programa que pida una frase (entrada por teclado), y pase la
# frase como parámetro a una función que debe eliminar los espacios en
# blanco (compactar la frase). El programa principal imprimirá por pantalla
# el resultado final.
def f(a):
    x = a.replace(" ", "")
    return x
frase = str(input("Escriba una frase: "))
print(f(frase))
