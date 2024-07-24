import math


def calcular_utilidades(P, U, GT):
    return P * U - GT

def comparar_utilidades(U_anterior):
    try:
        P = float(input("Introduce el precio de suscripción (P): "))
        U = int(input("Introduce el número de usuarios normales (U): "))
        GT = float(input("Introduce los gastos (GT): "))
        U_actuales = calcular_utilidades(P, U, GT)
        razon = U_actuales / U_anterior
        print(f"La razón entre las utilidades actuales y las del año anterior es: {razon:.2f}")
    except ValueError:
        print("Entrada inválida. Por favor, introduce valores numéricos válidos para P, U, GT y U_anterior.")
    except ZeroDivisionError:
        print("Las utilidades del año anterior no pueden ser cero.")

try:
    U_anterior = float(input("Introduce las utilidades del año anterior (U_anterior): "))
    comparar_utilidades(U_anterior)
except ValueError:
    print("Entrada inválida. Por favor, introduce un valor numérico válido para U_anterior.")