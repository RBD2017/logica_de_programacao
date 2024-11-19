print('----------------------------')
print('Notas do Aluno')
print('----------------------------')

while True:
    
    nota1 = float(input('Digite a primeira nota: '))
    if nota1 < 0 or nota1 > 10:
        print('Valor inválido para a primeira nota, tente novamente.')
        continue  

    nota2 = float(input('Digite a segunda nota: '))
    if nota2 < 0 or nota2 > 10:
        print('Valor inválido para a segunda nota, tente novamente.')
        continue  

    media = (nota1 + nota2) / 2
    print(f'Média semestral: {media:.2f}')
    break
