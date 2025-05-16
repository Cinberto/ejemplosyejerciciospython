#definir una TUPLA
frutas = ('Naranja', 'frutilla', 'sandia','pera','manzana')
#saber la longitud de la tupla
print(len(frutas))
#Acceder a un elemento de la tupla
print(frutas[0])
#Navegacion inversa
print(frutas[-1])
#Acceder a un rango
print(frutas[0:3]) #sin incluir el indice 3
#recorrer elementos
for fruta in frutas:
    print(fruta)   
#modificar una tupla... no se puede!
#modificamos la tupla a lista, modificamos la lista y la volvemos tupla de nuevo
frutasLista = list(frutas)
frutasLista[0] = 'Pera'
frutas = tuple(frutasLista)
print('\n', frutas)
#el ejercicio anterior no es una buena practica.
#eliminar la tupla 
del frutas
print(frutas) #error porque la tupla ya no existe