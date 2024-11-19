print('----------------------------')
print('Tempo de jogo')
print('----------------------------')

hora_inicial = int(input('Hora Inicial: '))
hora_final = int(input('Hora Final: '))


if hora_inicial < hora_final:
    duracao = hora_final - hora_inicial
else:
    duracao = (24 - hora_inicial) + hora_final


if duracao == 0:
    duracao = 24

print(f'O jogo durou {duracao} hora(s)')
