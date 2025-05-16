edad = int(input('Ingresa tu edad: ') )

veintes = 20 <= edad <= 30
print(veintes)
treintas = 30 <= edad <= 40
print(treintas)

if veintes or treintas:
    if veintes:
        print('Dentro del rango de los 20s')
    elif treintas:
        print('Dentro del rango de los 30s')    
    else:
        print('Fuera del rango de los 20s o 30s')    
