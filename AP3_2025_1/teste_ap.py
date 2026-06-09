def selection_sort(vetor):
    n = len(vetor)
    for i in range(n):
        indice_minimo = i
        for j in range(i + 1, n):
            if vetor[j] < vetor[indice_minimo]:
                indice_minimo = j

        # Realiza a troca
        vetor[i], vetor[indice_minimo] = vetor[indice_minimo], vetor[i]

        # Mostra o estado da lista a cada passo
        print(f"Passo {i + 1}: {vetor}")


# Testando com uma lista desordenada
lista = [29, 10, 14, 37, 13]
selection_sort(lista)