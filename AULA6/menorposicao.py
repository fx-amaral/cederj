N = int(input())
array = input().split()

for i in range(N):
    array[i] = int(array[i])

menor = array[0]
posicao = 0
for i in range(N):
    if array[i] < menor:
        menor = array[i]
        posicao = i

print(f'Menor valor: {menor}')
print(f'Posicao: {posicao}')
