# For
lista = []

for i in range(3):
    
    # Ingreso de datos
    dato_ingreso = input('Ingrese un numero: ')

    #Validacion
    if dato_ingreso.isnumeric():
        lista.append(int(dato_ingreso))
    else:
        print('No es un número')
        break

print(lista)

# While

x = 10

while x > 0:
    print(x)

    x -= 1

