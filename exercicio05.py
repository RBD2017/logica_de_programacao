print ('processamento de pagamento')

preco_produto = int(input('valor do produto:'))

qnt_produtos = int(input('quantidade comprada:'))

valor_recebido_cliente = int(input('valor recebido R$:'))

troco = (preco_produto * qnt_produtos) - valor_recebido_cliente

print(troco)
