def entrada_valida(dna):
    for letra in dna:
        if letra not in "AaCcGgTt":
            return False
    return True


def compressao_rle(dna):
    resultado = ""
    contador = 1

    for i in range(1, len(dna)):
        if dna[i] == dna[i - 1]:
            contador += 1
        else:
            resultado += dna[i - 1] + str(contador)
            contador = 1

    resultado += dna[-1] + str(contador)

    return resultado


dna = input().strip()

if entrada_valida(dna):
    print(compressao_rle(dna))
else:
    print("Entrada inválida")
