# Declarar una tupla con algunos elementos

mi_tupla = (1, 2, 3, 4, 5)

 

# Acceder al cuarto elemento

print("Cuarto elemento:", mi_tupla[3])

 

# Convertir la tupla en una lista para modificarla

lista_desde_tupla = list(mi_tupla)

 

# Agregar un nuevo elemento

lista_desde_tupla.append(6)

print("Lista después de agregar un elemento:", lista_desde_tupla)

 

# Convertir la lista de nuevo en una tupla

mi_tupla = tuple(lista_desde_tupla)

print("Tupla modificada:", mi_tupla)



