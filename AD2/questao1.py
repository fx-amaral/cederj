"""
Hoje é a inauguração de um grande supermercado em sua cidade, e todos estão muito excitados
com os baixos preços prometidos. Este supermercado tem N funcionários que trabalham no caixa,
identificados por números de 1 a N, onde cada funcionário leva um determinado tempo vi para processar
um item de um cliente. Ou seja, se um cliente tem cj itens em sua cesta, um determinado funcionário levará
vi*cj segundos para processar todos os itens deste cliente.
Quando um cliente entra na fila para ser atendido ele espera até que um funcionário esteja livre para o atendê-lo.
Se mais de um funcionário estiverem livres ao mesmo tempo, o cliente será atendido pelo funcionário de menor
número de identificação. Tal funcionário só estará livre novamente após processar todos os itens deste cliente.
Há M clientes na fila para serem atendidos, cada um com um determinado número de itens na sua cesta.
Dadas as informações sobre os funcionários nos caixas e os clientes, o gerente pediu sua ajuda para descobrir
quanto tempo levará para que todos os clientes sejam atendidos.

Entrada
A primeira linha conterá dois inteiros N e M, indicando o número de funcionários no caixa e o número de clientes,
respectivamente (1 ≤ N ≤ M ≤ 104).

Em seguida haverá N inteiros vi, indicando quanto tempo leva para o i-ésimo funcionário processar
um item (1 ≤ vi ≤ 100, para todo 1 ≤ i ≤ N).

Em seguida haverá M inteiros cj, indicando quantos itens o j-ésimo cliente tem em sua
cesta (1 ≤ cj ≤ 100, para todo 1 ≤ j ≤ M).

"""
#Entradas=============================================================
fc = input().split()
n = int(fc[0]) # nº de funcionários
m = int(fc[1]) # nº de clientes
v = list(map(int, input().split())) #tempo vi dos funcionários
c = list(map(int, input().split())) #nº de itens dos clientes


tempos_livres = [0] * n #lista com os tempos dos funcionários


for itens_dos_clientes in c: #Funcionário que fica livre primeiro
    menor_tempo = tempos_livres[0]
    indice_funcionario = 0

    for i in range(1, n):
        if tempos_livres[i] < menor_tempo:
            menor_tempo = tempos_livres[i]
            indice_funcionario = i

    tempo_trabalho = itens_dos_clientes * v[indice_funcionario]    #Calculando o tempo
    tempos_livres[indice_funcionario] += tempo_trabalho


resultado_final = tempos_livres[0] #Pegar o maior tempo
for tempo in tempos_livres:
    if tempo > resultado_final:
        resultado_final = tempo

print(resultado_final)


#print(n , m)