dias = ["lunes", "martes", "miercoles", "jueves", "viernes"]

# recuperar datos
print(dias[0])

# agregar elementos en las listas
dias.append("sabado")
dias.append("domingo")

# eliminar elementos
dias.pop(2)
del dias[0:2]

# actualizar elementos
dias[-1] = "lunes"

# mostrar todos los valores de la lista
for dia in dias:
    print(dia)
