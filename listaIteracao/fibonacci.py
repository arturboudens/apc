def fibonacci(n):
    x = 0
    y = 1
    aux = n
    aux2 = 0

    while(aux > 0):
        print(x)

        aux2 = x + y
        x = y
        y = aux2

        aux -= 1
        


n = int(input())
fibonacci(n)