"""Avaliação a distãncia de fundamentos de programação
   2026-1
   JOGO MISTÉRIO DO MUSEU"""



print('====JOGO MISTÉRIO DO MUSEU====')
while True:
            entrada = str(input('Escolha por onde deseja entrar(frente, servico ou telhado): '))
            if entrada == 'frente':
                tentativas = 3
                while tentativas != 0 :
                    dfrente = ''
                    dfrente = str(input('Digite 3 números(2 inteiros e um real) : ')).split()
                    dfrente[0] = int(dfrente[0])
                    dfrente[1] = int(dfrente[1])
                    dfrente[2] = float(dfrente[2])
                    if (dfrente[0] != 0) and (294 % dfrente[0] == 0) and (294 // dfrente[0] == dfrente[1]) and (dfrente[1] // dfrente[0] == dfrente[2]):
                        print("ok ok")
                        print(dfrente)
                        tentativas = 0
                        break
                    else:
                        tentativas -= 1
                        print(f'Erro, tentativas restantes : {tentativas}')

                ...
            elif entrada == 'servico':
                print('servico')
                ...
            elif entrada == 'telhado':
                print('telhado')
                ...
            else:
                print('Entrada inválida tente novamente')

            #break

            print('Escolha 2 itens(lanterna/chave/corda) separados por espaço :')