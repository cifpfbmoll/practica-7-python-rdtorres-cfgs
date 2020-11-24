#Desarrolla un programa utilizando la metodología “pair programming”, que nos
#sirva para gestionar nuestros contactos (la información a gestionar será el
#teléfono, nombre, apellido1, apellido2 y correo electrónico. El programa
#tendrá un menú, con las siguientes opciones: añadir contacto, consultar
#contacto a partir de la clave, consultar todos los contactos y eliminar
#contacto. Aprovecha lo que has aprendido hasta el momento (diccionarios,
#funciones, procedimientos…).#Roberto Torres Cruz – examen 1º evaluación.
agenda = True # Ponemos el menu operativo nada mas empezar
diccionario = {111: ['roberto', 'torres', 'cruz', 'email@inventado'],
               222: ['enrique', 'manuel', 'cocacola', 'email2@inventado']}
# Para agregarle todos los campos y guardarlos
#numero, nombre, apellido1, apellido2,email
def añadir(diccionario):
    numero = int(input("Escribe el numero: "))
    nombre = str(input("Escribe el nombre: "))
    apellido1 = str(input("Escribe el apellido1: "))
    apellido2 = str(input("Escribe el apellido2: "))
    email = str(input("Escribe el email: "))
    list_contacto = [nombre, apellido1, apellido2, email] #valores
    diccionario[numero] = list_contacto
    return diccionario
def eliminar(diccionario):
    eliminar_contacto = int(input("Escribeme el numero: "))
    print("¿Estás seguro de eliminarlo? ")
    check = input("Si/No ")
    if check == "Si" or check == "No":
        diccionario.pop(eliminar_contacto)
    # eliminar clave y valor usando clave de ref.
def consultabonita(diccionario):
    for k, v in diccionario.items():
        print(k,v)

def consultarcontacto(diccionario):
    consultar = int(input("Escriba el numero del contacto: "))
    error = "No se encuentra el contacto"
    print(diccionario.get(consultar, error))

while agenda:
    print("=======================================")
    print("=================Agenda================")
    print("=======================================")
    print("Opción 1: Añadir contacto")
    print("Opción 2: Eliminar contacto")
    print("Opción 3: Consultar todos los contactos")
    print("Opción 4: Consultar contacto por valor")
    #print(diccionario)
    menu =int(input("Elija una opción: "))
    if menu == 1:
        añadir(diccionario)
        print(diccionario)
        #Añadir contacto

    elif menu == 2:
        eliminar(diccionario)
        print(diccionario)
        #Eliminar contactos

    elif menu == 3:
    # Consultar todos los contactos
        consultabonita(diccionario)
    elif menu == 4:
        consultarcontacto(diccionario)
    # Consulta un contacto
    else:
        agenda = False
