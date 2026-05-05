#print(chr(97))
#print(ord('A'))}
#print(chr(97))
#print(ord('A'))


def es_char(caracter):
    """
    Funcion que se encarga de validar si el usuario ingreso un solo caracter.

    Args:
        caracter (str): Letra unica.
    
    Returns:    
        bool: Devuelve si es True o False el caracter que ingrese el usuario.
        Si es True es porque devuelve un caracter de (A-Z) y de (a-z).
        Si es False es porque ingreso una cadena de caracteres o porque no ingreso una letra. 
    """


    if len(caracter) != 1:
        print("Error. Ingrese solo un caracter.")
        return False

    valor = ord(caracter)
    retorno = False

    if (valor >= 65) and (valor <= 122):
        retorno = True

    else:
        print("Error. El caracter ingresado no es una letra.")
        retorno = False

    return retorno

ingresar_caracter = input("Ingrese un caracter: ")

resultado = es_char(ingresar_caracter)

print(resultado)
