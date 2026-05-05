from entrega_2.calculo import *

numero_uno = input("Primer numero: ")
numero_dos = input("Segundo numero: ")

numero_uno = float(numero_uno)
numero_dos = float(numero_dos)

resultado = sumar(numero_uno, numero_dos) 

print(f"La suma es: {resultado}")


resultado = restar(numero_uno, numero_dos)

print(f"La resta es: {resultado}")


while numero_dos == 0:
    print("Error. No se puede dividir entre cero.")
    numero_dos = input("Ingrese un numero distinto de cero: ")
    numero_dos = float(numero_dos)

resultado = dividir(numero_uno, numero_dos)

print(f"La division es: {resultado}")




resultado = multiplicar(numero_uno, numero_dos) 

print(f"La multiplicacion es: {resultado}")



