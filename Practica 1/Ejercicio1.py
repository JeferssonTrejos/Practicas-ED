# Crear una función llamada saludar que reciba un nombre e imprima 
# "Hola, “El nombre que se ingresó”

def saludo(nombre):
    print(f"Hola, {nombre}")

nombre = str(input("Ingrese su nombre: "))
saludo(nombre)
