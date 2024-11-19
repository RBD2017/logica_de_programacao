while True:
   
    x = int(input("Digite um número (ou 0 para sair): "))
    
    if x == 0:
        print("Programa encerrado.")
        break
    
    if x % 2 != 0:
        x += 1  
    
    soma = 0
    for i in range(5):
        soma += x + (i * 2) 
    
    print(f"SOMA = {soma}")
