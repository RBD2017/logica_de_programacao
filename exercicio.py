
largura = float(input("Digite a largura do terreno (m): "))
comprimento = float(input("Digite o comprimento do terreno (m): "))
valor_metro_quadrado = float(input("Digite o valor do metro quadrado (R$): "))


area = largura * comprimento

preco_terreno = area * valor_metro_quadrado


print(f"Área do terreno: {area:.2f} m²")
print(f"Preço do terreno: R$ {preco_terreno:.2f}")
