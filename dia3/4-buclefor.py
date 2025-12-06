#BUCLE FOR
for contador in range(1,11,1):
    print(contador)
    
#TABLA DE MULTIPLICAR
tabla = int(input("Ingrese la tabla de multiplicar que desea ver: "))
for contador in range(1,13,1):
    resultado = tabla * contador
    print(f"{tabla} x {contador} = {resultado}")