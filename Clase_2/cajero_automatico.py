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