# Funcion 1

# Nombre
# Argumentos
# Codigo
# Retorno

def sumar(a, b):

    resultado = a + b

    return resultado
    
 
resultado_suma = sumar(2, 3)
print(resultado_suma)
print(sumar(2, 3))


# Funcion 2
def resta():
    resultado = 2 - 3

    return resultado

print(resta())


# Funcion 3

def saludo(cantidad_saludos):
    """Esta función recoge los nombres ingresados por el usuario en una 
    lista y devuelve los mismos en formato lista"""

    lista_nombres = []

    # Bucle de ingreso de nombres
    for i in range(cantidad_saludos):

        nombre = input('Ingrese su nombre: ')
        print('Hola', nombre)

        lista_nombres.append(nombre)

    return lista_nombres

def orden(lista, sentido):
    """_summary_

    Args:
        lista (_type_): _description_
        sentido (_type_): _description_

    Returns:
        _type_: _description_
    """
    lista.sort(reverse=sentido)

    return lista



nombres = saludo(int(input('Ingrese la cantidad de saludos a efectuar: ')))

print(
    orden(nombres, True)
)


    

    