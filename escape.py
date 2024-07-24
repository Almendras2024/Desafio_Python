import math

# Función para calcular la velocidad de escape
def calcular_velocidad_escape(radio_km, constante_g):

    # Convertir el radio de kilómetros a metros
    radio_metros = radio_km * 1000

    # Calcular la velocidad de escape
    return math.sqrt(2 * constante_g * radio_metros)

# Solicitar los datos
radio = float(input("Ingrese el radio del planeta en kilómetros: \n"))
constante_g = float(input("Ingrese la constante g  en m/s^2: \n"))

# Calcular la velocidad de escape
velocidad_escape = calcular_velocidad_escape(radio, constante_g)

# Imprimir el resultado
print(f"La velocidad de escape es: {velocidad_escape:.2f} m/s")