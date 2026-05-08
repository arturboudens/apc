nFunc = int(input())
aux = nFunc
maior = -1
menor = 1000000001
total = 0
med = 0 

while aux > 0:
    nome, sal = input().split(',')
    sal = float(sal)

    if sal > maior:
        maior = sal
        nMaior = nome
    if sal < menor:
        menor = sal
        nMenor = nome

    aux -= 1
    total += sal


if nFunc != 0:
    med = total/nFunc
    print(f'{med:.2f}')
else:
    print("Não tem média")

if maior != -1:
    print(f'{nMaior} {maior:.2f}')
else:
    print("Não tem")

if menor != 1000000001:
    print(f'{nMenor} {menor:.2f}')
else: 
    print("Não tem")




