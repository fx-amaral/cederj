T=int(input())
F=[None]*61
F[0]=0
F[1]=1
for i in range(2,61):
    F[i]= F[i-1] + F[i-2]

for i in range(0,T):
    x=int(input())
    print('Fib({}) = {}'.format(x, F[x]))
    #print('F[{}] = {}'.format(i, F[i]))



