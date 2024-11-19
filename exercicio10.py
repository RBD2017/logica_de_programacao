print('--------------------------')
print('Operadora telefonia')
print('--------------------------')

minutos = int(input('quantidade de minutos'))
valor_fixo = 50
acresimo_conta = 2

if minutos <= 100:
    valor_a_pagar = valor_fixo
else:
    
    minutos_excedentes = minutos - 100
    valor_a_pagar = valor_fixo + (acresimo_conta * minutos_excedentes)

print(valor_a_pagar)
