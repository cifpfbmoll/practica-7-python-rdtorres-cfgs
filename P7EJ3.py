# Escribe un programa que lea (entrada por teclado) una frase, y la pase como
# parámetro a un procedimiento, y éste debe mostrar la frase con un carácter en
# cada línea.
def f(a):
    for i in range(len(a)):
        print(a[i])
frase = str(input("Escriba una frase: "))
f(frase)