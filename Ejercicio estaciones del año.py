mes = int(input('Indica un mes del año (1-12): '))
estacion = None
if mes == 1 or mes == 2 or mes == 12:
    estacion = 'verano'
    print(f'Para el mes {mes} la estación es: {estacion}')
elif mes == 3 or mes == 4 or mes == 5:
    estacion = 'otoño'
    print(f'Para el mes {mes} la estación es: {estacion}')
elif mes == 6 or mes == 7 or mes == 8:
    estacion = 'invierno'
    print(f'Para el mes {mes} la estación es: {estacion}')
elif mes == 9 or mes == 10 or mes == 11:
    estacion = 'primavera'
    print(f'Para el mes {mes} la estación es: {estacion}')
else:
    print('Valor fuera de rango')