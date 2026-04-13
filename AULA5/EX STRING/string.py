
lida = input("Entre com uma expressão numérica válida: ")
print("{"+lida+"} =", avalia(lida.strip()))


# Subprograma
 def avalia(lida):
    valor = 0
	if lida!="":
		partes = lida.split("+")
		for p in partes:
			valor = valor + float(p)
 return valor

