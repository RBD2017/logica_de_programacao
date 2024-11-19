print('-----------------------')
print('Senha Fixa')
print('-----------------------')

senha_correta = 2002

while True:
    senha = int(input('digite sua senha: '))
    if senha == senha_correta:
        print('Acesso Permitido ! ')    
        break

    else:
        print('senha incorreta tente novamente')
        

    