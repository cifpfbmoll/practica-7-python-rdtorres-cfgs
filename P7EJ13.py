#Escribe un programa que le pida al usuario si quiere calcular si un número
#es primo con for o con while, por tanto, habrá dos funciones que se
#caracterizan por hacer ese mismo cálculo de una manera (con for y sin
#breaks), o de otra (con while). Ambas funciones devolverá true (si es
#primo) o false (si no es primo). El programa principal informará del
#resultado. Además, como mejora puedes calcular el tiempo que tarda en
#encontrar la solución de una manera u otra. Comentario: aprovecha el código
#que tienes ya creado
import time
eleccion = (int(input("Elige un 1 o 2: ")))
numero = (int(input("Dime un numero: ")))
def EsPrimofor(numero):
    inicio = time.time()
    resto = 1
    for i in range(numero):
        if (i != 0) and (i != 1) and (numero % i == 0):
            resto = 0
        if resto == 0:
            print("True")
        else:
            print("False")
    final = time.time() - inicio
    return (final)

def EsPrimoWhile(numero):
    inicio = time.time()
    resto = 1
    mod = 1
    while (resto != 0):
        mod += 1
        resto = numero % mod
        if mod == numero:
            print("True")
        else:
            print("False")
    final = time.time() - inicio
    print("El while tarda: %.10f segundos." %final)
if eleccion == 1:
    EsPrimofor(numero)
else:
    EsPrimoWhile(numero)
