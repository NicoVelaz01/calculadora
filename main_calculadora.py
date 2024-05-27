import os
from funciones_calculadora import *

operando_a = pedir_operando()
operando_b = pedir_operando()

while True:

    os.system("cls")
    print(f"Numero A: {operando_a}")
    print(f"Numero B: {operando_b}" )

    match menu():
        case "1":
            os.system("cls")
            sumar_operandos(operando_a, operando_b)

        case "2":
            os.system("cls")
            restar_operandos(operando_a, operando_b)

        case "3":
            os.system("cls")
            dividir_operandos(operando_a, operando_b)

        case "4":
            os.system("cls")
            multiplicar_operandos(operando_a, operando_b)

        case "5":
            os.system("cls")
            mostrar_factorial(operando_a)
            mostrar_factorial(operando_b)

        case "6":
            os.system("cls")
            print("Fin del programa")
            break
    os.system("pause")