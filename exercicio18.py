print("Cálculo da Idade Média")
print("-----------------------")


soma_idades = 0
quantidade = 0

while True:
    idade = int(input("Digite a idade: "))
    
    if idade < 0:
       
        if quantidade == 0:
            print("IMPOSSÍVEL CALCULAR")
        break

    # Somar as idades e contar os indivíduos
    soma_idades += idade
    quantidade += 1

# Calcular e exibir a média se houver pelo menos uma idade válida
if quantidade > 0:
    media = soma_idades / quantidade
    print(f"A idade média do grupo é: {media:.2f}")


    
    