#calculadora
#entrada
n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))
operacion = input("Operación (+, -, *, /): ")
# condicional
if operacion == "+":
    resultado = n1 + n2
elif operacion == "-":
    resultado = n1 - n2
elif operacion == "*":
    resultado = n1 * n2
elif operacion == "/":
    if n2 == 0:
        resultado = "Error: no se puede dividir entre 0"
    else:
        resultado = n1 / n2
else:
    resultado = "Operación no válida"
#salida
print(f"{n1} {operacion} {n2} = {resultado}")