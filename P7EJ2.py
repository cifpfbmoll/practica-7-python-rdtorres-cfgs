# Escribe un programa que lea (entrada por teclado) el nombre y los dos
# apellidos de una persona (en tres cadenas de caracteres diferentes), los pase
# como parámetros a una función, y ésta debe unirlos y devolver una única
# cadena. La cadena final la imprimirá el programa por pantalla.
def f(a,b,c):
    list = [a,b,c]
    s =" "
    s = s.join(list)
    return s
nombre = str(input("Dime tu nombre: "))
apellido1 = str(input("Dime tu primer apellido: "))
apellido2 = str(input("Dime tu segundo apellido: "))

print(f(nombre, apellido1, apellido2))
