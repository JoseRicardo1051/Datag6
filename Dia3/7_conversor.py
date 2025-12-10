import os

# Tipo de cambio
cambio = 3.0 
historial = [] # hostorial global   
def limpiar ():
    os.system("cls" if os.name == "nt" else "clear")

def leer_cantidad(mensaje):
    """Lectura de numeros validos, se aceprta 10,5 y 10.5 , no se aceptan negativos"""
    while True:
        numero = input(mensaje).strip().replace(",", ".")
        try:
            valor = float(numero)
            if valor < 0:
                print("¡No se aceptan Ngativos, volver a ingresar!")
                continue
            return valor
        except:
            print("Entrada invalida, ingrese solo numeros.")

def borrar(n):
    """Quita .0 si es un numero entero se limita a 4 decimales"""
    if float(n).is_integer():
        return str(int(n))
    else:
        return f"{round(n,4)}"
def menu():
    global cambio, historial

    while True:
        limpiar()
        print("=========CONVERTIDOR DE MONEDAS==========")
        print(f"Tipo de cambio actual: 1 USD = {cambio}PEN")
        print("1. Convertir Soles a Dolares")
        print("2. Convertir Dolares a Soles")
        print("3. Cambiar tipo de cambio")
        print("4. Salir")
        print("5. Ver historial")
        print("6. Borrar historial")
        print("=======================")

        opcion = input("Sleccione un opcion: ")

        if opcion == "1":
            monto = leer_cantidad("Ingrese cantidad en Soles: ")
            resultado = monto / cambio
            texto = f"s/.{borrar(monto)} soles = $.{borrar(resultado)} dolares"
            historial.append(texto)
            print("\n" + texto)
            input("\nPresione Enter para continuar.....")
        
        elif opcion =="2":
            monto = leer_cantidad("Ingrese cantidad en Dolares: ")
            resultado = monto * cambio
            texto = f"$.{borrar(monto)} dolares = S/.{borrar(resultado)} soles"
            historial.append(texto)
            print(f"\n" + texto)
            input("\nPresione Enter para continuar.....")
        
        elif opcion == "3":
            nuevo = leer_cantidad ("Nueva cantidad de Cambio: ")
            if nuevo == 0:
                print("El tipo de cambio no puede ser 0: ")
            else:
                cambio = nuevo
                print(f"Tipo de cambio actualizado a {cambio} soles por dolar.")
            input("\nPresione Enter para continuar")
        
        elif opcion == "5":
            print("=========Historial=======")
            if historial:
                for h in historial:
                    print("- " + h)
            else:
                print("sin registro")
            input("\nPresione enter para continuar")

        elif opcion == "6":
            historial.clear()
            print("Hostorial borrado. ")
            input("\nPresione Enter para continuar")
        elif opcion == "4":
            print("¡Saliendo del sistema!")
            break
        
        else:
            print("Opcion invalida intente otra vez.")
            input("Enter para continuar")
        

# Ejecucion del programa
menu()



            
