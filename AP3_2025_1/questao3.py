def remove_espaco (frase):
    return frase.replace(" ","")

def contar_letras (frase):
    vogais_referencia = 'aeiouáéíóúàèìòùâêîôûãõ'
    vogais = 0
    consoantes = 0
    for letra in frase:
        if letra.isalpha():
            if letra in vogais_referencia:
                vogais += 1
            else:
                consoantes += 1
    return print(f'A frase tem {vogais} vogais e {consoantes} consoantes')

def palindromo (frase):
    if len(frase) <= 1:
        return True
    if frase[0] == frase[-1]:
        return palindromo (frase[1:-1])

    else:
        return False


texto_original = input().lower()
texto_sem_espacos = remove_espaco(texto_original)
print(f'A frase sem espaços é {texto_sem_espacos}')
contar_letras(texto_sem_espacos)

if palindromo(texto_sem_espacos):
    print('É palindromo')
else:
    print('Não é palindromo')