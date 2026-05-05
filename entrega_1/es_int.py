def es_int(dato:str) ->bool:
    """
    Funcion que se encarga de validar si el usuario ingreso un número entero (Int).
    
    Args
        valor (str): Numero.

    Returns: 
        bool: Devuelve True si el numero ingresado es un numero entero (ejemplo: 2).
        Caso contrario, devuelve False
    """
    retorno = False
    for caracter in dato:
        retorno = False
        if (ord(caracter) >= 48 and ord(caracter) <= 57):
            retorno = True
        else:
            retorno = False
            break
        
    return retorno

numero = input("Ingrese un numero: ")
valor = es_int(numero)

while valor == False:
    numero = input("Error. El dato ingresado es incorrecto. \nIngrese un numero: ")
    valor = es_int(numero)

numero = int(numero)
print(valor)