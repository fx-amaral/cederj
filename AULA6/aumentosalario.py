#Salary increase

salario_atual = float(input())
novo_salario = 0
reajuste_ganho = 0

if salario_atual <= 400.00:
    reajuste_ganho = salario_atual * 0.15
    novo_salario = salario_atual + reajuste_ganho
    print(f'Novo salario: {novo_salario:.2f}')
    print(f'Reajuste ganho: {reajuste_ganho:.2f}')
    print('Em percentual: 15 %')
elif salario_atual >= 400.01 and salario_atual <= 800.00:
    reajuste_ganho = salario_atual * 0.12
    novo_salario = salario_atual + reajuste_ganho
    print(f'Novo salario: {novo_salario:.2f}')
    print(f'Reajuste ganho: {reajuste_ganho:.2f}')
    print('Em percentual: 12 %')
elif salario_atual >= 800.01 and salario_atual <= 1200.00:
    reajuste_ganho = salario_atual * 0.10
    novo_salario = salario_atual + reajuste_ganho
    print(f'Novo salario: {novo_salario:.2f}')
    print(f'Reajuste ganho: {reajuste_ganho:.2f}')
    print('Em percentual: 10 %')
elif salario_atual >= 1200.01 and salario_atual <= 2000.00:
    reajuste_ganho = salario_atual * 0.07
    novo_salario = salario_atual + reajuste_ganho
    print(f'Novo salario: {novo_salario:.2f}')
    print(f'Reajuste ganho: {reajuste_ganho:.2f}')
    print('Em percentual: 7 %')
elif salario_atual >= 2000.01:
    reajuste_ganho = salario_atual * 0.04
    novo_salario = salario_atual + reajuste_ganho
    print(f'Novo salario: {novo_salario:.2f}')
    print(f'Reajuste ganho: {reajuste_ganho:.2f}')
    print('Em percentual: 4 %')