print('-------------------------------')

print('Lanchonete')

print('-------------------------------')

codigo_produto = int(input('codigo do produto: '))

qnt_comprada = int(input('quantidade: '))

if codigo_produto == 1:
    pagamento = codigo_produto = 5.00 * qnt_comprada

elif codigo_produto == 2:
    pagamento = codigo_produto = 3.50 * qnt_comprada

elif codigo_produto == 3:
    pagamento = codigo_produto = 4.80 * qnt_comprada

elif codigo_produto == 4:
    pagamento = codigo_produto = 8.90 * qnt_comprada

elif codigo_produto == 5:
    pagamento = codigo_produto = 7.32 * qnt_comprada

elif codigo_produto > 5:
    print(KeyError)

print(pagamento)