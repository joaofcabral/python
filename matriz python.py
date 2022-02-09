#matriz.python

print("Matriz usando lista...")

    matriz = [
                    [3, 2 , 6],
                    [3, 3, 8],
                    [1, 2, 5]
                ]
    for linha in matriz:
        print(linha)
    lin = int(input("Numero da linha: "))
    col = int(input("Numero da coluna: "))

    print(matriz[lin][col])

    

linha = [0] * 5
matriz = [linha] * 3
print(matriz)
