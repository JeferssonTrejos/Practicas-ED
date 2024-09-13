# Ejercicio 4: Eliminar Elementos 
# Dada la lista frutas = ["manzana", "banana", "naranja", "mango", "pera"], 
# elimina "naranja" de la lista usando remove(), 
# y luego elimina el último elemento usando pop(). 
# Imprime la lista después de cada eliminación. 

frutas = ["manzana", "banana", "naranja", "mango", "pera"]
print("Lista original \n",frutas,'\n')
frutas.remove("naranja") 
print("Lista despues de eliminar 'naranja': \n", frutas,'\n')

frutas.pop() 
print("Lista despues de eliminar el último elemento:\n", frutas)
