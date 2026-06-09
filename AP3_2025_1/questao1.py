import random

def gera_vetor (tamanho):
    vetor = [random.randint(1,100) for _ in range(tamanho)]
    return vetor

def ordena_vetor (vetor):
    n = len(vetor)
    for i in range(n):
        menor_valor = i
        for j in range(i+1, n):
            if vetor[j] < vetor[menor_valor]:
                menor_valor = j
        vetor[i],vetor[menor_valor] = vetor[menor_valor],vetor[i]

def imprime_vetor (vetor):
    print(' '.join(str(vetor) for vetor in vetor))


n = int(input())
vetor = gera_vetor(n)
imprime_vetor(vetor)
ordena_vetor(vetor)
imprime_vetor(vetor)

if n >= 4:
    a , b , c , d = vetor[:4]
    print(a, b, c ,d)
    a , b = b , a
    print(a, b)