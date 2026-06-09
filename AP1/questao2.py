'''
Dado um texto T e uma palavra alvo w, encontre todas as ocorrências de w em T como palavra inteira, isto é, delimitada por início/fim de string. Relate as posições de início de cada ocorrência na ordem em que aparecem no texto.
Entrada: Duas linhas. A primeira contém o texto T. A segunda contém a palavra alvo w (sem espaços).
Saída: Uma lista com as posições de início de cada ocorrência de w como palavra inteira no texto, separadas por espaço. Se não houver ocorrências, imprima nenhuma.
Observações:
A busca deve considerar letras maiúsculas e minúsculas como iguais (ex.: ``Casa'' = ``casa'').
Considere como parte de palavra apenas caracteres alfanuméricos [A--Z, a--z, 0--9].
A busca deve contar sobreposições (ex.: T = ``banana'' e w = ``ana'' possui aparições iniciando nas posições 2 e 4
'''

T = input().lower()
w = input().strip().lower()

n = len(T)
m = len(w)

posicoes = []

for i in range(0, n - m + 1):
    iguais = True

    for j in range(m):
        if T[i + j] != w[j]:
            iguais = False
            break

    if iguais:
        posicoes.append(i + 1)

if len(posicoes) == 0:
    print("nenhuma")
else:
    print(*posicoes)
