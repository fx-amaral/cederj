def eh_ocorrencia(matriz, n, m, palavra, i, j, dl, dc):
    posicoes = []
    linha = i
    coluna = j

    for k in range(len(palavra)):
        if linha < 0 or linha >= n or coluna < 0 or coluna >= m:
            return False, []

        if matriz[linha][coluna] != palavra[k]:
            return False, []

        posicoes.append("(" + str(linha + 1) + "," + str(coluna + 1) + ")")

        linha = linha + dl
        coluna = coluna + dc

    return True, posicoes


n, m = map(int, input().split())

matriz = []
for _ in range(n):
    matriz.append(input().strip().lower())

palavra = input().strip().lower()

# Direções (8)
dir_linha = [0, 0, 1, -1, 1, 1, -1, -1]
dir_coluna = [1, -1, 0, 0, 1, -1, 1, -1]

encontrou = False

for i in range(n):
    for j in range(m):
        for d in range(8):
            dl = dir_linha[d]
            dc = dir_coluna[d]

            ok, pos = eh_ocorrencia(matriz, n, m, palavra, i, j, dl, dc)

            if ok:
                encontrou = True
                for p in pos:
                    print(p, end=" ")
                print()

if not encontrou:
    print("nenhuma")
