#coleccion set
planetas = {'Mercurio', 'Venus', 'Tierra', 'Marte', 'Jupiter', 'Saturno', 'Urano', 'Neptuno'}   #creamos un conjunto de planetas
#largo del conjunto
print(len(planetas))  #imprimimos el largo del conjunto
#revisar si un elemento esta presente   
print('Marte' in planetas)  #preguntamos si Marte esta en el conjunto
#agregar un elemento    
planetas.add('Pluton')  #agregamos Pluton al conjunto
#remover un elemento
planetas.remove('Pluton')  #removemos Pluton del conjunto
#eliminar elemento sin arrojar error
planetas.discard('Pluton')  #removemos Pluton del conjunto
#limpiar el conjunto
planetas.clear()  #limpiamos el conjunto
#eliminar el conjunto
del planetas  #eliminamos el conjunto

