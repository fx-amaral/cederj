def q2(nome_arquivo):
    teste = open(nome_arquivo, 'r+')
    teste.seek(0)
    linhas = teste.readlines()
    total = 0
    for linha in linhas:
        total += int(linha)
    valor = total / len(linhas)
    teste.write("\nValor: " + str(valor))
    teste.close()

nome = input()
q2(nome)