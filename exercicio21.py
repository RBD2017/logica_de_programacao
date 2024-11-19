print('----------------------')
print('posto de combustível')
print('----------------------')

alcool = 0
gasolina = 0
diesel = 0

while True:

    usuario = int(input('Informe um codigo (1, 2, 3) ou 4 para parar: '))
  
    if usuario < 1 or usuario > 4:
        print('código inválido , tente novamente')

    elif usuario == 1:
        alcool += 1

    elif usuario == 2:
        gasolina += 1

    elif usuario == 3:
        diesel += 1

    elif usuario == 4:
        print('Muito obrigado')
        print(f"álcool {alcool}")
        print(f"Gasolina {gasolina}")
        print(f"Diesel {diesel}")
        break

