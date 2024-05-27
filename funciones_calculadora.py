import os

def pedir_operando()-> int:

    while True:
        aux = input("Ingrese un numero: ")
        if aux.isdigit():
            operando = int(aux)
            break
        else:
            print("Numero invalido")
    
    return operando
##
def menu()-> str:

    print(f"{'Menu de Opciones':^50s}")
    print("1- Sumar los numeros")
    print("2- Restar los numeros")
    print("3- Dividir los numeros")
    print("4- Multiplicar los numeros")
    print("5- Factorial de los numeros")
    print("6- Salir")

    return input("Ingrese una opcion: ")
##
def sumar_operandos(operando_a:int, operando_b:int)-> None:

    resultado = operando_a + operando_b
    print(f"El resultado de {operando_a} + {operando_b} es: {resultado}")
##
def restar_operandos(operando_a: int, operando_b: int)-> None:

    resultado = operando_a - operando_b
    print(f"El resultado de {operando_a} - {operando_b} es: {resultado}")
##
def dividir_operandos(operando_a: int, operando_b:int)-> None:

    if operando_a == 0 or operando_b == 0:
        raise ZeroDivisionError("No se puede realizar la division por 0")
    else:
        resultado = operando_a / operando_b
        print(f"El resultado de {operando_a} / {operando_b} es: {resultado}")
##
def multiplicar_operandos(operando_a: int, operando_b: int)-> None:

    resultado = operando_a * operando_b
    print(f"El resultado de {operando_a} * {operando_b} es: {resultado}")
##
def factorial(operando: int)-> int:
    
    fact = None
    if operando == 0 or operando == 1:
        fact = 1
    else:
        fact = operando * factorial(operando - 1)

    return fact
##
def mostrar_factorial(operando)-> None:

    fact = factorial(operando)
    print(f"El factorial de {operando} es: {fact}")