#Escribe un programa que lea el nombre de una persona y un carácter (entrada
#por teclado), le pase estos datos a una función que comprobará si dicho
#carácter está en su nombre. El resultado de dicha función lo imprimirá el
#programa principal por pantalla.
def f(a,b):
    c = a.find(b)
    return c
nombre = str(input("Dime un nombre: "))
letra = str(input("Dime una letra: "))
if (f(nombre,letra)) < 0:
    print("No está el caracter")
else:
    print("El caracter sí está")
