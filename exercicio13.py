print('----------------------------')

print('Arremeso de dardo')

print('----------------------------')

arremeso1 = int(input('distancia 1: '))

arremeso2 = int(input('distancia 2: '))

arremeso3 = int(input('distancia 3: '))

if arremeso1 >= arremeso2 and arremeso1 >= arremeso3:
    maior = arremeso1

elif arremeso2 >= arremeso1 and arremeso2 >= arremeso3:
    maior = arremeso2

else:
    maior = arremeso3

print(f"o maior arremesso foi {maior}")
