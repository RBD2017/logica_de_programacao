print('------------------------------')
print('Notas aluno')
print('------------------------------')

nota_aluno_primeiro_semestre = float(input('Notas do Primeiro Semestre:'))

nota_aluno_segundo_semestre = float(input('Notas do Segundo Semestre'))

media_final1 = nota_aluno_primeiro_semestre * 8

media2_final2 = nota_aluno_segundo_semestre * 8

print(f"{media_final1:.5} , {media2_final2:.5}")

if media_final1 > 48 or media2_final2 > 48:
    print('Parabens vc foi aprovado')
else:
    print('aluno reprovado')



