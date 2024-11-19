
n = int(input("Digite o número de experimentos realizados: "))


total_cobaias = 0
total_coelhos = 0
total_ratos = 0
total_sapos = 0


for _ in range(n):
    
    entrada = input("Digite a quantidade e o tipo de cobaia (C/R/S): ").split()
    quantidade = int(entrada[0])
    tipo = entrada[1].upper()  
   
    total_cobaias += quantidade

    
    if tipo == 'C':
        total_coelhos += quantidade
    elif tipo == 'R':
        total_ratos += quantidade
    elif tipo == 'S':
        total_sapos += quantidade


if total_cobaias > 0:
    percentual_coelhos = (total_coelhos / total_cobaias) * 100
else:
    percentual_coelhos = 0

if total_cobaias > 0:
    percentual_ratos = (total_ratos / total_cobaias) * 100
else:
    percentual_ratos = 0

if total_cobaias > 0:
    percentual_sapos = (total_sapos / total_cobaias) * 100
else:
    percentual_sapos = 0


print("\nRELATÓRIO FINAL:")
print(f"Total: {total_cobaias} cobaias")
print(f"Total de coelhos: {total_coelhos}")
print(f"Total de ratos: {total_ratos}")
print(f"Total de sapos: {total_sapos}")
print(f"Percentual de coelhos: {percentual_coelhos:.2f} %")
print(f"Percentual de ratos: {percentual_ratos:.2f} %")
print(f"Percentual de sapos: {percentual_sapos:.2f} %")
