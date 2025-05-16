nombres = ['Juan', 'Ana',  'Pedro', 'María']
print(nombres)
print(nombres[2])
print(nombres[1])
#acceder a los elementos de manera inversa
print(nombres[-2])
# preguntar el largo de una lista
print(len(nombres))
#agregar un elemento
nombres.append('Luis')
print(nombres)
#insertar un elemento en una posición específica
nombres.insert(3, 'Octavio')
print(nombres)  
#remover un elemento
nombres.remove('Octavio')
print(nombres)
#remover el último elemento
nombres.pop()
print(nombres)
#remover un elemento en una posición específica
del nombres[0]
print(nombres)
#limpiar la lista
#nombres.clear()
print(nombres)
#borrar la lista
#del nombres
#print(nombres)
#ordenar una lista
nombres = ['Juan', 'Ana',  'Pedro', 'María']
nombres.sort()
print(nombres)
#imprimir un rango
print(nombres[1:3]) #no incluye el último elemento
print(nombres[1:]) #hasta el final
print(nombres[:2]) #desde el principio
#cambiar un valor
nombres[3] = 'Roberto'
print(nombres)
#recorrer una lista
for nombre in nombres:
    print(nombre)
else:
    print('No hay más nombres en la lista')
    