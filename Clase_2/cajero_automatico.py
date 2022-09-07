from ast import While


print('\n\n### Bienvenido al cajero ###\n\n')
print('### ¿A qué opción desea ingresar? ###\n\n')
while True:
    print('  1 - DEPOSITO \n')
    print('  2 - EXTRACCION \n')
    print('  3 - TRANSFERENCIA \n')
    print('  4 - SALIR \n')
    opcion = int(input('Ingrese el número de la opción deseada: '))
    
    if opcion == 1:
        x = int (input('Ingrese el monto a Depositar: '))
    elif opcion == 2:
        x = int (input('Ingrese el monto a Extraer: '))
    elif opcion == 3:
        x = int (input('Ingrese el monto a Transferir: '))
    elif opcion == 4:
        print('Usted Salió')
        break
    else:
        print("El número ingresado no es una opcion")



"""
while True:

print("\n\n MENU \n")
print("1. Deposito")
print("2. Extraccion")
print("3. Transferencia")
print("4. Salir")
opcion = input("Selecciona una opcion: ")

"""


"""
print('1 - Deposito\n2 - Extranccion\n3 - Transferencia\n4 - Salir')
opcion = int(input('ingrese la opcion deseada'))

while opcion != 4 :
if opcion == 1:
x = int(input('ingrese monto a depositar: '))
elif opcion == 2:
x = int(input('ingrese monto a extraer: '))
elif opcion == 3
x = int(input('ingrese monto a Transferir: '))
else:
print('La opcion ingresada no corresponde')
print('1 - Deposito\n2 - Extranccion\n3 - Transferencia\n4 - Salir')
opcion = int(input('ingrese la opcion deseada'))

print('Salio del sistema')

"""