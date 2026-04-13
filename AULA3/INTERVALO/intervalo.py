IN=0
OUT=0
N=int(input())
if N<10000:
    for i in range(N):
        X=int(input())
        if X>=10 and X<=20:
            IN+=1
        else:
            OUT+=1
print(IN, "in")
print(OUT, "out")