T=int(input())
A=0
M=0
D=0
if T > 365:
    M=T % 365
    D = M % 30
    M = M // 30
    A=T//365

    print(A, 'ano(s)')
    print(M, 'mes(es)')
    print(D, 'dia(s)')

else:
    M=T // 30
    D = T % 30
    print(A,'ano(s)')
    print(M,'mes(es)')
    print(D,'dia(s)')