#funciones en python
#def mi_funcion(nombre, apellido):
#    print("Hola desde mi funcion")
#    print(f'Nombre: {nombre} Apellido: {apellido}')
#mi_funcion('Cintia', 'Bertoncini')
#mi_funcion('Juan', 'Perez')
#mi_funcion('Ana', 'Gomez')

#def sumar(a, b):
 #   return a + b  #en este caso la funcion devuelve la suma de los dos valores
#resultado = sumar(8, 9)
#print(f'resultado de la suma: {sumar (8, 9)}') #ó tambien...
#print(f'resultado de la suma: {resultado}')

#def sumar(a=0, b=0) 
#    return a + b  #en este caso la funcion devuelve la suma de los dos valores
#resultado = sumar()
#print(f'resultado de la suma: {resultado}')
#print(f'resultado de la suma: {sumar(2,8)}')
# a y b en el principio tienen los valores por default cdro, lo que no quiere decir que se le puedan
#asignar otros valores al llamar a la funcion y sobreescribir los valores por default
#si no se le asigna ningun valor a los parametros, la funcion toma los valores por default
 
#ARGUMENTOS VARIABLES EN UNA FUNCION:

#def listaNombres(*nombres):        #internmente python lo convierte en tupla, pudiendo iterar los elementos
 #   for nombre in nombres:
#        print(nombre)               #recordar que una tupla no puede ser modificada


#listaNombres('Estefania', 'Sofia', 'Jazmin', 'Giuliana', 'Piero', 'Emilia')

#ARGUMENTOS VARIABLES TIPO (LLAVE, VALOR) EN UNA FUNCION:
 
#def listarTerminos(**terminos):
#    for llave, valor in terminos.items():
#        print(f'{llave}: {valor}')

#listarTerminos(COO='Chief Operating Officer', CEO='Chief Executive Officer', CTO='Chief Technology Officer', CMO='Chief Marketing Officer')

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)
#podemos colocar los nombres directamente en la funcipon, o hacer una variable que contenga los nombres
nombres = ['Estefi', 'Sofi', 'Jaz', 'Giuli', 'Piero', 'Emi']
desplegarNombres(nombres)
#desplegarNombres(['Estef i', 'Sofi', 'Jaz', 'Giuli', 'Piero', 'Emi']) #tambien se puede hacer de esta manera
desplegarNombres('piero') #en este caso, como no es una lista, sino un string, la funcion lo toma como una lista de caracteres
#y los imprime uno por uno
#en el caso de numeros, int, no se pueden iterar, a menos que los coloquemos entre
#paréntesis, como una tupla:
desplegarNombres((10,12)) #en este caso, la funcion toma los numeros como una tupla y los imprime uno por uno
#también podemos enumerarlos en una lista, colocando los numeros entre corchete
