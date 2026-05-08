n = int(input())
aux = 0

while(aux <= n):
    if aux % 3 == 0 and aux % 7 == 0:
        print(aux, end=' ')
    aux += 1

    
