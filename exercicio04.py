print ('pagamento do funcionario !')

nome_funcionario = str(input('nome do funcionario: '))

valor_hora = int(input('valor da hora trabalhada:'))

horas_trabalhada = int(input('horas trabalhada: R$'))

pagamento_funcionario = valor_hora * horas_trabalhada

print(f"o pagamento  pelo funcionario {nome_funcionario}  é {pagamento_funcionario}")