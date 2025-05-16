print('Proporciona los siguientes datos del libro:')
libro = input('Ingresa el nombre del libro:' )
autor = input('Ingresa el nombre del autor: ')
codigo = input('Ingresa el ID del libro: ')
precio = float(input('Ingresa el precio del libro: '))
envioGratuito = input('Indica si el envio es gratuito (True/False): ')

if envioGratuito == 'True':
    envioGratuito = True
elif envioGratuito == 'False':
    envioGratuito = False
else:
    envioGratuito = 'Valor incorrecto, debe ser True/False'

print(f'''
      nombre del libro: {libro}
      autor: {autor}
      ID del libro: {codigo}
      precio del libro: {precio}
      envio gratuito: {envioGratuito}
''')

