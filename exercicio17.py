print('--------------------------')
print('Problema Crescente')
print('--------------------------')

while True:
    x = int(input('Digite o primeiro número: '))
    y = int(input('Digite o segundo número: '))
    
    if x == y:
        break  
    elif x < y:
        print('Crescente')
    else:
        print('Decrescente')

print('FIM DO PROGRAMA')
