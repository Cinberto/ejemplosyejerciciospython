#Una función recursiva es una función que se llama a sí misma para completar cierta tarea
#Ejemplo de función recursiva
#5! = 5 * 4 * 3 * 2 * 1
#5! = 5 * 4 * 3 * 2
#5! = 5 * 4 * 6
#5! = 5 * 24
#5! = 120 

def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)   
    
print(f"El factorial de {numero} es {factorial(numero)}")    