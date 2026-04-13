POS = 0
MED = 0
for i in range(6):
    N=float(input())
    if N>0:
        POS+=1
        MED+=N
print(POS,"valores positivos")
print(f"{MED/POS:.1f}")