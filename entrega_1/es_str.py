
def es_str(dato: str) -> bool:
    """
    Funcion que se encarga de que el usuario ingrese una cadena de caracteres y validarla.
    Los caracteres validos son desde (A-Z) hasta (a-z).

    Args:
        dato (str): La cadena de caracteres que escribirá el usuario.

    Returns:
        bool: Es True si la cadena cumple con las condiciones de la funcion.
        Caso contrario devolvera False.
    """


    if len(dato) == 0:
        return False
        
    retorno = True 
    
    for caracter in dato:
        valor = ord(caracter)

        if not ((valor >= 65 and valor <= 90) or (valor >= 97 and valor <= 122)):

            print("Error. Cadena de caracteres no ingresado")
            retorno = False
            break
        else:
            retorno = True

    return retorno


ingresar_string = input("Ingrese una cadena de caracteres: ")
respuesta = es_str(ingresar_string)
print(respuesta)