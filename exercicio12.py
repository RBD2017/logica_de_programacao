print('----------------------------------')
print('Programa diabetes')
print('----------------------------------')

medida_glicose = float(input('Medida da glicose: '))

if medida_glicose < 90:
    print('Normal')

elif medida_glicose > 100 and medida_glicose < 140:
    print('Elevado')

else:
    print('Diabetes')