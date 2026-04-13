V=int(input())
H=0
M=0
if V < 60:
   S=V
   print(H,':',M,':',S)
elif V >= 60:
   S=V % 60
   M=V//60
   if M > 60:
        H=M//60
        M=M % 60
        print(H,':',M,':',S)
   else:
       print(H,':',M,':',S)