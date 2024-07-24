import math

def calcular_utilidades(P, U, GT):
    return P * U - GT

try:
    P = float(input("Introduce el precio de suscripción (P): "))
    U = int(input("Introduce el número de usuarios (U): "))
    GT = float(input("Introduce el gasto total (GT): "))
    utilidades = calcular_utilidades(P, U, GT)
    print(f"Las utilidades son: {utilidades:.2f}")
except ValueError:
    print("Entrada inválida. Por favor, introduce valores numéricos válidos para P, U y GT.")