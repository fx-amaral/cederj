X=[None]*10
for i in range(len(X)):
    X[i]=int(input())
    if X[i]<=0:
        X[i]=1
    print('X[{}] = {}'.format(i, X[i]))

