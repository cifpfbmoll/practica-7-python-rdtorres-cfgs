#Escribe un programa que lea una frase (entrada por teclado), y la pase como
#parámetro a un procedimiento. El procedimiento contará el número de vocales
#(de cada una) que aparecen, y lo imprimirá por pantalla.
def f(a):
    list = ['a','e','i','o','u','A','E','I','O','U']
    for i in list:
        if a.count(i) > 0:
            print("La vocal %s aparece %s vez." %(i,a.count(i)))
frase = str(input("Escribe una frase: "))
f(frase)
