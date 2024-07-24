import math

def calcular_utilidades(P_normal, P_premium, U_normal, U_premium, GT):
    return (P_normal * U_normal + P_premium * U_premium) - GT

try:
    P_normal = float(input("Introduce el precio de suscripción para usuarios normales (P_normal): "))
    P_premium = P_normal * 1.5
    U_normal = int(input("Introduce el número de usuarios normales (U_normal): "))
    U_premium = int(input("Introduce el número de usuarios premium (U_premium): "))
    GT = float(input("Introduce el gasto total (GT): "))
    utilidades = calcular_utilidades(P_normal, P_premium, U_normal, U_premium, GT)
    print(f"Las utilidades son: {utilidades:.2f}")
except ValueError:
    print("Entrada inválida. Por favor, introduce valores numéricos válidos para P_normal, U_normal, U_premium y GT.")