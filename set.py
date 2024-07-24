# Crear una lista con muchos datos repetidos

lista_con_repetidos = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 6, 6, 7, 8, 8, 9, 9, 9, 9, 9]

 

# Crear un set a partir de la lista con datos repetidos

mi_set = set(lista_con_repetidos)

print("Set después de eliminar duplicados:", mi_set)

 

# Agregar algunos elementos adicionales, incluidos repetidos

mi_set.add(10)

mi_set.add(2)  # Este no se agregará porque ya está en el set

mi_set.update([11, 12, 12, 13, 14, 14])  # Agregar varios elementos, con repetidos

 

# Mostrar el set final

print("Set final después de agregar elementos adicionales:", mi_set)