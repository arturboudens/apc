def print_rectangle(tamanho):
    tamanho = int(tamanho)
    borda = tamanho * '+'
    espaco = (tamanho - 2) * ' '

    print(tamanho)
    print(f'{borda}')
    print(f'+{espaco}+')
    print(f'{borda}')

tamanho1, tamanho2, tamanho3 = input().split()

tamanho1 = int(tamanho1)
tamanho2 = int(tamanho2)
tamanho3 = int(tamanho3)

print_rectangle(tamanho1)
print_rectangle(tamanho2)
print_rectangle(tamanho3)