edad = int(input('proporciona tu edad: '))

if 0 <= edad <= 10:
    print(f' con {edad} años, la infancia es increíble')
elif 11 <= edad <= 20:
    print(f' con {edad} años, muchos cambios y mucho estudio')
elif 21 <= edad <= 30:    
    print(f' con {edad} años, hay amor y comienza el trabajo')
else:
    print('Esa edad no está en el rango que me interesa')