print('----------------------------------------')
print('Troco Verificado')
print('----------------------------------------')


preco_produto = float(input('Valor do produto: '))
qnt_produtos = int(input('Quantidade comprada: '))
valor_recebido_cliente = float(input('Valor recebido R$: '))


soma_produtos = preco_produto * qnt_produtos


if valor_recebido_cliente >= soma_produtos:
    
    troco = valor_recebido_cliente - soma_produtos
    print(f'Troco a ser devolvido: R$ {troco:.2f}')
else:
    
    falta = soma_produtos - valor_recebido_cliente
    print(f'Faltam ainda R$ {falta:.2f}')
