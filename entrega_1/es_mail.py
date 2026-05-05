
def es_mail(valor):
    """
    La funcion valida si una cadena de texto cumple con el formato de correo electrónico.
    La validación requiere que el mail comience con una letra, y tenga por lo menos, 
    un arroba (@) y un punto (.).

    Args:
        valor (str): La cadena de caracteres que representa el mail.

    Returns:
        bool: True si cumple con las condiciones, False en caso contrario.
    """

    retorno = False
    contador_puntos = 0
    contador_arrobas = 0
    contador = 0
    for caracteres in valor:

        caracter = ord(caracteres)

        if contador == 0:
            if (caracter >= 65 and caracter <= 90) or (caracter >= 97 and caracter <=122):
                retorno = True
            else:
                print("Error: El mail debe empezar con una letra.")
                retorno = False

        contador += 1

        if caracter == 46:
            contador_puntos += 1

        if caracter == 64:
            contador_arrobas += 1

        if contador_puntos > 1:
            print("Error. Solo se permite un punto (.)")
            retorno = False


        if contador_arrobas > 1:
            print("Error. Solo se permite un arroba (@).")
            retorno = False

    if contador_arrobas != 1 or contador_puntos != 1:
        print("Error: El mail debe contener exactamente un arroba (@) y un punto (.)")
        retorno = False

    return retorno


ingresar_mail = input("Ingrese su mail: ")
resultado = es_mail(ingresar_mail)
print(resultado)
