#Escribe un programa que te pida una frase, y pase la frase como parámetro a
#una función. Ésta debe devolver si es palíndroma o no, y el programa
#principal escribirá el resultado por pantalla:
def f(a):
    a = a.replace(" ", "")
    x = a
    if a == (x[::-1]):
        b = str(f'La frase {frase}, es palindroma o capicua')
        return b
    else:
        b = str("La palabra no es palindroma o capicua")
        return (f'La frase, {frase} no es palindroma o capicua')

frase = input("Introduce una frase: ")
print(f(frase))
