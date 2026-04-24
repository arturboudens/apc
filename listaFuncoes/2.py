def nota(n):
    n = int(n)
    print(f'|{n * '★'}{(10 - n) * '☆'}|')

n = 5
nota(n)