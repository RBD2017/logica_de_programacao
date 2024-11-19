print('----------------------------------')
print('Aumento para os funcionarios ')
print('----------------------------------')

salario_atual = float(input('Salario atual R$: '))

if salario_atual == 1000.00:
    aumento = (salario_atual * 20) / 100
    print(f" o novo salario é R$:  {salario_atual + aumento}")
    print(f"aumento foi de R${aumento}")
    porcetagem = 20
    print(f"a porcetagem foi de {porcetagem}%")
elif salario_atual >= 1000.00 and salario_atual <= 3000.00:
    aumento = (salario_atual * 15) / 100
    print(f" o novo salario é R$:  {salario_atual + aumento}")
    print(f"aumento foi de R${aumento}")
    porcetagem = 15
    print(f"a porcetagem foi de {porcetagem}%")

elif salario_atual >= 3000.00 and salario_atual <= 8000.00:
    aumento = (salario_atual * 10) / 100
    print(f" o novo salario é R$:  {salario_atual + aumento}")
    print(f"aumento foi de R${aumento}")
    porcetagem = 10
    print(f"a porcetagem foi de {porcetagem}%")

else:
    salario_atual >= 8000.00
    aumento = (salario_atual * 5 ) / 100
    print(f" o novo salario é R$:  {salario_atual + aumento}")
    print(f"aumento foi de R${aumento}")
    porcetagem = 5
    print(f"a porcetagem foi de {porcetagem}%")