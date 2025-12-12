dias = ("lunes", "martes", "miercoles", "jueves", "viernes")
# diferencia entre de tupla= no se cambia, no se agrega elementos,a menos que se convierta a lista
print(f"Tipo de dato original: {type(dias)}")
dias = list(dias)
print(f"Tipo de dato modificado: {type(dias)}")
dias.append("sabado")
dias = tuple(dias)

print(dias)
